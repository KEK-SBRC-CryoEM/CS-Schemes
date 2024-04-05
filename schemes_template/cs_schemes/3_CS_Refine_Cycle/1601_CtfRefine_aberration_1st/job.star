
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
fn_data          $$CS_ctfrefine_refine_data
fn_post          $$CS_postprocess_map
do_aniso_mag     No
do_ctf           No
do_defocus       No
do_astig         No
do_bfactor       No
do_phase         No
  do_tilt        Yes
do_trefoil       Yes
do_4thorder      Yes
minres           30
nr_mpi                              48
nr_threads                          8
do_queue                            Yes
queuename        1601_CtfRefine_aberration_1st
qsub                                sbatch
qsub_extra1                         m7i-vcpu192-gpu0
qsubscript                          /efs/em/aws_slurm_relion50_cpu_axcore.sh
min_dedicated                       24
other_args                          ""
