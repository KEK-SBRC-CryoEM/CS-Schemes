
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/080_CSS_Refine_Cycle/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CSS_mbin_pprefine_cycles_max      2               2 
cur_cycles                        1               1 
cycle_incre                       1               1 
SS_comm_mbin_0o95box_pmd        200             200 
SS_comm_mbin_angpix               1.244           1.244 
wait_sec                        180             180 
maxtime_hr                       96              96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
SS_comm_wait_prev_proc    0        0 
has_exited                0        0 
do_cycle                  0        0 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
prev_proc_exited                     Schemes/070_CSS_Init_Refine3D/RELION_JOB_EXIT_SUCCESS                          Schemes/070_CSS_Init_Refine3D/RELION_JOB_EXIT_SUCCESS 
CSS_mbin_pprefine_refined_star       Schemes/070_CSS_Init_Refine3D/1500_Refine3D_local/run_data.star                Schemes/070_CSS_Init_Refine3D/1500_Refine3D_local/run_data.star 
CSS_mbin_pprefine_postproc_star      Schemes/070_CSS_Init_Refine3D/1600_PostProcess_local/postprocess.star          Schemes/070_CSS_Init_Refine3D/1600_PostProcess_local/postprocess.star  
CSS_mbin_pprefine_ref3d              Schemes/070_CSS_Init_Refine3D/1500_Refine3D_local/run_class001.mrc             Schemes/070_CSS_Init_Refine3D/1500_Refine3D_local/run_class001.mrc 
cycles_ctfrefine_refine_data_temp    Schemes/080_CSS_Refine_Cycle/1607_Refine3D_polish/run_data.star                Schemes/080_CSS_Refine_Cycle/1607_Refine3D_polish/run_data.star 
cycles_postprocess_map_temp          Schemes/080_CSS_Refine_Cycle/1608_PostProcess_polish/postprocess.star          Schemes/080_CSS_Refine_Cycle/1608_PostProcess_polish/postprocess.star 
cycles_refine3d_refine_map_temp      Schemes/080_CSS_Refine_Cycle/1607_Refine3D_polish/run_class001.mrc             Schemes/080_CSS_Refine_Cycle/1607_Refine3D_polish/run_class001.mrc 
cycles_ctfrefine_refine_data         ""                                                                             "" 
cycles_postprocess_map               ""                                                                             "" 
cycles_refine3d_refine_map           ""                                                                             "" 
SS_comm_mbin_imported_mask3d_path    Schemes/070_CSS_Init_Refine3D/1202_Import_mask3d/$$SS_comm_mbin_mask3d_name    Schemes/070_CSS_Init_Refine3D/1202_Import_mask3d/$$SS_comm_mbin_mask3d_name 
SS_comm_mbin_mask3d_name             mask3d.mrc                                                                     mask3d.mrc 
SS_comm_sym_name                     D2                                                                             D2 
SS_comm_motioncorr_mics_star         Schemes/010_GTF_Motioncorr/motioncorr/corrected_micrographs.star               Schemes/010_GTF_Motioncorr/motioncorr/corrected_micrographs.star 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_prev_proc_exited            bool=file_exists    has_exited                      prev_proc_exited                     undefined 
INCRE_cur_cycles                float=plus          cur_cycles                      cycle_incre                          cur_cycles 
CHECK_max_cycles                bool=le             do_cycle                        cur_cycles                           CSS_mbin_pprefine_cycles_max 
INIT_ctfrefine_refine_data      string=set          cycles_ctfrefine_refine_data    CSS_mbin_pprefine_refined_star       undefined 
INIT_postprocess_map            string=set          cycles_postprocess_map          CSS_mbin_pprefine_postproc_star      undefined 
INIT_refine3d_refine_map        string=set          cycles_refine3d_refine_map      CSS_mbin_pprefine_ref3d              undefined 
UPDATE_ctfrefine_refine_data    string=set          cycles_ctfrefine_refine_data    cycles_ctfrefine_refine_data_temp    undefined 
UPDATE_postprocess_map          string=set          cycles_postprocess_map          cycles_postprocess_map_temp          undefined 
UPDATE_refine3d_refine_map      string=set          cycles_refine3d_refine_map      cycles_refine3d_refine_map_temp      undefined 
WAIT                            wait                undefined                       wait_sec                             undefined 
EXIT_maxtime                    exit_maxtime        undefined                       maxtime_hr                           undefined 
EXIT                            exit                undefined                       undefined                            undefined 

# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
1601_CtfRefine_aberration       1601_CtfRefine_aberration       new            0 
1602_CtfRefine_magnification    1602_CtfRefine_magnification    new            0 
1603_CtfRefine_ctf_param        1603_CtfRefine_ctf_param        new            0 
1604_Refine3D_ctfrefine         1604_Refine3D_ctfrefine         new            0 
1605_PostProcess_ctfrefine      1605_PostProcess_ctfrefine      new            0 
1606_Polish                     1606_Polish                     new            0 
1607_Refine3D_polish            1607_Refine3D_polish            new            0 
1608_PostProcess_polish         1608_PostProcess_polish         new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                            INIT_ctfrefine_refine_data      1    EXIT_maxtime                    SS_comm_wait_prev_proc 
EXIT_maxtime                    HAS_prev_proc_exited            0    undefined                       undefined 
HAS_prev_proc_exited            WAIT                            1    INIT_ctfrefine_refine_data      has_exited 
INIT_ctfrefine_refine_data      INIT_postprocess_map            0    undefined                       undefined 
INIT_postprocess_map            INIT_refine3d_refine_map        0    undefined                       undefined 
INIT_refine3d_refine_map        1601_CtfRefine_aberration       0    undefined                       undefined 
1601_CtfRefine_aberration       1602_CtfRefine_magnification    0    undefined                       undefined 
1602_CtfRefine_magnification    1603_CtfRefine_ctf_param        0    undefined                       undefined 
1603_CtfRefine_ctf_param        1604_Refine3D_ctfrefine         0    undefined                       undefined 
1604_Refine3D_ctfrefine         1605_PostProcess_ctfrefine      0    undefined                       undefined 
1605_PostProcess_ctfrefine      1606_Polish                     0    undefined                       undefined 
1606_Polish                     1607_Refine3D_polish            0    undefined                       undefined 
1607_Refine3D_polish            1608_PostProcess_polish         0    undefined                       undefined 
1608_PostProcess_polish         INCRE_cur_cycles                0    undefined                       undefined 
INCRE_cur_cycles                CHECK_max_cycles                0    undefined                       undefined 
CHECK_max_cycles                EXIT                            1    UPDATE_ctfrefine_refine_data    do_cycle 
UPDATE_ctfrefine_refine_data    UPDATE_postprocess_map          0    undefined                       undefined 
UPDATE_postprocess_map          UPDATE_refine3d_refine_map      0    undefined                       undefined 
UPDATE_refine3d_refine_map      1601_CtfRefine_aberration       0    undefined                       undefined 