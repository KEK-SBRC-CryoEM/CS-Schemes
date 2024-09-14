
# version 30001 

data_job 

_rlnJobTypeLabel             relion.refine3d 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_img                              Schemes/070_CSS_Init_Refine3D/070040_Select_rm_bars_xy/particles.star 
fn_ref                              $$imported_ref3d 
fn_mask                             $$imported_mask3d 
fn_cont                             "" 
ref_correct_greyscale               No 
trust_ref_size                      No 
ini_high                            15 
sym_name                            $$SS_comm_sym_name 
do_ctf_correction                   Yes 
ctf_intact_first_peak               No 
particle_diameter                   $$SS_comm_optimal_pmd 
do_zero_mask                        Yes 
do_solvent_fsc                      No 
do_blush                            Yes 
sampling                            "7.5 degrees" 
offset_range                        5 
offset_step                         1 
auto_local_sampling                 "1.8 degrees" 
relax_sym                           "" 
auto_faster                         No 
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
helical_rise_min                    0 
helical_rise_max                    0 
helical_rise_inistep                0 
helical_twist_min                   0 
helical_twist_max                   0 
helical_twist_inistep               0 
do_parallel_discio                  Yes 
nr_pool                             $$SS_comm_mbin_nr_pool 
do_pad1                             Yes 
do_preread_images                   $$SS_comm_mbin_do_preread_images 
scratch_dir                         XXX_JSE_REPLACE_PARALLEL_XXX 
do_combine_thru_disc                No 
use_gpu                             XXX_JSE_REPLACE_PARALLEL_XXX 
gpu_ids                             XXX_JSE_REPLACE_PARALLEL_XXX 
nr_mpi                              XXX_JSE_REPLACE_PARALLEL_XXX 
nr_threads                          XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue                            XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                           070070_Refine3D_global 
qsub                                XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1                         XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2                         XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript                          XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated                       XXX_JSE_REPLACE_PARALLEL_XXX 
other_args                          XXX_JSE_REPLACE_PARALLEL_XXX 
