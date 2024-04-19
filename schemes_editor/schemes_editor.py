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
import os
import shutil
import datetime
import argparse
from jobstar_editor import jobstar_editor
from schemestar_editor import schemestar_editor

class SchemesEditor():
    # Constructors
    __SE_DEFAULT_FILE_KEY      = 'DefaultFile'
    __SE_PARALLEL_SETTING_KEY  = 'ParallelSettings'
    __SE_SYSTEM_SETTING_KEY    = 'SystemSettings'
    __SE_EM_SETTING_KEY        = 'EmSettings'
    __SE_SAMPLE_SETTING_KEY    = 'SampleSettings'
    __JOB_STAR_KEY_MAPPING_PS_YAML_FILE_PATH = './jobstar_editor/config_to_job_star_key_mapping_ps.yml'
    __JOB_STAR_KEY_MAPPING_SYS_YAML_FILE_PATH = './jobstar_editor/config_to_job_star_key_mapping_sys.yml'
#    __SE_DIR_NAME              = 'schemes_settings' 
    __SCHEMES_DIR_NAME         = 'Schemes'


    def __init__(self):
        self.default_file_dict=[]

    def __load_yaml_file(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        return yaml_dict

    def create_default_file(self, yaml_file_path): 
        self.default_file_dict = self.__load_yaml_file(yaml_file_path)
        parallel_setting_default = self.default_file_dict[type(self).__SE_DEFAULT_FILE_KEY][type(self).__SE_PARALLEL_SETTING_KEY]
        system_setting_default = self.default_file_dict[type(self).__SE_DEFAULT_FILE_KEY][type(self).__SE_SYSTEM_SETTING_KEY]
        em_settingdefault = self.default_file_dict[type(self).__SE_DEFAULT_FILE_KEY][type(self).__SE_EM_SETTING_KEY]
        sample_setting_default = self.default_file_dict[type(self).__SE_DEFAULT_FILE_KEY][type(self).__SE_SAMPLE_SETTING_KEY]
        return parallel_setting_default, system_setting_default, em_settingdefault, sample_setting_default

    def __make_output_subdir_backup(self, output_subdir_path):
        if os.path.exists(output_subdir_path): 
            print('[PDE_MESSAGE]', 'The output subdirectory "{}" already exists! Making a backup of the existing subdirectory...'.format(output_subdir_path))
            dt_now = datetime.datetime.now()
            backup_output_subdir_path = output_subdir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
            os.rename(output_subdir_path, backup_output_subdir_path)
        assert not os.path.exists(output_subdir_path), '[PDE_ASSERT] The output subdirectory "{}" must NOT exist at this point of code!'.format(output_subdir_path)


    def __make_output_schemes(self, template_schemes_dir_path, output_dir_path):
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

    def edit(self, template_schemes_dir_path, output_dir_path, parallel_setting_file_path, system_setting_file_path, em_setting_file_path, sample_setting_file_path):

        # [*] configs_dir_path: a path of directory containing all configuration yaml files
        # [*] template_schemes_dir_path: a path of tempate RELION Schemes directory 
        # [*] output_dir_path: a path of output directory.
        #     Under this directory the following subdirecties will be created 
        #     - Output "Schemes" subdirectroy and related files based on the template "Schemes" 
        #     - Output "ParallelSettings" subdirectroy and parallel settings files of all algorithm types 
        
        if not os.path.exists(output_dir_path):
            print('[PS_MESSAGE] The specified output directory "{}" does not exist yet! Creating the directory'.format(output_dir_path))
            os.mkdir(output_dir_path)
        assert os.path.exists(output_dir_path), '[PS_ASSERT] The output directory "{}" must exist at this point of code!'.format(output_dir_path)

#        ep_editor = ExecutablePathEditor.ExecutablePathEditor()
#        ep_editor.edit(configs_dir_path, template_schemes_dir_path , output_dir_path, computing_environment, output_schemes_subdir_path)
#        yaml_file_path = './configs/gotocloud/config_default.yml'
#        self.default_file_dict = self.__load_yaml_file(yaml_file_path)
#        sample_setting = self.default_file_dict['DefaultFile'][type(self).__SE_SAMPLE_SETTING_KEY]
#        print(self.default_file_dict['DefaultFile'][type(self).__SE_SAMPLE_SETTING_KEY])

        js_editor = jobstar_editor.JobStarEditor()
        output_schemes_subdir_path = self.__make_output_schemes(template_schemes_dir_path, output_dir_path)
#        settings_subdir_path = os.path.join(output_dir_path, type(self).__SS_DIR_NAME)
        js_editor.edit(parallel_setting_file_path, type(self).__JOB_STAR_KEY_MAPPING_PS_YAML_FILE_PATH, output_dir_path, output_schemes_subdir_path)
        js_editor.edit(system_setting_file_path, type(self).__JOB_STAR_KEY_MAPPING_SYS_YAML_FILE_PATH, output_dir_path, output_schemes_subdir_path)
        ss_editor = schemestar_editor.SchemeStarEditor()
        ss_editor.edit(output_schemes_subdir_path, sample_setting_file_path, output_dir_path)
        ss_editor.edit(output_schemes_subdir_path, em_setting_file_path, output_dir_path)



if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--default_file",  type=str,  default= '../../configs/gotocloud/config_default.yml', help = 'Path of input configuration yaml file.  (Default "./configs/gotocloud/config_type_algo.yml")')
    parser.add_argument("-s", "--schemes_dir",   type=str,  default='../../schemes_template/cs_schemes', help = 'Path of input template RELION Schemes directory containing all Schemes related files.  (Default "./Schemes")')
    parser.add_argument("-o", "--output_dir",    type=str,  default='./',  help = 'Path of output root directroy where all outputs will be saved.  (default "../")')

    args = parser.parse_args()
    option_default_file_path            = args.default_file
    option_template_schemes_dir_path    = args.schemes_dir
    option_output_dir_path              = args.output_dir

    se_editor = SchemesEditor()

#    yaml_file_path = './configs/gotocloud/config_default.yml'
    parallel_setting_default, system_setting_default, em_setting_default, sample_setting_default = se_editor.create_default_file(option_default_file_path)
#    parser = argparse.ArgumentParser()
    parser.add_argument("-par", "--parallel_default", type=str, default= parallel_setting_default, help = 'Path of input parallel settig yaml file.  (Default "{}")'.format(parallel_setting_default))
    parser.add_argument("-sys", "--system_default",   type=str, default= system_setting_default,   help = 'Path of input system settig yaml file.  (Default "{}")'.format(system_setting_default))
    parser.add_argument("-em",  "--em_default",       type=str, default= em_setting_default,       help = 'Path of input em settig yaml file.  (Default "{}")'.format(em_setting_default))
    parser.add_argument("-sam", "--sample_default",   type=str, default= sample_setting_default,   help = 'Path of input sample settig yaml file.  (Default "{}")'.format(sample_setting_default))

    # Rename arguments for readability
    # No arguments with this program
    
    # Rename options for readability
    args = parser.parse_args()
    option_parallel_setting_file_path  = args.parallel_default
    option_system_setting_file_path     = args.system_default
    option_em_setting_file_path         = args.em_default
    option_sample_setting_file_path     = args.sample_default

    print('[SE_MESSAGE] Specified values of all options')
    print('[SE_MESSAGE]   Input configurations directory path  := {}'.format(option_default_file_path))
    print('[SE_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[SE_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[SE_MESSAGE]   Input parallel setting file path     := {}'.format(option_parallel_setting_file_path))
    print('[SE_MESSAGE]   Input system setting file path       := {}'.format(option_system_setting_file_path))
    print('[SE_MESSAGE]   Input em setting file path           := {}'.format(option_em_setting_file_path))
    print('[SE_MESSAGE]   Input sample setting file path       := {}'.format(option_sample_setting_file_path))
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] Editing settings in the specified schemes...')
    se_editor = SchemesEditor()
    se_editor.edit(option_template_schemes_dir_path, option_output_dir_path, option_parallel_setting_file_path, option_system_setting_file_path, option_em_setting_file_path, option_sample_setting_file_path)
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] DONE!')
