
# version 30001

data_scheme_general

_rlnSchemeName                       Schemes/3_CS_Refine_Cycle/
_rlnSchemeCurrentNodeName            WAIT
 

# version 30001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3  
CS_refine3d_pmd_0o95       260        260
CS_angpix                    1.0375     1.0375
maxtime_hr                  96         96
wait_sec                   180        180
 

# version 30001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3
CS_wait_prev_proc      1       1 
has_exited             0       0
 

# version 30001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
prev_proc_exited           Schemes/2_CS_Init_Refine3D/RELION_JOB_EXIT_SUCCESS                   Schemes/2_CS_Init_Refine3D/RELION_JOB_EXIT_SUCCESS
CS_refine3d_refine_map     Schemes/2_CS_Init_Refine3D/1500_Refine3D_local/run_class001.mrc      Schemes/2_CS_Init_Refine3D/1500_Refine3D_local/run_class001.mrc
CS_postprocess_map         Schemes/2_CS_Init_Refine3D/1600_PostProcess_local/postprocess.star   Schemes/2_CS_Init_Refine3D/1600_PostProcess_local/postprocess.star
CS_ctfrefine_refine_data   Schemes/2_CS_Init_Refine3D/1500_Refine3D_local/run_data.star         Schemes/2_CS_Init_Refine3D/1500_Refine3D_local/run_data.star
CS_imported_mask3d         Schemes/2_CS_Init_Refine3D/1202_Import_mask3d/$$CS_mask3d_name       Schemes/2_CS_Init_Refine3D/1202_Import_mask3d/$$CS_mask3d_name
CS_mask3d_name             mask3d_emd_21992_additional_3_align_manu_tm_lpf3o1125_apix1o0375_d288_wo_det.mrc           　　　　　　mask3d_emd_21992_additional_3_align_manu_tm_lpf3o1125_apix1o0375_d288_wo_det.mrc
CS_motioncorr_mics         Schemes/0_CS_prep/motioncorr/corrected_micrographs.star              Schemes/0_CS_prep/motioncorr/corrected_micrographs.star 
CS_sym_name_refine3d_apo   C1                               C1 

# version 30001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
EXIT                  exit              undefined        undefined         undefined 
EXIT_maxtime          exit_maxtime      undefined        maxtime_hr        undefined 
HAS_prev_proc_exited  bool=file_exists  has_exited       prev_proc_exited  undefined
WAIT                  wait              undefined        wait_sec          undefined 
 

# version 30001

data_scheme_jobs

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
1601_CtfRefine_aberration_1st       1601_CtfRefine_aberration_1st       new            0 
1602_CtfRefine_magnification_1st    1602_CtfRefine_magnification_1st    new            0 
1603_CtfRefine_ctf_param_1st        1603_CtfRefine_ctf_param_1st        new            0 
1604_Refine3D_ctfrefine_1st         1604_Refine3D_ctfrefine_1st         new            0 
1605_PostProcess_ctfrefine_1st      1605_PostProcess_ctfrefine_1st      new            0 
1606_Polish_1st                     1606_Polish_1st                     new            0 
1607_Refine3D_polish_1st            1607_Refine3D_polish_1st            new            0 
1608_PostProcess_polish_1st         1608_PostProcess_polish_1st         new            0 
1701_CtfRefine_aberration_2nd       1701_CtfRefine_aberration_2nd       new            0 
1702_CtfRefine_magnification_2nd    1702_CtfRefine_magnification_2nd    new            0 
1703_CtfRefine_ctf_param_2nd        1703_CtfRefine_ctf_param_2nd        new            0 
1704_Refine3D_ctfrefine_2nd         1704_Refine3D_ctfrefine_2nd         new            0 
1705_PostProcess_ctfrefine_2nd      1705_PostProcess_ctfrefine_2nd      new            0 
1706_Polish_2nd                     1706_Polish_2nd                     new            0 
1707_Refine3D_polish_2nd            1707_Refine3D_polish_2nd            new            0 
1708_PostProcess_polish_2nd         1708_PostProcess_polish_2nd         new            0 
1801_CtfRefine_aberration_3rd       1801_CtfRefine_aberration_3rd       new            0 
1802_CtfRefine_magnification_3rd    1802_CtfRefine_magnification_3rd    new            0 
1803_CtfRefine_ctf_param_3rd        1803_CtfRefine_ctf_param_3rd        new            0 
1804_Refine3D_ctfrefine_3rd         1804_Refine3D_ctfrefine_3rd         new            0 
1805_PostProcess_ctfrefine_3rd      1805_PostProcess_ctfrefine_3rd      new            0 
1806_Polish_3rd                     1806_Polish_3rd                     new            0 
1807_Refine3D_polish_3rd            1807_Refine3D_polish_3rd            new            0 
1808_PostProcess_polish_3rd         1808_PostProcess_polish_3rd         new            0 
 

