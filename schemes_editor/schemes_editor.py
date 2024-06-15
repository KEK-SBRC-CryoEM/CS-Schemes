#!/usr/bin/env python3.7
##########################################################################################
# Authors: Misato Yamamoto (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023-2024 KEK IMMS SBRC
# 
# Description:
# Simplify setting of parameters for RELION Schemes. 
# The parameters in all job.star files are replaced by values in yaml config files.
# User set up the values of setting in yaml files. 
# Administrator must set the environment variable <SE_ENV_DEFAULT_CONFIGS>. 
# It is recommended to set this variable in the .bashrc file.
# 
# Usage:
# $ python3  schemes_editor.py  -t /path/to/Template_Scheme  -s /path/to/config_sample_setting.yml
# 
##########################################################################################
# 
# ========================================================================================
# - Installation Directory Structure
# [Installation Root Directory]                            <<<< The root path can be arbitrary.
#   |--- scheme_editor                                     <<<< The script directory containing Python scripts of Sheme Editor.
#   |   |--- schemes_editor.py                             <<<< The main Python script of Sheme Editor.
#   |   |
#   |   |--- schemestar_editor                             
#   |   |   |--- schemestar_editor.py                      
#   |   |
#   |   |--- jobstar_editor                                
#   |       |--- jobstar_editor.py                         
#   |       |--- config_jobtype_to_algotype_item.yml       
#   |       |--- config_to_jobstar_keymap_parallel.yml     
#   |       |--- config_to_jobstar_keymap_system.yml       
#   |
#   |--- configs                                            <<<< The configurations directory containning templates and predefined configuration files.
#   |   |--- common
#   |   |   |--- config_em_setting_kek_krios.yml            
#   |   |   |--- config_em_setting_kek_talos.yml            
#   |   |
#   |   |--- common_tutorial
#   |   |   |--- config_sample_settings.yml                 
#   |   |
#   |   |--- [System Name]                                  <<<< System environment dependent configurations (e.g., gotocloud, kek_rbl)
#   |   |   |--- default_configs.yml                        
#   |   |   |--- config_level_algo.yml                      
#   |   |   |--- config_level_device.yml                    
#   |   |   |--- config_level_submission.yml                
#   |   |   |--- config_system_settings.yml                 
#   |   |   |--- config_type_algo_gtc.yml                   
#   |   |
#   |   |--- [System Name]_tutorial                         <<<< System environment dependent configurations for RELION tutorial dataset (e.g., gotocloud, kek_rbl)
#   |   |   |--- default_configs.yml                        
#   |   |   |--- config_em_setting.yml                      
#   |   |   |--- config_level_algo.yml                      
#   |   |   |--- config_type_algo.yml                       
#   |   |
#   |   |--- (TBD)template                                  <<<< The template configurations directory.  Use the files in this directory as templates to create user-defined configurations.
#   |       |--- (TBD)template_config_sample_settings.yml   <<<< The template configuration file for sample-depended parameters settings.
#   |       |--- (TBD)template_default_configs.yml          <<<< The template configuration file for default configurations.
#   |       |--- (TBD)template_config_em_settings.yml       <<<< The template configuration file for EM-depended parameters settings.
#   |       |--- (TBD)template_config_type_algo.yml         <<<< The template configuration file for algorithm-type-depended parameters settings.
#   |       |--- (TBD)template_config_level_algo.yml        <<<< The template configuration file for algorithm-level-depended parameters settings.
#   |       |--- (TBD)template_config_level_device.yml      <<<< The template configuration file for device-leve-depended parameters settings.
#   |       |--- (TBD)template_config_level_submission.yml  <<<< The template configuration file for submission-level-depended parameters settings.
#   |       |--- (TBD)template_config_system_settings.yml   <<<< The template configuration file for system-depended parameters settings.
#   |
#   |--- schemes_templates                                  <<<< The Schemes templates directory containing a set of predefined RELION Schemes templates.
#      |--- cs_schemes                                      <<<< The CS-Schemes template directory. Use this Schemes template as a example to create user-defined RELION Schemes template.
#      |  |--- *                                            <<<< Scheme directories each containg a Scheme of this RELION Schemes template (e.g., "010_GTF_Motioncorr", "060_CSS_Clean_Stack_3D").
#      |     |--- scheme.star                               <<<< The scheme star file of this Scheme. This file defines the SPA workflow of this RELION Schemes.
#      |     |--- *                                         <<<< Job directories each for a job belong to this RELION Schemes (e.g., "010010_Import_movies", "060010_Select_split_parts").
#      |        |--- job.star                               <<<< The job star file of this job.
#      |
#      ...                                                  <<<< More predefined Schemes template directories.
# 
# - <REQUIRED INPUT> User-Defined Sample Settings Configurations Files
#   |--- /path/to/config_sample_setting*.yml                <<<< A user-defined configuration file for sample-depended parameters settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
# 
# - <REQUIRED INPUT> User-Specified or User-Defined Schemes Template Directory Structure
# [Input Root Directory]                                    <<<< The root path can be arbitrary. It can be RELION project directory.
#   |--- [Schemes Template Directory Name]                  <<<< A Schemes template directory containing a use-specified or user-defined RELION Schemes template. The directory name can be arbitrary (e.g., "Schemes", "Schemes_Templates").
#      |--- *                                               <<<< Scheme directories each containg a Scheme of this RELION Schemes template.
#         |--- scheme.star                                  <<<< The scheme star file of this Scheme. This file defines the SPA workflow of this RELION Schemes.
#         |--- *                                            <<<< Job directories each for a job belong to this RELION Schemes.
#            |--- job.star                                  <<<< The job star file of this job.
# 
# - <OPTINAL INPUT> User-Defined Environment Variables
#   export SE_ENV_DEFAULT_CONFIGS = /path/to/config_default_settings*.yml
# 
# - <OPTINAL INPUT> User-Defined Configurations Files
#   |--- /path/to/config_default_settings*.yml              <<<< A user-defined configuration file for configuration default settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
#   |--- /path/to/config_em_settings*.yml                   <<<< A user-defined configuration file for EM-related parameter settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
#   |--- /path/to/config_type_algo*.yml                     <<<< A user-defined configuration file for algorithm-type-depended parameters settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
#   |--- /path/to/config_level_algo*.yml                    <<<< A user-defined configuration file for algorithm-level-depended parameters settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
#   |--- /path/to/config_level_device*.yml                  <<<< A user-defined configuration file for device-leve-depended parameters settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
#   |--- /path/to/config_level_submission*.yml              <<<< A user-defined configuration file for submission-level-depended parameters settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
#   |--- /path/to/config_system_settings*.yml               <<<< A user-defined configuration file for system-depended parameters settings. The file path as well as the file name format can be arbitrary but recommended to use the file name formats given here.
# 
# - <OUTPUT> User-Specified Output Directory Structure
# [OUTPUT Root Directory]                                   <<<< The default path is "./Schemes_Edited". It can be the RELION project directory or current directory (i.e., "./").
#   |--- Schemes                                            <<<< An output Schemes directory created by this script. This Schemes are edited and executable with "relion_schemegui.py".
#   |  |--- *                                               
#   |     |--- scheme.star                                  <<<< The parameters in this file are editted by this script!
#   |     |--- *                                            
#   |        |--- job.star                                  <<<< The parameters in this file are editted by this script!
#   |
#   |--- SE_schemestar_settings                             <<<< An output subdirectory created by this script. It contains the executable file PATH settings file.
#   |  |--- sse_scheme_star_[Scheme Name].yml               <<<< Output yaml files containing the sample settings in all Schemes (one output yaml files per a single Scheme).
#   |
#   |--- SE_jobstar_settings                                <<<< An output subdirectory created by this script. It contains the paralle setting files of all algorithm types.
#      |--- jse_algo_type_*                                 <<<< Output parallel setting files for all algorithm types (one output file per a single algorithm type).
# 
# ========================================================================================


