
# version 30001 

data_job 

_rlnJobTypeLabel             relion.ctfrefine 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_data          Schemes/080_CSS_PPRefine_Cycle/080020_CtfRefine_aniso_mag/particles_ctf_refine.star 
fn_post          $$cycles_postprocess_map 
do_aniso_mag     No 
do_ctf           Yes 
do_defocus       Per-particle 
do_astig         Per-micrograph 
do_bfactor       No 
do_phase         No 
do_tilt          No 
do_trefoil       No 
do_4thorder      No 
minres           30 
nr_mpi           XXX_JSE_REPLACE_PARALLEL_XXX 
nr_threads       XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue         XXX_JSE_REPLACE_PARALLEL_XXX 
queuename        080030_CtfRefine_ctf_params 
qsub             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1      XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2      XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript       XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated    XXX_JSE_REPLACE_PARALLEL_XXX 
other_args       XXX_JSE_REPLACE_PARALLEL_XXX 
