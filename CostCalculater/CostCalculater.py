#!/usr/bin/env python3.7
##########################################################################################
# Author: Misato Yamamoto  (misatoy＠post.kek.jp), Toshio Moriya (toshio.moriya@kek.jp)
# 
# Copyright (c) 2023 KEK IMMS SBRC
# 
# Description:
# Calculate process time and cost for Relion.
# Only if AWS is used, the cost is calculated based on the price per instance set in yaml files.
# Output results to csv file. 
#
# Usage:
# !!! 'starfile' installation is required　!!!  (when executed on AWS headnode)
# $ python3 -m pip install starfile
#
# Example)
#  -- fsx
#   |-- CostCalculater
#     |-- CostCalculater.py
#     |-- Config_instance_info.yml
#   |-- RELION project directory
#
# $ cd /fsx/RELION project directory
# $ python3 /fsx/CostCalculater/CostCalculater.py
#
#　You can also use as follows.
# $ python3 /fsx/CostCalculater/CostCalculater.py --relion_dir /fsx/<RELION project directory>
#
##########################################################################################
# Output data to csv file.
# - JOB-related items (from default_pipeline.star)
#   - Job type/Job ID 
#
# - Parallel Settings-related items (from job.star)
#   - Job Name 
#   - GPUs 
#   - MPIs 
#   - Threads
#   - MPIs/Nodes
#   - Nodes (Calculation result from MPIs and MPIs/Nodes)
#
# - Process time 
#   - process time (hh:mm:ss)  (from timestamp difference between 2 files)
#   - process time (hours)     (Conversion of timestamp difference)
#
# - Instance-rerated items
#   - Instance name 
#   - Instance type (from instance_info.yml)
#   - Cores (from Config_instance_info.yml)
#   - Instance Price/hours (from Config_instance_info.yml)
#
# - Cost-rerated items
#   - Cost/job (Calculation results from Nodes, process time (hours) and Instance Price/hours )
#
# - Total of all jobs
#   - Total Time (Sum of process time (hours))
#   - Total Cost (Sum of Cost/job)
#
##########################################################################################
#
# ========================================================================================
# Directory structure
# 
# - Script Directory 
#   |-- CostCalculaterr.py
#   |-- Config_instance_info.yml
#
# - <INPUT>
#   |-- RELION Project dir   (default: current dir)
#     |-- default_pipeline.star
#     |-- Job type dir/Job ID dir
#       |-- note.txt     <- first create file 
#       |-- RELION_JOB_EXIT_SUCCESS    <- last create file
#       |-- job.star
#
# - <OUTPUT>  (default: current dir)
#   |-- cc_result_<project dir name>.csv
#


import os
import csv
import re
import os.path
import datetime
import yaml
import starfile
import argparse

