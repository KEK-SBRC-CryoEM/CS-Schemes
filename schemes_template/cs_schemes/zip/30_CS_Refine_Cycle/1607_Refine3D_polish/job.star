
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
fn_img                              Schemes/30_CS_Refine_Cycle/1606_Polish/shiny.star 
fn_ref                              Schemes/30_CS_Refine_Cycle/1604_Refine3D_ctfrefine/run_class001.mrc 
fn_mask                             $$CS_imported_mask3d 
fn_cont                             "" 
ref_correct_greyscale               Yes 
trust_ref_size                      Yes 
ini_high                            0 
sym_name                            $$CS_sym_name_refine3d_apo
do_ctf_correction                   Yes 
ctf_intact_first_peak               No 
particle_diameter                   $$CS_refine3d_pmd_0o95
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
nr_pool                             30 
do_pad1                             Yes 
do_preread_images                   No
scratch_dir                         /scratch/moriya-em 
do_combine_thru_disc                No 
use_gpu                             Yes
gpu_ids                             0:1:2:3 
nr_mpi                              5
nr_threads                          9
do_queue                            No
queuename                           "1607_Refine3D_polish"
qsub                                "CS_NOT_USED"
qsub_extra1                         "CS_NOT_USED"
qsubscript                          "CS_NOT_USED"
min_dedicated                       0
other_args                          ""

