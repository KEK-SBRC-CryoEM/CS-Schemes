
# version 30001

data_scheme_general

_rlnSchemeName                       Schemes/13_CS_Clean_Stack_3D/
_rlnSchemeCurrentNodeName            WAIT
 

# version 30001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CS_class3d_pmd           169             169
CS_nr_3d_classes           3               3  
CS_refine3d_pmd          169             169
CS_angpix                  2.49            2.49
CS_low_pass                7.47            7.47
maxtime_hr                96              96
wait_sec                 180             180 

# version 30001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
CS_use_mask3d_class3d    1      1
CS_use_mask3d_refine3d   1      1
CS_wait_prev_proc        1      1
has_exited               0      0


# version 30001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
prev_proc_exited        Schemes/12_CS_AbInitReconst3D/RELION_JOB_EXIT_SUCCESS                            Schemes/12_CS_AbInitReconst3D/RELION_JOB_EXIT_SUCCESS
imported_ref3d          Schemes/13_CS_Clean_Stack_3D/0601_Import_ref3d/$$CS_ref3d_name                   Schemes/13_CS_Clean_Stack_3D/0601_Import_ref3d/$$CS_ref3d_name
imported_mask3d         Schemes/13_CS_Clean_Stack_3D/0602_Import_mask3d/$$CS_mask3d_name                 Schemes/13_CS_Clean_Stack_3D/0602_Import_mask3d/$$CS_mask3d_name
CS_selected_parts       Schemes/11_CS_Create_Stack/0303_Select_split_stack_parts/particles_split1.star   Schemes/11_CS_Create_Stack/0303_Select_split_stack_parts/particles_split1.star
CS_ref3d_path           /fsx/Inputs_Map/ref3d_emd_21992_additional_3_align_manu_tm_lpf7o47_apix2o49_d112.mrc /fsx/Inputs_Map/ref3d_emd_21992_additional_3_align_manu_tm_lpf7o47_apix2o49_d112.mrc
CS_mask3d_path          /fsx/Inputs_Map/mask3d_emd_21992_additional_3_align_manu_tm_lpf7o47_apix2o49_d112.mrc /fsx/Inputs_Map/mask3d_emd_21992_additional_3_align_manu_tm_lpf7o47_apix2o49_d112.mrc
CS_ref3d_name           ref3d_emd_21992_additional_3_align_manu_tm_lpf7o47_apix2o49_d112.mrc    ref3d_emd_21992_additional_3_align_manu_tm_lpf7o47_apix2o49_d112.mrc
CS_mask3d_name          mask3d_emd_21992_additional_3_align_manu_tm_lpf7o47_apix2o49_d112.mrc   mask3d_emd_21992_additional_3_align_manu_tm_lpf7o47_apix2o49_d112.mrc
mask3d_cls3d               ""                                             ""
mask3d_ref3d               ""                                             ""
CS_sym_name_class3d        C1                                             C1
CS_sym_name_refine3d_apo   C1                                             C1 
select_class3d_exe   "/efs/em/pyenv/versions/anaconda3-5.3.1/envs/cryolo-1.8.0/bin/python /fsx/GoToFly/SelectClass3D/gtf_relion4_run_select_class3d.py"        "/efs/em/pyenv/versions/anaconda3-5.3.1/envs/cryolo-1.8.0/bin/python /fsx/GoToFly/SelectClass3D/gtf_relion4_run_select_class3d.py"


# version 30001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
EXIT                  exit                 undefined         undefined               undefined 
EXIT_maxtime          exit_maxtime         undefined         maxtime_hr              undefined 
HAS_prev_proc_exited  bool=file_exists     has_exited        prev_proc_exited        undefined
SET_mask3d_class3d    string=set           mask3d_cls3d      imported_mask3d         undefined
SET_mask3d_refine3d   string=set           mask3d_ref3d      imported_mask3d         undefined
WAIT                  wait                 undefined         wait_sec                undefined 
 

# version 30001

data_scheme_jobs

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
0601_Import_ref3d                 0601_Import_ref3d                new            0
0602_Import_mask3d                0602_Import_mask3d               new            0
0700_Class3D                      0700_Class3D                     new            0 
0800_External_select3d            0800_External_select3d           new            0 
0900_Refine3D                     0900_Refine3D                    new            0  
1000_PostProcess                  1000_PostProcess                 new            0 
 

# version 30001

data_scheme_edges

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                              0601_Import_ref3d                1  EXIT_maxtime          CS_wait_prev_proc
EXIT_maxtime                      HAS_prev_proc_exited             0  undefined             undefined
HAS_prev_proc_exited              WAIT                             1  0601_Import_ref3d     has_exited
0601_Import_ref3d                 0602_Import_mask3d               0  undefined             undefined
0602_Import_mask3d                0700_Class3D                     1  SET_mask3d_class3d    CS_use_mask3d_class3d
SET_mask3d_class3d                0700_Class3D                     0  undefined             undefined
0700_Class3D                      0800_External_select3d           0  undefined             undefined 
0800_External_select3d            0900_Refine3D                    1  SET_mask3d_refine3d   CS_use_mask3d_refine3d  
SET_mask3d_refine3d               0900_Refine3D                    0  undefined             undefined
0900_Refine3D                     1000_PostProcess                 0  undefined             undefined 
1000_PostProcess                  EXIT                             0  undefined             undefined 
