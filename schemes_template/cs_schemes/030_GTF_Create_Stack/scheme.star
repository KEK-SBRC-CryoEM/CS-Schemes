
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/030_GTF_Create_Stack/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CS_mics_box              400             400 
CS_mics_box_0o95         380             380 
CS_min_nr_parts       400000          400000 
CS_min_nr_mics          2000            2000 
CS_parts_box             100             100 
CS_parts_x_coods_max    3896            3896 
CS_parts_x_coods_min     200             200 
CS_parts_y_coods_max    3896            3896 
CS_parts_y_coods_min     200             200 
CS_cryolo_thr              0.1             0.1 
CS_log_diam_min          100             100 
CS_log_diam_max          160             160 
CS_log_adjust_thr          0.25            0.25 
CS_log_upper_thr           5               5 
prev_nr_mics               0               0 
current_nr_mics            0               0 
current_nr_parts           0               0 
active_thr                 0.0             0.0 
maxtime_hr                96              96 
wait_sec                 180             180 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
CS_limit_mics          1            1 
CS_use_log_pick        1            1 
has_ctffind            0            0 
has_larger_nr_mics     0            0 
has_required_nr_mics   0            0 
has_required_nr_parts  0            0 
limit_mics             0            0 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
CS_ctf_mics             Schemes/020_GTF_Ctffind/0202_Select_mic/micrographs.star                        Schemes/020_GTF_Ctffind/0202_Select_mic/micrographs.star  
selected_rm_bars_parts  Schemes/030_GTF_Create_Stack/0302_Select_rm_bars_xy/particles.star                Schemes/030_GTF_Create_Stack/0302_Select_rm_bars_xy/particles.star 
split_mics              Schemes/030_GTF_Create_Stack/0102_Select_split_stack_mics/micrographs_split1.star Schemes/030_GTF_Create_Stack/0102_Select_split_stack_mics/micrographs_split1.star 
all_mics                Schemes/030_GTF_Create_Stack/0101_Select_mic/micrographs.star                     Schemes/030_GTF_Create_Stack/0101_Select_mic/micrographs.star 
cryolo_exe              /efs/em/crYOLO/gtf_relion4_run_cryolo_system.sh                                 /efs/em/crYOLO/gtf_relion4_run_cryolo_system.sh 
cryolo_repo             /efs/em/crYOLO                                                                  /efs/em/crYOLO 
cryolo_coords           Schemes/030_GTF_Create_Stack/0200_External_cryolo/autopick.star                   Schemes/030_GTF_Create_Stack/0200_External_cryolo/autopick.star 
log_coords              Schemes/030_GTF_Create_Stack/0201_AutoPick_log/autopick.star                      Schemes/030_GTF_Create_Stack/0201_AutoPick_log/autopick.star 
mics_import             undefined                                                                       undefined 
active_coords           undefined                                                                       undefined 
micrographs             micrographs                                                                     micrographs 
particles               particles                                                                       particles 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
EXIT                           exit                 undefined              undefined               undefined 
EXIT_maxtime                   exit_maxtime         undefined              maxtime_hr              undefined 
HAS_ctffind                    bool=file_exists     has_ctffind            CS_ctf_mics             undefined 
COUNT_mics                     float=count_images   current_nr_mics        CS_ctf_mics             micrographs 
HAS_mics_increased             bool=gt              has_larger_nr_mics     current_nr_mics         prev_nr_mics 
SET_prev_nr_mics               float=set            prev_nr_mics           current_nr_mics         undefined 
HAS_required_nr_mics           bool=ge              has_required_nr_mics   current_nr_mics         CS_min_nr_mics 
LIMIT_nr_mics                  bool=set             limit_mics             CS_limit_mics           undefined 
SET_split_mics                 string=set           mics_import            split_mics              undefined 
SET_all_mics                   string=set           mics_import            all_mics                undefined 
COUNT_parts                    float=count_images   current_nr_parts       selected_rm_bars_parts  particles 
HAS_required_nr_parts          bool=ge              has_required_nr_parts  current_nr_parts        CS_min_nr_parts 
ACTIVATE_cryolo_coords         string=set           active_coords          cryolo_coords           undefined 
ACTIVATE_log_coords            string=set           active_coords          log_coords              undefined 
ACTIVATE_cryolo_thr            float=set            active_thr             CS_cryolo_thr           undefined 
ACTIVATE_log_thr               float=set            active_thr             CS_log_adjust_thr       undefined 
WAIT                           wait                 undefined              wait_sec                undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
0102_Select_split_stack_mics      0102_Select_split_stack_mics     continue       0 
0200_External_cryolo              0200_External_cryolo             continue       0 
0201_AutoPick_log                 0201_AutoPick_log                continue       0 
0300_Extract                      0300_Extract                     continue       0 
0301_Select_rm_bars_x             0301_Select_rm_bars_x            continue       0 
0302_Select_rm_bars_xy            0302_Select_rm_bars_xy           continue       0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                              EXIT_maxtime                     0  undefined                     undefined 
EXIT_maxtime                      HAS_ctffind                      0  undefined                     undefined 
HAS_ctffind                       WAIT                             1  COUNT_mics                    has_ctffind 
COUNT_mics                        HAS_mics_increased               0  undefined                     undefined 
HAS_mics_increased                WAIT                             1  SET_prev_nr_mics              has_larger_nr_mics 
SET_prev_nr_mics                  HAS_required_nr_mics             0  undefined                     undefined 
HAS_required_nr_mics              WAIT                             1  LIMIT_nr_mics                 has_required_nr_mics 
LIMIT_nr_mics                     SET_all_mics                     1  0102_Select_split_stack_mics  limit_mics 
0102_Select_split_stack_mics      SET_split_mics                   0  undefined                     undefined 
SET_split_mics                    0200_External_cryolo             1  0201_AutoPick_log             CS_use_log_pick 
SET_all_mics                      0200_External_cryolo             1  0201_AutoPick_log             CS_use_log_pick 
0200_External_cryolo              ACTIVATE_cryolo_coords           0  undefined                     undefined 
ACTIVATE_cryolo_coords            ACTIVATE_cryolo_thr              0  undefined                     undefined 
ACTIVATE_cryolo_thr               0300_Extract                     0  undefined                     undefined 
0201_AutoPick_log                 ACTIVATE_log_coords              0  undefined                     undefined 
ACTIVATE_log_coords               ACTIVATE_log_thr                 0  undefined                     undefined 
ACTIVATE_log_thr                  0300_Extract                     0  undefined                     undefined 
0300_Extract                      0301_Select_rm_bars_x            0  undefined                     undefined 
0301_Select_rm_bars_x             0302_Select_rm_bars_xy           0  undefined                     undefined 
0302_Select_rm_bars_xy            COUNT_parts                      0  undefined                     undefined 
COUNT_parts                       HAS_required_nr_parts            0  undefined                     undefined 
HAS_required_nr_parts             WAIT                             1  EXIT                          has_required_nr_parts 
