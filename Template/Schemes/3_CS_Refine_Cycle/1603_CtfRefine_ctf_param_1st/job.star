
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
fn_data          Schemes/3_CS_Refine_Cycle/1602_CtfRefine_magnification_1st/particles_ctf_refine.star
fn_post          $$CS_postprocess_map
do_aniso_mag     No
do_ctf           Yes
do_defocus       Per-particle
do_astig         Per-micrograph
do_bfactor       No
do_phase         No
  do_tilt        No
do_trefoil       No
do_4thorder      No
minres           30
nr_mpi                    16
nr_threads                    2
do_queue                    No
queuename        1603_CtfRefine_ctf_param_1st
qsub                    ""
qsub_extra1                    invalid_partition
qsubscript                    ""
min_dedicated                    16
other_args                    "" 
