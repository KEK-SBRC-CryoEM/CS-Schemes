
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
fn_mic             $$CS_motioncorr_mics
fn_data            Schemes/3_CS_Refine_Cycle/1704_Refine3D_ctfrefine_2nd/run_data.star
fn_post            Schemes/3_CS_Refine_Cycle/1705_PostProcess_ctfrefine_2nd/postprocess.star
first_frame        1
last_frame         -1
extract_size       -1
rescale            -1
do_float16         No
do_param_optim     No
eval_frac          0.5
optim_min_part     3500
do_polish          Yes 
do_own_params      Yes
opt_params         ""
sigma_vel          0.2
sigma_div          5000
sigma_acc          2
minres             20
maxres             -1
nr_mpi                              32
nr_threads                          12
do_queue                            Yes
queuename          1706_Polish_2nd
qsub                                sbatch
qsub_extra1                         m7i-vcpu192-gpu0
qsubscript                          /efs/em/aws_slurm_relion50_cpu_axcore.sh
min_dedicated                       16
other_args                          ""
