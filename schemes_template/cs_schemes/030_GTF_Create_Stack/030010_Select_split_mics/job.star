
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
fn_mic                  $$SS_comm_ctf_mics_star
fn_data                 "" 
do_class_ranker         No 
rank_threshold          0.5 
select_nr_parts         -1 
select_nr_classes       -1 
do_recenter             No 
do_regroup              No 
nr_groups               1 
do_select_values        No 
select_label            rlnCtfMaxResolution 
select_minval           -9999. 
select_maxval           9999. 
do_discard              No 
discard_label           rlnImageName 
discard_sigma           4 
do_split                Yes 
do_random               No 
split_size              $$GTF_pick_min_nr_mics 
nr_split                -1 
do_remove_duplicates    No 
duplicate_threshold     30 
image_angpix            -1 
do_filaments            No 
dendrogram_threshold    0.85 
dendrogram_minclass     -1000 
do_queue                XXX_JSE_REPLACE_PARALLEL_XXX 
queuename               030010_Select_split_mics 
qsub                    XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2             XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript              XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated           XXX_JSE_REPLACE_PARALLEL_XXX 
other_args              XXX_JSE_REPLACE_PARALLEL_XXX 