class CostCalculater():
    # Private class constants
    #__RESULT_FILE_NAME = 'results.csv'
    __OUTPUT_HEADER_JOB=['JobType/JobID']
    __OUTPUT_HEADER_PARALLEL_SETTINGS = ['Job Name','GPUs','MPI','Thread','MPIs/Node','Nodes']
    __OUTPUT_HEADER_PROCESS_TIME = ['Elapse hh:mm:ss','Elapse_hours'] 
    __OUTPUT_HEADER_INSTANCE= ['EC2 Instance Name','EC2 Instance Type','Cores/node','Cost/hours(USD)','Cost(USD)']
    __PIPELINE_STAR_FILE_NAME = 'default_pipeline.star'
    __NOTE_TXT_FILE_NAME = 'note.txt'
    __EXIT_SUCCESS_FILE_NAME = 'RELION_JOB_EXIT_SUCCESS'
    __JOB_STAR_FILE_NAME = 'job.star'
    __JOB_STAR_KEY_LIST = ['queuename', 'gpu_ids', 'nr_mpi', 'nr_threads', 'min_dedicated']
    __INSTANCE_INFO_YML_NAME = 'Config_instance_info.yml'
    __CC_FILE_PREFIX  = 'cc_result_' 
    __CC_RESULT_FILE_EXT = '.csv'

    def __init__(self):
        # Private instance variables
        self.__job_id_dir_path_list = []
        self.__cc_result_processtime_and_cost_list_list = []
        self.__process_time_hours_list = []
        self.__cost_per_job_list = []
        self.__output_header =[]
        self.__total_time_and_cost_list = []

    # Get parallel setting data from job.star saved when relion execution.
    # Save all contents of 'data_joboptions_values' in job.star file as dict data  -> self.__job_star_options_dict
    def __construct_job_star_dict(self, file_path):
        self.__job_star_options_dict = {}
        job_star_dict = starfile.read(file_path)
        self.__job_star_options_dict['jobtypelabel'] = job_star_dict['job']['rlnJobTypeLabel'][0]
        for i in range(len(job_star_dict ['joboptions_values'])):
            key = job_star_dict['joboptions_values']['rlnJobOptionVariable'][i]
            value = job_star_dict['joboptions_values']['rlnJobOptionValue'][i]
            self.__job_star_options_dict[key] = value

    # Get timestamp of files
    def __get_timestamp(self, file_path):
        sec = os.path.getmtime(file_path)
        timestamp = datetime.datetime.fromtimestamp(sec)
        return timestamp
    
    # Calculatting processing time per job from difference between timestamps of 2 files.
    def __calc_timestamp_diff(self, first_created_file_path, last_created_file_path):
        start_date = self.__get_timestamp(first_created_file_path)
        end_date = self.__get_timestamp(last_created_file_path)
        timestamp_diff = end_date - start_date
        #self.__calculate_time_sec = self.__timestamp_diff.total_seconds()
        timestamp_diff_hour = timestamp_diff.total_seconds()/3600
        return timestamp_diff, timestamp_diff_hour

    # Get Relion processing time (hh:mm:ss and hours)
    def __get_process_time(self, relion_dir_path, job_id_dir_path):
        self.__process_time_list = []
        # Calculate processing time per job from difference between timestamps of 2 files.
        first_created_file_path = os.path.join(relion_dir_path, job_id_dir_path, type(self).__NOTE_TXT_FILE_NAME)
        last_created_file_path = os.path.join(relion_dir_path, job_id_dir_path, type(self).__EXIT_SUCCESS_FILE_NAME)
        if not os.path.exists(first_created_file_path) or not os.path.exists(last_created_file_path):
            print('[CC_MESSAGE] WARNING: Relion output file "{}" or "{}" dose not exist!'.format(first_created_file_path, last_created_file_path))
            [self.__process_time_hhmm, self.__process_time_hour]=["N/A", 0]
            self.__process_time_list.extend([self.__process_time_hhmm, self.__process_time_hour])
            self.__process_time_hours_list.append(0)
        else:
            [self.__process_time_hhmm, self.__process_time_hour] = self.__calc_timestamp_diff(first_created_file_path, last_created_file_path)
            self.__process_time_list.extend([self.__process_time_hhmm, round(self.__process_time_hour,3)])
            self.__process_time_hours_list.append(self.__process_time_hour)
    
    # Get job id directories saved in default_pipeline.star under RELION project dir
    def __get_jobid_dir_path(self,relion_dir_path):
        pipline_star_file_path = os.path.join(relion_dir_path, type(self).__PIPELINE_STAR_FILE_NAME)
        assert os.path.exists(pipline_star_file_path), '[CC_ASSERT] The default_pipeline.star file "{}" must exist!'.format(pipline_star_file_path)
        pipline_dict = starfile.read(pipline_star_file_path)
        for i in range(len(pipline_dict['pipeline_processes'])):
            self.__job_id_dir_path_list.append(pipline_dict['pipeline_processes']['rlnPipeLineProcessName'][i])

    def __get_parallel_settings(self):
        self.__parallel_settings_list = []
        for job_star_key in type(self).__JOB_STAR_KEY_LIST:
            if job_star_key in self.__job_star_options_dict.keys():
                # Counts nunber of gpus, only if gpus are used.
                if job_star_key == 'gpu_ids':
                    if 'use_gpu' in self.__job_star_options_dict.keys() and self.__job_star_options_dict['use_gpu'] == 'Yes':  
                        nr_gpus = [len(re.sub(r'[^0-9]', '', self.__job_star_options_dict[job_star_key]))][0]
                    else:
                        nr_gpus = ""
                    self.__parallel_settings_list.append(nr_gpus)
                else:
                    self.__parallel_settings_list.append(self.__job_star_options_dict[job_star_key])
            elif job_star_key == 'gpu_ids' and 'cryolo' in self.__job_star_options_dict['queuename']:
                nr_gpus = [len(re.sub(r'[^0-9]', '', self.__job_star_options_dict['param3_value']))][0]
                self.__parallel_settings_list.append(nr_gpus)
            else:
                self.__parallel_settings_list.append("")   # If the key dose not exist, add empty to list.

        if set(['do_queue','nr_mpi', 'min_dedicated']).issubset(self.__job_star_options_dict.keys()) and self.__job_star_options_dict['do_queue'] == 'Yes':  
            self.__nr_nodes = (int(self.__job_star_options_dict['nr_mpi']) + int(self.__job_star_options_dict['min_dedicated']) - 1) // int(self.__job_star_options_dict['min_dedicated'])
        elif 'cryolo' in self.__job_star_options_dict['queuename']:
            self.__nr_nodes = self.__job_star_options_dict['param3_value'].count('0')  # Number of '0' is considered as the number of nodes in the case of 'cyrolo.
        else:
            self.__nr_nodes = 0
        self.__parallel_settings_list.append(self.__nr_nodes)

    def __get_instance_info(self, instance_info_yml_path, aws_region):
        assert os.path.exists(instance_info_yml_path), '[CC_ASSERT] The yaml file set instance price "{}" must exist!'.format(instance_info_yml_path)
        with open(instance_info_yml_path, 'r') as yaml_file:
            instance_info_dict_list = yaml.safe_load(yaml_file)
        self.__instance_info_list=[]
        for instance_info_dict in instance_info_dict_list:
            if instance_info_dict['Region'] == aws_region: 
                if set(['qsub_extra1','do_queue']).issubset(self.__job_star_options_dict.keys()) and self.__job_star_options_dict['do_queue'] == 'Yes':
                    for instance_info_setting_dict in instance_info_dict['InstanceSettings']:
                        if instance_info_setting_dict['Name'] == self.__job_star_options_dict['qsub_extra1']:  
                            self.__cost_per_hours = instance_info_setting_dict['CostPerHours']
                            self.__instance_info_list = list(instance_info_setting_dict.values())
                            break
                    instance_info_setting_dict_name = [name.get('Name') for name in instance_info_dict['InstanceSettings']]
                    if self.__job_star_options_dict['qsub_extra1'] not in instance_info_setting_dict_name:
                        print('Cost of instance "{}" is not set in "{}" '.format(self.__job_star_options_dict['qsub_extra1'],type(self).__INSTANCE_INFO_YML_NAME))
                        self.__cost_per_hours = 0
                        self.__instance_info_list = [self.__job_star_options_dict['qsub_extra1']]+[""]*(len(instance_info_setting_dict.values()) - 2) + [self.__cost_per_hours]
                else:
                    self.__cost_per_hours = 0
                    self.__instance_info_list = [""]*(len(instance_info_dict['InstanceSettings'][0].values()) - 1) + [self.__cost_per_hours]

    def __construct_results_list(self, relion_dir_path = './', instance_yml_dir_path=os.path.dirname(__file__), aws_region='ap-northeast-1'):
        self.__get_jobid_dir_path(relion_dir_path)
        for job_id_dir_path in self.__job_id_dir_path_list:
            self.__output_header = []
            self.__results_list = []
            job_star_file_path = os.path.join(relion_dir_path, job_id_dir_path, type(self).__JOB_STAR_FILE_NAME)
            assert os.path.exists(job_star_file_path), '[CC_ASSERT] The job.star file "{}" must exist!'.format(job_star_file_path)
    
            self.__construct_job_star_dict(job_star_file_path)
            self.__get_parallel_settings()
            self.__get_process_time(relion_dir_path, job_id_dir_path)
            self.__results_list.append(job_id_dir_path)
            self.__results_list.extend(self.__parallel_settings_list)
            self.__results_list.extend(self.__process_time_list)
            self.__output_header.extend(type(self).__OUTPUT_HEADER_JOB)
            self.__output_header.extend(type(self).__OUTPUT_HEADER_PARALLEL_SETTINGS)
            self.__output_header.extend(type(self).__OUTPUT_HEADER_PROCESS_TIME)
            # Create instance price dict per region 
            # If the instance price file dose not exist, not calculate cost per job and total cost.
            instance_info_yml_path = os.path.join(instance_yml_dir_path, type(self).__INSTANCE_INFO_YML_NAME)
            if os.path.exists(instance_info_yml_path):
                self.__get_instance_info(instance_info_yml_path, aws_region)
                cost_per_job = self.__cost_per_hours * self.__nr_nodes * self.__process_time_hour
                self.__results_list.extend(self.__instance_info_list)
                self.__results_list.append(round(cost_per_job, 3))
                self.__cost_per_job_list.append(cost_per_job)
                self.__output_header.extend(type(self).__OUTPUT_HEADER_INSTANCE)
            self.__cc_result_processtime_and_cost_list_list.append(self.__results_list)
        
        # Calculate total cost for all job 
        self.__total_time_and_cost_list = [""]*(len(self.__output_header)-len(type(self).__OUTPUT_HEADER_INSTANCE)-2)
        self.__total_time_and_cost_list.extend(['Total Time', round(sum(self.__process_time_hours_list),3)])
        self.__total_time_and_cost_list.extend([""]*(len(type(self).__OUTPUT_HEADER_INSTANCE)-2))
        self.__total_time_and_cost_list.extend(['Total Cost', round(sum(self.__cost_per_job_list),3)])

    # Save the calculation results of processing time and cost to a csv file.
    def __save_cc_result_csv(self, relion_dir_path, output_dir_path):
        relion_project_name = os.path.basename(os.path.abspath(relion_dir_path))
        cc_result_file_name = type(self).__CC_FILE_PREFIX + relion_project_name + type(self).__CC_RESULT_FILE_EXT
        cc_result_file_path = os.path.join(output_dir_path, cc_result_file_name)
        with open(cc_result_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.__output_header)                 # write header
            for __cc_result_processtime_and_cost_list in self.__cc_result_processtime_and_cost_list_list:
                writer.writerow(__cc_result_processtime_and_cost_list)                  # write the calculation results each job
            writer.writerow(self.__total_time_and_cost_list)      # write total processing time and total cost


    def edit(self, instance_yml_dir_path = os.path.dirname(__file__), relion_dir_path = './', output_dir_path = './', aws_region='ap-northeast-1'):
        # [*] instance_yml_dir_path: a path of directory containing yaml file with instance price.
        # [*] relion_dir_path: a path of RELION project directory 
        # [*] output_dir_path: a path of output directory.
        
        # Check preconditions!
        assert os.path.exists(instance_yml_dir_path), '[CC_ASSERT] The configurations directory "{}" must exist!'.format(instance_yml_dir_path)
        assert os.path.exists(relion_dir_path), '[CC_ASSERT] The template Schemes directory "{}" must exist!'.format(relion_dir_path)
        if not os.path.exists(output_dir_path):
            print('[CC_MESSAGE] The specified output directory "{}" does not exist yet! Creating the directory'.format(output_dir_path))
            os.mkdir(output_dir_path)
        assert os.path.exists(output_dir_path), '[CC_ASSERT] The output directory "{}" must exist at this point of code!'.format(output_dir_path)
        
        self.__construct_results_list(relion_dir_path, instance_yml_dir_path, aws_region)
        self.__save_cc_result_csv(relion_dir_path, output_dir_path)


