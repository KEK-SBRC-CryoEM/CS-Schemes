
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
  do_queue                    No 
    fn_exe         $$select_class3d_exe 
  in_3dref         "" 
 in_coords         "" 
   in_mask         "" 
    in_mic         "" 
    in_mov         "" 
   in_part        Schemes/13_CS_Clean_Stack_3D/0700_Class3D/run_it050_data.star
min_dedicated                    1 
nr_threads                    1 
other_args                    "" 
param10_label         "" 
param10_value         "" 
param1_label         "" 
param1_value         "" 
param2_label         "" 
param2_value         "" 
param3_label         "" 
param3_value                    "" 
param4_label         "" 
param4_value         "" 
param5_label         "" 
param5_value         "" 
param6_label         "" 
param6_value         "" 
param7_label         "" 
param7_value         "" 
param8_label         "" 
param8_value         "" 
param9_label         "" 
param9_value         "" 
      qsub                    "" 
qsub_extra1                    invalid_partition 
qsubscript                    "" 
 queuename 0800_External_select3d 
