
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
fn_in_other               $$SS_comm_mbin_mask3d_path 
node_type                 "3D mask (.mrc)" 
optics_group_particles    "" 
do_queue                  XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                 070060_Import_mask3d 
qsub                      XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1               XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2               XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript                XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated             XXX_JSE_REPLACE_PARALLEL_XXX 
other_args                XXX_JSE_REPLACE_PARALLEL_XXX 
