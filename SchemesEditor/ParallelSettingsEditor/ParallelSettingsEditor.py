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
                assert len(job_star_line_token_list) == type(self).N_IDX_JST, '[PS_ASSERT] Something is seriously wrong with this star file! The token counts of "_rlnJobTypeLabel" line should be always "{}" instead of "{}"!'.format(type(self).N_IDX_JST, len(job_star_line_token_list))
                assert job_star_line_token_list[type(self).IDX_JST_KEY] == self.__job_star_param_key, '[PS_ASSERT] This should never be False!'
                if self.__job_star_param_value in job_star_line_token_list[type(self).IDX_JST_VALUE]:
                    algo_type = self.__algo_type_converted
                else:
                    algo_type = self.__algo_type_unconverted
                # Successfully found job type! 
                # let's get out of for loop immediately!
                break
        assert algo_type is not None, '[PS_ASSERT] Something is seriously wrong with either this star file or coding! (algo_type = "{}")'.format(algo_type)
        
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
    
    # Public class variables
    
    ALGO_TYPE_NAME_PREFIX = 'algo_type_'
    # Define indicates that this job type and the associated algorithm type should be ignored since it does not support parallel computing 
    ALGO_TYPE_IGNORED     = ALGO_TYPE_NAME_PREFIX + 'ignored'
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
        raise NotImplementedError('[PS_ERROR] This is a singleton class! Not allowed to create instance by constructor!')

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

    # <Private Instancd Method> Constructs a list of JobTypeToAlgoTypeHandler for each job type
    # and register to the dictionary where
    #   KEY   : job type
    #   VALUE : a list of JobTypeToAlgoTypeHandler
    # If the assicated list of JobTypeToAlgoTypeHandler is empty, it does not do anything (meaning ignores the job type)!
    def __construct_job_type_to_algo_type_handler_list_dict(self):
        type(self).__job_type_to_algo_type_handler_list_dict = {}
        
        # Define list of job type which should be sperated into mulitple algorithm types based on key parameter settings.
        job_type = 'relion.class3d'
        job_type_to_algo_type_handler_list = []    # Initialize with empty list
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('dont_skip_align', 'Yes', type(self).ALGO_TYPE_NAME_PREFIX + 'class3d_default', type(self).ALGO_TYPE_UNCONVERTED))
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('dont_skip_align', 'No', type(self).ALGO_TYPE_NAME_PREFIX + 'class3d_noalign', type(self).ALGO_TYPE_UNCONVERTED))
        type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list
        
        job_type = 'relion.class2d'
        job_type_to_algo_type_handler_list = []    # Initialize with empty list
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('do_em', 'Yes', type(self).ALGO_TYPE_NAME_PREFIX + 'class2d_em', type(self).ALGO_TYPE_UNCONVERTED))
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('do_grad', 'Yes', type(self).ALGO_TYPE_NAME_PREFIX + 'class2d_vdam', type(self).ALGO_TYPE_UNCONVERTED))
        type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list

        job_type = 'relion.motioncorr'
        job_type_to_algo_type_handler_list = []    # Initialize with empty list
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('do_own_motioncor', 'Yes', type(self).ALGO_TYPE_NAME_PREFIX + 'motioncorr_own', type(self).ALGO_TYPE_UNCONVERTED))
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('do_own_motioncor', 'No', type(self).ALGO_TYPE_NAME_PREFIX + 'motioncorr_mocor2', type(self).ALGO_TYPE_UNCONVERTED))
        type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list
        
        job_type = 'relion.ctffind'
        job_type_to_algo_type_handler_list = []    # Initialize with empty list
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('use_gctf', 'Yes', type(self).ALGO_TYPE_NAME_PREFIX + 'ctffind_gctf', type(self).ALGO_TYPE_UNCONVERTED))
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('use_ctffind4', 'Yes', type(self).ALGO_TYPE_NAME_PREFIX + 'ctffind_ctff4', type(self).ALGO_TYPE_UNCONVERTED))
        type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list
        
        job_type = 'relion.external'
        job_type_to_algo_type_handler_list = []    # Initialize with empty list
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('queuename', 'cryolo', type(self).ALGO_TYPE_NAME_PREFIX + 'external_cryolo', type(self).ALGO_TYPE_UNCONVERTED))
        job_type_to_algo_type_handler_list.append(JobTypeToAlgoTypeHandler('queuename', 'select3d', type(self).ALGO_TYPE_NAME_PREFIX + 'external_select3d', type(self).ALGO_TYPE_UNCONVERTED))
        type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list

        # Define list of job type which should be ignored.
        # Register an empty list of JobTypeToAlgoTypeHandler 
        # to indicate that this job type should be ignored
        job_type = 'relion.import'
        job_type_to_algo_type_handler_list = []    # Initialize with empty list
        type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list
        
        job_type = 'relion.select.onvalue'
        job_type_to_algo_type_handler_list = []    # Initialize with empty list
        type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list

        job_type = 'relion.select.split'
        job_type_to_algo_type_handler_list = []    # Initialize with empty list
        type(self).__job_type_to_algo_type_handler_list_dict[job_type] = job_type_to_algo_type_handler_list

    # <Public Instancd Method> Convert Job Type defined in a job star file to Algorithm Type for Parallel Settings Editor of RELION Schemes
    def convert(self, job_star_file_path):
        assert os.path.exists(job_star_file_path), '[PS_ASSERT] The file "{}" must exist at this point of code!'.format(job_star_file_path)
        with open(job_star_file_path, 'r') as job_star_file:
            # Read all lines from this job star file while removing all leading and trailing whitespaces from each line
            # NOTE: 2023/05/02 Toshio Moriya
            # The orignal job_star_line should be kept in job_star_line_list, especailly including tailing white space 
            # If job_star_line is stripped here, white space will be increased at the end of lines to be replaced
            # job_star_line_list = [job_star_line.strip() for job_star_line in job_star_file.readlines()]
            job_star_line_list = [job_star_line for job_star_line in job_star_file.readlines()]
        assert len(job_star_line_list) > 0, '[PS_ASSERT] The star file "{}" contains no lines! Something is seriously wrong with this star file!'.format(job_star_file_path)
        
        # Extract job type of this job star file
        job_type = None
        for job_star_line in job_star_line_list:
            if '_rlnJobTypeLabel' in job_star_line:
                job_star_line_token_list = job_star_line.split()
                assert len(job_star_line_token_list) == type(self).__N_IDX_JST, '[PS_ASSERT] Something is seriously wrong with this star file! The token counts of "_rlnJobTypeLabel" line should be always "{}" in stead of "{}"!'.format(type(self).__N_IDX_JST, len(job_star_line_token_list))
                job_type = job_star_line_token_list[type(self).__IDX_JST_VALUE]
                # Successfully found job type! 
                # let's get out of for loop immediately!
                break
        assert job_type is not None, '[PS_ASSERT] Something is seriously wrong with either this star file or coding! (job_type = "{}")'.format(job_type)
        
        # Define and initialize return value
        algo_type = None
        
        # Check if this job type is NOT in the list of JobTypeToAlgoTypeHandler
        # meaning this job type does not need to be sperated into multiple algorithm types
        if job_type not in type(self).__job_type_to_algo_type_handler_list_dict:
            print('[PS_MESSAGE] Found a job type "{}" that should not be converted'.format(job_type))
            # convert job-type-to-algorithm-type
            assert 'relion.' in job_type, '[PS_ASSERT] Invalid assumption where all RELION job types are in the form of "relion.*" instead of "{}"!'.format(job_type)
            # Possoble format of RELION job type keys
            # relion.job_type (e.g. relion.class3d)
            # relion.job_type.sub_job_type  (e.g. relion.select.onvalue)
            algo_type = job_type.replace('relion.', type(self).ALGO_TYPE_NAME_PREFIX).replace('.', '_')
        else:
            job_type_to_algo_type_handler_list = type(self).__job_type_to_algo_type_handler_list_dict[job_type]
            # Check if this job type and the associated algorithm type should be ignored since it does not support parallel computing 
            if len(job_type_to_algo_type_handler_list) > 0:
                print('[PS_MESSAGE] Found a job type "{}" that should be converted'.format(job_type))
                for job_type_to_algo_type_handler in job_type_to_algo_type_handler_list:
                    algo_type = job_type_to_algo_type_handler.handle(job_type, job_star_line_list)
                    if algo_type != type(self).ALGO_TYPE_UNCONVERTED:
                        # This job type is handled, meaning successfully converted! 
                        # let's get out of for loop immediately!
                        break
            else: 
                assert len(job_type_to_algo_type_handler_list) == 0, '[PS_ASSERT] Something is seriously wrong with coding!'
                print('[PS_MESSAGE] Found a job type "{}" that should be ignored'.format(job_type))
                algo_type = type(self).ALGO_TYPE_IGNORED
        assert algo_type is not None, '[PS_ASSERT] Something is seriously wrong with this coding! (algo_type = "{}")'.format(algo_type)
        assert algo_type != type(self).ALGO_TYPE_UNCONVERTED, '[PS_ASSERT] Something is seriously wrong with this coding! (algo_type = "{}")'.format(algo_type)
        
        return algo_type, job_star_line_list

