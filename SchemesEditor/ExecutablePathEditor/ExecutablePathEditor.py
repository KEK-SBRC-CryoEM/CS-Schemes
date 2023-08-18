#!/usr/bin/env python3.7
#################################################################################################
# Author: Misato Yamamoto  (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023 KEK IMMS SBRC
# 
# Description:
# Simplify the setting of the executable file PATH according to computing environment for RELION Schemes. 
# The executable file PATH in the job.star files are replaced by values in yaml config files.
# User set up the executable PAHT in yaml files. 
#
# Usage
# $ python3 ExecutablePathEditor.py
#
#　You can also use as follows.
# $ python3 ExecutablePathEditor.py --e GoToCloud
#
#################################################################################################

# ========================================================================================
# Directory structure
# 
# - Script Directory 
#   |-- ExecutablePathEditor.py
#   |-- config_to_job_star_key_mapping.yml
#   |
#   |-- Configs  # A sample of configurations directory (Use this as a template to create user-defined configurations)
#   | |-- config_executable_path.py
#   |
#   |-- Schemes             <<<< a sample of template schemes directory (Use this as a template to create user-defined schemes)
#     |-- **                <<<< a single scheme directoy
#       |-- **              <<<< a job directory of the single scheme
#         |- job.star       <<<< a job star file of the single scheme
# 
# - <INPUT> User-Defined Configurations Directory 
#   |-- config_executable_path.py
#
# - <INPUT> User-Defined Template Schemes Directory
#   |-- Schemes             <<<< the schemes directory
#     |-- **                <<<< a single scheme directoy
#       |-- **              <<<< a job directory of the single scheme
#         |- job.star       <<<< a job star fole of the single scheme
#
# - <OUTPUT> Output Directory (Can be RELION project folder)
#   |-- Schemes             <<<< An output directory to be created. It will contain all schemes to be used for RELION Schemes execution
#   | |-- **                <<<< a single scheme directoy
#   |   |-- **              <<<< scheme job directory
#   |     |- job.star       <<<< a job star file of a single scheme job
#   |-- ExecutablePathSettings    <<<< An output directory to be created. It will contain the executable file PATH setting file.
#     |-- executable_path_settings.yml    <<<< Output a the executable file PATH setting file.
# 
# ========================================================================================

import yaml
import glob
import os
import shutil
import datetime
import starfile
import argparse

