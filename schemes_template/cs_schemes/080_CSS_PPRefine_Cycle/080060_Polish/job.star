
# version 30001 

data_job 

_rlnJobTypeLabel             relion.polish 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_mic             $$SS_comm_motioncorr_mics_star 
fn_data            Schemes/080_CSS_PPRefine_Cycle/080040_Refine3D_ctfrefine/run_data.star 
fn_post            Schemes/080_CSS_PPRefine_Cycle/080050_PostProcess_ctfrefine/postprocess.star 
first_frame        1 
last_frame         -1 
extract_size       -1 
rescale            -1 
do_float16         No 
do_param_optim     No 
eval_frac          0.5 
optim_min_part     10000 
do_polish          Yes 
opt_params         "" 
do_own_params      Yes 
sigma_vel          0.2 
sigma_div          5000 
sigma_acc          2 
minres             20 
maxres             -1 
nr_mpi             XXX_JSE_REPLACE_PARALLEL_XXX 
nr_threads         XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue           XXX_JSE_REPLACE_PARALLEL_XXX 
queuename          080060_Polish 
qsub               XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1        XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2        XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript         XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated      XXX_JSE_REPLACE_PARALLEL_XXX 
other_args         XXX_JSE_REPLACE_PARALLEL_XXX 