# ========================================================================================
# Directory structure
# 
# - Script Directory 
#   |-- ParallelSettingsEditor.py
#   |-- config_to_job_star_key_mapping.yml
#   |
#   |-- Configs  # A sample of configurations directory (Use this as a template to create user-defined configurations)
#   | |-- config_type_algo.yml
#   | |-- config_level_submission.yml
#   | |-- config_level_device.yml
#   | |-- config_level_algo.yml
#   |
#   |-- Schemes             <<<< a sample of template schemes directory (Use this as a template to create user-defined schemes)
#     |-- **                <<<< a single scheme directoy
#       |-- **              <<<< a job directory of the single scheme
#         |- job.star       <<<< a job star file of the single scheme
# 
# - <INPUT> User-Defined Configurations Directory 
#   |-- config_type_algo.yml
#   |-- config_level_submission.yml
#   |-- config_level_device.yml
#   |-- config_level_algo.yml
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
#   |-- ParallelSettings    <<<< An output directory to be created. It will contain the paralle setting files of all algorithm types.
#     |-- ps_algo_type_*    <<<< Output a parallel setting file of a single algorithm type
# 
# ========================================================================================
class ParallelSettingsEditor:
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
    
    __CONFIG_ALGO_TYPE_YAML_FILE_NAME = 'config_type_algo' + __YAML_FILE_EXT
    
    __CONFIG_TO_JOB_STAR_KEY_MAPPING_YAML_FILE_NAME = 'config_to_job_star_key_mapping' + __YAML_FILE_EXT
    
    __ALGO_TYPE_KEY = 'AlgoType'
    __ALGO_TYPE_NAME_PREFIX = JobTypeToAlgoTypeConvertor.ALGO_TYPE_NAME_PREFIX
    
    __PS_KEY          = 'ParallelSettings'
    __PS_DIR_NAME     = 'ParallelSettings'
    __PS_FILE_PREFIX  = 'ps_'    # Abbreviations of "parallel settings"
    
    __MERGED_ALGO_TYPE_PARLLEL_SETTINGS_LIST_YAML_FILE_NAME = __PS_FILE_PREFIX + __ALGO_TYPE_NAME_PREFIX + 'all_list' + __YAML_FILE_EXT
    
    __SCHEMES_DIR_NAME             = 'Schemes'  # Name of RELION Schemes Directory
    __JOB_STAR_FILE_RPATH_PATTERN  = '**/**/job.star'  # Relative to Relion Project Directory
    
    # Define indices for tokens of each Job Star Parameter Entry line (JSPEL is abbribiation of "Job Star Parameter Entry Line")
    __I_ENUM = -1
    __I_ENUM += 1; __IDX_JSPEL_KEY   = __I_ENUM
    __I_ENUM += 1; __IDX_JSPEL_VALUE = __I_ENUM
    __I_ENUM += 1; __N_IDX_JSPEL     = __I_ENUM
    
    # Constructor
    def __init__(self):
        # Private instance variables
        # Holds a list of all algorithm type dictionaries 
        self.__merged_algo_type_dict_list= []
    
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
            print('[PS_MESSAGE]', 'The output subdirectory "{}" already exists! Making a backup of the existing subdirectory...'.format(output_subdir_path))
            dt_now = datetime.datetime.now()
            backup_output_subdir_path = output_subdir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(output_subdir_path, backup_output_subdir_path)
        assert not os.path.exists(output_subdir_path), '[PS_ASSERT] The output subdirectory "{}" must NOT exist at this point of code!'.format(output_subdir_path)

    # <Private Instance Method> Create a dictionary for each algorithm from the parallel settings defined in the config files. 
    # Then, combine individual algorithm dictionaries as a single list of all algorithm dictionaries
    # and keep the list as an instance variable
    def __create_merged_algo_type_dict_list(self, configs_dir_path):
        # configs_dir_path: a path of directory containing all configuration yaml files
        
        # Check preconditions!
        # NOTE: 2023/05/01 Toshio Moriya
        # Actually this should be error check instead of assertion!
        assert os.path.exists(configs_dir_path), '[PS_ASSERT] The configurations directory "{}" must exist!'.format(configs_dir_path)
        
        # Reinitialize the list of all algorithm dictionaries
        if len(self.__merged_algo_type_dict_list) > 0:
            print('[PS_MESSAGE] Reinitializing the list of all algorithm dictionaries...')
            self.__merged_algo_type_dict_list = []
        assert len(self.__merged_algo_type_dict_list) == 0, '[PS_ASSERT] self.__merged_algo_type_dict_list should be empty instead of containing "{}" dictionaries at this point code! Something is seriously wrong with this coding!'.format(len(self.__merged_algo_type_dict_list))
        
        # Structure of algo_type_dict_dict
        #   algo_type_dict_dict := {AlgoType:*, algo_type_dict}
        #   algo_type_dict      := {SubmissionLevel:*, DeviceLevel:*, AlgoLevel:*}
        config_algo_type_yaml_file_path = os.path.join(configs_dir_path, type(self).__CONFIG_ALGO_TYPE_YAML_FILE_NAME)
        algo_type_dict_dict = self.__load_yaml_file(config_algo_type_yaml_file_path)
        
        for algo_type_dict in algo_type_dict_dict:
            all_level_algo_type_dict = {}
            all_level_parallel_settings_dict = {}
            
            for config_level_yaml_info in type(self).__CONFIG_LEVEL_YAML_INFO_LIST:
                config_level_yaml_name = config_level_yaml_info[type(self).__IDX_CLYI_FILE_NAME]
                config_level_key       = config_level_yaml_info[type(self).__IDX_CLYI_KEY]
                config_level_value     = algo_type_dict[config_level_key]
                
                # Structure of config_level_dict_dict
                #   config_level_dict_dict := {*Level:*, config_level_dict}
                #   config_level_dict      := {Settings: {CONFIG_LEVEL_PARAM_A:*, CONFIG_LEVEL_PARAM_B:*, CONFIG_LEVEL_PARAM_C:*, ...}}
                config_level_yaml_file_path = os.path.join(configs_dir_path, config_level_yaml_name)
                config_level_dict_dict = self.__load_yaml_file(config_level_yaml_file_path)
                
                # Extract configuraltion of each level and merge them
                for config_level_dict in config_level_dict_dict:
                    if config_level_dict[config_level_key] == config_level_value:
                       all_level_algo_type_dict.update(config_level_dict)
                       all_level_parallel_settings_dict.update(config_level_dict[type(self).__PS_KEY])
            
            merged_algo_type_dict = {**algo_type_dict, **all_level_algo_type_dict, type(self).__PS_KEY:{**all_level_parallel_settings_dict}}
            self.__merged_algo_type_dict_list.append(merged_algo_type_dict)

    # <Private Instance Method> Save the parameter settings as yml files
    def __save_merged_algo_type_dict_list(self, parallel_settings_subdir_path):
        if len(self.__merged_algo_type_dict_list) > 0:
            self.__make_output_subdir_backup(parallel_settings_subdir_path)
            assert not os.path.exists(parallel_settings_subdir_path), '[PS_ASSERT] The output paralle settings subdirectory "{}" must NOT exist at this point of code!'.format(parallel_settings_subdir_path)
            os.mkdir(parallel_settings_subdir_path)
             
            for merged_algo_type_dict in self.__merged_algo_type_dict_list: 
                merged_algo_type_setting_yaml_file_name = type(self).__PS_FILE_PREFIX + merged_algo_type_dict[type(self).__ALGO_TYPE_KEY] + type(self).__YAML_FILE_EXT
                merged_algo_type_setting_yaml_file_path = os.path.join(parallel_settings_subdir_path, merged_algo_type_setting_yaml_file_name)
                self.__save_yaml_file(merged_algo_type_setting_yaml_file_path, merged_algo_type_dict)
            merged_algo_type_setting_list_yaml_file_path = os.path.join(parallel_settings_subdir_path, type(self).__MERGED_ALGO_TYPE_PARLLEL_SETTINGS_LIST_YAML_FILE_NAME) 
            self.__save_yaml_file(merged_algo_type_setting_list_yaml_file_path, self.__merged_algo_type_dict_list)
        else:
            assert len(self.__merged_algo_type_dict_list) == 0, '[PS_ASSERT] self.__merged_algo_type_dict_list should be empty at this point of code!'
            print('[PS_MESSAGE] self.__merged_algo_type_dict_list is empty. Please call __create_merged_algo_type_dict_list() before calling __save_merged_algo_type_dict_list')

    # <Private Instance Method> Replace values of paralle settings of all job star (job.star) in the specified template Schemes dirctory
    # and save the results to the output Schemes directory.
    def __replace_schemes_parallel_settings(self, output_schemes_subdir_path):
        # Obtain directory path of this script
        script_dir_path = os.path.dirname(__file__)
        
        # Create JobTypeToAlgoTypeConvertor (Singleton Class)
        job_type_to_algo_type_convertor = JobTypeToAlgoTypeConvertor.get_singleton()
                
        # File pattern of job star file in tempate RELION Schemes  
        output_job_star_file_path_pattern = os.path.join(output_schemes_subdir_path, type(self).__JOB_STAR_FILE_RPATH_PATTERN)
        
        # Replace values of paralle settings of all job star (job.star) in the specified template Schemes dirctory
        for output_job_star_file_path in glob.glob(output_job_star_file_path_pattern):
            assert os.path.exists(output_job_star_file_path), '[PS_ASSERT] The file "{}" must exist at this point of code!'.format(output_job_star_file_path)
            
            algo_type, job_star_line_list = job_type_to_algo_type_convertor.convert(output_job_star_file_path)
            
            if algo_type != JobTypeToAlgoTypeConvertor.ALGO_TYPE_IGNORED:
                output_job_star_file_contents = None
                with open(output_job_star_file_path, 'r+') as output_job_star_file:
                    # Read all contents of file
                    output_job_star_file_contents = output_job_star_file.read()
                    assert output_job_star_file_contents is not None, '[PS_ASSERT] Something is seriously wrong with either this star file or coding! (output_job_star_file_contents = "{}")'.format(output_job_star_file_contents)
                    
                    # Create list to replace the values(two-dimensional array)
                    merged_algo_type_dict = [merged_algo_type_dict for merged_algo_type_dict in self.__merged_algo_type_dict_list if merged_algo_type_dict[type(self).__ALGO_TYPE_KEY] == algo_type][0]
                    
                    config_to_job_star_key_mapping_yaml_file_path = os.path.join(script_dir_path, type(self).__CONFIG_TO_JOB_STAR_KEY_MAPPING_YAML_FILE_NAME)
                    config_to_job_star_key_mapping_dict = self.__load_yaml_file(config_to_job_star_key_mapping_yaml_file_path)
                    config_key_list = config_to_job_star_key_mapping_dict.keys()
                    
                    for config_key in config_key_list:
                        for job_star_line in job_star_line_list:
                            job_star_line_token_list = job_star_line.split()
                            if len(job_star_line_token_list) == type(self).__N_IDX_JSPEL:     # lines does not have assumed number of tokens!
                                target_job_star_param_key = job_star_line_token_list[type(self).__IDX_JSPEL_KEY]
                                # NOTE: 2023/05/01 Toshio Moriya
                                # 'N/A' does not seem to be used at this point
                                # if target_job_star_param_key == config_to_job_star_key_mapping_dict[config_key] and merged_algo_type_dict[type(self).__PS_KEY][config_key] != 'N/A':
                                # NOTE: 2023/05/04 Toshio Moriya
                                # Changed 'N/A' to "PS_NOT_APPLICABLE" as used in config yaml files
                                if target_job_star_param_key == config_to_job_star_key_mapping_dict[config_key] and merged_algo_type_dict[type(self).__PS_KEY][config_key] != 'PS_NOT_APPLICABLE':
                                    ### # NOTE: 2023/05/04 Toshio Moriya
                                    ### # other_args (AdditionalArguments) might have a value already (eg. '--do_at_most $$do_at_most', '--fast_subsets')
                                    ### # Here, we append config value to existing value in this job.star file
                                    ### # However, this is a little bit dangerous since other_args is considered as an exception!!
                                    ### # Realized this is a bad idea since it will append value forever if user run this sciprt multiple time on the same schemes!
                                    ### # Going back to original way as above
                                    ### if target_job_star_param_key == 'other_args':
                                    ###     target_job_star_param_value = job_star_line_token_list[type(self).__IDX_JSPEL_VALUE]
                                    ###     merged_algo_type_dict[type(self).__PS_KEY][config_key] = '{} {}\n'.format(target_job_star_param_value, merged_algo_type_dict[type(self).__PS_KEY][config_key])
                                    # Assumed format of job star file: The field width of the key/label is 36 characters wide and one white space after the value.
                                    new_job_star_line = '{:36s}{:s}\n'.format(target_job_star_param_key, merged_algo_type_dict[type(self).__PS_KEY][config_key])
                                    # Replace settings according to all replace pairs
                                    output_job_star_file_contents = output_job_star_file_contents.replace(job_star_line, new_job_star_line)
                    
                    # Delete all contents of the current job star file
                    output_job_star_file.seek(0)
                    output_job_star_file.truncate(0)
                    
                    # Save the result of replacements to the current job star file
                    output_job_star_file.write(output_job_star_file_contents)

    # <Public Instance Method> Edit paralle settings of all job star (job.star) in the specified template Schemes dirctory 
    # by replacing the values with specified in config yaml files.
    # and save the results to the output Schemes directory.

    def make_output_schemes(self, template_schemes_dir_path, output_dir_path):
        # Check preconditions!
        # NOTE: 2023/05/01 Toshio Moriya
        # Actually these should be error checks instead of assertions!
        assert os.path.exists(template_schemes_dir_path), '[PS_ASSERT] The template Schemes directory "{}" must exist!'.format(template_schemes_dir_path)
        assert template_schemes_dir_path, '[PS_ASSERT] The template Schemes directory "{}" must NOT exist!'.format(template_schemes_dir_path)
        # NOTE: 2023/05/03 Toshio Moriya
        # Removed the following requirement to allow the users to name the template_schemes_dir as they like
        # assert os.path.basename(os.path.normpath(template_schemes_dir_path)) == type(self).__SCHEMES_DIR_NAME, '[PS_ASSERT] The specified template Schemes directory "{}" is invalid! It must end with "{}"!'.format(template_schemes_dir_path, type(self).__SCHEMES_DIR_NAME)

        output_schemes_subdir_path = os.path.join(output_dir_path, type(self).__SCHEMES_DIR_NAME)
        # Make a back up of schemes
        self.__make_output_subdir_backup(output_schemes_subdir_path)
        assert not os.path.exists(output_schemes_subdir_path), '[PS_ASSERT] The output Schemes subdirectory "{}" must NOT exist at this point of code!'.format(output_schemes_subdir_path)
        
        # Create output Schemes directory by copying template Schemes directory 
        shutil.copytree(template_schemes_dir_path, output_schemes_subdir_path)
        return output_schemes_subdir_path

    def edit(self, configs_dir_path, output_dir_path, output_schemes_subdir_path):
        # [*] configs_dir_path: a path of directory containing all configuration yaml files
        # [*] template_schemes_dir_path: a path of tempate RELION Schemes directory 
        # [*] output_dir_path: a path of output directory.
        #     Under this directory the following subdirecties will be created 
        #     - Output "Schemes" subdirectroy and related files based on the template "Schemes" 
        #     - Output "ParallelSettings" subdirectroy and parallel settings files of all algorithm types 
        
        # Check preconditions!
        # NOTE: 2023/05/01 Toshio Moriya
        # Actually these should be error checks instead of assertion!
        assert os.path.exists(configs_dir_path), '[PS_ASSERT] The configurations directory "{}" must exist!'.format(configs_dir_path)
        #assert os.path.exists(template_schemes_dir_path), '[PS_ASSERT] The template Schemes directory "{}" must exist!'.format(template_schemes_dir_path)
        # NOTE: 2023/05/03 Toshio Moriya
        # Removed the following requirement to allow the users to name the template_schemes_dir as they like
        # assert os.path.basename(os.path.normpath(template_schemes_dir_path)) == type(self).__SCHEMES_DIR_NAME, '[PS_ASSERT] The specified template Schemes directory "{}" is invalid! It must end with "{}"!'.format(template_schemes_dir_path, type(self).__SCHEMES_DIR_NAME)
        
        if not os.path.exists(output_dir_path):
            print('[PS_MESSAGE] The specified output directory "{}" does not exist yet! Creating the directory'.format(output_dir_path))
            os.mkdir(output_dir_path)
        assert os.path.exists(output_dir_path), '[PS_ASSERT] The output directory "{}" must exist at this point of code!'.format(output_dir_path)
        
        #  Set instance variables
        parallel_settings_subdir_path = os.path.join(output_dir_path, type(self).__PS_DIR_NAME)
        self.__create_merged_algo_type_dict_list(configs_dir_path)
        self.__save_merged_algo_type_dict_list(parallel_settings_subdir_path)
        self.__replace_schemes_parallel_settings(output_schemes_subdir_path)

