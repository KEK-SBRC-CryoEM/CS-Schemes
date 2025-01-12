
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/010_GTF_MotionCorr/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
EM_mics_apix                      XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
EM_kV                             XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
EM_Cs                             XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
prev_nr_movies                    0                             0 
current_nr_movies                 0                             0 
EM_first_frame_for_sum            XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
EM_dose_per_frame                 XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
GTF_eer_grouping                  XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
EM_motioncorr_bfactor             XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
EM_motioncorr_patch_x             XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
EM_motioncorr_patch_y             XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
GTF_motioncorr_do_at_most         XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_motioncorr_total_max_limit    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
wait_sec                          180                           180 
maxtime_hr                        96                            96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
has_larger_nr_movies             0                             0 
GTF_motioncorr_run_only_once     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
EM_movie_files             XXX_SSE_REPLACE_EM_XXX                                                     XXX_SSE_REPLACE_EM_XXX 
EM_mtf_file                XXX_SSE_REPLACE_EM_XXX                                                     XXX_SSE_REPLACE_EM_XXX 
movies_star                Schemes/010_GTF_MotionCorr/010010_Import_movies/movies.star                Schemes/010_GTF_MotionCorr/010010_Import_movies/movies.star 
GTF_gain_ref_file          XXX_SSE_REPLACE_SAMPLE_XXX                                                 XXX_SSE_REPLACE_SAMPLE_XXX 
EM_motioncorr_gain_rot     XXX_SSE_REPLACE_EM_XXX                                                     XXX_SSE_REPLACE_EM_XXX 
EM_motioncorr_gain_flip    XXX_SSE_REPLACE_EM_XXX                                                     XXX_SSE_REPLACE_EM_XXX 
motioncorr_mics_star       Schemes/010_GTF_MotionCorr/010020_MotionCorr/corrected_micrographs.star    Schemes/010_GTF_MotionCorr/010020_MotionCorr/corrected_micrographs.star
movies                     movies                                                                     movies 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
COUNT_movies            float=count_images    current_nr_movies       movies_star          movies 
HAS_movies_increased    bool=gt               has_larger_nr_movies    current_nr_movies    prev_nr_movies 
SET_prev_nr_movies      float=set             prev_nr_movies          current_nr_movies    undefined 
WAIT                    wait                  undefined               wait_sec             undefined 
EXIT_maxtime            exit_maxtime          undefined               maxtime_hr           undefined 
EXIT                    exit                  undefined               undefined            undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
010010_Import_movies    010010_Import_movies    continue       0 
010020_MotionCorr       010020_MotionCorr       continue       0 
010030_Select_mics      010030_Select_mics      continue       0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                    EXIT_maxtime            0    undefined             undefined 
EXIT_maxtime            010010_Import_movies    0    undefined             undefined 
010010_Import_movies    COUNT_movies            0    undefined             undefined 
COUNT_movies            HAS_movies_increased    0    undefined             undefined 
HAS_movies_increased    WAIT                    1    SET_prev_nr_movies    has_larger_nr_movies 
SET_prev_nr_movies      010020_MotionCorr       0    undefined             undefined 
010020_MotionCorr       010030_Select_mics      0    undefined             undefined 
010030_Select_mics      WAIT                    1    EXIT                  GTF_motioncorr_run_only_once 
