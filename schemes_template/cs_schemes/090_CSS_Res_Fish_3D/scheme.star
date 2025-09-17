
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
CSS_mbin_resfish3d_classes           XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_resfish3d_tval              XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_optimal_pmd                  XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_0o95box_pmd             XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_angpix                  XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_nr_pool                 XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
EM_mics_apix                         XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
CSS_mbin_resfish3d_locres_bfactor    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
wait_sec                             180                           180 
maxtime_hr                           96                            96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
CSS_mbin_resfish3d_wait_prev_proc     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_resfish3d_skip_nacls3d       XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_do_preread_images        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_resfish3d_do_fast_subsets    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
has_exited                            0                             0 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
CSS_mbin_resfish3d_prev_proc_exited    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_resfish3d_refined_star        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_resfish3d_ref3d               XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
gref3d_parts                           ""                            "" 
gref3d_ref3d                           ""                            "" 
selected_nacls3d_parts                 Schemes/090_CSS_Res_Fish_3D/090020_External_select3d/selected_data.star        Schemes/090_CSS_Res_Fish_3D/090020_External_select3d/selected_data.star 
selected_nacls3d_ref3d                 Schemes/090_CSS_Res_Fish_3D/090020_External_select3d/selected_model_map.mrc    Schemes/090_CSS_Res_Fish_3D/090020_External_select3d/selected_model_map.mrc 
SS_comm_mbin_imported_mask3d_path      XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_mask3d_name               XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_sym_name                       XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
EM_mtf_file                            XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_prev_proc_exited    bool=file_exists    has_exited      CSS_mbin_resfish3d_prev_proc_exited    undefined 
INIT_gref3d_parts       string=set          gref3d_parts    CSS_mbin_resfish3d_refined_star        undefined 
INIT_gref3d_ref3d       string=set          gref3d_ref3d    CSS_mbin_resfish3d_ref3d               undefined 
UPDATE_gref3d_parts     string=set          gref3d_parts    selected_nacls3d_parts                 undefined 
UPDATE_gref3d_ref3d     string=set          gref3d_ref3d    selected_nacls3d_ref3d                 undefined 
WAIT                    wait                undefined       wait_sec                               undefined 
EXIT_maxtime            exit_maxtime        undefined       maxtime_hr                             undefined 
EXIT                    exit                undefined       undefined                              undefined 


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
WAIT                            INIT_gref3d_parts               1    EXIT_maxtime              CSS_mbin_resfish3d_wait_prev_proc 
EXIT_maxtime                    HAS_prev_proc_exited            0    undefined                 undefined 
HAS_prev_proc_exited            WAIT                            1    INIT_gref3d_parts         has_exited 
INIT_gref3d_parts               INIT_gref3d_ref3d               0    undefined                 undefined 
INIT_gref3d_ref3d               090010_Class3D_noalign          1    090030_Refine3D_global    CSS_mbin_resfish3d_skip_nacls3d 
090010_Class3D_noalign          090020_External_select3d        0    undefined                 undefined 
090020_External_select3d        UPDATE_gref3d_parts             0    undefined                 undefined 
UPDATE_gref3d_parts             UPDATE_gref3d_ref3d             0    undefined                 undefined 
UPDATE_gref3d_ref3d             090030_Refine3D_global          0    undefined                 undefined 
090030_Refine3D_global          090040_PostProcess_global       0    undefined                 undefined 
090040_PostProcess_global       090050_Refine3D_local           0    undefined                 undefined 
090050_Refine3D_local           090060_PostProcess_local        0    undefined                 undefined 
090060_PostProcess_local        090070_LocalRes                 0    undefined                 undefined 
090070_LocalRes                 EXIT                            0    undefined                 undefined 
