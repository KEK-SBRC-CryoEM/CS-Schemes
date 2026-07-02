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

### usage examples ###
# 1) all settings in one config yaml file
# python main.py -c config/all_settings_prews.yaml --verbose --debug
#  
# 2) settings split into multiple yaml files
# python main.py -c config/user_input_empiar10673_gpcr.yaml config/environment_settings_prews.yaml config/analyses_settings.yaml --verbose --debug
#
# 3) user input direct from CLI + every other settings in one config yaml file
# python main.py -c config/all_settings_prews.yaml -m "/home/tmoriya/shared_for_all/data/jair/EMPIAR10673_GPCR/PostProcess/job115/postprocess.mrc" -k "/home/tmoriya/shared_for_all/data/jair/autoparam/CS-Schemes/configs/common/config_em_settings_empiar10673_gpcr.yml" -n  "/home/tmoriya/shared_for_all/data/jair/autoparam/CS-Schemes/configs/common/config_sample_settings_empiar10673_gpcr.yml" --verbose --debug
#
# 4) user input direct from CLI + other settings split into multiple yaml files
# python main.py  config/environment_settings_prews.yaml  config/analyses_settings.yaml -m "/home/tmoriya/shared_for_all/data/jair/EMPIAR10673_GPCR/PostProcess/job115/postprocess.mrc" -k "/home/tmoriya/shared_for_all/data/jair/autoparam/CS-Schemes/configs/common/config_em_settings_empiar10673_gpcr.yml" -n  "/home/tmoriya/shared_for_all/data/jair/autoparam/CS-Schemes/configs/common/config_sample_settings_empiar10673_gpcr.yml" --verbose --debug
###

logger = logging.getLogger("PIPELINE")

## input YAML processing ##
def load_settings(filepath_list):
    settings = {}
    for filepath in filepath_list:
        settings = settings | utils.load_yaml(filepath)

    return settings

def process_system_settings(settings):
    # check for missing env and script files
    env_notfound  = [(name, path)         for name, path in settings["env"].items()     if not Path(path).is_file()]
    tool_notfound = [(name, path["path"]) for name, path in settings["toolbox"].items() if not Path(path["path"]).is_file()]

    # write to log
    for (name,path) in env_notfound+tool_notfound:
        logger.warning(f"File not found!\t{name.upper()}:\t{path}")
    
    # link scripts to their executable
    for tool in settings["toolbox"]:
        exec_placeholder = settings["toolbox"][tool].get("env")
        if exec_placeholder: # if there is env, replace name by its filepath
            exec_path = settings["env"][exec_placeholder]
            settings["toolbox"][tool]["env"] = exec_path

    return settings["toolbox"]

def process_workflow_settings(settings):
    # from input file: workflow.{name, command,  command arg list}
    # then we add workflow.{invocation, output_dir, output}
    settings = {entry["name"]: {"command"   : entry["command"],
                                "args"      : entry["args"],
                                "invocation": None, # derived from command and args
                                "output_dir": None, # basedir + name
                                "output"    : None,}
                                                for entry in settings}

    return {"workflow": settings}

def process_user_inputs(settings):
    user        = {"user":settings}
    em_settings = {"em_settings":settings.get("em_settings", {})}
    sp_settings = {"sample_settings":settings.get("sample_settings", {})}

    if "em_settings_filepath" in settings.keys():
        em_settings["em_settings"] |= utils.load_yaml(settings["em_settings_filepath"])["Settings"]

    if "sample_settings_filepath" in settings.keys():
        sp_settings["sample_settings"] |= utils.load_yaml(settings["sample_settings_filepath"])["Settings"]
    # todo: add to config.yaml, list of settings_filepath which would be loaded like em_settings

    return {"input": user|em_settings|sp_settings}

## preprocessing ##
def get_output(data_dict, attribute_path):
    try:
        if isinstance(attribute_path, str):
            # parse key1.key2 so we can access attributes of dict of dict
            keys = attribute_path.split(".")
        else:
            keys = attribute_path

        value = data_dict
        for k in keys:
            value = value[k]
        return value

    except KeyError:
        # logger.error(f"ERROR: VALUE NOT FOUND FOR {analysis_name} {attribute_name}")
        return None

