
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/090_CSS_Res_Fish_3D/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CSS_mbin_resfish3d_classes             2                2 
CSS_mbin_resfish3d_tval              256              256 
SS_comm_optimal_pmd                  232              232 
SS_comm_mbin_0o95box_pmd             334              334 
SS_comm_mbin_angpix                    0.8008           0.8008 
CSS_mbin_resfish3d_locres_bfactor    -40              -40 
wait_sec                             180              180 
maxtime_hr                            96               96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
SS_comm_wait_prev_proc                1        1 
CSS_mbin_resfish3d_do_fast_subsets    0        0 
has_exited                            0        0 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
prev_proc_exited                     Schemes/080_CSS_PPRefine_Cycle/RELION_JOB_EXIT_SUCCESS                           Schemes/080_CSS_PPRefine_Cycle/RELION_JOB_EXIT_SUCCESS 
CSS_mbin_resfish3d_refined_star      Schemes/080_CSS_PPRefine_Cycle/080070_Refine3D_polish/run_data.star              Schemes/080_CSS_PPRefine_Cycle/080070_Refine3D_polish/run_data.star 
CSS_mbin_resfish3d_ref3d             Schemes/080_CSS_PPRefine_Cycle/080070_Refine3D_polish/run_class001.mrc           Schemes/080_CSS_PPRefine_Cycle/080070_Refine3D_polish/run_class001.mrc 
SS_comm_mbin_imported_mask3d_path    Schemes/070_CSS_Init_Refine3D/070060_Import_mask3d/$$SS_comm_mbin_mask3d_name    Schemes/070_CSS_Init_Refine3D/070060_Import_mask3d/$$SS_comm_mbin_mask3d_name 
SS_comm_mbin_mask3d_name             mbin_mask3d_apix0o8008_d440.mrc                                                  mbin_mask3d_apix0o8008_d440.mrc 
SS_comm_sym_name                     D2                                                                               D2 

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
090010_Class3D_noalign       090010_Class3D_noalign       new            0 
090020_External_select3d     090020_External_select3d     new            0 
090030_Refine3D_global       090030_Refine3D_global       new            0 
090040_PostProcess_global    090040_PostProcess_global    new            0 
090050_Refine3D_local        090050_Refine3D_local        new            0 
090060_PostProcess_local     090060_PostProcess_local     new            0 
090070_LocalRes              090070_LocalRes              new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                         090010_Class3D_noalign       1    EXIT_maxtime              SS_comm_wait_prev_proc 
EXIT_maxtime                 HAS_prev_proc_exited         0    undefined                 undefined 
HAS_prev_proc_exited         WAIT                         1    090010_Class3D_noalign    has_exited 
090010_Class3D_noalign       090020_External_select3d     0    undefined                 undefined 
090020_External_select3d     090030_Refine3D_global       0    undefined                 undefined 
090030_Refine3D_global       090040_PostProcess_global    0    undefined                 undefined 
090040_PostProcess_global    090050_Refine3D_local        0    undefined                 undefined 
090050_Refine3D_local        090060_PostProcess_local     0    undefined                 undefined 
090060_PostProcess_local     090070_LocalRes              0    undefined                 undefined 
090070_LocalRes              EXIT                         0    undefined                 undefined 
