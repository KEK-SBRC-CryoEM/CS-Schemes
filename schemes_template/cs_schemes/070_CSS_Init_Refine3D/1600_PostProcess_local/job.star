
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
fn_in                   Schemes/070_CSS_Init_Refine3D/1500_Refine3D_local/run_half1_class001_unfil.mrc 
fn_mask                 $$imported_mask3d 
angpix                  $$SS_comm_mbin_angpix 
do_auto_bfac            Yes 
autob_lowres            10 
do_adhoc_bfac           No 
adhoc_bfac              -1000 
do_skip_fsc_weighting   No 
low_pass                5 
fn_mtf                  "" 
mtf_angpix              1 
do_queue                No 
queuename               070100_PostProcess_local 
qsub                    CSS_NOT_APPLICABLE 
qsub_extra1             CSS_NOT_APPLICABLE 
qsub_extra2             CSS_NOT_APPLICABLE 
qsubscript              CSS_NOT_APPLICABLE 
min_dedicated           0 
other_args              "" 