if __name__ == "__main__":
    # Parse command argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--instance_yml_dir", type=str, default=os.path.dirname(__file__),  help = 'Path of directory containing yaml file with instance price.  (Default "script directory path")')
    parser.add_argument("-r", "--relion_dir",       type=str, default='./', help = 'Path of RELION project directory.  (Default "./")')
    parser.add_argument("-o", "--output_dir",       type=str, default='./', help = 'Path of output root directory where result csv file will be saved.  (default "./")')
    parser.add_argument("-a", "--aws_region",       type=str, default='ap-northeast-1', help = 'AWS region in use.  (default "ap-northeast-1")')

    args = parser.parse_args()
    
    # Rename options for readability
    option_instance_yml_dir_path    = args.instance_yml_dir
    option_relion_dir_path          = args.relion_dir
    option_output_dir_path          = args.output_dir
    option_aws_region               = args.aws_region

    print('[CC_MESSAGE] Specified values of all options')
    print('[CC_MESSAGE]   Input instance yaml directory path   := {}'.format(option_instance_yml_dir_path))
    print('[CC_MESSAGE]   Input Relion project directory path  := {}'.format(option_relion_dir_path))
    print('[CC_MESSAGE]   Output root directory path           := {}'.format(option_output_dir_path))
    print('[CC_MESSAGE]   AWS region in use                    := {}'.format(option_aws_region))
    print('[CC_MESSAGE] ')
    print('[CC_MESSAGE] Calculating execution time and cost of all jobs in relion project directory...')
    print('[CC_MESSAGE] ')
    print('[CC_MESSAGE] ')
    cost_calculater = CostCalculater()
    cost_calculater.edit(option_instance_yml_dir_path, option_relion_dir_path)
    print('[CC_MESSAGE] ')
    print('[CC_MESSAGE] ')
    print('[CC_MESSAGE] DONE!')