class ExecutablePathEditor():
    # Private class constants
    EE_DIR_NAME = 'ExecutablePathSettings'
    __YAML_FILE_EXT = '.yml'
    __CONFIG_EXECUTABLE_YAML_FILE_NAME = 'config_executable_path' + __YAML_FILE_EXT
    __EE_EXECUTABLE_SETTING_YAML_NAME = 'executable_path_settings'+ __YAML_FILE_EXT
    __CONFIG_TO_JOB_STAR_KEY_MAPPING_YAML_FILE_NAME = 'config_to_job_star_key_mapping' + __YAML_FILE_EXT

    __SCHEMES_DIR_NAME             = 'Schemes'  # Name of RELION Schemes Directory
    __JOB_STAR_FILE_PATH_PATTERN  = '**/**/job.star'  

    __I_ENUM = -1
    __I_ENUM += 1; __IDX_JSPEL_KEY   = __I_ENUM
    __I_ENUM += 1; __IDX_JSPEL_VALUE = __I_ENUM
    __I_ENUM += 1; __N_IDX_JSPEL     = __I_ENUM

    def __init__(self):
        # Private instance variables
        self.__executable_dict = {}

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
    
    # Save job.star contents as dictionary data
    def __construct_job_star_dict(self, file_path):
        self.__job_star_options_dict = {}
        job_star_dict = starfile.read(file_path)
        self.__job_star_options_dict['jobtypelabel'] = job_star_dict['job']['rlnJobTypeLabel'][0]
        for i in range(len(job_star_dict ['joboptions_values'])):
            key = job_star_dict['joboptions_values']['rlnJobOptionVariable'][i]
            value = job_star_dict['joboptions_values']['rlnJobOptionValue'][i]
            self.__job_star_options_dict[key] = value

    # Construct dictionary data of the executable file PATH according to computing environment. 
    def __construct_executable_dict(self, configs_dir_path, computing_environment):
        # Check preconditions!
        # configs_dir_path: a path of directory containing all configuration yaml files
        # Check if template_schemes_dir_path exists.
        #assert configs_dir_path, '[EE_ASSERT] The template Schemes directory "{}" must exist!'.format(configs_dir_path)
        if not os.path.exists(configs_dir_path):
            print('[EE_MESSAGE] Error! The template Schemes directory "{}" does NOT exist! Please set the correct PATH using "--c" option.'.format(configs_dir_path))
            return

        config_executable_yaml_file_path = os.path.join(configs_dir_path, type(self).__CONFIG_EXECUTABLE_YAML_FILE_NAME)
        # Load yaml file and keep the contents as a list of a dictionary data
        executable_dict_list = self.__load_yaml_file(config_executable_yaml_file_path)
        
        # Get executable file PATH  settings according to environment as dictionary data
        env = [executable_dict.get('ComputingEnvironment') for executable_dict in executable_dict_list]

        # Check preconditions!
        # Check if settings for specified computing environment exist.
        if computing_environment not in env:
            print('[EE_MESSAGE] Error! Computing environment "{}" is not set in the yaml file. Please set the correct value using "--e" option.'.format(computing_environment))
            return
        
        for executable_dict in executable_dict_list:
            if executable_dict['ComputingEnvironment'] == computing_environment:
                self.__executable_dict = executable_dict['ExecutableFilePath']      
                break

    # Save executable file PATH settings according to environment as yml file.
    def __save__executable_dict(self, executable_settings_subdir_path):
        if len(self.__executable_dict) > 0:
            # Make a back up of executable file PATH settings directory.
            self.__make_output_subdir_backup(executable_settings_subdir_path)
            assert not os.path.exists(executable_settings_subdir_path), '[EE_ASSERT] The output executable settings subdirectory "{}" must NOT exist at this point of code!'.format(executable_settings_subdir_path)
            os.mkdir(executable_settings_subdir_path)
            executable_settings_yaml_file_path = os.path.join(executable_settings_subdir_path, type(self).__EE_EXECUTABLE_SETTING_YAML_NAME) 
            self.__save_yaml_file(executable_settings_yaml_file_path, self.__executable_dict)
        else:
            assert len(self.__executable_dict) == 0, '[EE_ASSERT] self.__executable_dict should be empty at this point of code!'
            print('[EE_MESSAGE] self.__executable_dict is empty. Please call __construct_executable_dict before calling __save__executable_dict')

    # Make back-up if a file with same name already exists.
    def __make_output_subdir_backup(self, output_subdir_path):
        if os.path.exists(output_subdir_path): 
            print('[EE_MESSAGE]', 'The output subdirectory "{}" already exists! Making a backup of the existing subdirectory...'.format(output_subdir_path))
            dt_now = datetime.datetime.now()
            backup_output_subdir_path = output_subdir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(output_subdir_path, backup_output_subdir_path)
        assert not os.path.exists(output_subdir_path), '[EE_ASSERT] The output subdirectory "{}" must NOT exist at this point of code!'.format(output_subdir_path)

    def __replace_schemes_executable_path(self, template_schemes_dir_path, output_schemes_subdir_path):
        # Check preconditions!
        # Check if template_schemes_dir_path exists.
        assert template_schemes_dir_path, '[EE_ASSERT] The template Schemes directory "{}" must exist!'.format(template_schemes_dir_path)
        if not os.path.exists(template_schemes_dir_path):
            print('[EE_MESSAGE] Error! The template Schemes directory "{}" does NOT exist! Please set the correct PATH using "--s" option.'.format(template_schemes_dir_path))
            return

        # Obtain directory path of this script
        script_dir_path = os.path.dirname(__file__)
        
        # Make a back up of schemes
        self.__make_output_subdir_backup(output_schemes_subdir_path)
        assert not os.path.exists(output_schemes_subdir_path), '[EE_ASSERT] The output Schemes subdirectory "{}" must NOT exist at this point of code!'.format(output_schemes_subdir_path)
        # Create output Schemes directory by copying template Schemes directory 
        shutil.copytree(template_schemes_dir_path, output_schemes_subdir_path)
        
        # File pattern of job star file in template RELION Schemes  
        output_job_star_file_path_pattern = os.path.join(output_schemes_subdir_path, type(self).__JOB_STAR_FILE_PATH_PATTERN)

        config_to_job_star_key_mapping_yaml_file_path = os.path.join(script_dir_path, type(self).__CONFIG_TO_JOB_STAR_KEY_MAPPING_YAML_FILE_NAME)
        config_to_job_star_key_mapping_dict = self.__load_yaml_file(config_to_job_star_key_mapping_yaml_file_path)
        # List keys to change values in the job.star file
        target_job_star_key_list = config_to_job_star_key_mapping_dict.values()

        # Replace values of executable file PATH settings of all job star (job.star) in the specified template Schemes dirctory
        for output_job_star_file_path in glob.glob(output_job_star_file_path_pattern):
            assert os.path.exists(output_job_star_file_path), '[EE_ASSERT] The file "{}" must exist at this point of code!'.format(output_job_star_file_path)
            job_star_line_list = self.__construct_file_line_list(output_job_star_file_path)
            self.__construct_job_star_dict(output_job_star_file_path)
            output_job_star_key_list = self.__job_star_options_dict.keys()
            # Check if keys to change values (target_job_star_key_list) exists in job.star file (= in output_job_star_key_list).
            # If there are duplicate keys between target_job_star_key_list and output_job_star_key_list, add them to the changed_job_star_key_list.
            changed_job_star_key_list = list(set(target_job_star_key_list) & set(output_job_star_key_list))
            
            # If keys to changed value doesn't exist, exit this loop.
            if len(changed_job_star_key_list) == 0:
                print('[EE_MESSAGE] No change                    :{}'.format(output_job_star_file_path))
                continue
            print('[EE_MESSAGE] Rewrite executable file PATH :{}'.format(output_job_star_file_path))
            
            output_job_star_file_contents = None
            with open(output_job_star_file_path, 'r+') as output_job_star_file:
                # Read all contents of file
                output_job_star_file_contents = output_job_star_file.read()
                assert output_job_star_file_contents is not None, '[EE_ASSERT] Something is seriously wrong with either this star file or coding! (output_job_star_file_contents = "{}")'.format(output_job_star_file_contents)
                # Create list to replace the values(two-dimensional array)
                for changed_job_star_key in changed_job_star_key_list:
                    config_key = None
                    #if job_star_options_dict['jobtypelabel'] == 'relion.external':
                    # Separate cases for External job, because External jobs(select3d and cryolo) use same format of job.star
                    if self.__job_star_options_dict['jobtypelabel'] == 'relion.external':
                        if changed_job_star_key == 'fn_exe':
                            if 'select3d' in self.__job_star_options_dict['queuename']:
                                config_key = 'SelectClass3DExecutable'
                            if 'cryolo' in self.__job_star_options_dict['queuename']:
                                config_key = 'CrYOLOExecutable'
                        if changed_job_star_key == 'param1_value':
                            if 'cryolo' in self.__job_star_options_dict['queuename']:
                                config_key = 'CrYOLORepo'
                    else:
                        config_key = [key for key, value in config_to_job_star_key_mapping_dict.items() if value == changed_job_star_key][0]
                    if config_key != None:
                        for job_star_line in job_star_line_list:
                            job_star_line_token_list = job_star_line.split()
                            if len(job_star_line_token_list) == type(self).__N_IDX_JSPEL:     # lines does not have assumed number of tokens!
                                target_job_star_param_key = job_star_line_token_list[type(self).__IDX_JSPEL_KEY]
                                if target_job_star_param_key == changed_job_star_key:
                                    # Assumed format of job star file: The field width of the key/label is 36 characters wide and one white space after the value.
                                    new_job_star_line = '{:36s}{:s}\n'.format(target_job_star_param_key, self.__executable_dict[config_key])
                                    # Replace settings according to all replace pairs
                                    output_job_star_file_contents = output_job_star_file_contents.replace(job_star_line, new_job_star_line)

                        # Delete all contents of the current job star file
                        output_job_star_file.seek(0)
                        output_job_star_file.truncate(0)
                    
                        # Save the result of replacements to the current job star file
                        output_job_star_file.write(output_job_star_file_contents)

    def edit(self, configs_dir_path, template_schemes_dir_path , output_dir_path, computing_environment):
        # [*] configs_dir_path          : Path of input configurations directory containing all configuration yaml files.
        # [*] template_schemes_dir_path : Path of input template RELION Schemes directory containing all Schemes related files.
        # [*] output_dir_path           : Path of output root directroy where all outputs will be saved.
        # [*] computing_environment     : Computing enveironment (eg. Reedbush, GoToCloud)
        if not os.path.exists(output_dir_path):
            print('[EE_MESSAGE] The specified output directory "{}" does not exist yet! Creating the directory'.format(output_dir_path))
            os.mkdir(output_dir_path)
        assert os.path.exists(output_dir_path), '[EE_ASSERT] The output directory "{}" must exist at this point of code!'.format(output_dir_path)

        executable_settings_subdir_path = os.path.join(output_dir_path, type(self).EE_DIR_NAME)
        output_schemes_subdir_path = os.path.join(output_dir_path, type(self).__SCHEMES_DIR_NAME)

        self.__construct_executable_dict(configs_dir_path, computing_environment)
        self.__save__executable_dict(executable_settings_subdir_path)
        self.__replace_schemes_executable_path(template_schemes_dir_path, output_schemes_subdir_path)


