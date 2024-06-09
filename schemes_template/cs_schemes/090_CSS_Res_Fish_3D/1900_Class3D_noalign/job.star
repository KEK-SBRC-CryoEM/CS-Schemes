
# version 30001 

data_job 

_rlnJobTypeLabel             relion.class3d 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_img                              $$CSS_mbin_resfish3d_refined_star 
fn_cont                             "" 
fn_ref                              $$CSS_mbin_resfish3d_ref3d 
fn_mask                             $$SS_comm_mbin_imported_mask3d_path 
ref_correct_greyscale               Yes 
trust_ref_size                      No 
ini_high                            0 
sym_name                            $$SS_comm_sym_name 
do_ctf_correction                   Yes 
ctf_intact_first_peak               No 
nr_classes                          $$CSS_mbin_resfish3d_classes 
tau_fudge                           $$CSS_mbin_resfish3d_tval 
nr_iter                             25 
do_fast_subsets                     $$CSS_mbin_resfish3d_do_fast_subsets 
particle_diameter                   $$SS_comm_optimal_pmd 
do_zero_mask                        Yes 
highres_limit                       -1 
do_blush                            Yes 
dont_skip_align                     No 
sampling                            "7.5 degrees" 
offset_range                        5 
offset_step                         1 
do_local_ang_searches               No 
sigma_angles                        5 
relax_sym                           "" 
allow_coarser                       No 
do_helix                            No 
helical_tube_inner_diameter         -1 
helical_tube_outer_diameter         -1 
range_rot                           -1 
range_tilt                          15 
range_psi                           10 
helical_range_distance              -1 
keep_tilt_prior_fixed               Yes 
do_apply_helical_symmetry           Yes 
helical_nr_asu                      1 
helical_twist_initial               0 
helical_rise_initial                0 
helical_z_percentage                30 
do_local_search_helical_symmetry    No 
helical_twist_max                   0 
helical_twist_min                   0 
helical_twist_inistep               0 
helical_rise_max                    0 
helical_rise_min                    0 
helical_rise_inistep                0 
do_parallel_discio                  Yes 
nr_pool                             16 
do_pad1                             Yes 
do_preread_images                   No 
scratch_dir                         "" 
do_combine_thru_disc                No 
use_gpu                             No 
gpu_ids                             "" 
nr_mpi                              25 
nr_threads                          7 
do_queue                            Yes 
queuename                           090010_Class3D_noalign 
qsub                                sbatch 
qsub_extra1                         c7i-vcpu192-gpu0 
qsub_extra2                         1 
qsubscript                          /efs/em/aws_slurm_relion50_cpu_xcore.sh 
min_dedicated                       25 
other_args                          "" 
