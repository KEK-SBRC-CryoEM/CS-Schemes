#!/usr/bin/env python3.7
#################################################################################################
# Author: Misato Yamamoto  (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023 KEK IMMS SBRC
# 
# Description:
# Simplify the setting of measurements condition and protein data. 
# Them in the scheme.star files are replaced by values in yaml config files.
# User set up mesurements condition in config_measurements_condition.yaml and protein data in config_protein_data.yml. 
#
# Usage
# $ python3 ProteinDataEditor.py
#
#
#################################################################################################

# ========================================================================================
# Directory structure
# 
# - Script Directory 
#   |-- ProteinDataEditor.py
#   |-- config_to_job_star_key_mapping.yml
#   |
#   |-- Configs  # A sample of configurations directory (Use this as a template to create user-defined configurations)
#   | |-- config_measurements_condition.yml
#   | |-- config_protein_data.yml
#   |
#   |-- Schemes             <<<< a sample of template schemes directory (Use this as a template to create user-defined schemes)
#     |-- **                <<<< a single scheme directoy
#       |-- scheme.star     <<<< a scheme star file per the single scheme   
#       |-- **              <<<< a job directory of the single scheme
#         |- job.star       <<<< a job star file of the single scheme
# 
# - <INPUT> User-Defined Configurations Directory 
#   |-- Configs  # A sample of configurations directory (Use this as a template to create user-defined configurations)
#     |-- config_measurements_condition.yml
#     |-- config_protein_data.yml
#     |-- config_data_type.yml
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
#   |-- ProteinDataSettings    <<<< An output directory to be created. It will contain the executable file PATH setting file.
#     |-- pde_scheme_star_<scheme name>'.yml          <<<< Output file of the protein data setting for scheme star per single scheme.
# 
# ========================================================================================

import yaml
import glob
import os
import shutil
import datetime
import argparse

