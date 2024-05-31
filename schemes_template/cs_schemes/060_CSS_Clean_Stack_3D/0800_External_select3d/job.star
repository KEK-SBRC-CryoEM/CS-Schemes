
# version 30001 

data_job 

_rlnJobTypeLabel             relion.external 
_rlnJobIsContinue                       1 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_exe           $$select_class3d_exe 
in_mov           "" 
in_mic           "" 
in_part          $$CSS_cls3d_parts
in_coords        "" 
in_3dref         "" 
in_mask          "" 
param1_label     "" 
param1_value     "" 
param2_label     "" 
param2_value     "" 
param3_label     "" 
param3_value     "" 
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
nr_threads       1 
do_queue         No 
queuename        0800_External_select3d 
qsub             CSS_NOT_APPLICABLE 
qsub_extra1      CSS_NOT_APPLICABLE 
qsub_extra2      CSS_NOT_APPLICABLE 
qsubscript       CSS_NOT_APPLICABLE 
min_dedicated    0 
other_args       "" 
