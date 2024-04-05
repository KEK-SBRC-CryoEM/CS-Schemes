
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
fn_in                   Schemes/4_CS_Res_Fish/2300_Refine3D_local/run_half1_class001_unfil.mrc
fn_mask                 $$CS_imported_mask3d
angpix                  $$CS_angpix
do_auto_bfac            Yes
autob_lowres            10
do_adhoc_bfac           No
adhoc_bfac              -1000
do_skip_fsc_weighting   No    
low_pass                5
fn_mtf                  ""
mtf_angpix              1
do_queue                            No
queuename               2400_PostProcess_local
qsub                                ""
qsub_extra1                         invalid_partition
qsubscript                          ""
min_dedicated                       1
other_args                          ""
      
 
