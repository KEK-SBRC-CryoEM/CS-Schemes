
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
fn_model                "" 
fn_mic                  "" 
fn_data                 $$selected_parts 
do_class_ranker         No 
rank_threshold          0.5 
select_nr_parts         -1 
select_nr_classes       -1 
do_recenter             No 
do_regroup              No 
nr_groups               1 
do_select_values        No 
select_label            rlnCtfMaxResolution 
select_maxval           9999. 
select_minval           -9999. 
do_discard              No 
discard_label           rlnImageName 
discard_sigma           4 
do_split                Yes 
do_random               No 
split_size              $$CSS_min_nr_parts 
nr_split                -1 
do_remove_duplicates    No 
duplicate_threshold     30 
image_angpix            -1 
do_filaments            No 
dendrogram_threshold    0.85 
dendrogram_minclass     -1000 
do_queue                No 
queuename               0400_Select_split_parts 
qsub                    CSS_NOT_APPLICABLE 
qsub_extra1             CSS_NOT_APPLICABLE 
qsub_extra2             CSS_NOT_APPLICABLE 
qsubscript              CSS_NOT_APPLICABLE 
min_dedicated           0 
other_args              "" 
