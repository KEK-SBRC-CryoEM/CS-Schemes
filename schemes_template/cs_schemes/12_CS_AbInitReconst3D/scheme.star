
# version 30001

data_scheme_general

_rlnSchemeName                       Schemes/12_CS_AbInitReconst3D/
_rlnSchemeCurrentNodeName            WAIT
 

# version 30001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CS_class2d_pmd             153        153
CS_abinit3D_pmd            153        153 
CS_nr_2d_classes           200        200 
CS_rank_threshold_class2d    0.06       0.06
CS_rank_threshold_abinit3D   0.26       0.26
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
prev_proc_exited        Schemes/11_CS_Create_Stack/RELION_JOB_EXIT_SUCCESS                               Schemes/11_CS_Create_Stack/RELION_JOB_EXIT_SUCCESS 
CS_selected_parts       Schemes/11_CS_Create_Stack/0303_Select_split_stack_parts/particles_split1.star   Schemes/11_CS_Create_Stack/0303_Select_split_stack_parts/particles_split1.star 
CS_sym_name_initial     C1                       C1
python_exe              /efs/em/pyenv/versions/anaconda3-5.3.1/envs/topaz/bin/python                     /efs/em/pyenv/versions/anaconda3-5.3.1/envs/topaz/bin/python


# version 30001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
EXIT                   exit                 undefined            undefined            undefined 
EXIT_maxtime           exit_maxtime         undefined            maxtime_hr           undefined 
HAS_prev_proc_exited   bool=file_exists     has_exited           prev_proc_exited     undefined
WAIT                   wait                 undefined            wait_sec             undefined 
 

# version 30001

data_scheme_jobs

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4  
0401_Class2D_em                0401_Class2D_em             new            0  
0402_Select_class2d            0402_Select_class2d         new            0 
0403_Class2D_em                0403_Class2D_em             new            0
0404_Select_class2d            0404_Select_class2d         new            0
0500_InitialModel              0500_InitialModel           new            0
 

# version 30001

data_scheme_edges

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                            0401_Class2D_em                  1  EXIT_maxtime         CS_wait_prev_proc
EXIT_maxtime                    HAS_prev_proc_exited             0  undefined            undefined 
HAS_prev_proc_exited            WAIT                             1  0401_Class2D_em      has_exited 
0401_Class2D_em                 0402_Select_class2d              0  undefined            undefined 
0402_Select_class2d             0403_Class2D_em                  0  undefined            undefined 
0403_Class2D_em                 0404_Select_class2d              0  undefined            undefined 
0404_Select_class2d             0500_InitialModel                0  undefined            undefined 
0500_InitialModel               EXIT                             0  undefined            undefined 
