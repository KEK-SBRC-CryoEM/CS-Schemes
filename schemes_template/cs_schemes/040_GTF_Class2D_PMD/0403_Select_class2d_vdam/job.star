
# version 30001

data_job

_rlnJobTypeLabel             relion.select
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
discard_label rlnImageName 
discard_sigma          4 
do_class_ranker        Yes 
do_discard         No 
  do_queue         No 
 do_random         No 
do_recenter         No 
do_regroup         No 
do_remove_duplicates         No 
do_select_values         No 
  do_split         No 
duplicate_threshold         30 
   fn_data         "" 
    fn_mic         "" 
  fn_model Schemes/040_GTF_Class2D_PMD/0402_Class2d_vdam/run_it200_optimiser.star 
image_angpix         -1 
min_dedicated         24 
 nr_groups          1 
  nr_split         -1 
other_args         "" 
python_exe     /lustre1/emsystem/apps/pyenv/versions/anaconda3-5.3.1/envs/topaz/bin/python 
      qsub       qsub 
qsub_extra1      invalid_partition
qsub_extra2      invalid_partition
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
rank_threshold       $$GTF_rank_threshold 
select_label rlnCtfMaxResolution 
select_maxval      9999. 
select_minval     -9999. 
select_nr_classes          0 
select_nr_parts         -1 
split_size        100 
 
