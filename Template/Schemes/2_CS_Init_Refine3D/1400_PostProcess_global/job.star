
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
fn_in                   Schemes/2_CS_Init_Refine3D/1300_Refine3D_global/run_half1_class001_unfil.mrc
fn_mask                 $$imported_mask3d
angpix                  $$CS_angpix
do_auto_bfac            Yes
autob_lowres            10
do_adhoc_bfac           No
adhoc_bfac              -1000
do_skip_fsc_weighting   No    
low_pass                5
fn_mtf                  ""
mtf_angpix              1
do_queue                    No
queuename               1400_PostProcess_global
 qsub                    ""
qsub_extra1                    invalid_partition
qsubscript                    ""      
min_dedicated                    1
other_args                    ""
      
 
