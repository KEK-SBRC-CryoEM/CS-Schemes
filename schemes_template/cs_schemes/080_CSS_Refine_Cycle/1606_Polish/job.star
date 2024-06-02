
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
fn_data            Schemes/080_CSS_Refine_Cycle/1604_Refine3D_ctfrefine/run_data.star 
fn_post            Schemes/080_CSS_Refine_Cycle/1605_PostProcess_ctfrefine/postprocess.star 
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
nr_mpi             32 
nr_threads         12 
do_queue           Yes 
queuename          080060_Polish 
qsub               sbatch 
qsub_extra1        r7i-vcpu192-gpu0 
qsub_extra2        2 
qsubscript         /efs/em/aws_slurm_relion50_cpu_axcore.sh 
min_dedicated      16 
other_args         "" 
