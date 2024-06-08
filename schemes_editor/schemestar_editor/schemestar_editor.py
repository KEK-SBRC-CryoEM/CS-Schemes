#!/usr/bin/env python3.7
##########################################################################################
# Authors: Misato Yamamoto (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023-2024 KEK IMMS SBRC
# 
# Description:
# To simplify changing settings in the scheme.star files.
# The Parameters in the scheme.star files are replaced by values in yaml config files.
# User set sample data information in config_sample_settings.yml.
# User must specify the path to config_sample_settings.yml when executing this script.
# 
# Usage:
# $ python3  schemestar_editor.py  -t /path/to/Template_Scheme  -c /path/to/config_sample_settings.yml  
# 
##########################################################################################

# ========================================================================================
# - Installation Directory Structure
#   the description is given in schemes_editor.py
# 
# - <REQUIRED INPUT> User-Specified or User-Defined Schemes Template Directory Structure
# [Input Root Directory]                                    <<<< The root path can be arbitrary. It can be RELION project directory.
#   |--- [Schemes Template Directory Name]                  <<<< A Schemes template directory containing a use-specified or user-defined RELION Schemes template. The directory name can be arbitrary (e.g., "Schemes", "Schemes_Templates").
#      |--- *                                               <<<< Scheme directories each containg a Scheme of this RELION Schemes template.
#         |--- scheme.star                                  <<<< The scheme star file of this Scheme. This file defines the SPA workflow of this RELION Schemes.
#         |--- *                                            <<<< Job directories each for a job belong to this RELION Schemes.
#            |--- job.star                                  <<<< The job star file of this job.
# 
# - <OPTINAL INPUT> User-Defined Configuration Files
#   |--- /path/to/config_em_settings*.yml                   <<<< A user-defined configuration file for EM-related parameter settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
#   |--- /path/to/config_sample_setting*.yml                <<<< A user-defined configuration file for Sample related parameter settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
# 
# - <OUTPUT> User-Specified Output Directory Structure
# [OUTPUT Root Directory]                                   <<<< The default path is "./Schemes_Edited". It can be the RELION project directory or current directory (i.e., "./").
#   |--- Schemes                                            <<<< An output Schemes directory created by this script. This Schemes are edited and executable with "relion_schemegui.py".
#   |  |--- *                                               
#   |     |--- scheme.star                                  <<<< The parameters in this file are editted by this script!
#   |     |--- *                                            
#   |        |--- job.star                                  <<<< The parameters in this file are editted by this script!
#   |
#   |--- SSE_schemestar_settings                             <<<< An output subdirectory created by this script. It contains the executable file PATH settings file.
#   |  |--- sse_scheme_star_[Scheme Name].yml                <<<< Output yaml files containing the sample settings in all Schemes (a single output yaml file per a single Scheme).
# 
# ========================================================================================


import yaml
import os
import shutil
import datetime
import argparse
import subprocess
import starfile


class SchemeStarEditor():
    # Private class constants
    __SCHEMES_DIR_NAME                      = 'Schemes'  # Name of RELION Schemes directory 
    __SCHEME_STAR_FILE_NAME                 = 'scheme.star'
#    __SSE_SCHEME_STAR_FILE_RPATH_PATTERN    = '**/' + __SSE_SCHEME_STAR_FILE_NAME
    
    __YAML_FILE_EXT                         = '.yml'
    __SSE_SETTING_KEY                       = 'Settings'
    __SSE_SCHEME_NAME_KEY                   = 'SchemeName'
    
    __DEFAULT_OUTPUT_DIR_PATH               = './Schemes_Edited'
    __SSE_SETTING_FILE_PREFIX               = 'sse_scheme_star_'
