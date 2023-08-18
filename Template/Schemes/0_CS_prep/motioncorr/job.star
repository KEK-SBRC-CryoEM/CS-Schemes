
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
input_star_mics         Schemes/0_CS_prep/importmovies/movies.star 
first_frame_sum         $$CS_first_frame_sum
last_frame_sum          -1 
dose_per_frame          $$CS_dose_per_frame 
pre_exposure            0 
eer_grouping            $$CS_eer_grouping 
do_float16              No
do_dose_weighting       Yes
do_save_noDW            Yes 
do_save_ps              Yes  
group_for_ps            4 
bfactor                 200
patch_x                 5 
patch_y                 5 
group_frames            1    
bin_factor              1 
fn_gain_ref             ""
gain_rot                "No rotation (0)" 
gain_flip               "No flipping (0)"
fn_defect               ""
do_own_motioncor        Yes 
fn_motioncor2_exe       $$motioncor2_exe 
gpu_ids                    "" 
other_motioncor2_args   "" 
nr_mpi                    4 
nr_threads                    9 
do_queue                    No 
queuename               motioncorr
qsub                    ""
qsub_extra1                    invalid_partition
qsubscript                    ""
min_dedicated                    4 
other_args                    "--do_at_most $$do_at_most" 

   


