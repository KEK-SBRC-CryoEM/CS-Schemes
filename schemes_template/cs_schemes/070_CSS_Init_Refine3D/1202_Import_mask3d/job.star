
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
do_raw                   No
fn_in_raw                Micrographs/*.tif
is_multiframe            Yes
optics_group_name        opticsGroup1
fn_mtf                   ""
angpix                   0.885
kV                       200
Cs                       1.4 
Q0                       0.1 
beamtilt_x               0 
beamtilt_y               0 
do_other                 Yes 
fn_in_other              $$CSS_mbin_mask3d_path
node_type                "3D mask (.mrc)" 
optics_group_particles   ""  
do_queue                 No 
qsub                     qsub 
queuename                1202_Import_mask3d
qsubscript               "" 
min_dedicated            24 
other_args               "" 
qsub_extra1              invalid_partition 
qsub_extra2              invalid_partition 