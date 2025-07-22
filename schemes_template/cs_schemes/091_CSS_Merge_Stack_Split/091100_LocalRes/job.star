
# version 30001 

data_job 

_rlnJobTypeLabel             relion.localres.own 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_in                 Schemes/091_CSS_Merge_Stack_Split/091080_Refine3D_local/run_half1_class001_unfil.mrc 
fn_mask               $$CSS_mbin_imported_mask3d_path 
angpix                $$SS_comm_mbin_angpix 
do_resmap_locres      No 
fn_resmap             XXX_JSE_REPLACE_SYSTEM_XXX 
pval                  0.05 
maxres                0 
minres                0 
stepres               1 
do_relion_locres      Yes 
adhoc_bfac            $$CSS_mbin_mergesplit_locres_bfactor 
fn_mtf                $$EM_mtf_file 
nr_mpi                XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue              XXX_JSE_REPLACE_PARALLEL_XXX 
queuename             091100_LocalRes 
qsub                  XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1           XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2           XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript            XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated         XXX_JSE_REPLACE_PARALLEL_XXX 
other_args            XXX_JSE_REPLACE_PARALLEL_XXX 