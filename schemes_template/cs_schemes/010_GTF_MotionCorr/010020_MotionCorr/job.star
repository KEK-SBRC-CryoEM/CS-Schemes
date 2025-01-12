
# version 30001 

data_job 

_rlnJobTypeLabel             relion.motioncorr 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
input_star_mics          Schemes/010_GTF_MotionCorr/010010_Import_movies/movies.star 
first_frame_sum          $$EM_first_frame_for_sum 
last_frame_sum           -1 
dose_per_frame           $$EM_dose_per_frame 
pre_exposure             0 
eer_grouping             $$GTF_eer_grouping 
do_float16               No 
do_dose_weighting        Yes 
do_save_noDW             Yes 
do_save_ps               Yes 
group_for_ps             4 
bfactor                  $$EM_motioncorr_bfactor 
patch_x                  $$EM_motioncorr_patch_x 
patch_y                  $$EM_motioncorr_patch_y 
group_frames             1 
bin_factor               1 
fn_gain_ref              $$GTF_gain_ref_file 
gain_rot                 $$EM_motioncorr_gain_rot 
gain_flip                $$EM_motioncorr_gain_flip 
fn_defect                "" 
do_own_motioncor         Yes 
fn_motioncor2_exe        XXX_JSE_REPLACE_SYSTEM_XXX 
gpu_ids                  XXX_JSE_REPLACE_PARALLEL_XXX 
other_motioncor2_args    "" 
nr_mpi                   XXX_JSE_REPLACE_PARALLEL_XXX 
nr_threads               XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue                 XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                010020_MotionCorr 
qsub                     XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1              XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2              XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript               XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated            XXX_JSE_REPLACE_PARALLEL_XXX 
other_args               XXX_JSE_REPLACE_PARALLEL_XXX 
