
# version 30001 

data_job 

_rlnJobTypeLabel             relion.select.class2dauto 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_model               Schemes/050_GTF_AbInitReconst3D/0401_Class2D_em/run_it025_optimiser.star 
fn_mic                 "" 
fn_data                "" 
do_class_ranker        Yes 
rank_threshold         $$GTF_rank_thresh_cls2d 
select_nr_classes      -1 
select_nr_parts        -1 
python_exe             $$python_exe 
do_recenter            No 
do_regroup             No 
nr_groups              1 
do_select_values       No 
select_label           rlnCtfMaxResolution 
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
queuename              0402_Select_class2d 
qsub                   GTF_NOT_APPLICABLE 
qsub_extra1            GTF_NOT_APPLICABLE 
qsub_extra2            GTF_NOT_APPLICABLE 
qsubscript             GTF_NOT_APPLICABLE 
min_dedicated          0 
other_args             "" 
