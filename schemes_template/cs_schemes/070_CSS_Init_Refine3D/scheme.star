
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
SS_comm_dup_thresh                 XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
EM_mics_apix                       XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
CSS_mbin_reextract_mics_box        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_reextract_mics_0o95box    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_reextract_parts_box       XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_reextract_parts_x_min     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_reextract_parts_x_max     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_reextract_parts_y_min     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_reextract_parts_y_max     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_optimal_pmd                XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_0o95box_pmd           XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_angpix                XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_nr_pool               XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
wait_sec                           180                           180 
maxtime_hr                         96                            96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
CSS_mbin_reextract_wait_prev_proc    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
has_exited                           0                             0 
SS_comm_mbin_do_preread_images       XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 

# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
CSS_mbin_reextract_prev_proc_exited    XXX_SSE_REPLACE_SAMPLE_XXX                                                       XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_ctf_mics_star                  XXX_SSE_REPLACE_SAMPLE_XXX                                                       XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_reextract_refined_star        XXX_SSE_REPLACE_SAMPLE_XXX                                                       XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_ref3d_path                XXX_SSE_REPLACE_SAMPLE_XXX                                                       XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_ref3d_name                XXX_SSE_REPLACE_SAMPLE_XXX                                                       XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_mask3d_path               XXX_SSE_REPLACE_SAMPLE_XXX                                                       XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_mask3d_name               XXX_SSE_REPLACE_SAMPLE_XXX                                                       XXX_SSE_REPLACE_SAMPLE_XXX 
imported_ref3d                         Schemes/070_CSS_Init_Refine3D/070050_Import_ref3d/$$SS_comm_mbin_ref3d_name      Schemes/070_CSS_Init_Refine3D/070050_Import_ref3d/$$SS_comm_mbin_ref3d_name 
imported_mask3d                        Schemes/070_CSS_Init_Refine3D/070060_Import_mask3d/$$SS_comm_mbin_mask3d_name    Schemes/070_CSS_Init_Refine3D/070060_Import_mask3d/$$SS_comm_mbin_mask3d_name 
SS_comm_sym_name                       XXX_SSE_REPLACE_SAMPLE_XXX                                                       XXX_SSE_REPLACE_SAMPLE_XXX 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_prev_proc_exited    bool=file_exists    has_exited    CSS_mbin_reextract_prev_proc_exited    undefined 
WAIT                    wait                undefined     wait_sec                               undefined 
EXIT_maxtime            exit_maxtime        undefined     maxtime_hr                             undefined 
EXIT                    exit                undefined     undefined                              undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
070010_Extract_reextract     070010_Extract_reextract     new            0 
070020_Select_rm_dup         070020_Select_rm_dup         new            0 
070030_Select_rm_bars_x      070030_Select_rm_bars_x      new            0 
070040_Select_rm_bars_xy     070040_Select_rm_bars_xy     new            0 
070050_Import_ref3d          070050_Import_ref3d          new            0 
070060_Import_mask3d         070060_Import_mask3d         new            0 
070070_Refine3D_global       070070_Refine3D_global       new            0 
070080_PostProcess_global    070080_PostProcess_global    new            0 
070090_Refine3D_local        070090_Refine3D_local        new            0 
070100_PostProcess_local     070100_PostProcess_local     new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                         070010_Extract_reextract     1    EXIT_maxtime                CSS_mbin_reextract_wait_prev_proc 
EXIT_maxtime                 HAS_prev_proc_exited         0    undefined                   undefined 
HAS_prev_proc_exited         WAIT                         1    070010_Extract_reextract    has_exited 
070010_Extract_reextract     070020_Select_rm_dup         0    undefined                   undefined 
070020_Select_rm_dup         070030_Select_rm_bars_x      0    undefined                   undefined 
070030_Select_rm_bars_x      070040_Select_rm_bars_xy     0    undefined                   undefined 
070040_Select_rm_bars_xy     070050_Import_ref3d          0    undefined                   undefined 
070050_Import_ref3d          070060_Import_mask3d         0    undefined                   undefined 
070060_Import_mask3d         070070_Refine3D_global       0    undefined                   undefined 
070070_Refine3D_global       070080_PostProcess_global    0    undefined                   undefined 
070080_PostProcess_global    070090_Refine3D_local        0    undefined                   undefined 
070090_Refine3D_local        070100_PostProcess_local     0    undefined                   undefined 
070100_PostProcess_local     EXIT                         0    undefined                   undefined 
