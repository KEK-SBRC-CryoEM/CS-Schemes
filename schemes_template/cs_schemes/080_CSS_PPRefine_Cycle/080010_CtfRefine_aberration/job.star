
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
fn_data          $$cycles_ctfrefine_refine_data 
fn_post          $$cycles_postprocess_map 
do_aniso_mag     No 
do_ctf           No 
do_defocus       No 
do_astig         No 
do_bfactor       No 
do_phase         No 
do_tilt          Yes 
do_trefoil       Yes 
do_4thorder      Yes 
minres           30 
nr_mpi           XXX_JSE_REPLACE_PARALLEL_XXX 
nr_threads       XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue         XXX_JSE_REPLACE_PARALLEL_XXX 
queuename        080010_CtfRefine_aberration 
qsub             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1      XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2      XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript       XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated    XXX_JSE_REPLACE_PARALLEL_XXX 
other_args       XXX_JSE_REPLACE_PARALLEL_XXX 