#    __SCHEME_STAR_KEY_PREFIX                = 'CS_'
    __ERROR_FILE_NAME                       = 'sse_error_output.txt' 
    
    # <Public Instance Constructor>
    def __init__(self):
        # Private instance variables
        self.__edit_schemes_dir_path      = ""    # A path of tempate RELION Schemes directory for editing (meaning that the script overrides this Schemes).
        self.__config_file_path           = ""    # A path of schemestar configuration file.
        self.__output_dir_path            = ""    # A path of output directory containg all outputs of this script (see "<OUTPUT> User-Specified Output Directory Structure").
        self.__schemestar_dict_list       = []    # List of dictionary holding keys and values of all scheme star parameter
    
    # <Private Helper Instance Method> Load yaml file and keep the contents as a dictionary 
    # NOTE: 2024/06/08 Toshio Moriya: The following function is duplicated in mulitple scripts of Schemes Editor
    # Need to make a shared library!
    def __load_yaml_file(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        return yaml_dict
    
    # <Private Helper Instance Method> Save a dictionary as a yaml file
    # NOTE: 2024/06/08 Toshio Moriya: The following function is also good candidate for a shared library!
    def __save_yaml_file(self, yaml_file_path, yaml_dict):
        with open(yaml_file_path, "w") as yaml_file:
            yaml.safe_dump(yaml_dict, yaml_file, sort_keys=False)
    
    # <Private Instance Method> 
    def __create_scheme_star_key_list(self, edit_scheme_star_file_path):
#       edit_scheme_star_file_path = os.path.join(self.__edit_schemes_dir_path, scheme_name, type(self).__SSE_SCHEME_STAR_FILE_NAME)
        assert os.path.exists(edit_scheme_star_file_path), '[SSE_ASSERT] The scheme.star file "{}" must exist at this point of code!'.format(edit_scheme_star_file_path)
        scheme_star_dict = starfile.read(edit_scheme_star_file_path)
        scheme_star_key_list = []
        scheme_star_item_list_list = [['scheme_floats','rlnSchemeFloatVariableName'],['scheme_bools','rlnSchemeBooleanVariableName'],['scheme_strings','rlnSchemeStringVariableName']]
        for item_list in scheme_star_item_list_list:
            for i in range(len(scheme_star_dict[item_list[0]])):
                scheme_star_key = scheme_star_dict[item_list[0]][item_list[1]][i]
#                if type(self).__SCHEME_STAR_KEY_PREFIX in scheme_star_key:
                scheme_star_key_list.append(scheme_star_key)
        return scheme_star_key_list
    
    # <Private Instance Method> Create dictionary data of the parameter settings. 
    def __create_schemestar_dict(self):
        # Check if template_schemes_dir_path exists.
        if not os.path.exists(self.__config_file_path):
            print('[SSE_MESSAGE] Error! The config file "{}" does NOT exist! Please set the correct PATH using "--c" option.'.format(self.__config_file_path))
            return
        self.__schemestar_dict_list = []
        # Load yaml file and keep the contents as a dictionary data
        setting_dict = self.__load_yaml_file(self.__config_file_path)
        
        # Make sure the key to be repalaced exists in the target scheme.star file.
        # Create list to replace the values in scheme.star.
        scheme_name_list = os.listdir(self.__edit_schemes_dir_path)
        for scheme_name in scheme_name_list:
            schemestar_dict = {}
            schemestar_dict[type(self).__SSE_SETTING_KEY] = {}
            edit_scheme_star_file_path = os.path.join(self.__edit_schemes_dir_path, scheme_name, type(self).__SSE_SCHEME_STAR_FILE_NAME)
            if os.path.isfile(edit_scheme_star_file_path):
                scheme_star_key_list = self.__create_scheme_star_key_list(edit_scheme_star_file_path)
                scheme_setting_key_list = list(set(scheme_star_key_list) & set(setting_dict[type(self).__SSE_SETTING_KEY].keys()))
                if len(scheme_setting_key_list) != 0:
                    schemestar_dict[type(self).__SSE_SCHEME_NAME_KEY] = scheme_name
                    for scheme_setting_key in scheme_setting_key_list:
                        value = setting_dict[type(self).__SSE_SETTING_KEY][scheme_setting_key]
                        schemestar_dict[type(self).__SSE_SETTING_KEY][scheme_setting_key] = value
                    self.__schemestar_dict_list.append(schemestar_dict.copy())
    
    # <Private Helper Instance Method> Make a backup if a directory with same name already exists.
    # NOTE: 2024/06/08 Toshio Moriya: The following function is duplicated in mulitple scripts of Schemes Editor
    # Need to make a shared library!
    def __make_backup_dir(self, target_dir_path):
        if os.path.exists(target_dir_path): 
            print('[SSE_MESSAGE]', 'The directory "{}" already exists! Making a backup of the existing directory...'.format(target_dir_path))
            dt_now = datetime.datetime.now()
            backup_dir_path = target_dir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(target_dir_path, backup_dir_path)
        assert not os.path.exists(target_dir_path), '[SSE_ASSERT] The directory "{}" must NOT exist at this point of code!'.format(target_dir_path)
    
    # <Private Instance Method>  Save settings data as yml file.
    def __save_schemestar_dict_list(self):
        if len(self.__schemestar_dict_list) > 0:
            self.__make_backup_dir(self.__output_dir_path)
            assert not os.path.exists(self.__output_dir_path), '[SSE_ASSERT] The output directory "{}" must NOT exist at this point of code!'.format(self.__output_dir_path)
            os.mkdir(self.__output_dir_path)
            for schemestar_dict in self.__schemestar_dict_list:
                setting_yml_file_name = type(self).__SSE_SETTING_FILE_PREFIX + schemestar_dict[type(self).__SSE_SCHEME_NAME_KEY] + type(self).__YAML_FILE_EXT
                settings_dict_yaml_file_path = os.path.join(self.__output_dir_path, setting_yml_file_name)
                self.__save_yaml_file(settings_dict_yaml_file_path, schemestar_dict[type(self).__SSE_SETTING_KEY])
        else:
            assert len(self.__schemestar_dict_list) == 0, '[SSE_ASSERT] self.__schemestar_dict_list should be empty at this point of code!'
    
    # <Private Helper Instance Method> 
    # If some error occours during command execution, the error file is created and error messerges are written. 
    # NOTE: 2024/06/08 Toshio Moriya: The following function is also good candidate for a shared library!
    def __execute_command(self, command, output_file):
        try:
            # Execute the command and capture the output
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # If the command was successful, return the output
            if result.returncode == 0:
                return result.stdout
            # If there was an error, write the error message to the file
            else:
                with open(output_file, 'a') as file:
                    file.write(f"Error: {result.stderr}\n")
                return f"Error: {result.stderr}"
        except subprocess.CalledProcessError as e:
            # If there was an error, write the error message to the file
            with open(output_file, 'a') as file:
                file.write(f"Error: {e}\n")
            return f"Error: {e}"
    
    # <Private Instance Method> Replace values of scheme.star files with the values set in config files.
    def __replace_schemes_star_param(self):
        output_schemes_parent_dir_path = os.path.abspath(os.path.join(self.__edit_schemes_dir_path, os.pardir))
        current_dir_path = os.getcwd()
        output_file = os.path.join(self.__output_dir_path, type(self).__ERROR_FILE_NAME)
        for schemestar_dict in self.__schemestar_dict_list:
            scheme_name = schemestar_dict[type(self).__SSE_SCHEME_NAME_KEY]
            for settings_key in schemestar_dict[type(self).__SSE_SETTING_KEY].keys():
                scheme_setting_fin_key = settings_key
                edit_value = schemestar_dict[type(self).__SSE_SETTING_KEY][settings_key]
                # Replace the values in scheme.star by running Relion schemer command.
                # relion_schemer command must be run at parent directory of Schemes in which the values are replaced. 
                relion_schemer_command = 'relion_schemer --scheme ' + str(scheme_name) + ' --set_var ' + str(scheme_setting_fin_key) + ' --value ' + str(edit_value) + ' --original_value ' + str(edit_value)
#                print('[SSE_MESSAGE] Replace the values in the scheme.star file with the following relion command')
#                print('[SSE_MESSAGE] {}'.format(relion_schemer_command))
                os.chdir(output_schemes_parent_dir_path)
                self.__execute_command(relion_schemer_command, output_file)
        os.chdir(current_dir_path)
    
    # <Public Instance Method> 
    # NOTE: 2024/06/08 Toshio Moriya: The following function is duplicated in mulitple scripts of Schemes Editor
    # Need to make a shared library!
    def make_edit_schemes(self, template_schemes_dir_path, output_dir_path):
        # Check preconditions!
        # Check if template_schemes_dir_path exists.
        if not os.path.exists(template_schemes_dir_path):
            print('[SSE_ERROR] The template Schemes directory "{}" does NOT exist! Please make sure to provide correct template Schemes directory path using "--template_schemes_dir" option.'.format(template_schemes_dir_path))
            sys.exit(1)
        
        assert os.path.exists(output_dir_path), '[SSE_MESSAGE] The output directory "{}" must exist at this point of code!'.format(output_dir_path)
        
        # Make a backup of schemes
        edit_schemes_dir_path = os.path.join(output_dir_path, type(self).__SCHEMES_DIR_NAME)
        self.__make_backup_dir(edit_schemes_dir_path)
        assert not os.path.exists(edit_schemes_dir_path), '[SSE_MESSAGE] The template Schemes directory for editing "{}" must NOT exist at this point of code!'.format(edit_schemes_dir_path)
        
        # Create output Schemes directory by copying template Schemes directory 
        shutil.copytree(template_schemes_dir_path, edit_schemes_dir_path)
        
        return edit_schemes_dir_path
    
    # <Public Instance Method> 
    def edit(self, edit_schemes_dir_path, config_file_path, output_dir_path = __DEFAULT_OUTPUT_DIR_PATH):
        # [*] edit_schemes_dir_path : Path of input template RELION Schemes directory containing all Schemes related files for editing (meaning that the script overrides this Schemes).
        # [*] config_file_path      : Path of input configuration yaml file.
        # [*] output_dir_path       : Path of output root directroy where all outputs will be saved.
        # 
        # NOTE: 2024/06/08 Toshio Moriya:
        # At this point, this function overwrites tempate Schemes (i.e., edit_schemes_dir_path) by default!
        # To make a backup of existing Schemes in output directory and copy template Schemes to output directory for editting,
        # the caller must use "self.make_edit_schemes()" and get the path of copy template Schemes beforehand.
        
        # Initialize instance variables with argument values
        self.__edit_schemes_dir_path = edit_schemes_dir_path
        self.__config_file_path = config_file_path
        self.__output_dir_path = output_dir_path
        
        # Check preconditions!
        # NOTE: 2024/06/08 Toshio Moriya
        # Actually these should be error checks instead of assertion!
        assert os.path.exists(self.__edit_schemes_dir_path), '[SSE_ASSERT] The specifeid output Schemes directory "{}" must exist at this point of code!'.format(self.__edit_schemes_dir_path)
        assert os.path.exists(self.__config_file_path), '[SSE_ASSERT] The configuration file  "{}" must exist!'.format(self.__config_file_path)
        
        # Create dictonary to replace the value of scheme.star.
        self.__create_schemestar_dict()
        # Save parameter settings per single Scheme.
        # The function makes a backup of output directory of previous run if necessary.
        # The, creates a new output directory.
        self.__save_schemestar_dict_list()
        # Replace the value of configured parameters in all scheme.star.
        self.__replace_schemes_star_param()


if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--template_schemes_dir",    type=str,    required=True,                 help = 'Path of input template RELION Schemes directory containing all Schemes related files. This option is always required.')
    parser.add_argument("-c", "--config_yml",              type=str,    required=True,                 help = 'Path of input configuration yaml file. This option is always required.')
    parser.add_argument("-o", "--output_dir",              type=str,    default='./Schemes_Edited',    help = 'Path of output root directroy where all outputs will be saved. (default "./Schemes_Edited")')
    args = parser.parse_args()
    
    # Rename options for readability
    option_template_schemes_dir_path = args.template_schemes_dir
    option_config_file_path          = args.config_yml
    option_output_dir_path           = args.output_dir
    
    print('[SSE_MESSAGE] Parameter values provided by command line')
    print('[SSE_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[SSE_MESSAGE]   Input configuration file path        := {}'.format(option_config_file_path))
    print('[SSE_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] Editing all the schemes.star files in the specified RELION Schemes...')
    print('[SSE_MESSAGE] ')
    sse_editor = SchemeStarEditor()
    # Make a backup of existing Schemes in output directory and copy template Schemes to output directory for editting.
    edit_schemes_dir_path = sse_editor.make_edit_schemes(option_template_schemes_dir_path, option_output_dir_path)
    print('[SSE_MESSAGE]   The directory path of output Schemes for editing    := {}'.format(edit_schemes_dir_path))
    sse_editor.edit(edit_schemes_dir_path, option_config_file_path, option_output_dir_path)
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] DONE!')