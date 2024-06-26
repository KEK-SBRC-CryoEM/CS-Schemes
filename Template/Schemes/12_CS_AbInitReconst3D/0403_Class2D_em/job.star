
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
fn_img                       Schemes/12_CS_AbInitReconst3D/0402_Select_class2d/particles.star
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
do_preread_images                    No
scratch_dir                    /scratch/gotofly  
do_combine_thru_disc         No 
use_gpu                    Yes 
gpu_ids                    0:1:2:3
nr_mpi                    5     
nr_threads                    4
do_queue                    No 
queuename                    0403_Class2D_em 
qsub                    ""
qsub_extra1                    invalid_partition
qsubscript                    "" 
min_dedicated                    5
other_args                    --fast_subsets
