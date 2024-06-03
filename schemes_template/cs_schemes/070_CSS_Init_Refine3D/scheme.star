
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/070_CSS_Init_Refine3D/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
SS_comm_dup_thresh                   21               21 
EM_mics_apix                          0.885            0.885 
CSS_mbin_reextract_mics_box         360              360 
CSS_mbin_reextract_mics_0o95box     342              342 
CSS_mbin_reextract_parts_box        288              288 
CSS_mbin_reextract_parts_x_min      180              180 
CSS_mbin_reextract_parts_x_max     5580             5580 
CSS_mbin_reextract_parts_y_min      180              180 
CSS_mbin_reextract_parts_y_max     3912             3912 
SS_comm_optimal_pmd                 166              166 
SS_comm_mbin_0o95box_pmd            260              260 
SS_comm_mbin_angpix                   1.0375           1.0375 
wait_sec                            180              180 
maxtime_hr                           96               96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
SS_comm_wait_prev_proc    1        1 
has_exited                0        0 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
prev_proc_exited                   Schemes/060_CSS_Clean_Stack_3D/RELION_JOB_EXIT_SUCCESS                             Schemes/060_CSS_Clean_Stack_3D/RELION_JOB_EXIT_SUCCESS 
SS_comm_ctf_mics_star              Schemes/11_CS_Create_Stack/0102_Select_split_stack_mics/micrographs_split1.star    Schemes/11_CS_Create_Stack/0102_Select_split_stack_mics/micrographs_split1.star 
CSS_mbin_reextract_refined_star    Schemes/060_CSS_Clean_Stack_3D/0900_Refine3D/run_data.star                         Schemes/060_CSS_Clean_Stack_3D/0900_Refine3D/run_data.star 
SS_comm_mbin_ref3d_path            Inputs/ref3d.mrc                                                                   Inputs/ref3d.mrc 
SS_comm_mbin_ref3d_name            ref3d.mrc                                                                          ref3d.mrc 
SS_comm_mbin_mask3d_path           Inputs/mask3d.mrc                                                                  Inputs/mask3d.mrc 
SS_comm_mbin_mask3d_name           mask3d.mrc                                                                         mask3d.mrc 
imported_ref3d                     Schemes/070_CSS_Init_Refine3D/1201_Import_ref3d/$$SS_comm_mbin_ref3d_name          Schemes/070_CSS_Init_Refine3D/1201_Import_ref3d/$$SS_comm_mbin_ref3d_name 
imported_mask3d                    Schemes/070_CSS_Init_Refine3D/1202_Import_mask3d/$$SS_comm_mbin_mask3d_name        Schemes/070_CSS_Init_Refine3D/1202_Import_mask3d/$$SS_comm_mbin_mask3d_name 
SS_comm_sym_name                   D4                                                                                 D4 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_prev_proc_exited    bool=file_exists    has_exited    prev_proc_exited    undefined 
WAIT                    wait                undefined     wait_sec            undefined 
EXIT_maxtime            exit_maxtime        undefined     maxtime_hr          undefined 
EXIT                    exit                undefined     undefined           undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
1100_Extract_reextract     1100_Extract_reextract     new            0 
1101_Select_rm_dup         1101_Select_rm_dup         new            0 
1102_Select_rm_bars_x      1102_Select_rm_bars_x      new            0 
1103_Select_rm_bars_xy     1103_Select_rm_bars_xy     new            0 
1201_Import_ref3d          1201_Import_ref3d          new            0 
1202_Import_mask3d         1202_Import_mask3d         new            0 
1300_Refine3D_global       1300_Refine3D_global       new            0 
1400_PostProcess_global    1400_PostProcess_global    new            0 
1500_Refine3D_local        1500_Refine3D_local        new            0 
1600_PostProcess_local     1600_PostProcess_local     new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                       1100_Extract_reextract     1    EXIT_maxtime              SS_comm_wait_prev_proc 
EXIT_maxtime               HAS_prev_proc_exited       0    undefined                 undefined 
HAS_prev_proc_exited       WAIT                       1    1100_Extract_reextract    has_exited 
1100_Extract_reextract     1101_Select_rm_dup         0    undefined                 undefined 
1101_Select_rm_dup         1102_Select_rm_bars_x      0    undefined                 undefined 
1102_Select_rm_bars_x      1103_Select_rm_bars_xy     0    undefined                 undefined 
1103_Select_rm_bars_xy     1201_Import_ref3d          0    undefined                 undefined 
1201_Import_ref3d          1202_Import_mask3d         0    undefined                 undefined 
1202_Import_mask3d         1300_Refine3D_global       0    undefined                 undefined 
1300_Refine3D_global       1400_PostProcess_global    0    undefined                 undefined 
1400_PostProcess_global    1500_Refine3D_local        0    undefined                 undefined 
1500_Refine3D_local        1600_PostProcess_local     0    undefined                 undefined 
1600_PostProcess_local     EXIT                       0    undefined                 undefined 
