
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
fn_model                Schemes/050_GTF_AbInitReconst3D/0401_Class2D_em/run_it025_optimiser.star 
fn_mic                  "" 
fn_data                 "" 
do_class_ranker         Yes 
rank_threshold          $$GTF_lbin_abinit3d_clean2d_rank_thresh 
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
do_queue                No 
queuename               050030_Select_clean2d_parts 
qsub                    GTF_NOT_APPLICABLE 
qsub_extra1             GTF_NOT_APPLICABLE 
qsub_extra2             GTF_NOT_APPLICABLE 
qsubscript              GTF_NOT_APPLICABLE 
min_dedicated           0 
other_args              "" 