def resolve_value(value, data_dict, basedir, outdir):
    # regular input; replaces directories
    if isinstance(value, str):
        result = value.replace("$OUTDIR", outdir).replace("$BASEDIR", basedir)
    # input comes from another analysis
    elif isinstance(value, dict):
        result = get_output(data_dict, attribute_path=value["from"].split(".")) 

        if result is None:
            result = value.get("default", None)
            logger.warning(f"VALUE NOT FOUND: {value['from']}!")
            logger.warning(f"+ DEFAULTING TO {result}.")
            if result is None: # the obtained default value is still None
                logger.warning(f"+ THIS MAY CAUSE SOME COMMANDS TO FAIL!")
    else: # todo: limit to numbers only
        result = value

    return result

def make_command(env, cmd_path, args, workflow_data=None, basedir=None, outdir=None):
    if env:
        cmd = [env, cmd_path]
    else: 
        cmd = [cmd_path]

    for arg in args:
        # flag only
        if isinstance(arg, str):
            # example: arg = "--test"
            cmd.extend([arg])
        elif isinstance(arg, list) and len(arg)==1:
            # example: arg = ["--test"]
            resolved = resolve_value(*arg, workflow_data, basedir, outdir)
            cmd.extend([str(resolved)])
        # flag and value
        elif isinstance(arg, list) and len(arg)>1:
            # example: arg = ["--test", 1.1]
            flag, value = arg
            resolved = resolve_value(value, workflow_data, basedir, outdir)
            cmd.extend([flag, str(resolved)])
        elif isinstance(arg, dict):
            # example: arg = {from: workflow.process.output}
            resolved = resolve_value(arg, workflow_data, basedir, outdir)
            cmd.extend([str(resolved)])
        
    return cmd

## pipeline ##
def run_subprocess(name, invocation, output_directory=None):
    try: 
        result = subprocess.run(invocation, capture_output=True, text=True, encoding="utf-8")
        # note: important attributes from subprocess: stdout, stderr, returncode
        
        if output_directory:
            with open(os.path.join(output_directory, "out.txt"), "w") as f:
                f.write(result.stdout)

            with open(os.path.join(output_directory, "run.log"), "w") as f:
                f.write(result.stderr)
                f.write(f"\nexit code: {result.returncode}\n")
    
        # ensure it run successfully
        result.check_returncode()
    except subprocess.CalledProcessError:
        logger.error(f"Pipeline Crashed while running {name.upper()} with return code {result.returncode}!!")
        logger.error("+ Current analysis failed to run. Please, check its log file and the message below.")
        # logger.error(f"{result.stderr}")
        raise

    try: # parse output and return result
        result = json.loads(result.stdout)
    except (AttributeError, TypeError, json.JSONDecodeError):
        # not json, return result as is
        result = result.stdout
    return result

