
# version 30001 

data_job 

_rlnJobTypeLabel             relion.extract 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
star_mics                         $$SS_comm_ctf_mics_star 
coords_suffix                     "" 
do_reextract                      Yes 
fndata_reextract                  $$CSS_mbin_reextract_refined_star 
do_reset_offsets                  No 
do_recenter                       Yes 
recenter_x                        0 
recenter_y                        0 
recenter_z                        0 
do_float16                        No 
extract_size                      $$CSS_mbin_reextract_mics_box 
do_invert                         Yes 
do_norm                           Yes 
bg_diameter                       $$CSS_mbin_reextract_mics_0o95box 
black_dust                        -1 
white_dust                        -1 
do_rescale                        Yes 
rescale                           $$CSS_mbin_reextract_parts_box 
do_fom_threshold                  No 
minimum_pick_fom                  "" 
do_extract_helix                  No 
helical_tube_outer_diameter       200 
helical_bimodal_angular_priors    Yes 
do_cut_into_segments              Yes 
do_extract_helical_tubes          Yes 
helical_nr_asu                    1 
helical_rise                      1 
nr_mpi                            XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue                          XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                         070010_Extract_reextract 
qsub                              XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1                       XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2                       XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript                        XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated                     XXX_JSE_REPLACE_PARALLEL_XXX 
other_args                        XXX_JSE_REPLACE_PARALLEL_XXX 
