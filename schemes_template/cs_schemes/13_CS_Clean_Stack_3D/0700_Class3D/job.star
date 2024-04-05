
# version 30001

data_job

_rlnJobTypeLabel             relion.class3d
_rlnJobIsContinue                       0
_rlnJobIsTomo                           0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_img                             $$CS_selected_parts
fn_cont                            ""
fn_ref                             $$imported_ref3d
fn_mask                            $$mask3d_cls3d
ref_correct_greyscale              No
ini_high                           15
sym_name                           $$CS_sym_name_class3d
do_ctf_correction                  Yes
ctf_intact_first_peak              No 
nr_classes                         $$CS_nr_3d_classes 
tau_fudge                          4
nr_iter                            50 
do_fast_subsets                    Yes 
particle_diameter                  $$CS_class3d_pmd
do_zero_mask                       Yes
highres_limit                      -1
do_blush                           Yes 
dont_skip_align                    Yes 
sampling                           "7.5 degrees" 
offset_range                       5 
offset_step                        1 
do_local_ang_searches              No 
sigma_angles                       5 
relax_sym                          "" 
allow_coarser                      No 
do_helix                           No
helical_tube_inner_diameter        -1 
helical_tube_outer_diameter        -1 
range_rot                          -1 
range_tilt                         15 
range_psi                          10
helical_range_distance             -1 
keep_tilt_prior_fixed              Yes 
do_apply_helical_symmetry          Yes 
helical_nr_asu                     1 
helical_twist_initial              0 
helical_rise_initial               0 
helical_z_percentage               30 
do_local_search_helical_symmetry   No
helical_twist_max                  0 
helical_twist_min                  0 
helical_twist_inistep              0 
helical_rise_max                   0 
helical_rise_min                   0 
helical_rise_inistep               0 
do_parallel_discio                 Yes
nr_pool                            30 
do_pad1                            Yes
do_preread_images                   No
scratch_dir                         /scratch
do_combine_thru_disc               No 
use_gpu                             Yes
gpu_ids                             0:1:2:0:1:2:3:0:1:2:3:0:1:2:3:0:1:2:3:0:1:2:3:0:1:2:3:0:1:2
nr_mpi                              31
nr_threads                          6
do_queue                            Yes
queuename                          0700_Class3D  
qsub                                sbatch
qsub_extra1                         g5-vcpu48-gpu4
qsubscript                          /efs/em/aws_slurm_relion50_gpu.sh
min_dedicated                       4
other_args                          ""
