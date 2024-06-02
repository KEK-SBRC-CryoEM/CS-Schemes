
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/050_GTF_AbInitReconst3D/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
GTF_lbin_abinit3d_min_nr_parts            4000             4000 
GTF_lbin_abinit3d_clean2d_cycles_max         1                1 
cur_nr_parts                                 0                0 
pre_nr_parts                                 0                0 
cur_cls2d_cycles                             1                1 
cls2d_cycle_incr                             1                1 
SS_comm_class2d_classes                    100              100 
SS_comm_class2d_pmd                        200              200 
GTF_lbin_abinit3d_clean2d_rank_thresh        0.06             0.06 
GTF_lbin_abinit3d_rank_thresh                0.26             0.26 
GTF_lbin_abinit3d_pmd                      200              200 
wait_sec                                   180              180 
maxtime_hr                                  96               96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
GTF_lbin_abinit3d_do_limit_parts    0        0 
has_all_parts                       0        0 
has_larger_nr_parts                 0        0 
has_required_nr_parts               0        0 
do_cls2d_cycle                      0        0 
GTF_lbin_abinit3d_do_run_C1         1        1 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
GTF_lbin_abinit3d_in_parts_star    Schemes/030_GTF_Create_Stack/0302_Select_rm_bars_xy/particles.star               Schemes/030_GTF_Create_Stack/0302_Select_rm_bars_xy/particles.star 
split_parts                        Schemes/050_GTF_AbInitReconst3D/0400_Select_split_parts/particles_split1.star    Schemes/050_GTF_AbInitReconst3D/0400_Select_split_parts/particles_split1.star 
selected_parts                     ""                                                                               "" 
cls2d_cycle_parts_temp             Schemes/050_GTF_AbInitReconst3D/0402_Select_class2d/particles.star               Schemes/050_GTF_AbInitReconst3D/0402_Select_class2d/particles.star 
cls2d_cycle_parts                  ""                                                                               "" 
GTF_lbin_abinit3d_sym_name         C1                                                                               C1 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_all_parts                  bool=file_exists      has_all_parts            GTF_lbin_abinit3d_in_parts_star    undefined 
INIT_selected_parts            string=set            selected_parts           GTF_lbin_abinit3d_in_parts_star    undefined 
COUNT_parts                    float=count_images    cur_nr_parts             GTF_lbin_abinit3d_in_parts_star    particles 
HAS_parts_increased            bool=gt               has_larger_nr_parts      cur_nr_parts                       pre_nr_parts 
SET_pre_nr_parts               float=set             pre_nr_parts             cur_nr_parts                       undefined 
HAS_required_nr_parts          bool=ge               has_required_nr_parts    cur_nr_parts                       GTF_lbin_abinit3d_min_nr_parts 
UPDATE_selected_parts_cls2d    string=set            selected_parts           split_parts                        undefined 
CHECK_max_cls2d_cycles         bool=le               do_cls2d_cycle           cur_cls2d_cycles                   GTF_lbin_abinit3d_clean2d_cycles_max 
INIT_cls2d_cycle_parts         string=set            cls2d_cycle_parts        selected_parts                     undefined 
INCR_cur_cls2d_cycles          float=plus            cur_cls2d_cycles         cls2d_cycle_incr                   cur_cls2d_cycles 
UPDATE_cls2d_cycle_parts       string=set            cls2d_cycle_parts        cls2d_cycle_parts_temp             undefined 
WAIT                           wait                  undefined                wait_sec                           undefined 
EXIT_maxtime                   exit_maxtime          undefined                maxtime_hr                         undefined 
EXIT                           exit                  undefined                undefined                          undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
0400_Select_split_parts    0400_Select_split_parts    new            0 
0401_Class2D_em            0401_Class2D_em            new            0 
0402_Select_class2d        0402_Select_class2d        new            0 
0403_Class2D_em            0403_Class2D_em            new            0 
0404_Select_class2d        0404_Select_class2d        new            0 
0500_InitialModel          0500_InitialModel          new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                           EXIT_maxtime                   0    undefined                  undefined 
EXIT_maxtime                   HAS_all_parts                  0    undefined                  undefined 
HAS_all_parts                  WAIT                           1    INIT_selected_parts        has_all_parts 
INIT_selected_parts            INIT_cls2d_cycle_parts         1    COUNT_parts                GTF_lbin_abinit3d_do_limit_parts 
COUNT_parts                    HAS_parts_increased            0    undefined                  undefined 
HAS_parts_increased            WAIT                           1    SET_pre_nr_parts           has_larger_nr_parts 
SET_pre_nr_parts               HAS_required_nr_parts          0    undefined                  undefined 
HAS_required_nr_parts          WAIT                           1    0400_Select_split_parts    has_required_nr_parts 
0400_Select_split_parts        UPDATE_selected_parts_cls2d    0    undefined                  undefined 
UPDATE_selected_parts_cls2d    INIT_cls2d_cycle_parts         0    undefined                  undefined 
INIT_cls2d_cycle_parts         CHECK_max_cls2d_cycles         0    undefined                  undefined 
CHECK_max_cls2d_cycles         0403_Class2D_em                1    0401_Class2D_em            do_cls2d_cycle 
0401_Class2D_em                0402_Select_class2d            0    undefined                  undefined 
0402_Select_class2d            UPDATE_cls2d_cycle_parts       0    undefined                  undefined 
UPDATE_cls2d_cycle_parts       INCR_cur_cls2d_cycles          0    undefined                  undefined 
INCR_cur_cls2d_cycles          CHECK_max_cls2d_cycles         0    undefined                  undefined 
0403_Class2D_em                0404_Select_class2d            0    undefined                  undefined 
0404_Select_class2d            0500_InitialModel              0    undefined                  undefined 
0500_InitialModel              EXIT                           0    undefined                  undefined 
