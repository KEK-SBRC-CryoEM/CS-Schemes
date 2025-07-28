
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
fn_in                   Schemes/091_CSS_Merge_Stack_Split/091080_Refine3D_local/run_half1_class001_unfil.mrc 
fn_mask                 $$CSS_mbin_imported_mask3d_path 
angpix                  $$SS_comm_mbin_angpix 
do_auto_bfac            Yes 
autob_lowres            10 
do_adhoc_bfac           No 
adhoc_bfac              -1000 
do_skip_fsc_weighting   No 
low_pass                5 
fn_mtf                  $$EM_mtf_file 
mtf_angpix              $$EM_mics_apix 
do_queue                XXX_JSE_REPLACE_PARALLEL_XXX 
queuename               091090_PostProcess_local 
qsub                    XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2             XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript              XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated           XXX_JSE_REPLACE_PARALLEL_XXX 
other_args              XXX_JSE_REPLACE_PARALLEL_XXX 