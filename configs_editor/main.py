import os
import sys
import yaml
import time
import logging
import argparse
import subprocess
import utils
import json

from pathlib import Path

from css_parameters import CSSParameters

### dev ###
import pickle

PARAMS_OF_INTEREST = [
    #Common
    "SS_comm_class2d_pmd",
    "SS_comm_optimal_pmd",
    
    #030_GTF_Create_Stack
    "GTF_lbin_extract_mics_box",
    "GTF_lbin_extract_mics_0o95box",
    "GTF_lbin_extract_parts_box",
    "GTF_lbin_extract_parts_x_min",
    "GTF_lbin_extract_parts_x_max",
    "GTF_lbin_extract_parts_y_min",
    "GTF_lbin_extract_parts_y_max",
    
    #050_GTF_AbInitReconst3D
    # "GTF_lbin_abinit3d_pmd",

    #070_CSS_Init_Refine3D
    "CSS_mbin_reextract_mics_box",
    "CSS_mbin_reextract_mics_0o95box",
    "CSS_mbin_reextract_parts_box",
    "CSS_mbin_reextract_parts_x_min",
    "CSS_mbin_reextract_parts_x_max",
    "CSS_mbin_reextract_parts_y_min",
    "CSS_mbin_reextract_parts_y_max",
]

### / ###

logger = logging.getLogger("ANALYSES PIPELINE")

## preprocessing ##
def make_commandv0(executable, script, args, basedir=None, outdir=None):
    cmd = [executable, script] + [a for line in args for a in line.replace(" ", "").replace("$OUTDIR", outdir).replace("$BASEDIR", basedir).split(":")]
    return cmd

def get_output(analyses_data, analysis_name, attribute_name):
    try:
        return json.loads(analyses_data[analysis_name]["runtime"]["output"].stdout)[attribute_name]
    except AttributeError as e:
        return "ERROR: VALUE NOT FOUND"

def resolve_value(value, analyses_data, basedir, outdir):
    # regular input; replaces directories
    if isinstance(value, str):
        value = value.replace("$OUTDIR", outdir).replace("$BASEDIR", basedir)
    # input comes from another analysis
    elif isinstance(value, dict):
        value = get_output(analyses_data, value["from"], value["attribute"])
    return value

def make_command(executable, script, args, analyses_data=None, basedir=None, outdir=None):
    cmd = [executable, script]

    for arg in args:
        # flag only
        if isinstance(arg, str):
            # example: arg = "--test"
            cmd.extend([arg])
        elif isinstance(arg, list) and len(arg)==1:
            # example: arg = ["--test"]
            cmd.extend(arg)
        # flag and value
        elif isinstance(arg, list) and len(arg)>1:
            # example: arg = ["--test", 1.1]
            flag, value = arg
            resolved = resolve_value(value, analyses_data, basedir, outdir)
            cmd.extend([flag, str(resolved)])
        
    return cmd

## postprocessing ##
def compute_css_parameters(analyses_data, css_params_of_interest, output_directory):
    user_input = analyses_data["parameters"]
    data       = analyses_data["analyses_data"]

    params = CSSParameters(EM_mics_apix        = user_input["EM_mics_apix"],        # from: config_em_settings.yml
                           SS_comm_lbin_angpix = user_input["SS_comm_lbin_angpix"], # from: ???
                           SS_comm_mbin_angpix = user_input["SS_comm_mbin_angpix"], # from: ???
                           mics_upper_bound    = user_input["micrograph_size"],     # from micrograph
                           
                           # particle_diameter         = get_output(data, al_name, attr),
                           # negative_density_diameter = get_output(data, al_name, attr),
                           # fresnel_boxsize           = get_output(data, al_name, attr),
    )

    result = {"Settings":params.to_dict(css_params_of_interest)}
    utils.handle_output(result, output_directory=output_directory, show=False)

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

def run(config_filepath, basedir):
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
        analyses[name]["runtime"]["outdir"] = os.path.join(basedir, name)

        # command to exec
        analyses[name]["runtime"]["command"] = make_command(analyses[name]["config"]["executable"], 
                                                            analyses[name]["config"]["script"], 
                                                            analyses[name]["config"]["args"], 
                                                            analyses,
                                                            basedir,
                                                            analyses[name]["runtime"]["outdir"])

        ## 3. Execution
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

    result = {"analyses_data" : analyses,
              "parameters"    : config_yaml["parameters"]
    }
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config_file", type=str, required=True, help="Path to the configuration file (yaml).")
    parser = utils.add_common_cli_arguments(parser) # adds --verbose, --json, --output-dir
    args = parser.parse_args()

    # Directory creation
    basedir = utils.prepare_output_environment(args.output_dir or ".")

    # Logging
    utils.configure_logging(verbose=args.verbose, output_directory=basedir, capture_warnings=True)
    logger.info(f"\n- Config file: {args.config_file} \n- Output directory: {basedir}  \n- Verbose: {args.verbose}")

    try:
        # prepare and run all analyses
        analyses = run(config_filepath=args.config_file, basedir=basedir)

        # dev
        with open(os.path.join(output_directory, "analyses.pkl"), "wb") as f:
            pickle.dump(analyses, f) 

        # cs-schemes parameter computation
        compute_css_parameters(analyses, PARAMS_OF_INTEREST, basedir)

    except Exception:
        logger.exception("Pipeline Crashed!!".upper())
        raise


    