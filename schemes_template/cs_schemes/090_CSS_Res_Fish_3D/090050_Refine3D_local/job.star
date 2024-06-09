
# version 30001 

data_job 

_rlnJobTypeLabel             relion.refine3d 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
fn_img                              Schemes/090_CSS_Res_Fish/2100_Refine3D_global/run_data.star 
fn_cont                             "" 
fn_ref                              Schemes/090_CSS_Res_Fish/2100_Refine3D_global/run_class001.mrc 
fn_mask                             $$SS_comm_mbin_imported_mask3d_path 
ref_correct_greyscale               Yes 
trust_ref_size                      No 
ini_high                            0 
sym_name                            $$SS_comm_sym_name 
do_ctf_correction                   Yes 
ctf_intact_first_peak               No 
particle_diameter                   $$SS_comm_mbin_0o95box_pmd 
do_zero_mask                        Yes 
do_solvent_fsc                      Yes 
do_blush                            Yes 
sampling                            "1.8 degrees" 
offset_range                        5 
offset_step                         1 
auto_local_sampling                 "1.8 degrees" 
relax_sym                           "" 
auto_faster                         No 
do_helix                            No 
helical_tube_inner_diameter         -1 
helical_tube_outer_diameter         -1 
range_rot                           -1 
range_tilt                          15 
range_psi                           10 
helical_range_distance              -1 
keep_tilt_prior_fixed               Yes 
do_apply_helical_symmetry           Yes 
helical_nr_asu                      1 
helical_twist_initial               0 
helical_rise_initial                0 
helical_z_percentage                30 
do_local_search_helical_symmetry    No 
helical_rise_min                    0 
helical_rise_max                    0 
helical_rise_inistep                0 
helical_twist_min                   0 
helical_twist_max                   0 
helical_twist_inistep               0 
do_parallel_discio                  Yes 
nr_pool                             16 
do_pad1                             Yes 
do_preread_images                   No 
scratch_dir                         /scratch 
do_combine_thru_disc                No 
use_gpu                             Yes 
gpu_ids                             0:1:2:0:1:2:3:0:1:2:3:0:1:2 
nr_mpi                              15 
nr_threads                          6 
do_queue                            Yes 
queuename                           090050_Refine3D_local 
qsub                                sbatch 
qsub_extra1                         g5-vcpu48-gpu4 
qsub_extra2                         4 
qsubscript                          /efs/em/aws_slurm_relion50_gpu.sh 
min_dedicated                       4 
other_args                          "" 
