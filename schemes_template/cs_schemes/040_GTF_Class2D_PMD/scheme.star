
# version 30001

data_scheme_general

_rlnSchemeName                       Schemes/040_GTF_Class2D_PMD/
_rlnSchemeCurrentNodeName            WAIT
 

# version 30001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
GTF_adhoc_pmd     0.000000     0.000000 
GTF_cryolo_pmd  100.000   100.000 
GTF_min_nr_parts 100000.000   100000.000 
GTF_pmd_pad_step  20.000000     20.000000 
GTF_pmd_pad_min    0.000000      0.000000 
GTF_pmd_pad_max  120.000000    120.000000 
GTF_nr_2d_classes  200.000    200.000 
GTF_rank_threshold      0.050000     0.050000 
maxtime_hr    96.000000    96.000000 
wait_sec   180.000000   180.000000
current_nr_parts      0.000000     0.000000 
base_pmd     0.000000     0.000000 
prev_pmd_pad     0.000000     0.000000 
current_pmd_pad     0.000000     0.000000 
current_pmd  0.000000     0.000000 


# version 30001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
GTF_wait_prev_proc      1       1
has_exited             0       0
do_class2d 0 0
use_adhoc_pmd 0 0
has_larger_nr_parts            0            0 
has_subceeded_pmd_pad_min            0            0 
GTF_use_adhoc_pmd 0 0

# version 30001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
prev_proc_exited      Schemes/030_GTF_Create_Stack/RELION_JOB_EXIT_SUCCESS                       Schemes/030_GTF_Create_Stack/RELION_JOB_EXIT_SUCCESS 
selected_parts        Schemes/030_GTF_Create_Stack/select_rm_bars_xy/particles.star Schemes/030_GTF_Create_Stack/select_rm_bars_xy/particles.star
particles  particles  particles

# version 30001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
WAIT                   wait                undefined                 wait_sec           undefined 
EXIT_maxtime           exit_maxtime        undefined                 maxtime_hr         undefined 
HAS_prev_proc_exited   bool=file_exists    has_exited                prev_proc_exited   undefined 
COUNT_parts            float=count_images  current_nr_parts          selected_parts     particles
CHECK_do_class2d       bool=ge             do_class2d                current_nr_parts   GTF_min_nr_parts
CHECK_use_adhoc_pmd    bool=set            use_adhoc_pmd             GTF_use_adhoc_pmd  undefined
INIT_base_pmd_cryolo   float=set           base_pmd                  GTF_cryolo_pmd     undefined
INIT_base_pmd_adhoc    float=set           base_pmd                  GTF_adhoc_pmd      undefined
INIT_current_pmd_pad   float=set           current_pmd_pad           GTF_pmd_pad_max    undefined
PLUS_current_pmd       float=plus          current_pmd               base_pmd           current_pmd_pad 
SET_prev_pmd_pad       float=set           prev_pmd_pad              current_pmd_pad    undefined 
MINUS_current_pmd_pad  float=minus         current_pmd_pad           prev_pmd_pad       GTF_pmd_pad_step 
Check_pmd_pad_min      bool=lt             has_subceeded_pmd_pad_min current_pmd_pad    GTF_pmd_pad_min 
EXIT                   exit                undefined                 undefined          undefined 

# version 30001

data_scheme_jobs

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
0401_Select_split_stack   0401_Select_split_stack        new            0 
0402_Class2d_vdam         0402_Class2d_vdam              new            0 
0403_Select_class2d_vdam  0403_Select_class2d_vdam       new            0 
0404_Class2D_em           0404_Class2D_em                new            0 
0405_Select_class2d_em    0405_Select_class2d_em         new            0 


# version 30001

data_scheme_edges

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                      COUNT_parts                  1  EXIT_maxtime             GTF_wait_prev_proc 
EXIT_maxtime              HAS_prev_proc_exited         0  undefined                undefined 
HAS_prev_proc_exited      WAIT                         1  COUNT_parts              has_exited  
COUNT_parts               CHECK_do_class2d             0  undefined                undefined 
CHECK_do_class2d          WAIT                         1  0401_Select_split_stack  do_class2d 
0401_Select_split_stack   CHECK_use_adhoc_pmd          0  undefined                undefined 
CHECK_use_adhoc_pmd       INIT_base_pmd_cryolo         1  INIT_base_pmd_adhoc      use_adhoc_pmd
INIT_base_pmd_cryolo      INIT_current_pmd_pad         0  undefined                undefined 
INIT_base_pmd_adhoc       INIT_current_pmd_pad         0  undefined                undefined 
INIT_current_pmd_pad      PLUS_current_pmd             0  undefined                undefined 
PLUS_current_pmd          0402_Class2d_vdam            0  undefined                undefined 
0402_Class2d_vdam         0403_Select_class2d_vdam     0  undefined                undefined 
0403_Select_class2d_vdam  0404_Class2D_em              0  undefined                undefined
0404_Class2D_em           0405_Select_class2d_em       0  undefined                undefined 
0405_Select_class2d_em    SET_prev_pmd_pad             0  undefined                undefined 
SET_prev_pmd_pad          MINUS_current_pmd_pad        0  undefined                undefined 
MINUS_current_pmd_pad     Check_pmd_pad_min            0  undefined                undefined 
Check_pmd_pad_min         PLUS_current_pmd             1  EXIT                     has_subceeded_pmd_pad_min
