
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
fn_img                              $$selected_parts 
fn_cont                             $$cls3d_cont_data_path 
fn_ref                              $$imported_ref3d 
fn_mask                             $$mask3d_cls3d 
ref_correct_greyscale               No 
trust_ref_size                      No 
ini_high                            $$CSS_lbin_center3d_class3d_lpf 
sym_name                            $$CSS_lbin_center3d_class3d_sym 
do_ctf_correction                   Yes 
ctf_intact_first_peak               No 
nr_classes                          $$CSS_lbin_center3d_class3d_classes 
tau_fudge                           4 
nr_iter                             $$cls3d_cont_iter 
do_fast_subsets                     $$CSS_lbin_center3d_class3d_do_fast_subsets 
particle_diameter                   $$SS_comm_optimal_pmd 
do_zero_mask                        Yes 
highres_limit                       -1 
do_blush                            Yes 
dont_skip_align                     Yes 
sampling                            "7.5 degrees" 
offset_range                        $$cls3d_cont_offset_range 
offset_step                         $$cls3d_cont_offset_step 
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
nr_pool                             30 
do_pad1                             Yes 
do_preread_images                   No 
scratch_dir                         /scratch 
do_combine_thru_disc                No 
use_gpu                             Yes 
gpu_ids                             0:1:2:3:4:5:6:7 
nr_mpi                              9 
nr_threads                          6 
do_queue                            Yes 
queuename                           060060_Class3D 
qsub                                sbatch 
qsub_extra1                         g4dn-96c-384gb-8g 
qsub_extra2                         1 
qsubscript                          "" 
min_dedicated                       9 
other_args                          "" 
