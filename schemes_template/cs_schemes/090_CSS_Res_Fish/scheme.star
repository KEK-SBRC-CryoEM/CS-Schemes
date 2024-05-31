
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/090_CSS_Res_Fish/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CSS_mbin_optimal_pmd              232         232 
CSS_mbin_0o95box_pmd              334         334 
CSS_noalign3d_classes               2           2 
CSS_noalign3d_tval                256         256 
CSS_mbin_apix                       0.8008      0.8008 
CSS_bfactor                       -40         -40 
maxtime_hr                        96          96 
wait_sec                         180         180 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
CSS_wait_prev_proc       1      1 
CSS_mbin_do_fast_subsets 0      0 
has_exited               0      0 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
prev_proc_exited               Schemes/080_CSS_Refine_Cycle/RELION_JOB_EXIT_SUCCESS                       Schemes/080_CSS_Refine_Cycle/RELION_JOB_EXIT_SUCCESS 
CSS_class3d_refine_data        Schemes/080_CSS_Refine_Cycle/1607_Refine3D_polish/run_data.star            Schemes/080_CSS_Refine_Cycle/1607_Refine3D_polish/run_data.star 
CSS_class3d_refine_map         Schemes/080_CSS_Refine_Cycle/1607_Refine3D_polish/run_class001.mrc         Schemes/080_CSS_Refine_Cycle/1607_Refine3D_polish/run_class001.mrc 
CSS_imported_mbin_mask3d       Schemes/080_CSS_Refine_Cycle/1202_Import_mask3d/$$CSS_mbin_mask3d_name     Schemes/080_CSS_Refine_Cycle/1202_Import_mask3d/$$CSS_mbin_mask3d_name 
CSS_mbin_mask3d_name           mbin_mask3d_apix0o8008_d440.mrc                                            mbin_mask3d_apix0o8008_d440.mrc 
CSS_mbin_sym_name_class3d              C3                                                                C3 
CSS_mbin_sym_name_refine3d_apo         C3                                                                C3 

# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
EXIT                      exit              undefined       undefined           undefined 
WAIT                      wait              undefined       wait_sec            undefined 
EXIT_maxtime              exit_maxtime      undefined       maxtime_hr          undefined 
HAS_prev_proc_exited      bool=file_exists  has_exited      prev_proc_exited    undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
1900_Class3D_noalign             1900_Class3D_noalign       new            0 
2000_External_select3d           2000_External_select3d     new            0 
2100_Refine3D_global             2100_Refine3D_global       new            0 
2200_PostProcess_global          2200_PostProcess_global    new            0 
2300_Refine3D_local              2300_Refine3D_local        new            0 
2400_PostProcess_local           2400_PostProcess_local     new            0 
2500_LocalRes                    2500_LocalRes              new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                             1900_Class3D_noalign          1   EXIT_maxtime          CSS_wait_prev_proc 
EXIT_maxtime                     HAS_prev_proc_exited          0   undefined             undefined 
HAS_prev_proc_exited             WAIT                          1   1900_Class3D_noalign  has_exited 
1900_Class3D_noalign             2000_External_select3d        0   undefined             undefined 
2000_External_select3d           2100_Refine3D_global          0   undefined             undefined 
2100_Refine3D_global             2200_PostProcess_global       0   undefined             undefined 
2200_PostProcess_global          2300_Refine3D_local           0   undefined             undefined 
2300_Refine3D_local              2400_PostProcess_local        0   undefined             undefined 
2400_PostProcess_local           2500_LocalRes                 0   undefined             undefined 
2500_LocalRes                    EXIT                          0   undefined             undefined 
