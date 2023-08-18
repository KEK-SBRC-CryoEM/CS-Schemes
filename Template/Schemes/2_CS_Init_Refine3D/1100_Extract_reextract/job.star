
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
star_mics                        $$CS_selected_mics
coords_suffix                    "" 
do_reextract                     Yes 
fndata_reextract                 $$CS_extract_refine_data
do_reset_offsets                 No
do_recenter                      Yes
recenter_x                       0 
recenter_y                       0 
recenter_z                       0
do_float16                       No
extract_size                     $$CS_mics_box
do_invert                        Yes
do_norm                          Yes
bg_diameter                      $$CS_mics_box_0o95 
black_dust                       -1 
white_dust                       -1 
do_rescale                       Yes
rescale                          $$CS_parts_box
do_fom_threshold                 No 
minimum_pick_fom                 ""
do_extract_helix                 No 
helical_tube_outer_diameter      200 
helical_bimodal_angular_priors   Yes 
do_cut_into_segments             Yes 
do_extract_helical_tubes         Yes 
helical_nr_asu                   1 
helical_rise                     1
nr_mpi                    36  
do_queue                    No 
queuename                        1100_Extract_reextract
qsub                    "" 
qsub_extra1                    invalid_partition
qsubscript                    ""  
min_dedicated                    36    
other_args                    "" 
     

 




 
