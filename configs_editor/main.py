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


# todo: divide config file into "4"
#       1. environment settings: path to scripts
#       2. user inputs
#       3. analyses invokation
#       4. wiring of analysis outputs
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

## input YAML processing ##
def load_environment_settings(filepath):
    # load file and get only the environment settings
    settings = utils.load_yaml(filepath)["environment"]

    # check for missing env and script files
    env_notfound  = [(name, path)           for name, path in settings["env"].items()     if not Path(path).is_file()]
    tool_notfound = [(name, path["script"]) for name, path in settings["toolbox"].items() if not Path(path["script"]).is_file()]

    # write to log
    for (name,path) in env_notfound+tool_notfound:
        logger.warning(f"File not found!\t{name.upper()}:\t{path}")

    # filter out missing files (commented: as we dont know which tool will be used, better raise an exception when tries to exec it)
    # settings = {"env"    : {k:v for k,v in settings["env"].items()     if (k,v) not in env_notfound},
    #             "toolbox": {k:v for k,v in settings["toolbox"].items() if (k,v["script"]) not in tool_notfound}
    # }
    
    # link scripts to their executable
    for tool in settings["toolbox"]:
        exec_placeholder = settings["toolbox"][tool]["env"]
        exec_path        = settings["env"][exec_placeholder]
    
        settings["toolbox"][tool]["env"] = exec_path

    return settings["toolbox"]

def load_analyses_settings(filepath):
    # load file and get only the environment settings
    settings = utils.load_yaml(filepath)["analyses"]

    # analysis name as key for easy access
    settings = {a["name"]:{"config":a, "runtime":{}} for a in settings}

    return {"analyses": settings}

def load_user_inputs(filepath):
    userfile = utils.load_yaml(filepath)["user_inputs"]

    user        = {"user":userfile}
    em_settings = {"em_settings": utils.load_yaml(userfile["em_settings_filepath"])["Settings"]}
    sp_settings = {"sample_settings": utils.load_yaml(userfile["sample_settings_filepath"])["Settings"]}
    # todo: add to config.yaml, list of settings_filepath which would be loaded like em_settings

    return {"input": user|em_settings|sp_settings}

## preprocessing ##
def get_output(analyses_data, source, analysis_name, attribute_name):
    try:
        if source=="analyses":
            data = analyses_data[source][analysis_name]["runtime"]["output"]
        else:
            data = analyses_data[source][analysis_name]
        if isinstance(attribute_name, str):
            # parse key1.key2 so we can access attributes of dict of dict
            keys = attribute_name.split(".")
        else:
            keys = attribute_name

        value = data
        for k in keys:
            value = value[k]
        return value

    except KeyError:
        logger.exception(f"ERROR: VALUE NOT FOUND FOR {analysis_name} {attribute_name}")
        return None

def resolve_value(value, analyses_data, basedir, outdir):
    # regular input; replaces directories
    if isinstance(value, str):
        value = value.replace("$OUTDIR", outdir).replace("$BASEDIR", basedir)
    # input comes from another analysis
    elif isinstance(value, dict):
        source, name = value["from"].split(".")
        value = get_output(analyses_data, source, name, value["attribute"])
    return value

def make_command(env, script, args, analyses_data=None, basedir=None, outdir=None):
    cmd = [env, script]

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
def run_subprocess(command, output_directory=None, name=None):
    # important attributes from subprocess: stdout, stderr, returncode
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    
    if output_directory:
        with open(os.path.join(output_directory, "out.txt"), "w") as f:
            f.write(result.stdout)

        with open(os.path.join(output_directory, "run.log"), "w") as f:
            f.write(result.stderr)
            f.write(f"\nexit code: {result.returncode}\n")
    
    try: # ensure it run successfully
        result.check_returncode()
    except subprocess.CalledProcessError:
        logger.exception(f"Pipeline Crashed while running {name.upper()} with return code {result.returncode}!!")
        logger.exception("+ Current analysis failed to run. Please, check its log file and the message below.")
        logger.exception(f"{result.stderr}")
        raise

    try: # parse output and return result
        result = json.loads(result.stdout)
    except (AttributeError, TypeError, json.JSONDecodeError):
        # not json, return result as is
        result = result.stdout
    return result

