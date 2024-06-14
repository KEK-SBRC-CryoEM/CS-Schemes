
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/020_GTF_CtfFind/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
prev_nr_mics                  0                             0 
current_nr_mics               0                             0 
EM_ctffind_fit_res_min        XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
EM_ctffind_fit_res_max        XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
GTF_ctffind_search_def_min    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_ctffind_search_def_max    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_ctffind_res_max_limit     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
wait_sec                      180                           180 
maxtime_hr                    96                            96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
has_motioncorr        0                             0 
has_larger_nr_mics    0                             0 

# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
SS_comm_motioncorr_mics_star    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
micrographs                     micrographs                   micrographs 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_motioncorr        bool=file_exists      has_motioncorr        SS_comm_motioncorr_mics_star    undefined 
COUNT_mics            float=count_images    current_nr_mics       SS_comm_motioncorr_mics_star    micrographs 
HAS_mics_increased    bool=gt               has_larger_nr_mics    current_nr_mics                 prev_nr_mics 
SET_prev_nr_mics      float=set             prev_nr_mics          current_nr_mics                 undefined 
WAIT                  wait                  undefined             wait_sec                        undefined 
EXIT_maxtime          exit_maxtime          undefined             maxtime_hr                      undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
020010_CtfFind        020010_CtfFind        continue       0 
020020_Select_mics    020020_Select_mics    continue       0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                  EXIT_maxtime          0    undefined           undefined 
EXIT_maxtime          HAS_motioncorr        0    undefined           undefined 
HAS_motioncorr        WAIT                  1    COUNT_mics          has_motioncorr 
COUNT_mics            HAS_mics_increased    0    undefined           undefined 
HAS_mics_increased    WAIT                  1    SET_prev_nr_mics    has_larger_nr_mics 
SET_prev_nr_mics      020010_CtfFind        0    undefined           undefined 
020010_CtfFind        020020_Select_mics    0    undefined           undefined 
020020_Select_mics    WAIT                  0    undefined           undefined 
