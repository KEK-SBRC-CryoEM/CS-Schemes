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


import os
import argparse
#import ExecutablePathEditor
#import ParallelSettingsEditor
from ExecutablePathEditor import ExecutablePathEditor
from ParallelSettingsEditor import ParallelSettingsEditor
from ProteinDataEditor import ProteinDataEditor

class SchemesEditor():
    # Constructors

    def edit(self, configs_dir_path, template_schemes_dir_path, output_dir_path, computing_environment):
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

        ep_editor = ExecutablePathEditor.ExecutablePathEditor()
        output_schemes_subdir_path = ep_editor.make_output_schemes(template_schemes_dir_path, output_dir_path)
        ep_editor.edit(configs_dir_path, template_schemes_dir_path , output_dir_path, computing_environment, output_schemes_subdir_path)
        ps_editor = ParallelSettingsEditor.ParallelSettingsEditor()
        ps_editor.edit(configs_dir_path, output_dir_path, output_schemes_subdir_path)
        pd_editor = ProteinDataEditor.ProteinDataEditor()
        pd_editor.edit(configs_dir_path, output_dir_path, output_schemes_subdir_path)

 

if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configs_dir",        type=str,    default='./Configs',    help = 'Path of input configurations directory containing all configuration yaml files.  (Default "./Configs")')
    parser.add_argument("-s", "--schemes_dir",        type=str,    default='./Schemes',     help = 'Path of input template RELION Schemes directory containing all Schemes related files.  (Default "./Schemes")')
    parser.add_argument("-o", "--output_dir",         type=str,    default='../',       help = 'Path of output root directroy where all outputs will be saved.  (default "../")')
    parser.add_argument("-e", "--compute_env",        type=str,    default='Reedbush',      help = 'Computing environment in use.  (default "Reedbush")')
    
    args = parser.parse_args()
    ### args, unknown = parser.parse_known_args()

    # Rename arguments for readability
    # No arguments with this program
    
    # Rename options for readability
    option_configs_dir_path             = args.configs_dir
    option_template_schemes_dir_path    = args.schemes_dir
    option_output_dir_path              = args.output_dir
    option_computing_environment        = args.compute_env
    
    print('[SE_MESSAGE] Specified values of all options')
    print('[SE_MESSAGE]   Input configurations directory path  := {}'.format(option_configs_dir_path))
    print('[SE_MESSAGE]   Input tempate Schemes directory path := {}'.format(option_template_schemes_dir_path))
    print('[SE_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[SE_MESSAGE]   Input computing_environment          := {}'.format(option_computing_environment))
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] Editing settings in the specified shcemes...')
    css_editor = SchemesEditor()
    css_editor.edit(option_configs_dir_path, option_template_schemes_dir_path, option_output_dir_path, option_computing_environment)
    print('[SE_MESSAGE] ')
    print('[SE_MESSAGE] DONE!')
