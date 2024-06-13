
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
fn_data          Schemes/080_CSS_PPRefine_Cycle/080010_CtfRefine_aberration/particles_ctf_refine.star 
fn_post          $$cycles_postprocess_map 
do_aniso_mag     Yes 
do_ctf           No 
do_defocus       No 
do_astig         No 
do_bfactor       No 
do_phase         No 
do_tilt          No 
do_trefoil       No 
do_4thorder      No 
minres           30 
nr_mpi           XXX_JSE_REPLACE_PARALLEL_XXX 
nr_threads       XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue         XXX_JSE_REPLACE_PARALLEL_XXX 
queuename        080020_CtfRefine_aniso_mag 
qsub             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1      XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2      XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript       XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated    XXX_JSE_REPLACE_PARALLEL_XXX 
other_args       XXX_JSE_REPLACE_PARALLEL_XXX 
