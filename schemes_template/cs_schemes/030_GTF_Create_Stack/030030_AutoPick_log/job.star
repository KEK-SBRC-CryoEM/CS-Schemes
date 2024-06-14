
# version 30001 

data_job 

_rlnJobTypeLabel             relion.autopick.log 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_input_autopick                   $$mics_import 
angpix                              -1 
do_refs                             No 
do_log                              Yes 
do_topaz                            No 
continue_manual                     No 
log_diam_min                        $$GTF_pick_log_pdm_min 
log_diam_max                        $$GTF_pick_log_pdm_max 
log_invert                          No 
log_maxres                          20 
log_adjust_thr                      $$GTF_pick_log_adjust_thresh 
log_upper_thr                       $$GTF_pick_log_upper_thresh 
topaz_particle_diameter             -1 
do_topaz_pick                       No 
topaz_model                         "" 
do_topaz_train                      No 
topaz_nr_particles                  -1 
topaz_train_picks                   "" 
do_topaz_train_parts                No 
topaz_train_parts                   "" 
fn_topaz_exe                        relion_python_topaz 
topaz_other_args                    "" 
fn_refs_autopick                    "" 
do_ref3d                            No 
fn_ref3d_autopick                   "" 
ref3d_symmetry                      C1 
ref3d_sampling                      "30 degrees" 
lowpass                             20 
highpass                            -1 
angpix_ref                          -1 
psi_sampling_autopick               5 
do_invert_refs                      Yes 
do_ctf_autopick                     Yes 
do_ignore_first_ctfpeak_autopick    No 
threshold_autopick                  0.05 
mindist_autopick                    100 
maxstddevnoise_autopick             1.1 
minavgnoise_autopick                -999 
do_write_fom_maps                   No 
do_read_fom_maps                    No 
shrink                              0 
use_gpu                             XXX_JSE_REPLACE_PARALLEL_XXX 
gpu_ids                             XXX_JSE_REPLACE_PARALLEL_XXX 
do_pick_helical_segments            No 
helical_tube_outer_diameter         200 
helical_tube_length_min             -1 
helical_tube_kappa_max              0.1 
helical_nr_asu                      1 
helical_rise                        -1 
do_amyloid                          No 
nr_mpi                              XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue                            XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                           030030_AutoPick_log 
qsub                                XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1                         XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2                         XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript                          XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated                       XXX_JSE_REPLACE_PARALLEL_XXX 
other_args                          XXX_JSE_REPLACE_PARALLEL_XXX 
