
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
fn_mic                  "" 
fn_data                 Schemes/030_GTF_Create_Stack/030040_Extract_picks/particles.star 
do_class_ranker         No 
rank_threshold          0.5 
select_nr_parts         -1 
select_nr_classes       -1 
do_recenter             No 
do_regroup              No 
nr_groups               1 
do_select_values        Yes 
select_label            rlnCoordinateX 
select_minval           $$GTF_lbin_extract_parts_x_min 
select_maxval           $$GTF_lbin_extract_parts_x_max 
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
do_filaments            No 
dendrogram_threshold    0.85 
dendrogram_minclass     -1000 
do_queue                XXX_JSE_REPLACE_PARALLEL_XXX 
queuename               030050_Select_rm_bars_x 
qsub                    XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1             XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2             XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript              XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated           XXX_JSE_REPLACE_PARALLEL_XXX 
other_args              XXX_JSE_REPLACE_PARALLEL_XXX 
