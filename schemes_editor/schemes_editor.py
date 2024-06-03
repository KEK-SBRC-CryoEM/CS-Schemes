#!/usr/bin/env python3.7
##########################################################################################
# Author: Misato Yamamoto  (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023 KEK IMMS SBRC
# 
# Description:
# Simplify setting of parameters for RELION Schemes. 
# The parameters in all job.star files are replaced by values in yaml config files.
# User set up the values of setting in yaml files. 
# Administrator must set the environment variable <CS_SETTING_FILE_PATH>. It is recommended to set this variable in the .bashrc file.
##########################################################################################
# ========================================================================================
# Directory structure
# 
# - Script Directory 
#   |-- jobstar_editor
#     |-- jobstar_editor.py
#     |-- config_jobtype_to_algotype_item.yml
#     |-- config_to_job_star_key_mapping_ps.yml
#     |-- config_to_job_star_key_mapping_sys.yml
#   |-- schemestar_editor
#     |-- schemestar_editor.py
#  
# - Configs Directory   # A sample of configurations directory (Use this as a template to create user-defined configurations)
#    |-- config_setting_file_path.yml
#    |-- config_em_settings.yml
#    |-- config_sample_settings_xx.yml
#    |-- config_type_algo_xx.yml
#    |-- config_type_algo_xx.yml
#    |-- config_level_submission.yml
#    |-- config_level_device.yml
#    |-- config_level_algo.yml
#    |-- config_system_settings_xx.yml
#
# -  Schemes template Directory 
#    |-- Schemes             <<<< a sample of template schemes directory (Use this as a template to create user-defined schemes)
#      |-- **                <<<< a single scheme directoy
#        |-- scheme.star     <<<< a scheme star file per the single scheme   
#        |-- **              <<<< a job directory of the single scheme
#          |- job.star       <<<< a job star file of the single scheme
# 
# - <INPUT> User-Defined Environment variables
#     export CS_SETTING_FILE_PATH = /path/to/config_setting_file_path.yml
#
# - <INPUT> User-Defined Configurations Directory 
#   |-- configs              # A sample of configurations directory (Use this as a template to create user-defined configurations)
#     |-- config_em_settings_xx.yml
#     |-- config_sample_settings.yml
#     |-- config_type_algo_xx.yml
#     |-- config_type_algo_xx.yml
#     |-- config_system_settings_xx.yml
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
#   |-- jobstar_settings    <<<< An output directory to be created. It will contain the paralle setting files of all algorithm types.
#     |-- js_algo_type_*    <<<< Output a parallel setting file of a single algorithm type
# ========================================================================================


import yaml
import os
import shutil
import datetime
import argparse
from jobstar_editor import jobstar_editor
from schemestar_editor import schemestar_editor


