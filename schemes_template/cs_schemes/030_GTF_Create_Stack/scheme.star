
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
GTF_pick_min_nr_mics            2000            2000 
prev_nr_mics                       0               0 
current_nr_mics                    0               0 
current_nr_parts                   0               0 
GTF_pick_cryolo_thresh             0.1             0.1 
GTF_pick_log_pdm_min             100             100 
GTF_pick_log_pdm_max             160             160 
GTF_pick_log_adjust_thresh         0.25            0.25 
GTF_pick_log_upper_thresh          5               5 
active_thr                         0.0             0.0 
GTF_lbin_extract_mics_box        400             400 
GTF_lbin_extract_mics_0o95box    380             380 
GTF_lbin_extract_parts_box       100             100 
GTF_lbin_extract_parts_x_min     200             200 
GTF_lbin_extract_parts_x_max    3896            3896 
GTF_lbin_extract_parts_y_min     200             200 
GTF_lbin_extract_parts_y_max    3896            3896 
wait_sec                         180             180 
maxtime_hr                        96              96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
GTF_pick_do_limit_mics    1        1 
limit_mics                0        0 
has_ctffind               0        0 
has_larger_nr_mics        0        0 
has_required_nr_mics      0        0 
GTF_pick_use_log_pick     1        1 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
SS_comm_ctf_mics_star    Schemes/020_GTF_Ctffind/0202_Select_mic/micrographs.star                             Schemes/020_GTF_Ctffind/0202_Select_mic/micrographs.star 
all_mics                 Schemes/030_GTF_Create_Stack/0101_Select_mic/micrographs.star                        Schemes/030_GTF_Create_Stack/0101_Select_mic/micrographs.star 
split_mics               Schemes/030_GTF_Create_Stack/0102_Select_split_stack_mics/micrographs_split1.star    Schemes/030_GTF_Create_Stack/0102_Select_split_stack_mics/micrographs_split1.star 
mics_import              undefined                                                                            undefined 
cryolo_exe               /efs/em/crYOLO/gtf_relion4_run_cryolo_system.sh                                      /efs/em/crYOLO/gtf_relion4_run_cryolo_system.sh 
cryolo_repo              /efs/em/crYOLO                                                                       /efs/em/crYOLO 
cryolo_coords            Schemes/030_GTF_Create_Stack/0200_External_cryolo/autopick.star                      Schemes/030_GTF_Create_Stack/0200_External_cryolo/autopick.star 
log_coords               Schemes/030_GTF_Create_Stack/0201_AutoPick_log/autopick.star                         Schemes/030_GTF_Create_Stack/0201_AutoPick_log/autopick.star 
active_coords            undefined                                                                            undefined 
micrographs              micrographs                                                                          micrographs 
particles                particles                                                                            particles 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_ctffind               bool=file_exists      has_ctffind             SS_comm_ctf_mics_star         undefined 
COUNT_mics                float=count_images    current_nr_mics         SS_comm_ctf_mics_star         micrographs 
HAS_mics_increased        bool=gt               has_larger_nr_mics      current_nr_mics               prev_nr_mics 
SET_prev_nr_mics          float=set             prev_nr_mics            current_nr_mics               undefined 
HAS_required_nr_mics      bool=ge               has_required_nr_mics    current_nr_mics               GTF_pick_min_nr_mics 
LIMIT_nr_mics             bool=set              limit_mics              GTF_pick_do_limit_mics        undefined 
SET_split_mics            string=set            mics_import             split_mics                    undefined 
SET_all_mics              string=set            mics_import             all_mics                      undefined 
ACTIVATE_cryolo_coords    string=set            active_coords           cryolo_coords                 undefined 
ACTIVATE_log_coords       string=set            active_coords           log_coords                    undefined 
ACTIVATE_cryolo_thr       float=set             active_thr              GTF_pick_cryolo_thresh        undefined 
ACTIVATE_log_thr          float=set             active_thr              GTF_pick_log_adjust_thresh    undefined 
WAIT                      wait                  undefined               wait_sec                      undefined 
EXIT_maxtime              exit_maxtime          undefined               maxtime_hr                    undefined 
EXIT                      exit                  undefined               undefined                     undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
0102_Select_split_stack_mics    0102_Select_split_stack_mics    continue       0 
0200_External_cryolo            0200_External_cryolo            continue       0 
0201_AutoPick_log               0201_AutoPick_log               continue       0 
0300_Extract                    0300_Extract                    continue       0 
0301_Select_rm_bars_x           0301_Select_rm_bars_x           continue       0 
0302_Select_rm_bars_xy          0302_Select_rm_bars_xy          continue       0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                            EXIT_maxtime              0    undefined                       undefined 
EXIT_maxtime                    HAS_ctffind               0    undefined                       undefined 
HAS_ctffind                     WAIT                      1    COUNT_mics                      has_ctffind 
COUNT_mics                      HAS_mics_increased        0    undefined                       undefined 
HAS_mics_increased              WAIT                      1    SET_prev_nr_mics                has_larger_nr_mics 
SET_prev_nr_mics                HAS_required_nr_mics      0    undefined                       undefined 
HAS_required_nr_mics            WAIT                      1    LIMIT_nr_mics                   has_required_nr_mics 
LIMIT_nr_mics                   SET_all_mics              1    0102_Select_split_stack_mics    limit_mics 
0102_Select_split_stack_mics    SET_split_mics            0    undefined                       undefined 
SET_split_mics                  0200_External_cryolo      1    0201_AutoPick_log               GTF_pick_use_log_pick 
SET_all_mics                    0200_External_cryolo      1    0201_AutoPick_log               GTF_pick_use_log_pick 
0200_External_cryolo            ACTIVATE_cryolo_coords    0    undefined                       undefined 
ACTIVATE_cryolo_coords          ACTIVATE_cryolo_thr       0    undefined                       undefined 
ACTIVATE_cryolo_thr             0300_Extract              0    undefined                       undefined 
0201_AutoPick_log               ACTIVATE_log_coords       0    undefined                       undefined 
ACTIVATE_log_coords             ACTIVATE_log_thr          0    undefined                       undefined 
ACTIVATE_log_thr                0300_Extract              0    undefined                       undefined 
0300_Extract                    0301_Select_rm_bars_x     0    undefined                       undefined 
0301_Select_rm_bars_x           0302_Select_rm_bars_xy    0    undefined                       undefined 
0302_Select_rm_bars_xy          EXIT                      0    undefined                       undefined 
