
# version 30001 

data_job 

_rlnJobTypeLabel             relion.external 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_exe           $$cryolo_exe 
in_mov           "" 
in_mic           $$mics_import 
in_part          "" 
in_coords        "" 
in_3dref         "" 
in_mask          "" 
param1_label     cryolo_repo 
param1_value     $$cryolo_repo 
param2_label     threshold 
param2_value     $$GTF_pick_cryolo_thresh 
param3_label     device 
param3_value     0,1,2,3,4,5,6,7
param4_label     "" 
param4_value     "" 
param5_label     "" 
param5_value     "" 
param6_label     "" 
param6_value     "" 
param7_label     "" 
param7_value     "" 
param8_label     "" 
param8_value     "" 
param9_label     "" 
param9_value     "" 
param10_label    "" 
param10_value    "" 
nr_threads       1 
do_queue         Yes 
queuename        030020_External_cryolo 
qsub             sbatch 
qsub_extra1      g4dn-vcpu96-gpu8
qsub_extra2      1 
qsubscript       /efs/em/aws_slurm_relion50_gpu.sh 
min_dedicated    1 
other_args       "" 