# version 30001

data_scheme_edges

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                                1601_CtfRefine_aberration_1st          1  EXIT_maxtime                  CS_wait_prev_proc
EXIT_maxtime                        HAS_prev_proc_exited                   0  undefined                     undefined 
HAS_prev_proc_exited                WAIT                                   1  1601_CtfRefine_aberration_1st has_exited  
1601_CtfRefine_aberration_1st       1602_CtfRefine_magnification_1st       0  undefined                     undefined 
1602_CtfRefine_magnification_1st    1603_CtfRefine_ctf_param_1st           0  undefined                     undefined 
1603_CtfRefine_ctf_param_1st        1604_Refine3D_ctfrefine_1st            0  undefined                     undefined 
1604_Refine3D_ctfrefine_1st         1605_PostProcess_ctfrefine_1st         0  undefined                     undefined 
1605_PostProcess_ctfrefine_1st      1606_Polish_1st                        0  undefined                     undefined 
1606_Polish_1st                     1607_Refine3D_polish_1st               0  undefined                     undefined 
1607_Refine3D_polish_1st            1608_PostProcess_polish_1st            0  undefined                     undefined 
1608_PostProcess_polish_1st         1701_CtfRefine_aberration_2nd          0  undefined                     undefined 
1701_CtfRefine_aberration_2nd       1702_CtfRefine_magnification_2nd       0  undefined                     undefined 
1702_CtfRefine_magnification_2nd    1703_CtfRefine_ctf_param_2nd           0  undefined                     undefined 
1703_CtfRefine_ctf_param_2nd        1704_Refine3D_ctfrefine_2nd            0  undefined                     undefined 
1704_Refine3D_ctfrefine_2nd         1705_PostProcess_ctfrefine_2nd         0  undefined                     undefined 
1705_PostProcess_ctfrefine_2nd      1706_Polish_2nd                        0  undefined                     undefined 
1706_Polish_2nd                     1707_Refine3D_polish_2nd               0  undefined                     undefined 
1707_Refine3D_polish_2nd            1708_PostProcess_polish_2nd            0  undefined                     undefined 
1708_PostProcess_polish_2nd         1801_CtfRefine_aberration_3rd          0  undefined                     undefined 
1801_CtfRefine_aberration_3rd       1802_CtfRefine_magnification_3rd       0  undefined                     undefined 
1802_CtfRefine_magnification_3rd    1803_CtfRefine_ctf_param_3rd           0  undefined                     undefined 
1803_CtfRefine_ctf_param_3rd        1804_Refine3D_ctfrefine_3rd            0  undefined                     undefined 
1804_Refine3D_ctfrefine_3rd         1805_PostProcess_ctfrefine_3rd         0  undefined                     undefined 
1805_PostProcess_ctfrefine_3rd      1806_Polish_3rd                        0  undefined                     undefined 
1806_Polish_3rd                     1807_Refine3D_polish_3rd               0  undefined                     undefined 
1807_Refine3D_polish_3rd            1808_PostProcess_polish_3rd            0  undefined                     undefined 
1808_PostProcess_polish_3rd         EXIT                                   0  undefined                     undefined 
 
