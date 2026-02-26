import os
import sys
import yaml
import time
import logging
import argparse
import subprocess
import utils

from pathlib import Path

from css_parameters import CSSParameters

### dev ###
import pickle
### / ###

## preprocessing ##
def make_command(executable, script, args, basedir=None, outdir=None): 
    cmd = [executable, script] + [a for line in args for a in line.replace(" ", "").replace("$OUTDIR", outdir).replace("$BASEDIR", basedir).split(":")]
    return cmd

## postprocessing ## 
def func():
    params = CSSParameters(EM_mics_apix=analyses["parameters"]["EM_mics_apix"],               # from: config_em_settings.yml
                           SS_comm_lbin_angpix=analyses["parameters"]["SS_comm_lbin_angpix"], # from: ???
                           SS_comm_mbin_angpix=analyses["parameters"]["SS_comm_mbin_angpix"], # from: ???
                           mics_upper_bound=analyses["parameters"]["micrograph_size"])        # from micrograph



    # save YAML
    yaml.SafeDumper.add_representer(np.int64,   lambda dumper, data: dumper.represent_int(data.item()))
    yaml.SafeDumper.add_representer(np.float64, lambda dumper, data: dumper.represent_float(data.item()))

    data = {"Settings":params.to_dict(params_of_interest)}
    with open(filepath, "w") as file:
        yaml.safe_dump(data, file, sort_keys=False)




## pipeline ##
def run_subprocess(command, output_directory=None):
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")

    if output_directory:
        with open(os.path.join(output_directory, "out.txt"), "w") as f:
            f.write(result.stdout)

        with open(os.path.join(output_directory, "run.log"), "w") as f:
            f.write(result.stderr)
            f.write(f"\nexit code: {result.returncode}\n")
    
    return result

def run(config_filepath, base_dir):
    # 1. Load config file
    config_yaml = utils.load_yaml(config_filepath)

    # 2. Preprocessing
    ## 2.1 convert to dict to easily access analysis by name
    ### dict[name] -> dict["config"], dict["runtime"]
    analyses = {a["name"]:{"config":a, "runtime":{}} for a in config_yaml["analyses"]}
    logger.info("Configuration file contain these items:\n- " + "\n- ".join(analyses.keys()))

    ## 2.2 runtime properties
    for name in analyses.keys():
    # output directory path
        analyses[name]["runtime"]["outdir"] = os.path.join(base_dir, name)

        # command to exec
        analyses[name]["runtime"]["command"] = make_command(analyses[name]["config"]["executable"], 
                                                            analyses[name]["config"]["script"], 
                                                            analyses[name]["config"]["args"], 
                                                            base_dir,
                                                            analyses[name]["runtime"]["outdir"])

    ## 3. Execution
    for name in analyses.keys():
        logger.info(f"Running {name.upper()}...")
        # make output directory
        Path(analyses[name]["runtime"]["outdir"]).mkdir(parents=True, exist_ok=True)
        logger.info("+ Output Directory: " + analyses[name]["runtime"]["outdir"])
        logger.info("+ Command: " + " ".join(analyses[name]["runtime"]["command"]))
        
        # execute command
        analyses[name]["runtime"]["output"] = run_subprocess(analyses[name]["runtime"]["command"], 
                                                             analyses[name]["runtime"]["outdir"])
        # important attributes from subprocess: stdout, stderr, returncode
        logger.info(f"+ Return code: {analyses[name]['runtime']['output'].returncode}")
        logger.info(f"+ Output: {analyses[name]['runtime']['output'].stdout}")
        logger.info("Done!\n--------------------")

    # 4. Postprocess
    ## manually use this information to compute the desired parameters

    analyses["parameters"] = config_yaml["parameters"]
    return analyses



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config_file", type=str, required=True, help="Path to the configuration file (yaml).")
    parser = utils.add_common_cli_arguments(parser) # adds --verbose, --json, --output-dir
    args = parser.parse_args()

    # Directory creation
    base_dir = utils.prepare_output_environment(args.output_dir or ".")

    # Logging
    logger = utils.configure_logging(verbose=args.verbose, output_directory=base_dir, capture_warnings=True)
    logger = logging.getLogger("ANALYSES PIPELINE")
    logger.info(f"\n- Config file: {args.config_file} \n- Output directory: {base_dir}  \n- Verbose: {args.verbose}")

    # run main
    try:
        analyses = run(config_filepath=args.config_file, base_dir=base_dir)
    except Exception:
        logger.exception("Pipeline Crashed!!".upper())
        raise

    with open("analyses.pkl", "wb") as f: # dev
        pickle.dump(analyses, f) # dev
    