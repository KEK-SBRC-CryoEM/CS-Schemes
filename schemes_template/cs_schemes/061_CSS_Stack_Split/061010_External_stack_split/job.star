
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
fn_exe           XXX_JSE_REPLACE_SYSTEM_XXX 
in_mov           "" 
in_mic           "" 
in_part          $$CSS_mbin_stack_split_refined_star  
in_coords        "" 
in_3dref         "" 
in_mask          "" 
param1_label     splits_num 
param1_value     $$CSS_mbin_stack_split_splits_num 
param2_label     particles_num 
param2_value     $$CSS_mbin_stack_split_particles_num 
param3_label     scheme_list 
param3_value     $$CSS_mbin_stack_split_scheme_list 
param4_label     scheme_copy_source 
param4_value     $$CSS_mbin_stack_split_scheme_copy_source 
param5_label     link_type 
param5_value     $$CSS_mbin_stack_split_link_type 
param6_label     merge_scheme_node 
param6_value     $$CSS_mbin_stack_split_merge_scheme_node 
param7_label     merge_file 
param7_value     $$CSS_mbin_stack_split_merge_file 
param8_label     "" 
param8_value     "" 
param9_label     "" 
param9_value     "" 
param10_label    "" 
param10_value    "" 
nr_threads       XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue         XXX_JSE_REPLACE_PARALLEL_XXX 
queuename        061010_External_stack_split 
qsub             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1      XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2      XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript       XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated    XXX_JSE_REPLACE_PARALLEL_XXX 
other_args       XXX_JSE_REPLACE_PARALLEL_XXX 
