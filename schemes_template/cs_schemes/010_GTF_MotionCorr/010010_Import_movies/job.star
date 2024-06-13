
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
fn_in_raw                $$EM_movie_files 
is_multiframe            Yes 
optics_group_name        opticsGroup1 
fn_mtf                   $$EM_mtf_file 
angpix                   $$EM_mics_apix 
kV                       $$EM_kV 
Cs                       $$EM_Cs 
Q0                       0.1 
beamtilt_x               0 
beamtilt_y               0 
do_other                 No 
fn_in_other              "" 
node_type                "Particle coordinates (*.box, *_pick.star)" 
optics_group_particles   "" 
do_queue                 XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                010010_Import_movies 
qsub                     XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1              XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2              XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript               XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated            XXX_JSE_REPLACE_PARALLEL_XXX 
other_args               XXX_JSE_REPLACE_PARALLEL_XXX 