if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configs_dir",    type=str,    default='./Configs',    help = 'Path of input configurations directory containing all configuration yaml files.  (Default "./Configs")')
    parser.add_argument("-s", "--schemes_dir",    type=str,    default='./Schemes',    help = 'Path of input template RELION Schemes directory containing all Schemes related files.  (Default "./Schemes")')
    parser.add_argument("-o", "--output_dir",     type=str,    default='../',          help = 'Path of output root directroy where all outputs will be saved.  (default "../")')
    
    args = parser.parse_args()
    ### args, unknown = parser.parse_known_args()

    # Rename arguments for readability
    # No arguments with this program
    
    # Rename options for readability
    option_configs_dir_path          = args.configs_dir
    option_template_schemes_dir_path = args.schemes_dir
    option_output_dir_path           = args.output_dir
    
    print('[PS_MESSAGE] Specified values of all options')
    print('[PS_MESSAGE]   Input configurations directory path   := {}'.format(option_configs_dir_path))
    print('[PS_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[PS_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[PS_MESSAGE] ')
    print('[PS_MESSAGE] Editing parallel settings of all job.star files in the specified shcemes...')
    ps_editor = ParallelSettingsEditor()
    output_schemes_subdir_path = ps_editor.make_output_schemes(option_template_schemes_dir_path, option_output_dir_path)
    ps_editor.edit(option_configs_dir_path, option_output_dir_path, output_schemes_subdir_path)
    print('[PS_MESSAGE] ')
    print('[PS_MESSAGE] DONE!')
