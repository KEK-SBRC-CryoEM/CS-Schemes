
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
EM_ctffind_fit_res_min        XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
EM_ctffind_fit_res_max        XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
GTF_ctffind_search_def_min    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_ctffind_search_def_max    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_ctffind_res_max_limit     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
current_nr_motioncorr_mics    0                             0 
pre_nr_ctffind_mics           0                             0 
wait_sec                      180                           180 
maxtime_hr                    96                            96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
has_unprocessed_ctffind_mics    0                             0 
has_motioncorr                  0                             0

# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
SS_comm_motioncorr_mics_star    XXX_SSE_REPLACE_SAMPLE_XXX                                        XXX_SSE_REPLACE_SAMPLE_XXX 
ctffind_mics_star               Schemes/020_GTF_CtfFind/020010_CtfFind/micrographs_ctf.star       Schemes/020_GTF_CtfFind/020010_CtfFind/micrographs_ctf.star 
micrographs                     micrographs                                                       micrographs 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
COUNT_current_motioncorr_mics    float=count_images    current_nr_motioncorr_mics      SS_comm_motioncorr_mics_star    micrographs 
COUNT_pre_ctffind_mics           float=count_images    pre_nr_ctffind_mics             ctffind_mics_star               micrographs 
HAS_motioncorr                   bool=file_exists      has_motioncorr                  SS_comm_motioncorr_mics_star    undefined 
HAS_unprocessed_ctffind_mics     bool=gt               has_unprocessed_ctffind_mics    current_nr_motioncorr_mics      pre_nr_ctffind_mics 
WAIT                             wait                  undefined                       wait_sec                        undefined 
EXIT_maxtime                     exit_maxtime          undefined                       maxtime_hr                      undefined 


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
WAIT                             EXIT_maxtime                           0    undefined                        undefined 
EXIT_maxtime                     HAS_motioncorr                         1    COUNT_current_motioncorr_mics    has_motioncorr
HAS_motioncorr                   WAIT                                   0    undefined                        undefined 
COUNT_current_motioncorr_mics    COUNT_pre_ctffind_mics                 0    undefined                        undefined 
COUNT_pre_ctffind_mics           HAS_unprocessed_ctffind_mics           0    undefined                        undefined 
HAS_unprocessed_ctffind_mics     WAIT                                   1    020010_CtfFind                   has_unprocessed_ctffind_mics
020010_CtfFind                   020020_Select_mics                     0    undefined                        undefined 
020020_Select_mics               WAIT                                   0    undefined                        undefined 