import yaml
import os
import sys
import shutil
import datetime
import argparse
from jobstar_editor import jobstar_editor
from schemestar_editor import schemestar_editor


class SchemesEditor():
    # Private class constants
    # Constants related to input Schemes directory and key mapping yaml files
    __SCHEMES_DIR_NAME                    = 'Schemes'
    __JOBSTAR_KEYMAP_PARALLEL_FILE_NAME   = 'config_to_jobstar_keymap_parallel.yml'
    __JOBSTAR_KEYMAP_SYSTEM_FILE_NAME     = 'config_to_jobstar_keymap_system.yml'
    
    # Constants related to default configuration yaml files
    __SE_ENV_DEFAULT_CONFIGS              = 'SE_ENV_DEFAULT_CONFIGS'
    __SE_DEFAULT_CONFIG_FILE_PATHS_KEY    = 'DefaultConfigFilePaths'
    __SE_CONFIG_PARALLEL_KEY              = 'ParallelSettings'
    __SE_CONFIG_EM_KEY                    = 'EmSettings'
    __SE_CONFIG_SYSTEM_KEY                = 'SystemSettings'
    
    __SE_setup_configs_dir_name           = 'configs'
    __SE_setup_env_depend_dir_name        = 'environment_dependent'
    __SE_setup_default_configs_file_name  = 'default_configs.yml'
    
    # Constants related to outputs
    __DEFAULT_OUTPUT_DIR_PATH             = './Schemes_Edited'
    __JOBSTAR_EDITOR_DIR_NAME             = 'jobstar_editor'
    __PARALLEL_SETTINGS_DIR_NAME          = 'SE_parallel_settings'
    __SYSTEM_SETTINGS_DIR_NAME            = 'SE_system_settings'
    __EM_SETTINGS_DIR_NAME                = 'SE_em_settings'
    __SAMPLE_SETTINGS_DIR_NAME            = 'SE_sample_settings'
    
    # <Public Instance Constructor>
    def __init__(self):
        # Private instance variables
        self.__edit_schemes_dir_path       = ""    # A path of tempate RELION Schemes directory.
        self.__output_dir_path             = ""    # A path of output directory containg all outputs of this script (see "<OUTPUT> User-Specified Output Directory Structure").
    
    # <Private Helper Instance Method> Load yaml file and keep the contents as a dictionary 
    # NOTE: 2024/06/08 Toshio Moriya: The following function is duplicated in mulitple scripts of Schemes Editor
    # Need to make a shared library!
    def __load_yaml_file(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        return yaml_dict
    
    # <Private Helper Instance Method> Make a backup if a directory with same name already exists.
    # NOTE: 2024/06/08 Toshio Moriya: The following function is duplicated in mulitple scripts of Schemes Editor
    # Need to make a shared library!
    def __make_backup_dir(self, target_dir_path):
        if os.path.exists(target_dir_path): 
            print('[SE_MESSAGE]', 'The directory "{}" already exists! Making a backup of the existing directory...'.format(target_dir_path))
            dt_now = datetime.datetime.now()
            backup_dir_path = target_dir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(target_dir_path, backup_dir_path)
        assert not os.path.exists(target_dir_path), '[SE_ASSERT] The directory "{}" must NOT exist at this point of code!'.format(self.target_dir_path)
    
    # <Public Instance Method> 
    # NOTE: 2024/06/08 Toshio Moriya: The following function is duplicated in mulitple scripts of Schemes Editor
    # Need to make a shared library!
    def make_edit_schemes(self, template_schemes_dir_path, output_dir_path):
        # Check preconditions!
        # Check if template_schemes_dir_path exists.
        if not os.path.exists(template_schemes_dir_path):
            print('[SE_ERROR] The template Schemes directory "{}" does NOT exist! Please make sure to provide correct template Schemes directory path using "--template_schemes_dir" option.'.format(template_schemes_dir_path))
            sys.exit(1)
        
        # Make a backup of schemes
        edit_schemes_dir_path = os.path.join(output_dir_path, type(self).__SCHEMES_DIR_NAME)
        self.__make_backup_dir(edit_schemes_dir_path)
        assert not os.path.exists(edit_schemes_dir_path), '[SE_ASSERT] The output Schemes subdirectory "{}" must NOT exist at this point of code!'.format(edit_schemes_dir_path)
        
        # Create output Schemes directory by copying template Schemes directory 
        shutil.copytree(template_schemes_dir_path, edit_schemes_dir_path)
        
        return edit_schemes_dir_path
    
    # <Public Instance Method> 
    def edit(self, edit_schemes_dir_path, sample_config_file_path, parallel_config_file_path = None, em_config_file_path = None, system_config_file_path = None, output_dir_path = __DEFAULT_OUTPUT_DIR_PATH):
        # [*] edit_schemes_dir_path : Path of input template RELION Schemes directory containing all Schemes related files for editing (meaning that the script overrides this Schemes).
        # [*] *_config_file_path    : Paths of input configuration yaml files.
        # [*] output_dir_path       : Path of output root directroy where all outputs will be saved.
        # 
        # NOTE: 2024/06/08 Toshio Moriya:
        # At this point, this function overwrites tempate Schemes (i.e., edit_schemes_dir_path) by default!
        # To make a backup of existing Schemes in output directory and copy template Schemes to output directory for editting,
        # the caller must use "self.make_edit_schemes()" and get the path of copy template Schemes beforehand.
        
        # Initialize instance variables with argument values
        self.__edit_schemes_dir_path = edit_schemes_dir_path
        self.__output_dir_path = output_dir_path
        
        # NOTE: 2024/06/08 Toshio Moriya:
        # Actually the followings should be error checks instead of assertion!
        assert os.path.exists(self.__edit_schemes_dir_path), '[SE_ASSERT] Specified template Schemes directory "{}" must exist at this point of code!'.format(self.__edit_schemes_dir_path)
        assert os.path.exists(sample_config_file_path), '[SE_ASSERT] Specified configuration file "{}" must exist at this point of code!'.format(sample_config_file_path)
        
        # Check if default configs should be used
        if None in [parallel_config_file_path, em_config_file_path, system_config_file_path]:        
            # Try to get default paths of config yaml files from the user-defined defualt configs yaml files
            do_check_setup_default_configs_file_path = False
            try:
                # os.environ throws KeyError exception if specified environment variable does not exist
                default_config_file_path = os.environ[type(self).__SE_ENV_DEFAULT_CONFIGS]
                print('[SE_MESSAGE] ')
                print('[SE_MESSAGE] Found user-defined default configurations yaml file!')
                print('[SE_MESSAGE] Default configuration file path "{}" is set now.'.format(default_config_file_path))
                print('[SE_MESSAGE] ')
                
                # Generate default file paths from yaml file settings
                default_config_file_path_dict = self.__load_yaml_file(default_config_file_path)
                if parallel_config_file_path is None:
                    parallel_config_file_path = default_config_file_path_dict[type(self).__SE_DEFAULT_CONFIG_FILE_PATHS_KEY][type(self).__SE_CONFIG_PARALLEL_KEY]
                if em_config_file_path is None:
                    em_config_file_path = default_config_file_path_dict[type(self).__SE_DEFAULT_CONFIG_FILE_PATHS_KEY][type(self).__SE_CONFIG_EM_KEY]
                if system_config_file_path is None:
                    system_config_file_path = default_config_file_path_dict[type(self).__SE_DEFAULT_CONFIG_FILE_PATHS_KEY][type(self).__SE_CONFIG_SYSTEM_KEY]
                
            except KeyError as e:
                print('[SE_MESSAGE] ')
                print('[SE_MESSAGE] User-defined default configurations yaml file is not provided.')
                print('[SE_MESSAGE] ')
                do_check_setup_default_configs_file_path = True
                pass
            
            if do_check_setup_default_configs_file_path:
                print('[SE_MESSAGE] ')
                print('[SE_MESSAGE] KEK Schemes setup default configurations yaml file will be used.')
                print('[SE_MESSAGE] <TIPS> ')
                print('[SE_WARNING] You can define a default configurations yaml file and export the file path as follow:')
                print('[SE_WARNING] "export {}=path/to/default_configs.yml".'.format(type(self).__SE_ENV_DEFAULT_CONFIGS))
                print('[SE_WARNING] ')
                
                # Generate absolute path of setup default configs yaml file.
                # from relative path of setup default configs yaml file relative to the directory containg this script.
                setup_default_configs_file_rpath = os.path.join(type(self).__SE_setup_configs_dir_name, type(self).__SE_setup_env_depend_dir_name, type(self).__SE_setup_default_configs_file_name)
                script_path = os.path.abspath(__file__)
                script_dir_path = os.path.dirname(script_path)
                default_config_file_path = os.path.join(script_dir_path, setup_default_configs_file_rpath)
                default_config_file_path_dict = self.__load_yaml_file(default_config_file_path)
                print('[SE_MESSAGE] Default configurations file path "{}" is set now.'.format(default_config_file_path))
                print('[SE_MESSAGE] ')
                # Generate default file paths from yaml file settings
                default_config_file_path_dict = self.__load_yaml_file(default_config_file_path)
                if parallel_config_file_path is None:
                    parallel_config_file_path = default_config_file_path_dict[type(self).__SE_DEFAULT_CONFIG_FILE_PATHS_KEY][type(self).__SE_CONFIG_PARALLEL_KEY]
                if em_config_file_path is None:
                    em_config_file_path = default_config_file_path_dict[type(self).__SE_DEFAULT_CONFIG_FILE_PATHS_KEY][type(self).__SE_CONFIG_EM_KEY]
                if system_config_file_path is None:
                    system_config_file_path = default_config_file_path_dict[type(self).__SE_DEFAULT_CONFIG_FILE_PATHS_KEY][type(self).__SE_CONFIG_SYSTEM_KEY]
        
        assert os.path.exists(parallel_config_file_path), '[SE_ASSERT] The configuration file "{}" must exist at this point of code!'.format(parallel_config_file_path)
        assert os.path.exists(em_config_file_path), '[SE_ASSERT] The configuration file "{}" must exist at this point of code!'.format(em_config_file_path)
        assert os.path.exists(system_config_file_path), '[SE_ASSERT] The configuration file "{}" must exist at this point of code!'.format(system_config_file_path)
        
        print('[SE_MESSAGE] ')
        print('[SE_MESSAGE] Applied values to Scheme Editors')
        print('[SE_MESSAGE]   Input tempate Schemes directory path                := {}'.format(self.__edit_schemes_dir_path))
        print('[SE_MESSAGE]   Input sample settigs configuration yaml file path   := {}'.format(sample_config_file_path))
        print('[SE_MESSAGE]   Input parallel settigs configuration yaml file path := {}'.format(parallel_config_file_path))
        print('[SE_MESSAGE]   Input em settigs configuration yaml file path       := {}'.format(em_config_file_path))
        print('[SE_MESSAGE]   Input system settigs configuration yaml file path   := {}'.format(system_config_file_path))
        print('[SE_MESSAGE]   Output root directory path                          := {}'.format(self.__output_dir_path))
        print('[SE_MESSAGE] ')
        print('[SE_MESSAGE] ')
        # Execute job star editor
        script_dir_path = os.path.dirname(__file__)
        jobstar_keymap_system_file_path = os.path.join(script_dir_path, type(self).__JOBSTAR_EDITOR_DIR_NAME, type(self).__JOBSTAR_KEYMAP_SYSTEM_FILE_NAME)
        jobstar_keymap_parallel_file_path = os.path.join(script_dir_path, type(self).__JOBSTAR_EDITOR_DIR_NAME, type(self).__JOBSTAR_KEYMAP_PARALLEL_FILE_NAME)
        # NOTE: 2024/06/08 Toshio Moriya: Actually the followings should be error checks instead of assertion!
        assert os.path.exists(jobstar_keymap_parallel_file_path), '[SE_ASSERT] The job star key mapping for parallel settings file "{}" must exist at this point of code!'.format(jobstar_keymap_parallel_file_path)
        assert os.path.exists(jobstar_keymap_system_file_path), '[SE_ASSERT] The job star key mapping for system settings file "{}" must exist at this point of code!'.format(jobstar_keymap_system_file_path)
        
        js_editor = jobstar_editor.JobStarEditor()
        print('[SE_MESSAGE] Editing Parallel Settings of all job.star in this RELION Schemes...')
        js_editor.edit(self.__edit_schemes_dir_path, parallel_config_file_path, jobstar_keymap_parallel_file_path, os.path.join(self.__output_dir_path, type(self).__PARALLEL_SETTINGS_DIR_NAME))
        print('[SE_MESSAGE] Editing Sytem Settings of all job.star in this RELION Schemes...')
        js_editor.edit(self.__edit_schemes_dir_path, system_config_file_path, jobstar_keymap_system_file_path, os.path.join(self.__output_dir_path,type(self).__SYSTEM_SETTINGS_DIR_NAME))
        
        # Execute scheme star editor
        ss_editor = schemestar_editor.SchemeStarEditor()
        print('[SE_MESSAGE] Editing EM Settings of all scheme.star in this RELION Schemes...')
        ss_editor.edit(self.__edit_schemes_dir_path, em_config_file_path, os.path.join(self.__output_dir_path, type(self).__EM_SETTINGS_DIR_NAME))
        print('[SE_MESSAGE] Editing Sample Settings of all scheme.star in this RELION Schemes...')
        ss_editor.edit(self.__edit_schemes_dir_path, sample_config_file_path, os.path.join(self.__output_dir_path, type(self).__SAMPLE_SETTINGS_DIR_NAME))


if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-t",  "--template_schemes_dir",    type=str,    required=True,                  help = 'Path of input template RELION Schemes directory containing all Schemes related files. This argument is always required.')
    parser.add_argument("-s",  "--sample_config_yml",       type=str,    required=True,                  help = 'Path of input sample settigs configuration yaml file. This argument is always required.')
    parser.add_argument("-p",  "--parallel_config_yml",     type=str,    default= None,                  help = 'Path of input parallel settigs configuration yaml file. (The default defined in SE_ENV_DEFAULT_CONFIGS/config_default_settings.yml)')
    parser.add_argument("-e",  "--em_config_yml",           type=str,    default= None,                  help = 'Path of input em settigs configuration yaml file.  (The default defined in SE_ENV_DEFAULT_CONFIGS/config_default_settings.yml)')
    parser.add_argument("-y",  "--system_config_yml",       type=str,    default= None,                  help = 'Path of input system settigs configuration yaml file.  (The default defined in SE_ENV_DEFAULT_CONFIGS/config_default_settings.yml)')
    parser.add_argument("-o",  "--output_dir",              type=str,    default= './Schemes_Edited',    help = 'Path of output root directroy where all outputs will be saved. (default "./Schemes_Edited")')

    # Rename arguments for readability
    # No arguments with this program
    # Rename options for readability
    args = parser.parse_args()
    option_template_schemes_dir_path = args.template_schemes_dir
    option_sample_config_file_path   = args.sample_config_yml
    option_parallel_config_file_path = args.parallel_config_yml
    option_em_config_file_path       = args.em_config_yml
    option_system_config_file_path   = args.system_config_yml
    option_output_dir_path           = args.output_dir
  
    print('[SE_MESSAGE] Parameter values provided by command line')
    print('[SE_MESSAGE]   Input tempate Schemes directory path                := {}'.format(option_template_schemes_dir_path))
    print('[SE_MESSAGE]   Input sample settigs configuration yaml file path   := {}'.format(option_sample_config_file_path))
    print('[SE_MESSAGE]   Input parallel settigs configuration yaml file path := {}'.format(option_parallel_config_file_path))
    print('[SE_MESSAGE]   Input em settigs configuration yaml file path       := {}'.format(option_em_config_file_path))
    print('[SE_MESSAGE]   Input system settigs configuration yaml file path   := {}'.format(option_system_config_file_path))
    print('[SE_MESSAGE]   Output root directory path                          := {}'.format(option_output_dir_path))
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] Editing parameter settings in the specified RELION Schemes...')
    se_editor = SchemesEditor()
    # Make a backup of existing Schemes in output directory and copy template Schemes to output directory for editting.
    edit_schemes_dir_path = se_editor.make_edit_schemes(option_template_schemes_dir_path, option_output_dir_path)
    print('[SE_MESSAGE]   The directory path of output Schemes for editing    := {}'.format(edit_schemes_dir_path))
    se_editor.edit(edit_schemes_dir_path, option_sample_config_file_path, option_parallel_config_file_path, option_em_config_file_path, option_system_config_file_path, option_output_dir_path)
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] DONE!')
