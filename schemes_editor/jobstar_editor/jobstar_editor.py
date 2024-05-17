#!/usr/bin/env python3.7
##########################################################################################
# Author: Misato Yamamoto  (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023 KEK IMMS SBRC
# 
# Description:
# Simplify setting of parallel computing parameters for RELION Schemes. 
# Parallel computing parameters in all job.star files are replaced by values in yaml config files.
# User set up the values of parallel computing parameters in yaml files. 
# 
##########################################################################################

import yaml
import glob
import os
import shutil
import datetime
import argparse
import subprocess

# ========================================================================================
# Abbreviations:
#   algo      := algorithm
#   dir       := directory
#   config(s) := configuration(s)
#   ext       := extension
#   idx       := Index of ...
#   n         := The number of ...
#   param(s)  := parameter(s)
#   proj      := project
#   ps        := parallel settings, meaning paralle computing parameter settings
#   rpath     := relative path
# 
# Terms:
#   Parameter 'label' is called 'key'.
#   Dictionary 'key' is called as it is
# ========================================================================================

# ========================================================================================
class JobTypeToAlgoTypeHandler:
    # Public class variables
    # Define indices for tokens of a Job Star Parameter Entry Line (JST is abbribiation of "Job Star Token")
    # JobTypeToAlgoTypeConvertor needs these indices
    __I_ENUM = -1
    __I_ENUM += 1; IDX_JST_KEY   = __I_ENUM
    __I_ENUM += 1; IDX_JST_VALUE = __I_ENUM
    __I_ENUM += 1; N_IDX_JST     = __I_ENUM
    
    # <Public Instance Constructor>
    def __init__(self, job_star_param_key, job_star_param_value, algo_type_converted, algo_type_unconverted):
        # Private instance variables
        self.__job_star_param_key    = job_star_param_key
        self.__job_star_param_value  = job_star_param_value
        self.__algo_type_converted   = algo_type_converted
        self.__algo_type_unconverted = algo_type_unconverted

    # <Public Instance Method>
    def handle(self, job_type, job_star_line_list):
        algo_type = None
        # Find the line containing the job_star_param_key
        for job_star_line in job_star_line_list:
            if self.__job_star_param_key in job_star_line:
                job_star_line_token_list = job_star_line.split()
                assert len(job_star_line_token_list) == type(self).N_IDX_JST, '[JSE_ASSERT] Something is seriously wrong with this star file! The token counts of "_rlnJobTypeLabel" line should be always "{}" instead of "{}"!'.format(type(self).N_IDX_JST, len(job_star_line_token_list))
                assert job_star_line_token_list[type(self).IDX_JST_KEY] == self.__job_star_param_key, '[JSE_ASSERT] This should never be False!'
                if self.__job_star_param_value in job_star_line_token_list[type(self).IDX_JST_VALUE]:
                    algo_type = self.__algo_type_converted
                else:
                    algo_type = self.__algo_type_unconverted
                # Successfully found job type! 
                # let's get out of for loop immediately!
                break
        assert algo_type is not None, '[JSE_ASSERT] Something is seriously wrong with either this star file or coding! (algo_type = "{}")'.format(algo_type)
        
        return algo_type

# ========================================================================================
# Implemented as a Singleton Class
# Reference URL: https://qiita.com/KWS_0901/items/4433aa90b4b8a0d7b20e
class JobTypeToAlgoTypeConvertor:
    # Private class variables

    # Singleton Condition 1: 
    #   Define instances of the same type as private class variables.
    #   Use to guarantee that only one instance is created.
    __unique_instance = None
    
    # Private class constants

    # Define indices for tokens of a Job Star Parameter Entry Line
    # Actually index values are defined JobTypeToAlgoTypeHandler
    __IDX_JST_KEY    = JobTypeToAlgoTypeHandler.IDX_JST_KEY
    __IDX_JST_VALUE  = JobTypeToAlgoTypeHandler.IDX_JST_VALUE
    __N_IDX_JST      = JobTypeToAlgoTypeHandler.N_IDX_JST
    __JOBTYPE_TO_ALGOTYPE_ITEM_YAML_FILE_NAME = 'config_jobtype_to_algotype_item.yml'
    
    # Public class variables
    
    ALGO_TYPE_NAME_PREFIX = 'algo_type_'
    # Define indicates that this job type and the associated algorithm type should be ignored since it does not support parallel computing 
