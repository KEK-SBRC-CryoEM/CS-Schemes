
# version 30001 

data_job 

_rlnJobTypeLabel             relion.initialmodel 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_img                 Schemes/050_GTF_AbInitReconst3D/0404_Select_class2d/particles.star 
fn_cont                "" 
do_ctf_correction      Yes 
ctf_intact_first_peak  No 
nr_iter                200 
tau_fudge              4 
nr_classes             4 
particle_diameter      $$GTF_abinit3D_pmd 
do_solvent             Yes 
sym_name               $$GTF_sym_name_initial 
do_run_C1              $$GTF_abinit3D_run_C1 
do_parallel_discio     Yes 
nr_pool                30 
do_preread_images      No 
scratch_dir            /scratch 
do_combine_thru_disc   No 
use_gpu                Yes 
gpu_ids                0,1,2,3 
nr_mpi                 1 
nr_threads             4 
do_queue               Yes 
queuename              0500_InitialModel 
qsub                   sbatch 
qsub_extra1            g4dn-48c-192gb-4g 
qsub_extra2            1
qsubscript             "" 
min_dedicated          1 
other_args             "" 
