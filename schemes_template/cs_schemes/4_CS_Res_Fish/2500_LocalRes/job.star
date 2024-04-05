
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
nr_mpi                              48
do_queue                            Yes
queuename             2500_LocalRes
qsub                                sbatch
qsub_extra1                         m7i-vcpu192-gpu0
qsubscript                          /efs/em/aws_slurm_relion50_cpu_axcore.sh
min_dedicated                       24
other_args                          ""
