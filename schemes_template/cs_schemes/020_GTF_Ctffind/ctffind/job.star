
# version 30001

data_job

_rlnJobTypeLabel             relion.ctffind
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
input_star_mics            $$selected_motioncor_mics
use_noDW                   Yes 
do_phaseshift              No
phase_min                  0
phase_max                  180 
phase_step                 10 
dast                       100 
use_ctffind4               Yes
fn_ctffind_exe             $$ctffind_exe
use_given_ps               Yes 
slow_search                Yes 
ctf_win                    -1
box                        512 
resmin                     30  
resmax                     $$GTF_ctf_max_res
dfmin                      $$GTF_ctf_min_def
dfmax                      $$GTF_ctf_max_def
 dfstep                    100 
use_gctf                   No  
fn_gctf_exe                $$gctf_exe
do_ignore_ctffind_params   No
do_EPA                     Yes 
other_gctf_args            ""
gpu_ids                    ""
nr_mpi                     48
do_queue                   Yes
queuename                  ctffind  
qsub                       sbatch
qsub_extra1                m7i-vcpu192-gpu0
qsub_extra2                2
qsubscript                 /efs/em/aws_slurm_relion50_cpu_axcore.sh
min_dedicated              24
other_args                 ""


       

 
     
     

 
  

  
 
