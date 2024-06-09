
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/010_GTF_Motioncorr/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
EM_mics_apix                       0.83           0.83 
EM_kV                            300            300 
EM_Cs                              2.7            2.7 
EM_first_frame_for_sum             1              1 
EM_dose_per_frame                  0.74           0.74 
GTF_eer_grouping                   1              1 
EM_motioncorr_bfactor            200            200 
EM_motioncorr_patch_x              4              4 
EM_motioncorr_patch_y              3              3 
GTF_motioncorr_total_max_limit    80             80 
current_nr_import_movies           0              0 
pre_nr_motioncorr_mics             0              0 
motioncorr_do_at_most           9999           9999 
wait_sec                         180            180 
maxtime_hr                        96             96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
has_unprocessed_motioncorr_mics    0            0 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
EM_movie_files                   Micrographs/*.tif                                                          Micrographs/*.tif 
EM_mtf_file                      ""                                                                         "" 
EM_gain_ref_file                 ""                                                                         "" 
movies_star                      Schemes/010_GTF_Motioncorr/010010_Import_movies/movies.star                Schemes/010_GTF_Motioncorr/010010_Import_movies/movies.star 
motioncorr_mics_star             Schemes/010_GTF_Motioncorr/010020_MotionCorr/corrected_micrographs.star    Schemes/010_GTF_Motioncorr/010020_MotionCorr/corrected_micrographs.star 
selected_motioncorr_mics_star    Schemes/010_GTF_Motioncorr/010030_Select_mics/micrographs.star             Schemes/010_GTF_Motioncorr/010030_Select_mics/micrographs.star 
movies                           movies                                                                     movies 
micrographs                      micrographs                                                                micrographs 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
COUNT_current_import_movies        float=count_images        current_nr_import_movies           movies_star                 movies 
COUNT_pre_motioncorr_mics          float=count_images        pre_nr_motioncorr_mics             motioncorr_mics_star        micrographs 
HAS_unprocessed_motioncorr_mics    bool=gt                   has_unprocessed_motioncorr_mics    current_nr_import_movies    pre_nr_motioncorr_mics 
WAIT                               wait                      undefined                          wait_sec                    undefined 
EXIT_maxtime                       exit_maxtime              undefined                          maxtime_hr                  undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
importmovies              importmovies              continue       0 
motioncorr                motioncorr                continue       0 
select_motioncor_mics     select_motioncor_mics     continue       0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                                 EXIT_maxtime                           0  undefined      undefined 
EXIT_maxtime                         importmovies                           0  undefined      undefined 
importmovies                         COUNT_current_import_movies            0  undefined      undefined 
COUNT_current_import_movies          COUNT_pre_motioncorr_mics              0  undefined      undefined 
COUNT_pre_motioncorr_mics            HAS_unprocessed_motioncorr_mics        0  undefined      undefined 
HAS_unprocessed_motioncorr_mics      WAIT                                   1  motioncorr     has_unprocessed_motioncorr_mics 
motioncorr                           select_motioncor_mics                  0  undefined      undefined 
select_motioncor_mics                WAIT                                   0  undefined      undefined 
