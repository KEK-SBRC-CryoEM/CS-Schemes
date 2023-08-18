
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
nr_mpi                    16
nr_threads                    2
do_queue                    No
queuename        1601_CtfRefine_aberration_1st
qsub                    ""
qsub_extra1                    invalid_partition
qsubscript                    ""
min_dedicated                    16
other_args                    "" 
