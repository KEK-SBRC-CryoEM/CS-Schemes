
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
fn_data          Schemes/3_CS_Refine_Cycle/1701_CtfRefine_aberration_2nd/particles_ctf_refine.star
fn_post          Schemes/3_CS_Refine_Cycle/1608_PostProcess_polish_1st/postprocess.star
do_aniso_mag     Yes
do_ctf           No
do_defocus       No
do_astig         No
do_bfactor       No
do_phase         No
  do_tilt        No
do_trefoil       No
do_4thorder      No
minres           30
nr_mpi                              48
nr_threads                          8
do_queue                            Yes
queuename        1702_CtfRefine_magnification_2nd
qsub                                sbatch
qsub_extra1                         m7i-vcpu192-gpu0
qsubscript                          /efs/em/aws_slurm_relion50_cpu_axcore.sh
min_dedicated                       24
other_args                          ""
