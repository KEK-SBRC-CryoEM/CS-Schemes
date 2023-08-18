
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
fn_in                 Schemes/4_CS_Res_Fish/2300_Refine3D_local/run_half1_class001_unfil.mrc 
fn_mask               $$CS_imported_mask3d
angpix                $$CS_angpix
do_resmap_locres      No
fn_resmap             $$resmap_exe
pval                  0.05
maxres                0
minres                0
stepres               1
do_relion_locres      Yes
adhoc_bfac            $$CS_b_factor
fn_mtf                ""
nr_mpi                    18
do_queue                    No 
queuename             2500_LocalRes
qsub                    ""
qsub_extra1                    invalid_partition
qsubscript                    ""  
min_dedicated                    18 
other_args                    "" 