class SchemesEditor():
    # Constructors
    __SE_DEFAULT_FILE_KEY         = 'DefaultFile'
    __SE_PARALLEL_SETTING_KEY     = 'ParallelSettings'
    __SE_SYSTEM_SETTING_KEY       = 'SystemSettings'
    __SE_EM_SETTING_KEY           = 'EmSettings'
    __SE_SAMPLE_SETTING_KEY       = 'SampleSettings'
    __SCHEMES_DIR_NAME            = 'Schemes'
    __JOB_STAR_KEY_MAPPING_PS_YAML_FILE_NAME = 'config_to_job_star_key_mapping_ps.yml'
    __JOB_STAR_KEY_MAPPING_SYS_YAML_FILE_NAME = 'config_to_job_star_key_mapping_sys.yml'
    __JOBSTAR_EDITOR_DIR          = 'jobstar_editor'
    __PARALLEL_SETTINGS_DIR_NAME  = 'parallel_settings'
    __SYSTEM_SETTINGS_DIR_NAME    = 'system_settings'
    __SAMPLE_SETTINGS_DIR_NAME    = 'sample_settings'
    __EM_SETTINGS_DIR_NAME        = 'em_settings'
    __SETTING_FILE_PATH_ENV_VAR   = 'CS_SETTING_FILE_PATH'

    def __load_yaml_file(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        return yaml_dict

    def __make_output_subdir_backup(self, output_subdir_path):
        if os.path.exists(output_subdir_path): 
            print('[SE_MESSAGE]', 'The output subdirectory "{}" already exists! Making a backup of the existing subdirectory...'.format(output_subdir_path))
            dt_now = datetime.datetime.now()
            backup_output_subdir_path = output_subdir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(output_subdir_path, backup_output_subdir_path)
        assert not os.path.exists(output_subdir_path), '[SE_ASSERT] The output subdirectory "{}" must NOT exist at this point of code!'.format(output_subdir_path)

    def __make_output_schemes(self, template_schemes_dir_path, output_dir_path):
        # Check preconditions!
        # Check if template_schemes_dir_path exists.
        assert template_schemes_dir_path, '[SE_ASSERT] The template Schemes directory "{}" must exist!'.format(template_schemes_dir_path)
        if not os.path.exists(template_schemes_dir_path):
            print('[SE_MESSAGE] Error! The template Schemes directory "{}" does NOT exist! Please set the correct PATH using "--s" option.'.format(template_schemes_dir_path))
            return
        
        output_schemes_subdir_path = os.path.join(output_dir_path, type(self).__SCHEMES_DIR_NAME)
        # Make a back up of schemes
        self.__make_output_subdir_backup(output_schemes_subdir_path)
        assert not os.path.exists(output_schemes_subdir_path), '[EE_ASSERT] The output Schemes subdirectory "{}" must NOT exist at this point of code!'.format(output_schemes_subdir_path)
        # Create output Schemes directory by copying template Schemes directory 
        shutil.copytree(template_schemes_dir_path, output_schemes_subdir_path)
        return output_schemes_subdir_path
    
    def edit(self, template_schemes_dir_path, output_dir_path, parallel_setting_file_path = None, system_setting_file_path = None , sample_setting_file_path = None, em_setting_file_path = None):

        # [*] default_setting_file_path: a path of default setting file set in environment variables
        # [*] template_schemes_dir_path: a path of tempate RELION Schemes directory 
        # [*] output_dir_path: a path of output directory.
        #     Under this directory the following subdirecties will be created 
        #     - Output "Schemes" subdirectroy and related files based on the template "Schemes" 
        #     - Output "ParallelSettings" subdirectroy and parallel settings files of all algorithm types 
        
        if not os.path.exists(output_dir_path):
            print('[SE_MESSAGE] The specified output directory "{}" does not exist yet! Creating the directory'.format(output_dir_path))
            os.mkdir(output_dir_path)
        assert os.path.exists(output_dir_path), '[SE_ASSERT] The output directory "{}" must exist at this point of code!'.format(output_dir_path)

        script_dir = os.path.dirname(__file__)
        job_star_key_mapping_ps_yaml_file_path = os.path.join(script_dir, type(self).__JOBSTAR_EDITOR_DIR, type(self).__JOB_STAR_KEY_MAPPING_PS_YAML_FILE_NAME)
        job_star_key_mapping_sys_yaml_file_path = os.path.join(script_dir, type(self).__JOBSTAR_EDITOR_DIR, type(self).__JOB_STAR_KEY_MAPPING_SYS_YAML_FILE_NAME)

        # Execute Schemes editing
        output_schemes_subdir_path = self.__make_output_schemes(template_schemes_dir_path, output_dir_path)

        js_editor = jobstar_editor.JobStarEditor()
        ss_editor = schemestar_editor.SchemeStarEditor()

        # Create setting yaml file path
        default_setting_file_path = os.environ[type(self).__SETTING_FILE_PATH_ENV_VAR]
        # Generate default file paths from yaml file settings
        setting_file_path_dict = self.__load_yaml_file(default_setting_file_path)
        
        if parallel_setting_file_path == None:
            js_editor.edit(setting_file_path_dict[type(self).__SE_DEFAULT_FILE_KEY][type(self).__SE_PARALLEL_SETTING_KEY], job_star_key_mapping_ps_yaml_file_path, output_dir_path, output_schemes_subdir_path, type(self).__PARALLEL_SETTINGS_DIR_NAME)
        else:
            js_editor.edit(parallel_setting_file_path, job_star_key_mapping_ps_yaml_file_path, output_dir_path, output_schemes_subdir_path, type(self).__PARALLEL_SETTINGS_DIR_NAME)
        
        if system_setting_file_path == None:
            js_editor.edit(setting_file_path_dict[type(self).__SE_DEFAULT_FILE_KEY][type(self).__SE_SYSTEM_SETTING_KEY], job_star_key_mapping_sys_yaml_file_path, output_dir_path, output_schemes_subdir_path, type(self).__SYSTEM_SETTINGS_DIR_NAME)
        else:
            js_editor.edit(system_setting_file_path, job_star_key_mapping_sys_yaml_file_path, output_dir_path, output_schemes_subdir_path, type(self).__SYSTEM_SETTINGS_DIR_NAME)
        
        if sample_setting_file_path == None:
            ss_editor.edit(setting_file_path_dict[type(self).__SE_DEFAULT_FILE_KEY][type(self).__SE_SAMPLE_SETTING_KEY], output_dir_path, output_schemes_subdir_path, type(self).__SAMPLE_SETTINGS_DIR_NAME)
        else: 
            ss_editor.edit(sample_setting_file_path, output_dir_path, output_schemes_subdir_path, type(self).__SAMPLE_SETTINGS_DIR_NAME)
        
        if em_setting_file_path == None:
            ss_editor.edit(setting_file_path_dict[type(self).__SE_DEFAULT_FILE_KEY][type(self).__SE_EM_SETTING_KEY], output_dir_path, output_schemes_subdir_path, type(self).__EM_SETTINGS_DIR_NAME)
        else:
            ss_editor.edit(em_setting_file_path, output_dir_path, output_schemes_subdir_path, type(self).__EM_SETTINGS_DIR_NAME)


if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-s",   "--schemes_dir",   type=str, required=True, help = 'Path of input template RELION Schemes directory containing all Schemes related files. This option is always required.')
    parser.add_argument("-sam", "--sample_file",   type=str, default= None, help = 'Path of input sample settig yaml file. (The default path is set to the yamal file)')
    parser.add_argument("-ps",  "--parallel_file", type=str, default= None, help = 'Path of input parallel settig yaml file. (The default path is set to the yamal file)')
    parser.add_argument("-em",  "--em_file",       type=str, default= None, help = 'Path of input em settig yaml file. (The default path is set to the yamal file)')
    parser.add_argument("-sys", "--system_file",   type=str, default= None, help = 'Path of input system settig yaml file. (The default path is set to the yamal file)')
    parser.add_argument("-o",   "--output_dir",    type=str, default='./',  help = 'Path of output root directroy where all outputs will be saved. (default is set to current directory "./")')

    # Rename arguments for readability
    # No arguments with this program
    # Rename options for readability
    args = parser.parse_args()
    option_template_schemes_dir_path  = args.schemes_dir
    option_sample_setting_file_path   = args.sample_file
    option_parallel_setting_file_path = args.parallel_file
    option_em_setting_file_path       = args.em_file
    option_system_setting_file_path   = args.system_file
    option_output_dir_path            = args.output_dir
  
    print('[SE_MESSAGE] Specified values of all options')
    print('[SE_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[SE_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] Editing settings in the specified schemes...')
    se_editor = SchemesEditor()
    se_editor.edit(option_template_schemes_dir_path, option_output_dir_path, option_parallel_setting_file_path, option_system_setting_file_path, option_sample_setting_file_path, option_em_setting_file_path)
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] DONE!')