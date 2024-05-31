
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
fn_in                   Schemes/30_CS_Refine_Cycle/1604_Refine3D_ctfrefine/run_half1_class001_unfil.mrc 
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
do_queue                No 
queuename               "1605_PostProcess_ctfrefine" 
qsub                    "CS_NOT_USED" 
qsub_extra1             "CS_NOT_USED" 
qsubscript              "CS_NOT_USED" 
min_dedicated           0 
other_args              "" 

