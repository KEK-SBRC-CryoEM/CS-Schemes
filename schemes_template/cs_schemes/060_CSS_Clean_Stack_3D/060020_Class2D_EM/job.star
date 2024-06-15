
# version 30001 

data_job 

_rlnJobTypeLabel             relion.class2d 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_img                         $$cls2d_cycle_parts 
fn_cont                        "" 
do_ctf_correction              Yes 
ctf_intact_first_peak          No 
nr_classes                     $$SS_comm_class2d_classes 
tau_fudge                      2 
do_em                          Yes 
nr_iter_em                     25 
do_grad                        No 
nr_iter_grad                   200 
particle_diameter              $$SS_comm_class2d_pmd 
do_zero_mask                   Yes 
highres_limit                  -1 
do_center                      Yes 
dont_skip_align                Yes 
psi_sampling                   6 
offset_range                   5 
offset_step                    1 
allow_coarser                  No 
do_helix                       No 
helical_tube_outer_diameter    200 
do_bimodal_psi                 Yes 
range_psi                      6 
do_restrict_xoff               Yes 
helical_rise                   4.75 
do_parallel_discio             Yes 
nr_pool                        $$SS_comm_lbin_nr_pool 
do_preread_images              $$SS_comm_lbin_do_preread_images 
scratch_dir                    XXX_JSE_REPLACE_PARALLEL_XXX 
do_combine_thru_disc           No 
use_gpu                        XXX_JSE_REPLACE_PARALLEL_XXX 
gpu_ids                        XXX_JSE_REPLACE_PARALLEL_XXX 
nr_mpi                         XXX_JSE_REPLACE_PARALLEL_XXX 
nr_threads                     XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue                       XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                      060020_Class2D_EM 
qsub                           XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1                    XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2                    XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript                     XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated                  XXX_JSE_REPLACE_PARALLEL_XXX 
other_args                     XXX_JSE_REPLACE_PARALLEL_XXX 
