
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
fn_in_raw                $$GTF_fn_in_raw
is_multiframe            Yes
optics_group_name        opticsGroup1
fn_mtf                   $$GTF_fn_mtf
angpix                   $$GTF_angpix_mic
kV                       $$GTF_kV
Cs                       $$GTF_Cs 
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
qsubscript               "" 
min_dedicated            24 
other_args               "" 
qsub_extra1              invalid_partition
qsub_extra2              invalid_partition