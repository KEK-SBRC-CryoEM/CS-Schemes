
# version 50001

data_job

_rlnJobTypeLabel             relion.external
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 50001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
  do_queue         No 
    fn_exe         XXX_JSE_REPLACE_SYSTEM_XXX
  in_3dref         "" 
 in_coords         "" 
   in_mask         "" 
    in_mic         "" 
    in_mov         "" 
   in_part         "" 
min_dedicated      1 
nr_threads         1 
other_args         "" 
param10_label      "" 
param10_value      "" 
param1_label       yml_file 
param1_value       $$CSS_mbin_stack_split_yml 
param2_label       "" 
param2_value       "" 
param3_label       "" 
param3_value       "" 
param4_label       "" 
param4_value       "" 
param5_label       "" 
param5_value       "" 
param6_label       "" 
param6_value       "" 
param7_label       "" 
param7_value       "" 
param8_label       "" 
param8_value       "" 
param9_label       "" 
param9_value       "" 
      qsub         sbatch 
qsubscript         ""
 queuename         061010_External_stack_split 
 