
# version 30001 

data_job 

_rlnJobTypeLabel             relion.import 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
do_raw                    No 
fn_in_raw                 "" 
is_multiframe             Yes 
optics_group_name         "" 
fn_mtf                    "" 
angpix                    0.0 
kV                        0 
Cs                        0.0 
Q0                        0.0 
beamtilt_x                0 
beamtilt_y                0 
do_other                  Yes 
fn_in_other               $$SS_comm_lbin_ref3d_path 
node_type                 "3D reference (.mrc)" 
optics_group_particles    "" 
do_queue                  No 
queuename                 060040_Import_ref3d 
qsub                      CSS_NOT_APPLICABLE 
qsub_extra1               CSS_NOT_APPLICABLE 
qsub_extra2               CSS_NOT_APPLICABLE 
qsubscript                CSS_NOT_APPLICABLE 
min_dedicated             0 
other_args                "" 
