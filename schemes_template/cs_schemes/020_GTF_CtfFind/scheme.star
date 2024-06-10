
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/020_GTF_Ctffind/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
EM_ctffind_fit_res_min           30             30 
EM_ctffind_fit_res_max            4              4 
GTF_ctffind_search_def_min     3000           3000 
GTF_ctffind_search_def_max    20000          20000 
GTF_ctffind_res_max_limit         6              6 
current_nr_motioncorr_mics        0              0 
pre_nr_ctffind_mics               0              0 
wait_sec                        180            180 
maxtime_hr                       96             96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
has_unprocessed_ctffind_mics    0            0 
has_motioncorr                  0            0

# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
SS_comm_motioncorr_mics_star    Schemes/010_GTF_MotionCorr/010030_Select_mics/micrographs.star    Schemes/010_GTF_MotionCorr/010030_Select_mics/micrographs.star 
ctffind_mics_star               Schemes/020_GTF_CtfFind/020010_CtfFind/micrographs_ctf.star       Schemes/020_GTF_CtfFind/020010_CtfFind/micrographs_ctf.star 
ctffind_exe                     /programs/x86_64-linux/ctffind4/4.1.14-c7/bin/ctffind4            /programs/x86_64-linux/ctffind4/4.1.14-c7/bin/ctffind4 
gctf_exe                        ""                                                                "" 
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
ctffind               ctffind                 continue       0 
0202_Select_mic       0202_Select_mic         continue       0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                             EXIT_maxtime                           0    undefined     undefined 
EXIT_maxtime                     HAS_motioncorr                         1    COUNT_current_motioncorr_mics  has_motioncorr
HAS_motioncorr                   WAIT                                   0    undefined     undefined 
COUNT_current_motioncorr_mics    COUNT_pre_ctffind_mics                 0    undefined     undefined 
COUNT_pre_ctffind_mics           HAS_unprocessed_ctffind_mics           0    undefined     undefined 
HAS_unprocessed_ctffind_mics     WAIT                                   1    ctffind       has_unprocessed_ctffind_mics
ctffind                          0202_Select_mic                        0    undefined     undefined 
0202_Select_mic                  WAIT                                   0    undefined     undefined 