def run(workflow_data, toolbox_settings, basedir, debug=False):
    # 1. alias
    wdata = workflow_data

    # 2. Preprocessing
    ## 2.1 runtime properties
    for name in wdata["workflow"].keys(): # analysis name
        # output directory path
        wdata["workflow"][name]["output_dir"] = os.path.join(basedir, name)

        # get script name
        cmd_name = wdata["workflow"][name]["command"]

        # command to exec
        wdata["workflow"][name]["invocation"] = \
                        make_command(env      = toolbox_settings[cmd_name].get("env"), 
                                     cmd_path = toolbox_settings[cmd_name]["path"], 
                                     args     = wdata["workflow"][name]["args"], 
                                     workflow_data = wdata,
                                     basedir  = basedir,
                                     outdir   = wdata["workflow"][name]["output_dir"]
        )

        ## 3. Execution
        logger.info(f"Running {name.upper()}...")
        # make output directory
        Path(wdata["workflow"][name]["output_dir"]).mkdir(parents=True, exist_ok=True)
        logger.info("+ Output Directory  : " + wdata["workflow"][name]["output_dir"])
        logger.info("+ Invocation Command: " + " ".join(wdata["workflow"][name]["invocation"]))
        
        # execute command
        wdata["workflow"][name]["output"] = run_subprocess(name,
                                                           wdata["workflow"][name]["invocation"], 
                                                           wdata["workflow"][name]["output_dir"],)

        logger.info(f"+ Output: {wdata['workflow'][name]['output']}")
        logger.info("Done!")
        logger.info("-"*40)

        # save state data for debugging
        if debug:
            with open(os.path.join(basedir, "pipeline_data.pkl"), "wb") as file:
                pickle.dump(wdata, file)

        # save state data (future: this will be used to stop/continue the workflow)
        utils.handle_output(wdata, 
                            to_json=True, 
                            filename=os.path.join(basedir, "pipeline_data.json"),
                            show=False)

    return wdata

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config_filepath_list", nargs='+', required=True, help="Path to one or more configuration files (yaml).")
    # alternatively receive user inputs from CLI
    parser.add_argument("-m",  "--reference_map",   type=str, help="Path to the reference map (mrc).")
    parser.add_argument("-k",  "--em_settings",     type=str, help="Path to the CS-Schemes EM Settings files (yaml).")
    parser.add_argument("-n",  "--sample_settings", type=str, help="Path to the CS-Schemes Sample Settings files (yaml).")

    parser = utils.add_common_cli_arguments(parser) # adds --verbose, --json, --output-dir --debug
    args = parser.parse_args()

    # Directory creation
    basedir = utils.prepare_output_environment(args.output_dir or ".")

    # Logging
    utils.configure_logging(verbose=args.verbose, output_directory=basedir, capture_warnings=True)

    # Input files handling
    settings = load_settings(args.config_filepath_list)

    # CLI handling
    if "user_inputs" not in settings.keys():
        settings["user_inputs"] = {}
    if args.reference_map:
        settings["user_inputs"]["reference_map_filepath"]   = args.reference_map
    if args.em_settings:
        settings["user_inputs"]["em_settings_filepath"]     = args.em_settings
    if args.sample_settings:
        settings["user_inputs"]["sample_settings_filepath"] = args.sample_settings
    
    missing_settings = [ft for ft in ["user_inputs", "workflow", "system"] if ft not in settings.keys()] # todo: possibly could check subsections
    if missing_settings:
        logger.error("Check your inputs. The following settings are missing: "+" ".join(missing_settings))
        raise Exception("Missing input settings. Expected 'user_inputs', 'workflow', and 'system' sections") 

    if args.debug:
        logger.info("DEBUG MODE ON: saves pipeline_data.pkl after running the analysis pipeline.")
        logger.info("-"*40)
    logger.info(f"Output directory: {basedir}")
    logger.info(f"Verbose: {args.verbose}")
    logger.info("-"*40)
    for i, f in enumerate(args.config_filepath_list):
        logger.info(f"Config file #{i+1}: {f}")
    logger.info("-"*40)
    logger.info("Reference MAP: "+settings["user_inputs"]["reference_map_filepath"])
    logger.info("CS-Schemes EM Settings: "+settings["user_inputs"].get("em_settings_filepath", "None"))
    logger.info("CS-Schemes Sample Settings: "+settings["user_inputs"].get("sample_settings_filepath", "None"))
    logger.info("-"*40)

    try:
        # prepare and run all analyses
        workflow_result = run(#user_inputs       = process_user_inputs(settings["user_inputs"]), 
                              #workflow_settings = process_workflow_settings(settings["workflow"]),
                              workflow_data    = process_user_inputs(settings["user_inputs"]) | process_workflow_settings(settings["workflow"]),
                              toolbox_settings = process_system_settings(settings["system"]),
                              basedir=basedir,
                              debug=args.debug)
    except Exception:
        logger.error("Pipeline Crashed!!".upper())
        # raise


    