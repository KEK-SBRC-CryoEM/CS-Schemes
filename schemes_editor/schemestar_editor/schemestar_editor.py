#!/usr/bin/env python3.7
#################################################################################################
# Author: Misato Yamamoto  (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023 KEK IMMS SBRC
# 
# Description:
# To simplify changing settings in the scheme.star files.
# The Parameters in the scheme.star files are replaced by values in yaml config files.
# User set  sample data information in config_sample_settings.yml.
# User must specify the path to config_sample_settings.yml when executing this script.
#
# Usage
#
# $ python3 schemestar_editor.py -c /<path_to>/config_sample_settings.yml
#
#
#################################################################################################

# ========================================================================================
# Directory structure
# 
# - Script Directory 
#    |-- schemestar_editor
#      |-- schemestar_editor.py
#  
# - Configs Directory   # A sample of configurations directory (Use this as a template to create user-defined configurations)
#    |-- config_em_settings.yml
#    |-- config_sample_settings_xx.yml

# -  Schemes template Directory 
#    |-- Schemes             <<<< a sample of template schemes directory (Use this as a template to create user-defined schemes)
#      |-- **                <<<< a single scheme directoy
#        |-- scheme.star     <<<< a scheme star file per the single scheme   
#        |-- **              <<<< a job directory of the single scheme
#          |- job.star       <<<< a job star file of the single scheme
# 
# - <INPUT> User-Defined Configurations Directory 
#   |-- configs/common  # A sample of configurations directory (Use this as a template to create user-defined configurations)
#     |-- config_em_settings_xx.yml
#     |-- config_sample_settings.yml
#
# - <INPUT> User-Defined Template Schemes Directory
#   |-- Schemes             <<<< a sample of template schemes directory (Use this as a template to create user-defined schemes)
#     |-- **                <<<< a single scheme directoy
#       |-- scheme.star     <<<< a scheme star file per the single scheme   
#       |-- **              <<<< a job directory of the single scheme
#         |- job.star       <<<< a job star file of the single scheme
#
# - <OUTPUT> Output Directory (Can be RELION project folder)
#   |-- Schemes             <<<< An output directory to be created. It will contain all schemes to be used for RELION Schemes execution
#     |-- **                <<<< a single scheme directoy
#       |-- scheme.star     <<<< a scheme star file per the single scheme   <<< change parameters in this file by this script!
#       |-- **              <<<< a job directory of the single scheme
#         |- job.star       <<<< a job star file of the single scheme
#   |-- schemestar_ettings    <<<< An output directory to be created. It will contain the executable file PATH setting file.
#     |-- ss_scheme_star_<scheme name>'.yml          <<<< Output file of the protein data setting for scheme star per single scheme.
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
    __SS_DIR_NAME                        = 'schemestar_settings'
    __YAML_FILE_EXT                       = '.yml'
    __SS_SETTING_FILE_PREFIX              = 'ss_scheme_star_'
#    __SCHEME_STAR_KEY_PREFIX              = 'CS_'

    __SCHEMES_DIR_NAME                    = 'Schemes'  # Name of RELION Schemes Directory 
    __SCHEME_STAR_FILE_NAME               = 'scheme.star'
