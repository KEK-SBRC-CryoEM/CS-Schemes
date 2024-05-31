
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
fn_data          Schemes/080_CSS_Refine_Cycle/1601_CtfRefine_aberration/particles_ctf_refine.star
fn_post          $$cycles_postprocess_map
do_aniso_mag     Yes
do_ctf           No
do_defocus       No
do_astig         No
do_bfactor       No
do_phase         No
do_tilt          No
do_trefoil       No
do_4thorder      No
minres           30
nr_mpi           4
nr_threads       9
do_queue         No
queuename        "1602_CtfRefine_magnification"
qsub             "CSS_NOT_USED"
qsub_extra1      "CSS_NOT_USED"
qsub_extra2      "CSS_NOT_USED"
qsubscript       "CSS_NOT_USED"
min_dedicated    0
other_args       ""