#    ALGO_TYPE_IGNORED     = ALGO_TYPE_NAME_PREFIX + 'ignored'
    # Indicates that this algorithm type has not been converted from job type yet but should be
    ALGO_TYPE_UNCONVERTED = ALGO_TYPE_NAME_PREFIX + 'unconverted'
    
    # Private class variables
    
    # Define dictionary holds lists of job-type-to-algorithm-type handlers of all job types
    # which should be seperated into multiple algorithms (e.g. class2d -> class2d_em or class2d_vdam)
    # Each dictionary entry consist of 
    # - KEY   : job type
    # - VALUE : a list of job-type-to-algorithm-type handlers
    __job_type_to_algo_type_handler_list_dict = {}
    
    # Disabled Constructor
    # Singleton Condition 2: 
    #   Constructor visibility is private.
    #   In python, constructors cannot be defined private.
    # Singleton Condition 3: 
    #   Instance acquisition is limited to get_singleton() without constructor invocation.
    #   Do not use __init__ to enable instance acquisition from get_singleton().
    #   __new__ is called before __init__ at initialization.
    def __new__(cls):
        raise NotImplementedError('[JSE_ERROR] This is a singleton class! Not allowed to create instance by constructor!')

    # <Private Class Method> Internal constructor of instance
    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    # <Public Class Method>
    # Singleton Condition 4: 
    # Define a `getInstance()` class method that returns an instance of the same type.
    @classmethod
    def get_singleton(cls):
        # if instance not yet created
        if not cls.__unique_instance:
            cls.__unique_instance = cls.__internal_new__()
            cls.__unique_instance.__construct_job_type_to_algo_type_handler_list_dict()
        
        return cls.__unique_instance

    def __load_yaml_file(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        return yaml_dict

    # <Private Instancd Method> Constructs a list of JobTypeToAlgoTypeHandler for each job type
    # and register to the dictionary where
    #   KEY   : job type
    #   VALUE : a list of JobTypeToAlgoTypeHandler
    # If the assicated list of JobTypeToAlgoTypeHandler is empty, it does not do anything (meaning ignores the job type)!
    def __construct_job_type_to_algo_type_handler_list_dict(self):
        type(self).__job_type_to_algo_type_handler_list_dict = {}
        # create jobtype_to_algotype_dict from yaml file
        script_dir = os.path.dirname(__file__)
        jobtype_to_algotype_dict_list_item_yaml_file_path = os.path.join(script_dir, type(self).__JOBTYPE_TO_ALGOTYPE_ITEM_YAML_FILE_NAME)
        jobtype_to_algotype_dict_list = self.__load_yaml_file(jobtype_to_algotype_dict_list_item_yaml_file_path)
        # Define list of job type which should be sperated into mulitple algorithm types based on key parameter settings.
        for jobtype_to_algotype_dict in jobtype_to_algotype_dict_list:
            job_type = jobtype_to_algotype_dict['JobType']
            job_type_to_algo_type_handler_list = []    # Initialize with empty list
            for joboption_dict in jobtype_to_algotype_dict['JobOption']:
                job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler(joboption_dict['Key'], joboption_dict['Value'], type(self).ALGO_TYPE_NAME_PREFIX + joboption_dict['AlgoTypeName'], type(self).ALGO_TYPE_UNCONVERTED))
            type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list

    # <Public Instancd Method> Convert Job Type defined in a job star file to Algorithm Type for Parallel Settings Editor of RELION Schemes
    def convert(self, job_star_file_path):
        assert os.path.exists(job_star_file_path), '[JSE_ASSERT] The file "{}" must exist at this point of code!'.format(job_star_file_path)
        with open(job_star_file_path, 'r') as job_star_file:
            # Read all lines from this job star file while removing all leading and trailing whitespaces from each line
            # NOTE: 2023/05/02 Toshio Moriya
            # The orignal job_star_line should be kept in job_star_line_list, especailly including tailing white space 
            # If job_star_line is stripped here, white space will be increased at the end of lines to be replaced
            # job_star_line_list = [job_star_line.strip() for job_star_line in job_star_file.readlines()]
            job_star_line_list = [job_star_line for job_star_line in job_star_file.readlines()]
        assert len(job_star_line_list) > 0, '[JSE_ASSERT] The star file "{}" contains no lines! Something is seriously wrong with this star file!'.format(job_star_file_path)
        
        # Extract job type of this job star file
        job_type = None
        for job_star_line in job_star_line_list:
            if '_rlnJobTypeLabel' in job_star_line:
                job_star_line_token_list = job_star_line.split()
                assert len(job_star_line_token_list) == type(self).__N_IDX_JST, '[JSE_ASSERT] Something is seriously wrong with this star file! The token counts of "_rlnJobTypeLabel" line should be always "{}" in stead of "{}"!'.format(type(self).__N_IDX_JST, len(job_star_line_token_list))
                job_type = job_star_line_token_list[type(self).__IDX_JST_VALUE]
                # Successfully found job type! 
                # let's get out of for loop immediately!
                break
        assert job_type is not None, '[JSE_ASSERT] Something is seriously wrong with either this star file or coding! (job_type = "{}")'.format(job_type)
        
        # Define and initialize return value
        algo_type = None
        
        # Check if this job type is NOT in the list of JobTypeToAlgoTypeHandler
        # meaning this job type does not need to be sperated into multiple algorithm types
        if job_type not in type(self).__job_type_to_algo_type_handler_list_dict:
#            print('[JSE_MESSAGE] Found a job type "{}" that should not be converted'.format(job_type))
            # convert job-type-to-algorithm-type
            assert 'relion.' in job_type, '[JSE_ASSERT] Invalid assumption where all RELION job types are in the form of "relion.*" instead of "{}"!'.format(job_type)
            # Possoble format of RELION job type keys
            # relion.job_type (e.g. relion.class3d)
            # relion.job_type.sub_job_type  (e.g. relion.select.onvalue)
            algo_type = job_type.replace('relion.', type(self).ALGO_TYPE_NAME_PREFIX).replace('.', '_')
        else:
            job_type_to_algo_type_handler_list = type(self).__job_type_to_algo_type_handler_list_dict[job_type]
            # Check if this job type and the associated algorithm type should be ignored since it does not support parallel computing 
            if len(job_type_to_algo_type_handler_list) > 0:
#                print('[JSE_MESSAGE] Found a job type "{}" that should be converted'.format(job_type))
                for job_type_to_algo_type_handler in job_type_to_algo_type_handler_list:
                    algo_type = job_type_to_algo_type_handler.handle(job_type, job_star_line_list)
                    if algo_type != type(self).ALGO_TYPE_UNCONVERTED:
                        # This job type is handled, meaning successfully converted! 
                        # let's get out of for loop immediately!
                        break
            else: 
                assert len(job_type_to_algo_type_handler_list) == 0, '[JSE_ASSERT] Something is seriously wrong with coding!'
#                print('[JSE_MESSAGE] Found a job type "{}" that should be ignored'.format(job_type))
#                algo_type = type(self).ALGO_TYPE_IGNORED
        assert algo_type is not None, '[JSE_ASSERT] Something is seriously wrong with this coding! (algo_type = "{}")'.format(algo_type)
        assert algo_type != type(self).ALGO_TYPE_UNCONVERTED, '[JSE_ASSERT] Something is seriously wrong with this coding! (algo_type = "{}")'.format(algo_type)
        
        return algo_type, job_star_file_path

