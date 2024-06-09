
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/040_GTF_Class2D_PMDs/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
cur_nr_parts                               0               0 
pre_nr_parts                               0               0 
GTF_lbin_class2d_pmds_min_nr_parts    100000          100000 
GTF_lbin_class2d_pmds_base_pmd           100             100 
GTF_lbin_class2d_pmds_pad_min              0               0 
GTF_lbin_class2d_pmds_pad_max            120             120 
GTF_lbin_class2d_pmds_pad_step            20              20 
base_pmd                                   0               0 
pre_pmd_pad                                0               0 
cur_pmd_pad                                0               0 
cur_pmd                                    0               0 
active_cls2d_type                          0               0 
cls2d_type_incr                            1               1 
cls2d_type_vdam                            0               0 
cls2d_type_em                              1               1 
SS_comm_class2d_classes                  200             200 
GTF_lbin_class2d_pmds_rank_thresh          0.05            0.05 
wait_sec                                 180             180 
maxtime_hr                                96              96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
GTF_lbin_class2d_pmds_do_limit_parts    0        0 
has_all_parts                           0        0 
has_larger_nr_parts                     0        0 
has_required_nr_parts                   0        0 
is_same_cls2d_type                      1        1 
has_subceeded_pmd_pad_min               0        0 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
GTF_lbin_class2d_pmds_in_parts_star    Schemes/030_GTF_Create_Stack/030060_Select_rm_bars_xy/particles.star               Schemes/030_GTF_Create_Stack/030060_Select_rm_bars_xy/particles.star 
split_parts                            Schemes/050_GTF_AbInitReconst3D/050010_Select_split_parts/particles_split1.star    Schemes/050_GTF_AbInitReconst3D/050010_Select_split_parts/particles_split1.star 
selected_parts                         ""                                                                                 "" 
cls2d_vdam_optimiser                   Schemes/040_GTF_Class2D_PMDs/040020_Class2D_VDAM/run_it200_optimiser.star          Schemes/040_GTF_Class2D_PMDs/040020_Class2D_VDAM/run_it200_optimiser.star 
cls2d_em_optimiser                     Schemes/040_GTF_Class2D_PMDs/040030_Class2D_EM/run_it025_optimiser.star            Schemes/040_GTF_Class2D_PMDs/040030_Class2D_EM/run_it025_optimiser.star 
active_sort2d_optimiser                ""                                                                                 "" 
particles                              particles                                                                          particles 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_all_parts            bool=file_exists      has_all_parts                GTF_lbin_class2d_pmds_in_parts_star    undefined 
INIT_selected_parts      string=set            selected_parts               GTF_lbin_class2d_pmds_in_parts_star    undefined 
COUNT_parts              float=count_images    cur_nr_parts                 GTF_lbin_class2d_pmds_in_parts_star    particles 
HAS_parts_increased      bool=gt               has_larger_nr_parts          cur_nr_parts                           pre_nr_parts 
SET_pre_nr_parts         float=set             pre_nr_parts                 cur_nr_parts                           undefined 
HAS_required_nr_parts    bool=ge               has_required_nr_parts        cur_nr_parts                           GTF_lbin_class2d_pmds_min_nr_parts 
UPDATE_selected_parts    string=set            selected_parts               split_parts                            undefined 
INIT_base_pmd            float=set             base_pmd                     GTF_lbin_class2d_pmds_base_pmd         undefined 
INIT_cur_pmd_pad         float=set             cur_pmd_pad                  GTF_lbin_class2d_pmds_pad_max          undefined 
PLUS_cur_pmd             float=plus            cur_pmd                      base_pmd                               cur_pmd_pad 
CHECK_cls2d_type_vdam    bool=eq               is_same_cls2d_type           active_cls2d_type                      cls2d_type_vdam 
CHECK_cls2d_type_em      bool=eq               is_same_cls2d_type           active_cls2d_type                      cls2d_type_em 
SET_prev_pmd_pad         float=set             pre_pmd_pad                  cur_pmd_pad                            undefined 
SET_prev_pmd_pad         float=set             pre_pmd_pad                  cur_pmd_pad                            undefined 
ACTIVATE_sort2d_vdam     string=set            active_sort2d_optimiser      cls2d_vdam_optimiser                   undefined 
ACTIVATE_sort2d_em       string=set            active_sort2d_optimiser      cls2d_em_optimiser                     undefined 
SET_prev_pmd_pad         float=set             pre_pmd_pad                  cur_pmd_pad                            undefined 
MINUS_current_pmd_pad    float=minus           cur_pmd_pad                  pre_pmd_pad                            GTF_lbin_class2d_pmds_pad_step 
CHECK_pmd_pad_min        bool=lt               has_subceeded_pmd_pad_min    cur_pmd_pad                            GTF_lbin_class2d_pmds_pad_min 
INCR_active_cls2d_type   float=plus            active_cls2d_type            cls2d_type_incr                        active_cls2d_type 
WAIT                     wait                  undefined                    wait_sec                               undefined 
EXIT_maxtime             exit_maxtime          undefined                    maxtime_hr                             undefined 
EXIT                     exit                  undefined                    undefined                              undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
0401_Select_split_stack     0401_Select_split_stack     new            0 
0402_Class2d_vdam           0402_Class2d_vdam           new            0 
0403_Class2d_em             0403_Class2d_em             new            0 
0404_Select_sort2d          0404_Select_sort2d          new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                        EXIT_maxtime                0    undefined                  undefined 
EXIT_maxtime                HAS_all_parts               0    undefined                  undefined 
HAS_all_parts               WAIT                        1    INIT_selected_parts        has_all_parts 
INIT_selected_parts         INIT_base_pmd               1    COUNT_parts                GTF_lbin_class2d_pmds_do_limit_parts 
COUNT_parts                 HAS_parts_increased         0    undefined                  undefined 
HAS_parts_increased         WAIT                        1    SET_pre_nr_parts           has_larger_nr_parts 
SET_pre_nr_parts            HAS_required_nr_parts       0    undefined                  undefined 
HAS_required_nr_parts       WAIT                        1    0401_Select_split_stack    has_required_nr_parts 
0401_Select_split_stack     UPDATE_selected_parts       0    undefined                  undefined 
UPDATE_selected_parts       INIT_base_pmd               0    undefined                  undefined 
INIT_base_pmd               INIT_cur_pmd_pad            0    undefined                  undefined 
INIT_cur_pmd_pad            PLUS_cur_pmd                0    undefined                  undefined 
PLUS_cur_pmd                CHECK_cls2d_type_vdam       0    undefined                  undefined 
CHECK_cls2d_type_vdam       CHECK_cls2d_type_em         1    0402_Class2d_vdam          is_same_cls2d_type 
CHECK_cls2d_type_em         EXIT                        1    0403_Class2d_em            is_same_cls2d_type 
0402_Class2d_vdam           ACTIVATE_sort2d_vdam        0    undefined                  undefined 
0403_Class2d_em             ACTIVATE_sort2d_em          0    undefined                  undefined 
ACTIVATE_sort2d_vdam        0404_Select_sort2d          0    undefined                  undefined 
ACTIVATE_sort2d_em          0404_Select_sort2d          0    undefined                  undefined 
0404_Select_sort2d          SET_prev_pmd_pad            0    undefined                  undefined 
SET_prev_pmd_pad            MINUS_current_pmd_pad       0    undefined                  undefined 
MINUS_current_pmd_pad       CHECK_pmd_pad_min           0    undefined                  undefined 
CHECK_pmd_pad_min           PLUS_cur_pmd                1    INCR_active_cls2d_type     has_subceeded_pmd_pad_min 
INCR_active_cls2d_type      INIT_base_pmd               0    undefined                  undefined 
