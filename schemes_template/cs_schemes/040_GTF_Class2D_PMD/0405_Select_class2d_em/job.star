
# version 30001

data_job

_rlnJobTypeLabel             relion.select.onvalue
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_data                "" 
fn_mic                 ""
fn_model               Schemes/040_GTF_Class2D_PMD/0404_Class2D_em/run_it025_optimiser.star 
do_class_ranker        Yes 
rank_threshold         $$GTF_rank_threshold 
select_nr_classes      -1 
select_nr_parts        -1 
python_exe             $$python_exe
do_recenter            No 
do_regroup             No 
nr_groups              1
do_select_values       No
select_label           rlnCoordinateY
select_minval          -9999.
select_maxval          9999.
do_discard             No
discard_label          rlnImageName 
discard_sigma          4 
do_split               No 
do_random              No  
split_size             100 
nr_split               -1
do_remove_duplicates   No 
duplicate_threshold    30 
image_angpix           -1
do_queue               No 
queuename              0405_Select_class2d_em
qsub                   sbatch 
qsub_extra1            invalid_partition
qsub_extra2            invalid_partition
qsubscript             /efs/em/aws_slurm_relion.sh 
min_dedicated          1 
other_args             "" 
