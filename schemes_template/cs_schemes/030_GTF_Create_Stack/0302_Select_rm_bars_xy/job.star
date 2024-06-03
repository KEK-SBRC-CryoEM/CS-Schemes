
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
fn_data                Schemes/11_CS_Create_Stack/0301_Select_rm_bars_x/particles.star 
fn_mic                 "" 
fn_model               "" 
do_class_ranker        No 
rank_threshold         0.5 
select_nr_classes      -1 
select_nr_parts        -1 
python_exe             $$python_exe 
do_recenter            No 
do_regroup             No 
nr_groups              1 
do_select_values       Yes 
select_label           rlnCoordinateY 
select_minval          $$CS_parts_y_coods_min 
select_maxval          $$CS_parts_y_coods_max 
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
queuename              0302_Select_rm_bars_xy 
qsub                   CS_NOT_APPLICABLE 
qsub_extra1            CS_NOT_APPLICABLE 
qsubscript             CS_NOT_APPLICABLE 
min_dedicated          0 
other_args             "" 
