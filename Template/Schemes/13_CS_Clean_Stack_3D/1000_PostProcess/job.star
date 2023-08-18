
# version 30001

data_job

_rlnJobTypeLabel             relion.postprocess
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0


# version 30001

data_joboptions_values

loop_
_rlnJobOptionVariable #1
_rlnJobOptionValue #2
fn_in                   Schemes/13_CS_Clean_Stack_3D/0900_Refine3D/run_half1_class001_unfil.mrc 
fn_mask                 $$imported_mask3d
angpix                  $$CS_angpix
do_auto_bfac            No
autob_lowres            10
do_adhoc_bfac           No
adhoc_bfac              -1000
do_skip_fsc_weighting   Yes
low_pass                $$CS_low_pass
fn_mtf                  ""
mtf_angpix              1
do_queue                    No
queuename               1000_PostProcess
 qsub                    ""
qsub_extra1                    invalid_partition
qsubscript                    ""
min_dedicated                    1
other_args                    ""