class ProteinDataEditor():
    # Private class constants
    __PDE_DIR_NAME                        = 'ProteinDataSettings'
    __YAML_FILE_EXT                       = '.yml'
    __PDE_CONFIG_DATA_TYPE_YAML_FILE_NAME = 'config_data_type' + __YAML_FILE_EXT
    __PDE_SETTING_FILE_PREFIX             ='pde_scheme_star_'

    __SCHEMES_DIR_NAME                    = 'Schemes'  # Name of RELION Schemes Directory 
    __SCHEME_STAR_FILE_NAME               = 'scheme.star'

    __I_ENUM = -1
    __I_ENUM += 1; __IDX_JSPEL_KEY        = __I_ENUM
    __I_ENUM += 1; __IDX_JSPEL_VALUE1     = __I_ENUM
    __I_ENUM += 1; __IDX_JSPEL_VALUE2     = __I_ENUM
    __I_ENUM += 1; __N_IDX_JSPEL          = __I_ENUM

    def __init__(self):
        # Private instance variables
        self.__data_type_dict_list = []

    # Load yaml file and keep the contents as a dictionary 
    def __load_yaml_file(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        return yaml_dict
    
    # Save a dictionary data as yaml file.
    def __save_yaml_file(self, yaml_file_path, yaml_dict):
        with open(yaml_file_path, "w") as yaml_file:
            yaml.safe_dump(yaml_dict, yaml_file, sort_keys=False)

    # Construct line by line list of file
    def __construct_file_line_list(self, file_path):
        with open(file_path, "r") as file:
            file_line_list = [line for line in file.readlines()]
        return file_line_list

    # Construct dictionary data of the protein data settings. 
    def __construct_settings_dict(self, configs_dir_path, yaml_file_name, type_key, data_type):
        # Check preconditions!
        # configs_dir_path: a path of directory containing all configuration yaml files
        # Check if template_schemes_dir_path exists.
        assert configs_dir_path, '[PDE_ASSERT] The template Schemes directory "{}" must exist!'.format(configs_dir_path)
        if not os.path.exists(configs_dir_path):
            print('[PDE_MESSAGE] Error! The template Schemes directory "{}" does NOT exist! Please set the correct PATH using "--c" option.'.format(configs_dir_path))
            return

        yaml_file_path = os.path.join(configs_dir_path, yaml_file_name)
        # Load yaml file and keep the contents as a list of a dictionary data
        dict_list = self.__load_yaml_file(yaml_file_path)
        
        # Get executable file PATH  settings according to environment as dictionary data
        type = [dict.get(type_key) for dict in dict_list]

        # Check preconditions!
        # Check if settings for specified computing environment exist.
        if data_type not in type:
            print('[PDE_MESSAGE] Error! Type "{}" is not set in the yaml file. Please set the correct value.'.format(data_type))
            return
        for dict in dict_list:
            if dict[type_key] == data_type:
                settings_dict = dict['Settings']
                break
        return settings_dict

    def __make_data_type_dict_list(self, configs_dir_path):
        config_data_type_yaml_file_path = os.path.join(configs_dir_path, type(self).__PDE_CONFIG_DATA_TYPE_YAML_FILE_NAME)
        self.__data_type_dict_list = self.__load_yaml_file(config_data_type_yaml_file_path)
    
    # Save settings data as yml file.
    def __save_protein_data_setting_dict_list(self, configs_dir_path, settings_subdir_path):
        if len(self.__data_type_dict_list) > 0:
            self.__make_output_subdir_backup(settings_subdir_path)
            assert not os.path.exists(settings_subdir_path), '[PS_ASSERT] The output paralle settings subdirectory "{}" must NOT exist at this point of code!'.format(settings_subdir_path)
            os.mkdir(settings_subdir_path)
            for data_type_dict in self.__data_type_dict_list:
                settings_dict = self.__construct_settings_dict(configs_dir_path, data_type_dict['ConfigYml'], 'DataType', data_type_dict['DataType'])
                setting_yml_file_name = type(self).__PDE_SETTING_FILE_PREFIX + data_type_dict['SchemeName'] + type(self).__YAML_FILE_EXT
                settings_dict_yaml_file_path = os.path.join(settings_subdir_path, setting_yml_file_name)
                self.__save_yaml_file(settings_dict_yaml_file_path, settings_dict)
        else:
            assert len(self.__data_type_dict_list) == 0, '[PDE_ASSERT] self.__data_type_dict_list should be empty at this point of code!'
    
    # Make back-up if a file with same name already exists.
    def __make_output_subdir_backup(self, output_subdir_path):
        if os.path.exists(output_subdir_path): 
            print('[PDE_MESSAGE]', 'The output subdirectory "{}" already exists! Making a backup of the existing subdirectory...'.format(output_subdir_path))
            dt_now = datetime.datetime.now()
            backup_output_subdir_path = output_subdir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(output_subdir_path, backup_output_subdir_path)
        assert not os.path.exists(output_subdir_path), '[PDE_ASSERT] The output subdirectory "{}" must NOT exist at this point of code!'.format(output_subdir_path)

    def make_output_schemes(self, template_schemes_dir_path, output_dir_path):
        # Check preconditions!
        # Check if template_schemes_dir_path exists.
        assert template_schemes_dir_path, '[PDE_ASSERT] The template Schemes directory "{}" must exist!'.format(template_schemes_dir_path)
        if not os.path.exists(template_schemes_dir_path):
            print('[PDE_MESSAGE] Error! The template Schemes directory "{}" does NOT exist! Please set the correct PATH using "--s" option.'.format(template_schemes_dir_path))
            return
        
        output_schemes_subdir_path = os.path.join(output_dir_path, type(self).__SCHEMES_DIR_NAME)
        # Make a back up of schemes
        self.__make_output_subdir_backup(output_schemes_subdir_path)
        assert not os.path.exists(output_schemes_subdir_path), '[EE_ASSERT] The output Schemes subdirectory "{}" must NOT exist at this point of code!'.format(output_schemes_subdir_path)
        # Create output Schemes directory by copying template Schemes directory 
        shutil.copytree(template_schemes_dir_path, output_schemes_subdir_path)
        return output_schemes_subdir_path


    def __replace_schemes_star_param(self, configs_dir_path, output_schemes_subdir_path):
        for data_type_dict in self.__data_type_dict_list:
            settings_dict = self.__construct_settings_dict(configs_dir_path, data_type_dict['ConfigYml'], 'DataType', data_type_dict['DataType'])
            output_scheme_star_file_path_pattern = os.path.join(output_schemes_subdir_path, data_type_dict['SchemeName'], type(self).__SCHEME_STAR_FILE_NAME)
            # List keys to change values in the star.star file
            target_scheme_star_key_list = settings_dict.keys()
        # Replace values of protein data settings of all scheme star (scheme.star) in the specified template Schemes dirctory
            for output_scheme_star_file_path in glob.glob(output_scheme_star_file_path_pattern):
                assert os.path.exists(output_scheme_star_file_path), '[PDE_ASSERT] The file "{}" must exist at this point of code!'.format(output_scheme_star_file_path)
                if not os.path.exists(output_scheme_star_file_path):
                    print('[PDE_MESSAGE] Error! The file "{}" does NOT exist! Please make sure that the SchemeName in {} is correct or scheme.star exists.'.format(output_scheme_star_file_path, type(self).__PDE_CONFIG_DATA_TYPE_YAML_FILE_NAME))
                scheme_star_line_list = self.__construct_file_line_list(output_scheme_star_file_path)
            
                output_scheme_star_file_contents = None
                with open(output_scheme_star_file_path, 'r+') as output_scheme_star_file:
                    # Read all contents of file
                    output_scheme_star_file_contents = output_scheme_star_file.read()
                    assert output_scheme_star_file_contents is not None, '[PDE_ASSERT] Something is seriously wrong with either this star file or coding! (output_job_star_file_contents = "{}")'.format( output_scheme_star_file_contents)
                    # Create new line (new_scheme_star_line) to replace the values
                    for target_scheme_star_key in target_scheme_star_key_list:
                        for scheme_star_line in scheme_star_line_list:
                           scheme_star_line_token_list = scheme_star_line.split()
                           if len(scheme_star_line_token_list) == type(self).__N_IDX_JSPEL:     # lines does not have assumed number of tokens!
                               scheme_star_param_key = scheme_star_line_token_list[type(self).__IDX_JSPEL_KEY]
                               if scheme_star_param_key == target_scheme_star_key:
                                    # Change the field width of key/two values according string length. 
                                    if len(str(settings_dict[target_scheme_star_key])) > 8:
                                        # Asumes long strings (ex. mask name) here. 
                                        new_scheme_star_line = '{:30}{:40}{:40}\n'.format(scheme_star_param_key, settings_dict[target_scheme_star_key], settings_dict[target_scheme_star_key])
                                    else:
                                        # Assumes a number here.
                                        new_scheme_star_line = '{:30}{:10}{:10}\n'.format(scheme_star_param_key, settings_dict[target_scheme_star_key], settings_dict[target_scheme_star_key])
                                    # Replace settings according to all replace pairs
                                    output_scheme_star_file_contents = output_scheme_star_file_contents.replace(scheme_star_line, new_scheme_star_line)

                        # Delete all contents of the current scheme.star file
                        output_scheme_star_file.seek(0)
                        output_scheme_star_file.truncate(0)
                    
                        # Save the result of replacements to the current scheme.star file
                        output_scheme_star_file.write(output_scheme_star_file_contents)
 
    def edit(self, configs_dir_path, output_dir_path, output_schemes_subdir_path):
        # [*] configs_dir_path          : Path of input configurations directory containing all configuration yaml files.
        # [*] template_schemes_dir_path : Path of input template RELION Schemes directory containing all Schemes related files.
        # [*] output_dir_path           : Path of output root directroy where all outputs will be saved.
        if not os.path.exists(output_dir_path):
            print('[EE_MESSAGE] The specified output directory "{}" does not exist yet! Creating the directory'.format(output_dir_path))
            os.mkdir(output_dir_path)
        assert os.path.exists(output_dir_path), '[EE_ASSERT] The output directory "{}" must exist at this point of code!'.format(output_dir_path)

        settings_subdir_path = os.path.join(output_dir_path, type(self).__PDE_DIR_NAME)
        self.__make_data_type_dict_list(configs_dir_path)
        # Save measurement condition and protein data settings per single Scheme.
        self.__save_protein_data_setting_dict_list(configs_dir_path, settings_subdir_path)
        # Replace measurement condition and protein data of scheme.star 
        self.__replace_schemes_star_param(configs_dir_path, output_schemes_subdir_path)


if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configs_dir",    type=str,   default='./Configs',    help = 'Path of input configurations directory containing all configuration yaml files.  (Default "./Configs")')
    parser.add_argument("-s", "--schemes_dir",    type=str,   default='./Schemes',    help = 'Path of input template RELION Schemes directory containing all Schemes related files.  (Default "./Schemes")')
    parser.add_argument("-o", "--output_dir",     type=str,   default='../',          help = 'Path of output root directroy where all outputs will be saved.  (default "../")')
    args = parser.parse_args()
    
    # Rename options for readability
    option_configs_dir_path          = args.configs_dir
    option_template_schemes_dir_path = args.schemes_dir
    option_output_dir_path           = args.output_dir
    
    print('[PDE_MESSAGE] Specified values of all options')
    print('[PDE_MESSAGE]   Input configurations directory path  := {}'.format(option_configs_dir_path))
    print('[PDE_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[PDE_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[PDE_MESSAGE] ')
    print('[PDE_MESSAGE] ')
    print('[PDE_MESSAGE] Editing measurement condition and protein data of the job.star files in the specified shcemes...')
    print('[PDE_MESSAGE] ')
    pdeditor = ProteinDataEditor()
    # Backup existing Schemes in output directory and copy template Schemes to output directory.
    output_schemes_subdir_path = pdeditor.make_output_schemes(option_template_schemes_dir_path, option_output_dir_path)
    pdeditor.edit(option_configs_dir_path, option_output_dir_path, output_schemes_subdir_path)
    print('[PDE_MESSAGE] ')
    print('[PDE_MESSAGE] ')
    print('[PDE_MESSAGE] DONE!')