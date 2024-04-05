
# version 30001

data_scheme_general

_rlnSchemeName                       Schemes/4_CS_Res_Fish/
_rlnSchemeCurrentNodeName            WAIT
 

# version 30001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
maxtime_hr                        96          96
wait_sec                         180         180
CS_class3d_pmd                   253         253
CS_refine3d_pmd_optimal          188         188
CS_refine3d_pmd_0o95             253         253
CS_nr_3d_classes                   2           2
CS_angpix                          1.0375      1.0375
CS_b_factor                     -146        -146


# version 30001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 f
_rlnSchemeBooleanVariableResetValue #3 
CS_wait_prev_proc   1      1
has_exited          0      0

# version 30001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3
prev_proc_exited        Schemes/3_CS_Refine_Cycle/RELION_JOB_EXIT_SUCCESS                       Schemes/3_CS_Refine_Cycle/RELION_JOB_EXIT_SUCCESS
CS_class3d_refine_data  Schemes/3_CS_Refine_Cycle/1807_Refine3D_polish_3rd/run_data.star        Schemes/3_CS_Refine_Cycle/1807_Refine3D_polish_3rd/run_data.star 
CS_class3d_refine_map   Schemes/3_CS_Refine_Cycle/1807_Refine3D_polish_3rd/run_class001.mrc     Schemes/3_CS_Refine_Cycle/1807_Refine3D_polish_3rd/run_class001.mrc
CS_imported_mask3d      Schemes/2_CS_Init_Refine3D/1202_Import_mask3d/$$CS_mask3d_name          Schemes/2_CS_Init_Refine3D/1202_Import_mask3d/$$CS_mask3d_name
CS_mask3d_name          mask3d_emd_22963_centerd_apix1o0375_d256.mrc                            mask3d_emd_22963_centerd_apix1o0375_d256.mrc
CS_sym_name_refine3d_apo      C1                     C1
resmap_exe                    ""                     ""
select_class3d_exe  "/efs/em/pyenv/versions/anaconda3-5.3.1/envs/cryolo-1.8.0/bin/python /fsx/GoToFly/SelectClass3D/gtf_relion4_run_select_class3d.py"        "/efs/em/pyenv/versions/anaconda3-5.3.1/envs/cryolo-1.8.0/bin/python /fsx/GoToFly/SelectClass3D/gtf_relion4_run_select_class3d.py"


# version 30001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
WAIT                  wait              undefined    wait_sec           undefined 
EXIT_maxtime          exit_maxtime      undefined    maxtime_hr         undefined
HAS_prev_proc_exited  bool=file_exists  has_exited   prev_proc_exited   undefined
EXIT                  exit              undefined    undefined          undefined


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
WAIT                             1900_Class3D_noalign          1   EXIT_maxtime          CS_wait_prev_proc
EXIT_maxtime                     HAS_prev_proc_exited          0   undefined             undefined 
HAS_prev_proc_exited             WAIT                          1   1900_Class3D_noalign  has_exited
1900_Class3D_noalign             2000_External_select3d        0   undefined             undefined 
2000_External_select3d           2100_Refine3D_global          0   undefined             undefined
2100_Refine3D_global             2200_PostProcess_global       0   undefined             undefined 
2200_PostProcess_global          2300_Refine3D_local           0   undefined             undefined 
2300_Refine3D_local              2400_PostProcess_local        0   undefined             undefined
2400_PostProcess_local           2500_LocalRes                 0   undefined             undefined
2500_LocalRes                    EXIT                          0   undefined             undefined  
