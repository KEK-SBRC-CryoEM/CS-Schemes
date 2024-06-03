
# version 30001

data_job

_rlnJobTypeLabel             relion.select.split
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
discard_label          rlnImageName 
discard_sigma          4 
do_class_ranker        No 
do_discard             No 
 do_random             No 
do_recenter            No 
do_regroup             No 
do_remove_duplicates   No 
do_select_values       No 
  do_split             Yes 
duplicate_threshold    30 
   fn_data             "" 
    fn_mic             Schemes/11_CS_Create_Stack/0101_Select_mic/micrographs.star 
  fn_model             "" 
image_angpix           -1 
 nr_groups             1 
  nr_split             -1 
rank_threshold         0.5 
select_label           rlnCtfMaxResolution 
select_maxval          9999. 
select_minval          -9999. 
select_nr_classes      -1 
select_nr_parts        -1 
split_size             $$CS_min_nr_mics 
python_exe             $$python_exe 
do_queue               No 
queuename              0102_Select_split_stack_mics 
qsub                   CS_NOT_APPLICABLE 
qsub_extra1            CS_NOT_APPLICABLE 
qsubscript             CS_NOT_APPLICABLE 
min_dedicated          24 
other_args             "" 