def run(config_filepath, analyses_filepath, environment_filepath, basedir):
    # 1. Load config file
    # config_yaml = utils.load_yaml(config_filepath)
    env_settings      = load_environment_settings(environment_filepath)
    analyses_settings = load_analyses_settings(analyses_filepath)
    user_inputs       = load_user_inputs(config_filepath)
    
    config = analyses_settings | user_inputs
    
    # 2. Preprocessing
    ## 2.1 runtime properties
    for name in config["analyses"].keys():
        # output directory path
        config["analyses"][name]["runtime"]["outdir"] = os.path.join(basedir, name)

        # get script name
        script_name = config["analyses"][name]["config"]["script"]

        # command to exec
        config["analyses"][name]["runtime"]["command"] = \
                        make_command(env     = env_settings[script_name]["env"], 
                                    script  = env_settings[script_name]["script"], 
                                    args    = config["analyses"][name]["config"]["args"], 
                                    analyses_data = config,
                                    basedir = basedir,
                                    outdir  = config["analyses"][name]["runtime"]["outdir"]
        )

        ## 3. Execution
        logger.info(f"Running {name.upper()}...")
        # make output directory
        Path(config["analyses"][name]["runtime"]["outdir"]).mkdir(parents=True, exist_ok=True)
        logger.info("+ Output Directory: " + config["analyses"][name]["runtime"]["outdir"])
        logger.info("+ Command: " + " ".join(config["analyses"][name]["runtime"]["command"]))
        
        # execute command
        config["analyses"][name]["runtime"]["output"] = run_subprocess(config["analyses"][name]["runtime"]["command"], 
                                                                       config["analyses"][name]["runtime"]["outdir"],
                                                                       name)

        logger.info(f"+ Output: {config['analyses'][name]['runtime']['output']}")
        logger.info("Done!\n--------------------")

    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config_file", type=str, required=True, help="Path to the configuration file (yaml).")
    # missing files below default to config_file if not provided
    parser.add_argument("-e", "--env_settings", type=str, help="Path to the environment settings file (yaml).")
    parser.add_argument("-a", "--analyses_settings", type=str, help="Path to the analyses settings file (yaml).")

    parser = utils.add_common_cli_arguments(parser) # adds --verbose, --json, --output-dir --debug
    args = parser.parse_args()

    env_settings      = args.env_settings      or args.config_file
    analyses_settings = args.analyses_settings or args.config_file

    # Directory creation
    basedir = utils.prepare_output_environment(args.output_dir or ".")

    # Logging
    utils.configure_logging(verbose=args.verbose, output_directory=basedir, capture_warnings=True)
    logger.info(f"\n- Config file:\t{args.config_file} \n- Environment:\t{env_settings}  \n- Analyses:\t{analyses_settings}")
    logger.info(f"\n- Output directory: {basedir}  \n- Verbose: {args.verbose}")

    try:
        # prepare and run all analyses
        analyses_result = run(config_filepath      = args.config_file, 
                              analyses_filepath    = analyses_settings,
                              environment_filepath = env_settings,
                              basedir=basedir)

        # save data for debugging
        if args.debug:
            with open(os.path.join(basedir, "pipeline_data.pkl"), "wb") as f:
                pickle.dump(analyses_result, f) 

        # load css-parameter mapping
        css_inputs = utils.load_yaml(analyses_settings)["css_inputs"]

        # cs-schemes parameter computation
        compute_css_parameters(css_inputs,
                               analyses_result,
                               PARAMS_OF_INTEREST,
                               basedir)

    except Exception:
        logger.exception("Pipeline Crashed!!".upper())
        raise


    