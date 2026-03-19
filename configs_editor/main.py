import os
import sys
import yaml
import time
import logging
import argparse
import subprocess
import utils
import json
import pickle

from pathlib import Path

from css_parameters import CSSParameters

# todo: user can specify a directory that already exists
#       in this case, failed analyses are moved to a bkup folder and are reran
#       successfull analyses have their output from files appended to the dict:analysis_data
# todo: in the config.yaml and here, rename "from" to "analysis_name"

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
    "GTF_lbin_abinit3d_pmd",

    #070_CSS_Init_Refine3D
    "CSS_mbin_reextract_mics_box",
    "CSS_mbin_reextract_mics_0o95box",
    "CSS_mbin_reextract_parts_box",
    "CSS_mbin_reextract_parts_x_min",
    "CSS_mbin_reextract_parts_x_max",
    "CSS_mbin_reextract_parts_y_min",
    "CSS_mbin_reextract_parts_y_max",
]

logger = logging.getLogger("ANALYSES PIPELINE")

## preprocessing ##
def get_output_single(analyses_data, analysis_name, attribute_name):
    # todo: it doesnt work with dict of dicts, I believe a solution is not hard to implement but need many testing
    try:
        return json.loads(analyses_data[analysis_name]["runtime"]["output"].stdout)[attribute_name]
    except AttributeError as e:
        return "ERROR: VALUE NOT FOUND"

def get_output(analyses_data, analysis_name, attribute_name):
    try:
        data = json.loads(analyses_data[analysis_name]["runtime"]["output"].stdout)
        if isinstance(attribute_name, str):
            # parse key1.key2 so we can access attributes of dict of dict
            keys = attribute_name.split(".")
        else:
            keys = attribute_name
        value = data
        for k in keys:
            value = value[k]
        return value

    except (AttributeError, KeyError, TypeError, json.JSONDecodeError):
        logger.exception(f"ERROR: VALUE NOT FOUND FOR {analysis_name} {attribute_name}")
        return None

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
def compute_css_parameters(input_parameters, analyses_data, css_params_of_interest, output_directory):
    # process inputs from the yaml
    input_dict = {name:resolve_value(value, analyses_data, None, None) 
                    for name, value in input_parameters.items()}

    # filter fields that CSSParameters does not expect
    filtered_input = {k: v for k, v in input_dict.items() if k in CSSParameters.get_valid_fields()}

    # instantiate and run calculations
    params = CSSParameters(**filtered_input)
    result = {"Settings":params.to_dict(css_params_of_interest)}

    # save to a yaml file
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
        try:
            assert int(analyses[name]['runtime']['output'].returncode)==0
        except Exception:
            logger.exception(f"Pipeline Crashed while running {name.upper()}!!".upper())
            logger.exception("+ Current analysis failed to run. Please, check its log file.")
            raise
        logger.info(f"+ Output: {analyses[name]['runtime']['output'].stdout}")
        logger.info("Done!\n--------------------")

    result = {"analyses_data" : analyses,
              "parameters"    : config_yaml["parameters"]
    }
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config_file", type=str, required=True, help="Path to the configuration file (yaml).")
    parser = utils.add_common_cli_arguments(parser) # adds --verbose, --json, --output-dir --debug
    args = parser.parse_args()

    # Directory creation
    basedir = utils.prepare_output_environment(args.output_dir or ".")

    # Logging
    utils.configure_logging(verbose=args.verbose, output_directory=basedir, capture_warnings=True)
    logger.info(f"\n- Config file: {args.config_file} \n- Output directory: {basedir}  \n- Verbose: {args.verbose}")

    try:
        # prepare and run all analyses
        analyses = run(config_filepath=args.config_file, basedir=basedir)

        # save data for debugging
        if args.debug:
            with open(os.path.join(basedir, "pipeline_data.pkl"), "wb") as f:
                pickle.dump(analyses, f) 

        # cs-schemes parameter computation
        compute_css_parameters(analyses["parameters"],
                               analyses["analyses_data"],
                               PARAMS_OF_INTEREST,
                               basedir)

    except Exception:
        logger.exception("Pipeline Crashed!!".upper())
        raise


    