#    __SCHEME_STAR_FILE_RPATH_PATTERN      = '**/' + __SCHEME_STAR_FILE_NAME

    __SS_SETTING_KEY                      = 'Settings'
    __SS_SCHEME_NAME_KEY                  = 'SchemeName'

    __SS_FILE_PREFIX                      = 'ss_' 

    __ERROR_FILE_NAME                     = 'error_output.txt'
    __SCHEMESTAR_EDITOR_ERROR_FILE_NAME   =  __SS_FILE_PREFIX + __ERROR_FILE_NAME


    def __init__(self):
        # Private instance variables
        self.__schemestar_dict_list =[]

    # Load yaml file and keep the contents as a dictionary 
    def __load_yaml_file(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        return yaml_dict
    
    # Save a dictionary data as yaml file.
    def __save_yaml_file(self, yaml_file_path, yaml_dict):
        with open(yaml_file_path, "w") as yaml_file:
            yaml.safe_dump(yaml_dict, yaml_file, sort_keys=False)

    # Create dictionary data of the protein data settings. 
    def __create_schemestar_dict(self, configs_file_path, output_schemes_subdir_path):
        # Check preconditions!
        # configs_dir_path: a path of directory containing all configuration yaml files
        # Check if template_schemes_dir_path exists.
        assert configs_file_path, '[SS_ASSERT] The configs file "{}" must exist!'.format(configs_file_path)
        if not os.path.exists(configs_file_path):
            print('[SS_MESSAGE] Error! The configs file "{}" does NOT exist! Please set the correct PATH using "--c" option.'.format(configs_file_path))
            return
        self.__schemestar_dict_list = []
        # Load yaml file and keep the contents as a dictionary data
        setting_dict = self.__load_yaml_file(configs_file_path)

        # Make sure the key to be repalaced exists in the target scheme.star file.
        # Create list to replace the values in scheme.star.
        scheme_name_list = os.listdir(output_schemes_subdir_path)
        for scheme_name in scheme_name_list:
            schemestar_dict = {}
            schemestar_dict[type(self).__SS_SETTING_KEY] = {}
            output_scheme_star_file_path = os.path.join(output_schemes_subdir_path, scheme_name, type(self).__SCHEME_STAR_FILE_NAME)
            if os.path.isfile(output_scheme_star_file_path):
                scheme_star_key_list = self.__create_scheme_star_key_list(output_scheme_star_file_path)
                scheme_setting_key_list = list(set(scheme_star_key_list) & set(setting_dict[type(self).__SS_SETTING_KEY].keys()))
                if len(scheme_setting_key_list) != 0:
                    schemestar_dict[type(self).__SS_SCHEME_NAME_KEY] = scheme_name
                    for scheme_setting_key in scheme_setting_key_list:
                        value = setting_dict[type(self).__SS_SETTING_KEY][scheme_setting_key]
                        schemestar_dict[type(self).__SS_SETTING_KEY][scheme_setting_key] = value
                    self.__schemestar_dict_list.append(schemestar_dict.copy())

    # Save settings data as yml file.
    def __save_schemestar_dict_list(self, settings_subdir_path):
        if len(self.__schemestar_dict_list) > 0:
            self.__make_output_subdir_backup(settings_subdir_path)
            assert not os.path.exists(settings_subdir_path), '[SSE_ASSERT] The output paralle settings subdirectory "{}" must NOT exist at this point of code!'.format(settings_subdir_path)
            os.mkdir(settings_subdir_path)
            for schemestar_dict in self.__schemestar_dict_list:
                setting_yml_file_name = type(self).__SS_SETTING_FILE_PREFIX + schemestar_dict[type(self).__SS_SCHEME_NAME_KEY] + type(self).__YAML_FILE_EXT
                settings_dict_yaml_file_path = os.path.join(settings_subdir_path, setting_yml_file_name)
                self.__save_yaml_file(settings_dict_yaml_file_path, schemestar_dict[type(self).__SS_SETTING_KEY])
        else:
            assert len(self.__schemestar_dict_list) == 0, '[SSE_ASSERT] self.__schemestar_dict_list should be empty at this point of code!'
    
    # Make back-up if a file with same name already exists.
    def __make_output_subdir_backup(self, output_subdir_path):
        if os.path.exists(output_subdir_path): 
            print('[SSE_MESSAGE]', 'The output subdirectory "{}" already exists! Making a backup of the existing subdirectory...'.format(output_subdir_path))
            dt_now = datetime.datetime.now()
            backup_output_subdir_path = output_subdir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(output_subdir_path, backup_output_subdir_path)
        assert not os.path.exists(output_subdir_path), '[SSE_ASSERT] The output subdirectory "{}" must NOT exist at this point of code!'.format(output_subdir_path)

    def __create_scheme_star_key_list(self, output_scheme_star_file_path):
#        output_scheme_star_file_path = os.path.join(output_schemes_subdir_path, scheme_name, type(self).__SCHEME_STAR_FILE_NAME)
        assert os.path.exists(output_scheme_star_file_path), '[SSE_ASSERT] The scheme.star file "{}" must exist at this point of code!'.format(output_scheme_star_file_path)
        scheme_star_dict = starfile.read(output_scheme_star_file_path)
        scheme_star_key_list = []
        scheme_star_item_list_list = [['scheme_floats','rlnSchemeFloatVariableName'],['scheme_bools','rlnSchemeBooleanVariableName'],['scheme_strings','rlnSchemeStringVariableName']]
        for item_list in scheme_star_item_list_list:
            for i in range(len(scheme_star_dict[item_list[0]])):
                scheme_star_key = scheme_star_dict[item_list[0]][item_list[1]][i]
#                if type(self).__SCHEME_STAR_KEY_PREFIX in scheme_star_key:
                scheme_star_key_list.append(scheme_star_key)
        return scheme_star_key_list

    def make_output_schemes(self, template_schemes_dir_path, output_dir_path):
        # Check preconditions!
        # Check if template_schemes_dir_path exists.
        assert template_schemes_dir_path, '[SSE_ASSERT] The template Schemes directory "{}" must exist!'.format(template_schemes_dir_path)
        if not os.path.exists(template_schemes_dir_path):
            print('[SSE_MESSAGE] Error! The template Schemes directory "{}" does NOT exist! Please set the correct PATH using "--s" option.'.format(template_schemes_dir_path))
            return
        
        output_schemes_subdir_path = os.path.join(output_dir_path, type(self).__SCHEMES_DIR_NAME)
        # Make a back up of schemes
        self.__make_output_subdir_backup(output_schemes_subdir_path)
        assert not os.path.exists(output_schemes_subdir_path), '[EE_ASSERT] The output Schemes subdirectory "{}" must NOT exist at this point of code!'.format(output_schemes_subdir_path)
        # Create output Schemes directory by copying template Schemes directory 
        shutil.copytree(template_schemes_dir_path, output_schemes_subdir_path)
        return output_schemes_subdir_path

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
    
    # Replace values of scheme.star files with the values set in config files.
    def __replace_schemes_star_param(self, output_dir_path, output_schemes_subdir_path):
        output_schemes_parent_dir_path = os.path.abspath(os.path.join(output_schemes_subdir_path, os.pardir))
        current_dir_path = os.getcwd()
        output_file = os.path.join(output_dir_path, type(self).__SCHEMESTAR_EDITOR_ERROR_FILE_NAME)
        for schemestar_dict in self.__schemestar_dict_list:
            scheme_name = schemestar_dict[type(self).__SS_SCHEME_NAME_KEY]
            for settings_key in schemestar_dict[type(self).__SS_SETTING_KEY].keys():
                scheme_setting_fin_key = settings_key
                edit_value = schemestar_dict[type(self).__SS_SETTING_KEY][settings_key]
                # Replace the values in scheme.star by running Relion schemer command.
                # relion_schemer command must be run at parent directory of Schemes in which the values are replaced. 
                relion_schemer_command = 'relion_schemer --scheme ' + str(scheme_name) + ' --set_var ' + str(scheme_setting_fin_key) + ' --value ' + str(edit_value) + ' --original_value ' + str(edit_value)
#                print('[SSE_MESSAGE] Replace the values in the scheme.star file with the following relion command')
#                print('[SSE_MESSAGE] {}'.format(relion_schemer_command))
                os.chdir(output_schemes_parent_dir_path)
                self.__execute_command(relion_schemer_command, output_file)
        os.chdir(current_dir_path)

 
    def edit(self, configs_file_path, output_dir_path, schemes_subdir_path, settings_subdir_name = __SS_DIR_NAME):
        # [*] configs_file_path          : Path of input configuration yaml file.
        # [*] schemes_subdir_path        : Path of input template RELION Schemes directory containing all Schemes related files.
        # [*] output_dir_path            : Path of output root directroy where all outputs will be saved.
        if not os.path.exists(schemes_subdir_path):
            print('[EE_MESSAGE] The specified output directory "{}" does not exist yet! Creating the directory'.format(output_dir_path))
            os.mkdir(schemes_subdir_path)
        assert os.path.exists(schemes_subdir_path), '[EE_ASSERT] The output Schemes directory "{}" must exist at this point of code!'.format(schemes_subdir_path)
        settings_subdir_path = os.path.join(output_dir_path, settings_subdir_name)
        # Create dictonary to replace tha value of scheme.star.
        self.__create_schemestar_dict(configs_file_path, schemes_subdir_path)
        # Save measurement condition and protein data settings per single Scheme.
        self.__save_schemestar_dict_list(settings_subdir_path)
        # Replace the value of scheme.star 
        self.__replace_schemes_star_param(output_dir_path, schemes_subdir_path)


if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configs_file",   type=str,  required=True,  help = 'Path of input configuration yaml file. This option is always required.')
    parser.add_argument("-s", "--schemes_dir",    type=str,  required=True,  help = 'Path of input template RELION Schemes directory containing all Schemes related files. This option is always required.')
    parser.add_argument("-o", "--output_dir",     type=str,  default='./',   help = 'Path of output root directroy where all outputs will be saved. (default is set to current directory "./")')
    args = parser.parse_args()
    
    # Rename options for readability
    option_configs_file_path          = args.configs_file
    option_template_schemes_dir_path = args.schemes_dir
    option_output_dir_path           = args.output_dir
    
    print('[SSE_MESSAGE] Specified values of all options')
    print('[SSE_MESSAGE]   Input configurations file path       := {}'.format(option_configs_file_path))
    print('[SSE_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[SSE_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] Editing measurement condition and protein data of the job.star files in the specified shcemes...')
    print('[SSE_MESSAGE] ')
    ss_editor = SchemeStarEditor()
    # Backup existing Schemes in output directory and copy template Schemes to output directory.
    output_schemes_subdir_path = ss_editor.make_output_schemes(option_template_schemes_dir_path, option_output_dir_path)
    ss_editor.edit(option_configs_file_path, option_output_dir_path, output_schemes_subdir_path)
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] DONE!')