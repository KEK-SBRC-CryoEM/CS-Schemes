
# version 30001 

data_job 

_rlnJobTypeLabel             relion.external 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_exe           XXX_JSE_REPLACE_SYSTEM_XXX 
in_mov           "" 
in_mic           $$mics_import 
in_part          "" 
in_coords        "" 
in_3dref         "" 
in_mask          "" 
param1_label     cryolo_repo 
param1_value     XXX_JSE_REPLACE_SYSTEM_XXX 
param2_label     threshold 
param2_value     $$GTF_pick_cryolo_thresh 
param3_label     device 
param3_value     XXX_JSE_REPLACE_PARALLEL_XXX 
param4_label     "" 
param4_value     "" 
param5_label     "" 
param5_value     "" 
param6_label     "" 
param6_value     "" 
param7_label     "" 
param7_value     "" 
param8_label     "" 
param8_value     "" 
param9_label     "" 
param9_value     "" 
param10_label    "" 
param10_value    "" 
nr_threads       XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue         XXX_JSE_REPLACE_PARALLEL_XXX 
queuename        030020_External_cryolo 
qsub             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1      XXX_JSE_REPLACE_PARALLEL_XXX
qsub_extra2      XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript       XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated    XXX_JSE_REPLACE_PARALLEL_XXX 
other_args       XXX_JSE_REPLACE_PARALLEL_XXX 
