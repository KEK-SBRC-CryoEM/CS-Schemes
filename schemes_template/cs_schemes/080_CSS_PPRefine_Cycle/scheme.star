
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/080_CSS_PPRefine_Cycle/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CSS_mbin_pprefine_cycles_max    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
cur_cycles                      1                             1 
cycle_incre                     1                             1 
SS_comm_mbin_0o95box_pmd        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_angpix             XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_nr_pool            XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
EM_mics_apix                    XXX_SSE_REPLACE_EM_XXX        XXX_SSE_REPLACE_EM_XXX 
wait_sec                        180                           180 
maxtime_hr                      96                            96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
CSS_mbin_pprefine_wait_prev_proc    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
has_exited                          0                             0 
do_cycle                            0                             0 
SS_comm_mbin_do_preread_images      XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
CSS_mbin_pprefine_prev_proc_exited    XXX_SSE_REPLACE_SAMPLE_XXX                                                   XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_pprefine_refined_star        XXX_SSE_REPLACE_SAMPLE_XXX                                                   XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_pprefine_postproc_star       XXX_SSE_REPLACE_SAMPLE_XXX                                                   XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_pprefine_ref3d               XXX_SSE_REPLACE_SAMPLE_XXX                                                   XXX_SSE_REPLACE_SAMPLE_XXX 
cycles_ctfrefine_refine_data_temp     Schemes/080_CSS_PPRefine_Cycle/080070_Refine3D_polish/run_data.star          Schemes/080_CSS_PPRefine_Cycle/080070_Refine3D_polish/run_data.star 
cycles_postprocess_map_temp           Schemes/080_CSS_PPRefine_Cycle/080080_PostProcess_polish/postprocess.star    Schemes/080_CSS_PPRefine_Cycle/080080_PostProcess_polish/postprocess.star 
cycles_refine3d_refine_map_temp       Schemes/080_CSS_PPRefine_Cycle/080070_Refine3D_polish/run_class001.mrc       Schemes/080_CSS_PPRefine_Cycle/080070_Refine3D_polish/run_class001.mrc 
cycles_ctfrefine_refine_data          ""                                                                           "" 
cycles_postprocess_map                ""                                                                           "" 
cycles_refine3d_refine_map            ""                                                                           "" 
SS_comm_mbin_imported_mask3d_path     XXX_SSE_REPLACE_SAMPLE_XXX                                                   XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_mbin_mask3d_name              XXX_SSE_REPLACE_SAMPLE_XXX                                                   XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_sym_name                      XXX_SSE_REPLACE_SAMPLE_XXX                                                   XXX_SSE_REPLACE_SAMPLE_XXX 
EM_mtf_file                           XXX_SSE_REPLACE_EM_XXX                                                       XXX_SSE_REPLACE_EM_XXX 
SS_comm_motioncorr_mics_star          XXX_SSE_REPLACE_SAMPLE_XXX                                                   XXX_SSE_REPLACE_SAMPLE_XXX 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_prev_proc_exited            bool=file_exists    has_exited                      CSS_mbin_pprefine_prev_proc_exited    undefined 
INCRE_cur_cycles                float=plus          cur_cycles                      cycle_incre                           cur_cycles 
CHECK_max_cycles                bool=le             do_cycle                        cur_cycles                            CSS_mbin_pprefine_cycles_max 
INIT_ctfrefine_refine_data      string=set          cycles_ctfrefine_refine_data    CSS_mbin_pprefine_refined_star        undefined 
INIT_postprocess_map            string=set          cycles_postprocess_map          CSS_mbin_pprefine_postproc_star       undefined 
INIT_refine3d_refine_map        string=set          cycles_refine3d_refine_map      CSS_mbin_pprefine_ref3d               undefined 
UPDATE_ctfrefine_refine_data    string=set          cycles_ctfrefine_refine_data    cycles_ctfrefine_refine_data_temp     undefined 
UPDATE_postprocess_map          string=set          cycles_postprocess_map          cycles_postprocess_map_temp           undefined 
UPDATE_refine3d_refine_map      string=set          cycles_refine3d_refine_map      cycles_refine3d_refine_map_temp       undefined 
WAIT                            wait                undefined                       wait_sec                              undefined 
EXIT_maxtime                    exit_maxtime        undefined                       maxtime_hr                            undefined 
EXIT                            exit                undefined                       undefined                             undefined 

# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
080010_CtfRefine_aberration     080010_CtfRefine_aberration     new            0 
080020_CtfRefine_aniso_mag      080020_CtfRefine_aniso_mag      new            0 
080030_CtfRefine_ctf_params     080030_CtfRefine_ctf_params     new            0 
080040_Refine3D_ctfrefine       080040_Refine3D_ctfrefine       new            0 
080050_PostProcess_ctfrefine    080050_PostProcess_ctfrefine    new            0 
080060_Polish                   080060_Polish                   new            0 
080070_Refine3D_polish          080070_Refine3D_polish          new            0 
080080_PostProcess_polish       080080_PostProcess_polish       new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                            INIT_ctfrefine_refine_data      1    EXIT_maxtime                    CSS_mbin_pprefine_wait_prev_proc 
EXIT_maxtime                    HAS_prev_proc_exited            0    undefined                       undefined 
HAS_prev_proc_exited            WAIT                            1    INIT_ctfrefine_refine_data      has_exited 
INIT_ctfrefine_refine_data      INIT_postprocess_map            0    undefined                       undefined 
INIT_postprocess_map            INIT_refine3d_refine_map        0    undefined                       undefined 
INIT_refine3d_refine_map        080010_CtfRefine_aberration     0    undefined                       undefined 
080010_CtfRefine_aberration     080020_CtfRefine_aniso_mag      0    undefined                       undefined 
080020_CtfRefine_aniso_mag      080030_CtfRefine_ctf_params     0    undefined                       undefined 
080030_CtfRefine_ctf_params     080040_Refine3D_ctfrefine       0    undefined                       undefined 
080040_Refine3D_ctfrefine       080050_PostProcess_ctfrefine    0    undefined                       undefined 
080050_PostProcess_ctfrefine    080060_Polish                   0    undefined                       undefined 
080060_Polish                   080070_Refine3D_polish          0    undefined                       undefined 
080070_Refine3D_polish          080080_PostProcess_polish       0    undefined                       undefined 
080080_PostProcess_polish       INCRE_cur_cycles                0    undefined                       undefined 
INCRE_cur_cycles                CHECK_max_cycles                0    undefined                       undefined 
CHECK_max_cycles                EXIT                            1    UPDATE_ctfrefine_refine_data    do_cycle 
UPDATE_ctfrefine_refine_data    UPDATE_postprocess_map          0    undefined                       undefined 
UPDATE_postprocess_map          UPDATE_refine3d_refine_map      0    undefined                       undefined 
UPDATE_refine3d_refine_map      080010_CtfRefine_aberration     0    undefined                       undefined 
