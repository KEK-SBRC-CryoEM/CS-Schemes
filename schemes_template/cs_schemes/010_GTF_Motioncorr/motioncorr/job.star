
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
input_star_mics          Schemes/010_GTF_Motioncorr/importmovies/movies.star 
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
fn_gain_ref              $$EM_gain_ref_file 
gain_rot                 "No rotation (0)" 
gain_flip                "No flipping (0)" 
fn_defect                "" 
do_own_motioncor         Yes 
fn_motioncor2_exe        "" 
gpu_ids                  "" 
other_motioncor2_args    "" 
nr_mpi                   48 
nr_threads               8 
do_queue                 Yes 
queuename                010020_MotionCorr 
qsub                     sbatch 
qsub_extra1              m7i-vcpu192-gpu0 
qsub_extra2              1 
qsubscript               /efs/em/aws_slurm_relion50_cpu_axcore.sh 
min_dedicated            24 
other_args               "--do_at_most $$motioncorr_do_at_most" 
