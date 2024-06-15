#!/usr/bin/env python3.7
##########################################################################################
# Author: Misato Yamamoto  (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023 KEK IMMS SBRC
# 
# Description:
# Setup of RELION schemes editor scripts. 
# Running this script will git clone the schemes_editor and copy only the necessary setting files to the specified directory.
#
##########################################################################################
# ========================================================================================
# Directory structure
# 
# - <INPUT> User-Defined copy destination directory and system environment 
#    python3 installer_kek_schemes.py -e <system environment> -s <path to setup directory> 
#
# - <OUTPUT> User-Defined clone Directory 
#   |-- kek_schemes
#     |-- schemes_editor
#     | |-- jobstar_editor
#     | | |-- jobstar_editor.py
#     | | |-- config_jobtype_to_algotype_item.yml
#     | | |-- config_to_jobstar_keymap_parallel.yml
#     | | |-- config_to_jobstar_keymap_system.yml
#     | |-- schemestar_editor
#     | | |-- schemestar_editor.py
#     | |-- schemes_editor.py
#     |
#     |-- schemes_template
#     | |-- cs_schemes
#     |
#     |-- configs
#       |-- common
#       | |-- config_em_settings_kek_krios.yml
#       | |-- config_em_settings_tutorial.yml
#       | |-- config_sample_settings.yml
#       |-- common_tutorial
#       | |-- config_em_settings_kek_krios.yml
#       | |-- config_em_settings_tutorial.yml
#       | |-- config_sample_settings.yml
#       |-- gotocloud
#       | |-- config_type_algo.yml
#       | |-- config_level_submission.yml
#       | |-- config_level_device.yml
#       | |-- config_level_algo.yml
#       | |-- config_system_settings.yml
#       |-- gotocloud_tutorial
#       | |-- config_type_algo.yml
#       | |-- config_level_submission.yml
#       | |-- config_level_device.yml
#       | |-- config_level_algo.yml
#       | |-- config_system_settings.yml
#       |-- kek_rbl
#     ...
#
# - <OUTPUT> User-Defined setup Directory in case the spesified "gotocloud"  <<< Copy only the necessary files to the specified directory
#   |-- schemes_editor
#     |-- jobstar_editor
#     | |-- jobstar_editor.py
#     | |-- config_jobtype_to_algotype_item.yml
#     | |-- config_to_jobstar_keymap_parallel.yml
#     | |-- config_to_jobstar_keymap_system.yml
#     |-- schemestar_editor
#     | |-- schemestar_editor.py
#     |-- schemes_editor.py
#     |
#     |-- schemes_template
#     | |-- cs_schemes
#     |
#     |-- configs
#       |-- common
#       | |-- config_em_settings_kek_krios.yml
#       | |-- config_em_settings_tutorial.yml
#       | |-- config_sample_settings.yml
#       |-- common_tutorial
#       | |-- config_em_settings_kek_krios.yml
#       | |-- config_em_settings_tutorial.yml
#       | |-- config_sample_settings.yml
#       |-- environment_dependent
#       | |-- config_type_algo.yml
#       | |-- config_level_submission.yml
#       | |-- config_level_device.yml
#       | |-- config_level_algo.yml
#       | |-- config_system_settings.yml
#       |-- environment_dependent_tutorial
#         |-- config_type_algo.yml
#         |-- config_level_submission.yml
#         |-- config_level_device.yml
#         |-- config_level_algo.yml
#         |-- config_system_settings.yml
#
# ========================================================================================


import os
import shutil
import subprocess
import argparse
import datetime

def clone_repo(repo_url, clone_path):
    #glone Git repository
    subprocess.run(["git", "clone", repo_url, clone_path], check=True)

def copy_file(src_dir_path, dest_path):
     #copy the some directory to specified path
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    shutil.copytree(src_dir_path, dest_path, dirs_exist_ok=True)

def make_output_dir_backup(output_dir_path):
    if os.path.exists(output_dir_path): 
        print('[SE_MESSAGE]', 'The output subdirectory "{}" already exists! Making a backup of the existing subdirectory...'.format(output_dir_path))
        dt_now = datetime.datetime.now()
        backup_output_dir_path = output_dir_path + '_backup' + '_' + f'{dt_now.year:04}'+ f'{dt_now.month:02}' + f'{dt_now.day:02}' + f'{dt_now.hour:02}' + f'{dt_now.minute:02}' + f'{dt_now.second:02}'
        os.rename(output_dir_path, backup_output_dir_path)
        assert not os.path.exists(output_dir_path), '[SE_ASSERT] The output subdirectory "{}" must NOT exist at this point of code!'.format(output_dir_path)

def replace_text_in_file(file_path, old_text, new_text):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        file_data = file.read()
    
    # Replace the old text with the new text
    file_data = file_data.replace(old_text, new_text)
    
    # Open the file in write mode and write the modified data
    with open(file_path, 'w') as file:
        file.write(file_data)

