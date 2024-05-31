
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
GTF_ctf_max_def              20000          20000 
GTF_ctf_max_res                  4              4 
GTF_ctf_min_def               3000           3000  
GTF_ctf_select_maxres            6              6
current_nr_motioncorr_mics       0              0
pre_nr_ctffind_mics              0              0 
do_at_most                    9999           9999
maxtime_hr                      96             96 
wait_sec                       180            180 
 

# version 30001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
has_unprocessed_ctffind_mics            0            0 
 

# version 30001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
ctffind_mics              Schemes/020_GTF_Ctffind/ctffind/micrographs_ctf.star                Schemes/020_GTF_Ctffind/ctffind/micrographs_ctf.star
motioncorr_mics           Schemes/010_GTF_Motioncorr/motioncorr/corrected_micrographs.star    Schemes/010_GTF_Motioncorr/motioncorr/corrected_micrographs.star    
selected_motioncorr_mics  Schemes/010_GTF_Motioncorr/select_motioncor_mics/micrographs.star   Schemes/010_GTF_Motioncorr/select_motioncor_mics/micrographs.star 
motioncorr_micrographs    motioncorr_micrographs                                     motioncorr_micrographs
ctffind_micrographs       ctffind_micrographs                                        ctffind_micrographs


# version 30001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
COUNT_current_motioncorr_mics   float=count_images      current_nr_motioncorr_mics      selected_motioncorr_mics     motioncorr_micrographs
COUNT_pre_ctffind_mics          float=count_images      pre_nr_ctffind_mics             ctffind_mics                 ctffind_micrographs
EXIT_maxtime                    exit_maxtime            undefined                       maxtime_hr                   undefined 
HAS_motioncorr                  bool=file_exists        has_motioncorr                  motioncorr_mics              undefined
HAS_unprocessed_ctffind_mics    bool=gt                 has_unprocessed_ctffind_mics    current_nr_motioncorr_mics   pre_nr_ctffind_mics 
WAIT                            wait                    undefined                       wait_sec                     undefined 
 

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
WAIT                              EXIT_maxtime                           0  undefined     undefined 
EXIT_maxtime                      COUNT_current_motioncorr_mics          0  undefined     undefined 
COUNT_current_motioncorr_mics      COUNT_pre_ctffind_mics                0  undefined     undefined 
COUNT_pre_ctffind_mics            HAS_unprocessed_ctffind_mics           0  undefined     undefined 
HAS_unprocessed_ctffind_mics      WAIT                                   1  ctffind       has_unprocessed_ctffind_mics
ctffind                           0202_Select_mic                        0  undefined     undefined
0202_Select_mic                   WAIT                                   0  undefined     undefined 
