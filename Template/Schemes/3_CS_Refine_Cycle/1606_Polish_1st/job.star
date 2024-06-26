
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
fn_data            Schemes/3_CS_Refine_Cycle/1604_Refine3D_ctfrefine_1st/run_data.star
fn_post            Schemes/3_CS_Refine_Cycle/1605_PostProcess_ctfrefine_1st/postprocess.star
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
nr_mpi                    4
nr_threads                    9
do_queue                    No
queuename          1606_Polish_1st
qsub                    ""
qsub_extra1                    invalid_partition
qsubscript                    ""
min_dedicated                    4
other_args                    ""