def edit(system_env, setup_dir_path):
    SSE_configs_dir_name = 'configs'
    SSE_schemes_temp_dir_name ='schemes_template'
    SSE_scheme_editor_dir_name = 'schemes_editor'
    SSE_env_depend_dir_name = 'environment_dependent'
    SSE_tutorial_suffix = '_tutorial'
    SSE_common_dir_name = 'common'

    configs_dir_name_common = os.path.join(SSE_configs_dir_name, SSE_common_dir_name)
    configs_dir_name_common_tutorial = os.path.join(SSE_configs_dir_name, SSE_common_dir_name + SSE_tutorial_suffix)
    configs_dir_name_env_src = os.path.join(SSE_configs_dir_name, system_env)
    configs_dir_name_env_dest = os.path.join(SSE_configs_dir_name, SSE_env_depend_dir_name)
    configs_dir_name_env_tutorial_src = os.path.join(SSE_configs_dir_name, system_env + SSE_tutorial_suffix )
    configs_dir_name_env_tutorial_dest = os.path.join(SSE_configs_dir_name, SSE_env_depend_dir_name + SSE_tutorial_suffix)
    dir_name_list = [[SSE_scheme_editor_dir_name, ""],[configs_dir_name_common, configs_dir_name_common],[configs_dir_name_common_tutorial, configs_dir_name_common_tutorial],[configs_dir_name_env_src, configs_dir_name_env_dest],[configs_dir_name_env_tutorial_src, configs_dir_name_env_tutorial_dest], [SSE_schemes_temp_dir_name, SSE_schemes_temp_dir_name]]

    # Get clone repository path from script directory path.
    clone_dir_path = os.path.dirname(__file__)
    #copy the some directory to specified path
    setup_subdir = os.path.join(setup_dir_path, SSE_scheme_editor_dir_name)
    make_output_dir_backup(setup_subdir)
    assert not os.path.exists(setup_subdir), '[SSE_ASSERT] The setup directory "{}" must NOT exist at this point of code!'.format(dest_dir_path)
    for dir_name in dir_name_list:
        src_dir_path = os.path.join(clone_dir_path, dir_name[0])
        assert os.path.exists(src_dir_path), '[SSE_ASSERT] The source directory as git clone "{}" must exist!'.format(src_dir_path)
        dest_dir_path = os.path.join(setup_subdir, dir_name[1])
        copy_file(src_dir_path, dest_dir_path)
        assert os.path.exists(dest_dir_path), '[SSE_ASSERT] The destination directory to set up "{}" must exist!'.format(dest_dir_path)
    
    ### # Specify the file path and the strings to replace
    ### file_path = 'path/to/your/file.txt'
    ### old_text = 'old string to replace'
    ### new_text = 'new string to replace with'
    ### # Call the function to perform the replacement
    ### replace_text_in_file(file_path, old_text, new_text)
    
    current_path = os.getcwd()
    os.chdir(setup_dir_path)
    setup_dir_absolute_path = os.path.join(os.getcwd(),SSE_scheme_editor_dir_name)
    print('setup_dir_absolute_path :=', setup_dir_absolute_path)
    setup_dir_absolute_path
    
    evn_default_configs_file_path = os.path.join(setup_dir_absolute_path, configs_dir_name_env_dest, 'default_configs.yml')
    print('evn_default_configs_file_path :=', evn_default_configs_file_path)
    replace_text_in_file(evn_default_configs_file_path, 'XXX_SETUP_DIR_PATH_XXX', setup_dir_absolute_path)

    evn_tutorial_default_configs_file_path = os.path.join(setup_dir_absolute_path, configs_dir_name_env_tutorial_dest, 'config_type_algo.yml')
    print('evn_tutorial_default_configs_file_path :=', evn_tutorial_default_configs_file_path)
    replace_text_in_file(evn_tutorial_default_configs_file_path, 'XXX_SETUP_DIR_PATH_XXX', setup_dir_absolute_path)

    evn_default_config_type_algo_file_path = os.path.join(setup_dir_absolute_path, configs_dir_name_env_dest, 'config_type_algo.yml')
    print('evn_default_config_type_algo_file_path :=', evn_default_config_type_algo_file_path)
    replace_text_in_file(evn_default_config_type_algo_file_path, 'XXX_SETUP_DIR_PATH_XXX', setup_dir_absolute_path)

    evn_turorial_default_config_type_algo_file_path = os.path.join(setup_dir_absolute_path, configs_dir_name_env_tutorial_dest, 'config_type_algo.yml')
    print('evn_turorial_default_config_type_algo_file_path :=', evn_turorial_default_config_type_algo_file_path)
    replace_text_in_file(evn_turorial_default_config_type_algo_file_path, 'XXX_SETUP_DIR_PATH_XXX', setup_dir_absolute_path)

    os.chdir(current_path)

if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser(description="Install cs_schemes")
    parser.add_argument("-e", "--system_env",     type=str, required=True,         help="system environment.  e.g. gotocloud")
    parser.add_argument("-s", "--setup_dir_path", type=str, required=True,         help="PATH to copy destination directory")

    args = parser.parse_args()
    
    # Rename options for readability
    option_system_env       = args.system_env
    option_setup_dir_path   = args.setup_dir_path

    print('[SSE_MESSAGE] Specified values of all options')
    print('[SSE_MESSAGE]   Input system environment         := {}'.format(option_system_env))
    print('[SSE_MESSAGE]   Output setup directory path      := {}'.format(option_setup_dir_path))
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] setting up schemes_editor...')
    print('[SSE_MESSAGE] ')
    edit(option_system_env, option_setup_dir_path)
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] ')
    print('[SSE_MESSAGE] DONE!')
