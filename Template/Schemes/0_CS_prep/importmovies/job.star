
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
do_raw                   Yes
fn_in_raw                $$CS_fn_in_raw
is_multiframe            Yes
optics_group_name        opticsGroup1
fn_mtf                   $$CS_fn_mtf
angpix                   $$CS_angpix_mic
kV                       $$CS_kV
Cs                       $$CS_Cs 
Q0                       0.1 
beamtilt_x               0 
beamtilt_y               0 
do_other                 No 
fn_in_other              ref.mrc  
node_type                "Particle coordinates (*.box, *_pick.star)"  
optics_group_particles   ""  
do_queue                 No 
qsub                     qsub 
queuename                importmovies
qsubscript               /public/EM/RELION/relion/bin/relion_qsub.csh 
min_dedicated            24 
other_args               "" 
qsub_extra1              invalid_partition