# ========================================================================================
# Directory structure
# 
# - Script Directory 
#   |-- jobstar_editor
#     |-- jobstar_editor.py
#     |-- config_to_job_star_key_mapping_ps.yml
#     |-- config_to_job_star_key_mapping_sys.yml
# 
# - Configs Directory # A sample of configurations directory (Use this as a template to create user-defined configurations)
#     |-- config_type_algo_xx.yml
#     |-- config_type_algo_xx.yml
#     |-- config_level_submission.yml
#     |-- config_level_device.yml
#     |-- config_level_algo.yml
#     |-- config_system_settings_xx.yml
#  
# - Schemes template Directory              <<<< a sample of template schemes directory (Use this as a template to create user-defined schemes)
#     |-- **                <<<< a single scheme directoy
#       |-- **              <<<< a job directory of the single scheme
#         |- job.star       <<<< a job star file of the single scheme
# 
# - <INPUT> User-Defined Configurations file 
#   |-- config_type_algo_xx.yml
#   |-- config_system_settings.yml
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
#   |-- jobstar_settings    <<<< An output directory to be created. It will contain the paralle setting files of all algorithm types.
#     |-- js_algo_type_*    <<<< Output a parallel setting file of a single algorithm type
# 
# ========================================================================================
class JobStarEditor:
    # Private class constants
    
    __YAML_FILE_EXT = '.yml'
    
    # Define indices for entries of __CONFIG_LEVEL_YAML_INFO_LIST (CLYI is abbribiation of "Cofig Level YAML Info")
    __I_ENUM = -1
    __I_ENUM += 1; __IDX_CLYI_FILE_NAME = __I_ENUM
    __I_ENUM += 1; __IDX_CLYI_KEY       = __I_ENUM
    __I_ENUM += 1; __N_IDX_CLYI         = __I_ENUM
    
    # Define list of config level yaml information
    __CONFIG_LEVEL_YAML_INFO_LIST = []
    __CONFIG_LEVEL_YAML_INFO_LIST.append(['config_level_submission' + __YAML_FILE_EXT, 'SubmissionLevel' ])
    __CONFIG_LEVEL_YAML_INFO_LIST.append(['config_level_device' + __YAML_FILE_EXT,     'DeviceLevel'     ])
    __CONFIG_LEVEL_YAML_INFO_LIST.append(['config_level_algo' + __YAML_FILE_EXT,       'AlgoLevel'       ])
    
    # __CONFIG_ALGO_TYPE_YAML_FILE_NAME = 'config_type_algo' + __YAML_FILE_EXT
    # __CONFIG_TO_JOB_STAR_KEY_MAPPING_YAML_FILE_NAME = 'config_to_job_star_key_mapping_sys' + __YAML_FILE_EXT
    
    __ALGO_TYPE_KEY = 'AlgoType'
    __ALGO_TYPE_NAME_PREFIX = JobTypeToAlgoTypeConvertor.ALGO_TYPE_NAME_PREFIX
    
    __JS_KEY          = 'Settings'
    __JS_DIR_NAME     = 'jobstar_settings'
    __JS_LEVEL_COMB_KEY     = 'CombinationSettings'
    __JS_LEVEL_FILE_KEY     = 'LevelFile'
    __JS_FILE_PREFIX  = 'js_'    # Abbreviations of "jobstar settings"
    
    __JOBSTAR_SETTINGS_LIST_YAML_FILE_NAME = __JS_FILE_PREFIX + __ALGO_TYPE_NAME_PREFIX + 'all_list' + __YAML_FILE_EXT
    
    __SCHEMES_DIR_NAME             = 'Schemes'  # Name of RELION Schemes Directory
    __JOB_STAR_FILE_RPATH_PATTERN  = '**/**/job.star'  # Relative to Relion Project Directory
    __ERROR_FILE_NAME              = 'error_output.txt'
    __JOBSTAR_EDITOR_ERROR_FILE_NAME  =  __JS_FILE_PREFIX + __ERROR_FILE_NAME

    # Define indices for tokens of each Job Star Parameter Entry line (JSPEL is abbribiation of "Job Star Parameter Entry Line")
    __I_ENUM = -1
    __I_ENUM += 1; __IDX_JSPEL_KEY   = __I_ENUM
    __I_ENUM += 1; __IDX_JSPEL_VALUE = __I_ENUM
    __I_ENUM += 1; __N_IDX_JSPEL     = __I_ENUM
    
    # Constructor
    def __init__(self):
        # Private instance variables
        # Holds a list of all algorithm type dictionaries 
        self.__jobstar_config_dict_list= []
    # <Private Helper Instance Method> Load yaml file and keep the contents as a dictionary 
    def __load_yaml_file(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        return yaml_dict
    
    # <Private Helper Instance Method> Save a dictionary as a yaml file
    def __save_yaml_file(self, yaml_file_path, yaml_dict):
        with open(yaml_file_path, "w") as yaml_file:
            yaml.safe_dump(yaml_dict, yaml_file, sort_keys=False)
    
    # <Private Helper Instance Method> Backup an output subdirectory
    def __make_output_subdir_backup(self, output_subdir_path):
        if os.path.exists(output_subdir_path): 
            print('[JSE_MESSAGE]', 'The output subdirectory "{}" already exists! Making a backup of the existing subdirectory...'.format(output_subdir_path))
            dt_now = datetime.datetime.now()
            backup_output_subdir_path = output_subdir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(output_subdir_path, backup_output_subdir_path)
        assert not os.path.exists(output_subdir_path), '[JSE_ASSERT] The output subdirectory "{}" must NOT exist at this point of code!'.format(output_subdir_path)

    # <Private Instance Method> Create a dictionary for each algorithm from the parallel settings defined in the config files. 
    # Then, combine individual algorithm dictionaries as a single list of all algorithm dictionaries
    # and keep the list as an instance variable
    def __create_jobstar_config_dict_list(self, configs_file_path):
        # configs_dir_path: a path of directory containing all configuration yaml files
        # configs_file_path : a path of configuration yaml files
        # Check preconditions!
        # NOTE: 2023/05/01 Toshio Moriya
        # Actually this should be error check instead of assertion!
        assert os.path.exists(configs_file_path), '[JSE_ASSERT] The configurations file "{}" must exist!'.format(configs_file_path)
        
        # Reinitialize the list of all algorithm dictionaries
        if len(self.__jobstar_config_dict_list) > 0:
#            print('[JSE_MESSAGE] Reinitializing the list of all algorithm dictionaries...')
            self.__jobstar_config_dict_list = []
        assert len(self.__jobstar_config_dict_list) == 0, '[JSE_ASSERT] self.__jobstar_config_dict_list should be empty instead of containing "{}" dictionaries at this point code! Something is seriously wrong with this coding!'.format(len(self.__jobstar_config_dict_list))
        
        # Structure of algo_type_dict_dict
        #   algo_type_dict_dict := {AlgoType:*, algo_type_dict}
        #   algo_type_dict      := {SubmissionLevel:*, DeviceLevel:*, AlgoLevel:*}
        #   config_algo_type_yaml_file_path = os.path.join(configs_dir_path, type(self).__CONFIG_ALGO_TYPE_YAML_FILE_NAME)
        config_algo_type_yaml_file_path = configs_file_path
        algo_type_dict_dict = self.__load_yaml_file(config_algo_type_yaml_file_path)
        algo_type_key =[type(self).__JS_LEVEL_COMB_KEY, type(self).__JS_LEVEL_FILE_KEY]
        if type(algo_type_dict_dict) == list:
            self.__jobstar_config_dict_list = algo_type_dict_dict
        else:    
            if set(algo_type_key) == set(algo_type_dict_dict.keys()): 
                algo_type_dict_list = algo_type_dict_dict[type(self).__JS_LEVEL_COMB_KEY]
                for algo_type_dict in algo_type_dict_list:
                    all_level_algo_type_dict = {}
                    all_level_config_settings_dict = {}
                    for config_level_yaml_info_key in algo_type_dict_dict[type(self).__JS_LEVEL_FILE_KEY].keys():
                        config_level_yaml_file_path = algo_type_dict_dict[type(self).__JS_LEVEL_FILE_KEY][config_level_yaml_info_key]
                        config_level_key       = config_level_yaml_info_key
                        config_level_value     = algo_type_dict[config_level_key]
                        # Structure of config_level_dict_dict
                        #   config_level_dict_dict := {*Level:*, config_level_dict}
                        #   config_level_dict      := {Settings: {CONFIG_LEVEL_PARAM_A:*, CONFIG_LEVEL_PARAM_B:*, CONFIG_LEVEL_PARAM_C:*, ...}}
                        #   config_level_yaml_file_path = os.path.join(configs_dir_path, config_level_yaml_name)
                        config_level_dict_dict = self.__load_yaml_file(config_level_yaml_file_path)
                        # Extract configuraltion of each level and merge them
                        for config_level_dict in config_level_dict_dict:
                            if config_level_dict[config_level_key] == config_level_value:
                                all_level_algo_type_dict.update(config_level_dict)
                                all_level_config_settings_dict.update(config_level_dict[type(self).__JS_KEY])
                    jobstar_config_dict = {**algo_type_dict, **all_level_algo_type_dict, type(self).__JS_KEY:{**all_level_config_settings_dict}}
                    self.__jobstar_config_dict_list.append(jobstar_config_dict)
            else:
                print('[JSE_ERROR] Config yaml file structure is wrong...')

    # <Private Instance Method> Save the parameter settings as yml files
    def __save_jobstar_config_dict_list(self, jobstar_settings_subdir_path):
        if len(self.__jobstar_config_dict_list) > 0:
            self.__make_output_subdir_backup(jobstar_settings_subdir_path)
            assert not os.path.exists(jobstar_settings_subdir_path), '[JSE_ASSERT] The output paralle settings subdirectory "{}" must NOT exist at this point of code!'.format(jobstar_settings_subdir_path)
            os.mkdir(jobstar_settings_subdir_path)
            for jobstar_config_dict in self.__jobstar_config_dict_list: 
                jobstar_setting_yaml_file_name = type(self).__JS_FILE_PREFIX + jobstar_config_dict[type(self).__ALGO_TYPE_KEY] + type(self).__YAML_FILE_EXT
                jobstar_setting_yaml_file_path = os.path.join(jobstar_settings_subdir_path, jobstar_setting_yaml_file_name)
                self.__save_yaml_file(jobstar_setting_yaml_file_path, jobstar_config_dict)
            jobstar_setting_list_yaml_file_path = os.path.join(jobstar_settings_subdir_path, type(self).__JOBSTAR_SETTINGS_LIST_YAML_FILE_NAME)
            self.__save_yaml_file(jobstar_setting_list_yaml_file_path, self.__jobstar_config_dict_list)
        else:
            assert len(self.__jobstar_config_dict_list) == 0, '[JSE_ASSERT] self.__jobstar_config_dict_list should be empty at this point of code!'
            print('[JSE_MESSAGE] self.__jobstar_config_dict_list is empty. Please call __create_jobstar_config_dict_list() before calling __save_jobstar_config_dict_list')
    
    # If some error occours during command execution, the error file is created and error messerges are written. 
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

    # <Private Instance Method> Replace values of paralle settings of all job star (job.star) in the specified template Schemes dirctory
    # and save the results to the output Schemes directory.
    def __replace_schemes_jobstar_settings(self, output_dir_path, output_schemes_subdir_path, job_star_key_mapping_file_path):
        # Obtain directory path of this script
        # script_dir_path = os.path.dirname(__file__)
        # Create JobTypeToAlgoTypeConvertor (Singleton Class)
        job_type_to_algo_type_convertor = JobTypeToAlgoTypeConvertor.get_singleton()
        # File pattern of job star file in tempate RELION Schemes  
        output_job_star_file_path_pattern = os.path.join(output_schemes_subdir_path, type(self).__JOB_STAR_FILE_RPATH_PATTERN)
        # Replace values of paralle settings of all job star (job.star) in the specified template Schemes dirctory
        # Create key mapping dictionry to link keys in config yaml file to the keys in job.star file
        # config_to_job_star_key_mapping_yaml_file_path = os.path.join(script_dir_path, type(self).__CONFIG_TO_JOB_STAR_KEY_MAPPING_YAML_FILE_NAME)
        config_to_job_star_key_mapping_dict = self.__load_yaml_file(job_star_key_mapping_file_path)

        # Create Relion Command list to replace the values of job.star  
        error_output_file = os.path.join(output_dir_path, type(self).__JOBSTAR_EDITOR_ERROR_FILE_NAME)
        for output_job_star_file_path in glob.glob(output_job_star_file_path_pattern):
            assert os.path.exists(output_job_star_file_path), '[JSE_ASSERT] The file "{}" must exist at this point of code!'.format(output_job_star_file_path)
            algo_type, job_star_file_path = job_type_to_algo_type_convertor.convert(output_job_star_file_path)

#            jobstar_config_dict = [jobstar_config_dict for jobstar_config_dict in self.__jobstar_config_dict_list if jobstar_config_dict[type(self).__ALGO_TYPE_KEY] == algo_type][0]
            # Create list of relion_pipeliner command to replace the values in job.star with the value in self.__jobstar_config_dict_list.
            for jobstar_config_dict in self.__jobstar_config_dict_list:
                if jobstar_config_dict[type(self).__ALGO_TYPE_KEY] == algo_type:
                    for settings_key in jobstar_config_dict[type(self).__JS_KEY].keys():
                        edit_option = config_to_job_star_key_mapping_dict[settings_key]
                        edit_value = jobstar_config_dict[type(self).__JS_KEY][settings_key]
#                        if 'NOT_APPLICABLE' not in edit_value:
                        relion_command = 'relion_pipeliner --editJob ' + str(job_star_file_path) + ' --editOption ' + str(edit_option) + ' --editValue ' + str(edit_value)
#                        print('[JSE_MESSAGE] Replace the values in the job.star file with the following relion command')
#                        print('[JSE_MESSAGE] {}'.format(relion_command))
                        # Replace the values in job.star by running Relion command
                        self.__execute_command(relion_command, error_output_file)

    # <Public Instance Method> Edit paralle settings of all job star (job.star) in the specified template Schemes dirctory 
    # by replacing the values with specified in config yaml files.
    # and save the results to the output Schemes directory.

    def make_output_schemes(self, template_schemes_dir_path, output_dir_path):
        # Check preconditions!
        # NOTE: 2023/05/01 Toshio Moriya
        # Actually these should be error checks instead of assertions!
        assert os.path.exists(template_schemes_dir_path), '[JSE_ASSERT] The template Schemes directory "{}" must exist!'.format(template_schemes_dir_path)
        assert template_schemes_dir_path, '[JSE_ASSERT] The template Schemes directory "{}" must NOT exist!'.format(template_schemes_dir_path)
        # NOTE: 2023/05/03 Toshio Moriya
        # Removed the following requirement to allow the users to name the template_schemes_dir as they like
        # assert os.path.basename(os.path.normpath(template_schemes_dir_path)) == type(self).__SCHEMES_DIR_NAME, '[JSE_ASSERT] The specified template Schemes directory "{}" is invalid! It must end with "{}"!'.format(template_schemes_dir_path, type(self).__SCHEMES_DIR_NAME)

        output_schemes_subdir_path = os.path.join(output_dir_path, type(self).__SCHEMES_DIR_NAME)
        # Make a back up of schemes
        self.__make_output_subdir_backup(output_schemes_subdir_path)
        assert not os.path.exists(output_schemes_subdir_path), '[JSE_ASSERT] The output Schemes subdirectory "{}" must NOT exist at this point of code!'.format(output_schemes_subdir_path)
        
        # Create output Schemes directory by copying template Schemes directory 
        shutil.copytree(template_schemes_dir_path, output_schemes_subdir_path)
        return output_schemes_subdir_path

    def edit(self, configs_file_path, job_star_key_mapping_file_path, output_dir_path, output_schemes_subdir_path, settings_subdir_name = __JS_DIR_NAME):
        # [*] configs_dir_path: a path of directory containing all configuration yaml files
        # [*] template_schemes_dir_path: a path of tempate RELION Schemes directory 
        # [*] output_dir_path: a path of output directory.
        #     Under this directory the following subdirecties will be created 
        #     - Output "Schemes" subdirectroy and related files based on the template "Schemes" 
        #     - Output "ParallelSettings" subdirectroy and parallel settings files of all algorithm types 
        
        # Check preconditions!
        # NOTE: 2023/05/01 Toshio Moriya
        # Actually these should be error checks instead of assertion!
        assert os.path.exists(configs_file_path), '[JSE_ASSERT] The configurations file "{}" must exist!'.format(configs_file_path)
        assert os.path.exists(job_star_key_mapping_file_path), '[JSE_ASSERT] The configurations file "{}" must exist!'.format(job_star_key_mapping_file_path)
        #assert os.path.exists(template_schemes_dir_path), '[JSE_ASSERT] The template Schemes directory "{}" must exist!'.format(template_schemes_dir_path)
        # NOTE: 2023/05/03 Toshio Moriya
        # Removed the following requirement to allow the users to name the template_schemes_dir as they like
        # assert os.path.basename(os.path.normpath(template_schemes_dir_path)) == type(self).__SCHEMES_DIR_NAME, '[JSE_ASSERT] The specified template Schemes directory "{}" is invalid! It must end with "{}"!'.format(template_schemes_dir_path, type(self).__SCHEMES_DIR_NAME)
        
        if not os.path.exists(output_dir_path):
            print('[JSE_MESSAGE] The specified output directory "{}" does not exist yet! Creating the directory'.format(output_dir_path))
            os.mkdir(output_dir_path)
        assert os.path.exists(output_dir_path), '[JSE_ASSERT] The output directory "{}" must exist at this point of code!'.format(output_dir_path)
        
        #  Set instance variables
        jobstar_settings_subdir_path = os.path.join(output_dir_path, settings_subdir_name)
        self.__create_jobstar_config_dict_list(configs_file_path)
        self.__save_jobstar_config_dict_list(jobstar_settings_subdir_path)
        self.__replace_schemes_jobstar_settings(output_dir_path, output_schemes_subdir_path, job_star_key_mapping_file_path)


if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configs_file",   type=str,    required=True,    help = 'Path of input configuration yaml file. This option is always required.')
    parser.add_argument("-k", "--key_map_file",   type=str,    required=True,    help = 'Path of job.star key mapping yaml file. This option is always required.')
    parser.add_argument("-s", "--schemes_dir",    type=str,    required=True,    help = 'Path of input template RELION Schemes directory containing all Schemes related files. This option is always required.')
    parser.add_argument("-o", "--output_dir",     type=str,    default='./',     help = 'Path of output root directroy where all outputs will be saved. (default is set to current directory "./")')

    args = parser.parse_args()
    ### args, unknown = parser.parse_known_args()
    # Rename arguments for readability
    # No arguments with this program
    # Rename options for readability
    option_configs_file_path              = args.configs_file
    option_job_star_key_mapping_file_path = args.key_map_file
    option_template_schemes_dir_path      = args.schemes_dir
    option_output_dir_path                = args.output_dir
    
    print('[JSE_MESSAGE] Specified values of all options')
    print('[JSE_MESSAGE]   Input configurations file path   := {}'.format(option_configs_file_path))
    print('[JSE_MESSAGE]   Input key mapping file path      := {}'.format(option_job_star_key_mapping_file_path))
    print('[JSE_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[JSE_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[JSE_MESSAGE] ')
    print('[JSE_MESSAGE] Editing job.star settings of all job.star files in the specified shcemes...')
    js_editor = JobStarEditor()
    output_schemes_subdir_path = js_editor.make_output_schemes(option_template_schemes_dir_path, option_output_dir_path)
    js_editor.edit(option_configs_file_path, option_job_star_key_mapping_file_path, option_output_dir_path, output_schemes_subdir_path)
    print('[JSE_MESSAGE] ')
    print('[JSE_MESSAGE] DONE!')