if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configs_dir",    type=str,   default='./Configs',    help = 'Path of input configurations directory containing all configuration yaml files.  (Default "./Configs")')
    parser.add_argument("-s", "--schemes_dir",    type=str,   default='./Schemes',    help = 'Path of input template RELION Schemes directory containing all Schemes related files.  (Default "./Schemes")')
    parser.add_argument("-o", "--output_dir",     type=str,   default='../',          help = 'Path of output root directroy where all outputs will be saved.  (default "../")')
    parser.add_argument("-e", "--compute_env",    type=str,   default='Reedbush',     help = 'Computing environment in use.  (default "Reedbush")')
    args = parser.parse_args()
    
    # Rename options for readability
    option_configs_dir_path          = args.configs_dir
    option_template_schemes_dir_path = args.schemes_dir
    option_output_dir_path           = args.output_dir
    option_computing_environment     = args.compute_env
    
    print('[EE_MESSAGE] Specified values of all options')
    print('[EE_MESSAGE]   Input configurations directory path  := {}'.format(option_configs_dir_path))
    print('[EE_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[EE_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[EE_MESSAGE]   Input computing_environment          := {}'.format(option_computing_environment))
    print('[EE_MESSAGE] ')
    print('[EE_MESSAGE] ')
    print('[EE_MESSAGE] Editing executable file PATH of the job.star files in the specified shcemes...')
    print('[EE_MESSAGE] ')
    exeeditor = ExecutablePathEditor()
    exeeditor.edit(option_configs_dir_path, option_template_schemes_dir_path, option_output_dir_path, option_computing_environment)
    print('[EE_MESSAGE] ')
    print('[EE_MESSAGE] ')
    print('[EE_MESSAGE] DONE!')