
# version 30001 

data_job 

_rlnJobTypeLabel             relion.initialmodel 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_img                   Schemes/050_GTF_AbInitReconst3D/050050_Select_abinit3d_parts/particles.star 
fn_cont                  "" 
do_ctf_correction        Yes 
ctf_intact_first_peak    No 
nr_iter                  200 
tau_fudge                4 
nr_classes               4 
particle_diameter        $$GTF_lbin_abinit3d_pmd 
do_solvent               Yes 
sym_name                 $$GTF_lbin_abinit3d_sym_name 
do_run_C1                $$GTF_lbin_abinit3d_do_run_C1 
do_parallel_discio       Yes 
nr_pool                  $$SS_comm_lbin_nr_pool 
do_preread_images        $$SS_comm_lbin_do_preread_images 
scratch_dir              XXX_JSE_REPLACE_PARALLEL_XXX 
do_combine_thru_disc     No 
use_gpu                  XXX_JSE_REPLACE_PARALLEL_XXX 
gpu_ids                  XXX_JSE_REPLACE_PARALLEL_XXX 
nr_mpi                   XXX_JSE_REPLACE_PARALLEL_XXX 
nr_threads               XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue                 XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                050060_InitialModel 
qsub                     XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1              XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2              XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript               XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated            XXX_JSE_REPLACE_PARALLEL_XXX 
other_args               XXX_JSE_REPLACE_PARALLEL_XXX 
