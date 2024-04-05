
# version 30001

data_job

_rlnJobTypeLabel             relion.class2d
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_img                       $$CS_selected_parts
fn_cont                      "" 
do_ctf_correction            Yes   
ctf_intact_first_peak        No 
nr_classes                   $$CS_nr_2d_classes 
tau_fudge                    2 
do_em                        Yes 
nr_iter_em                   25
do_grad                      No
nr_iter_grad                 200 
particle_diameter            $$CS_class2d_pmd 
do_zero_mask                 Yes
highres_limit                -1
do_center                    Yes
dont_skip_align              Yes
psi_sampling                 6
offset_range                 5 
offset_step                  1
allow_coarser                No 
do_helix                     No
helical_tube_outer_diameter  200 
do_bimodal_psi               Yes 
range_psi                    6
do_restrict_xoff             Yes 
helical_rise                 4.75
do_parallel_discio           Yes
nr_pool                      30
do_preread_images                   No
scratch_dir                         ""
do_combine_thru_disc         No 
use_gpu                             No
gpu_ids                             0:1:2:0:1:2:3:0:1:2:3:0:1:2
nr_mpi                              63
nr_threads                          12
do_queue                            Yes
queuename                    0401_Class2D_em 
qsub                                sbatch
qsub_extra1                         c7i-vcpu192-gpu0
qsubscript                          /efs/em/aws_slurm_relion50_cpu_xcore.sh
min_dedicated                       16
other_args                          "--fast_subsets --cpu"
