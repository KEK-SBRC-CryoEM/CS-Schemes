
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
fn_in                   Schemes/060_CSS_Clean_Stack_3D/060080_Refine3D_global/run_half1_class001_unfil.mrc 
fn_mask                 $$imported_mask3d 
angpix                  $$SS_comm_lbin_angpix 
do_auto_bfac            No 
autob_lowres            10 
do_adhoc_bfac           No 
adhoc_bfac              -1000 
do_skip_fsc_weighting   Yes 
low_pass                $$CSS_lbin_center3d_postproc_adhoc_lpf 
fn_mtf                  "" 
mtf_angpix              1 
do_queue                XXX_JSE_REPLACE_PARALLEL_XXX 
queuename               060090_PostProcess_global 
qsub                    XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2             XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript              XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated           XXX_JSE_REPLACE_PARALLEL_XXX 
other_args              XXX_JSE_REPLACE_PARALLEL_XXX 
