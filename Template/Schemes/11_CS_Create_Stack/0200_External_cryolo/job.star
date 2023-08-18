
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
fn_exe         $$cryolo_exe
in_mov         ""
in_mic         $$mics_import
in_part        ""
in_coords      ""  
in_3dref       "" 
in_mask        "" 
param10_label  "" 
param10_value  "" 
param1_label   cryolo_repo 
param1_value   $$cryolo_repo 
param2_label   threshold 
param2_value   $$CS_cryolo_threshold 
param3_label   device 
param3_value                    0,1,2,3 
param4_label   "" 
param4_value   "" 
param5_label   "" 
param5_value   "" 
param6_label   "" 
param6_value   "" 
param7_label   "" 
param7_value   "" 
param8_label   "" 
param8_value   "" 
param9_label   "" 
param9_value   "" 
nr_threads                    1
do_queue                    No 
queuename      0200_Extenal_cryolo
qsub                    ""
qsub_extra1                    invalid_partition           
qsubscript                    ""
min_dedicated                    1 
other_args                    "" 

