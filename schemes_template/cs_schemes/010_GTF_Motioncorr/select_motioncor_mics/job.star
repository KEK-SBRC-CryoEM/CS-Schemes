
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
fn_model                "" 
fn_mic                  $$motioncorr_mics_star 
fn_data                 "" 
do_class_ranker         No 
rank_threshold          0.5 
select_nr_parts         -1 
select_nr_classes       -1 
do_recenter             No 
do_regroup              No 
nr_groups               1 
do_select_values        Yes 
select_label            rlnAccumMotionTotal 
select_minval           -9999. 
select_maxval           $$GTF_motioncorr_total_max_limit 
do_discard              No 
discard_label           rlnImageName 
discard_sigma           4 
do_split                No 
do_random               No 
split_size              100 
nr_split                -1 
do_remove_duplicates    No 
duplicate_threshold     30 
image_angpix            -1 
do_queue                No 
queuename               010030_Select_motioncorr_mics 
qsub                    GTC_NOT_APPLICABLE 
qsub_extra1             GTC_NOT_APPLICABLE 
qsub_extra2             GTC_NOT_APPLICABLE 
qsubscript              GTC_NOT_APPLICABLE 
min_dedicated           0 
other_args              "" 
