
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
GTF_lbin_abinit3d_min_nr_parts           XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_lbin_abinit3d_clean2d_cycles_max     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
cur_nr_parts                             0                             0 
pre_nr_parts                             0                             0 
cur_cls2d_cycles                         1                             1 
cls2d_cycle_incr                         1                             1 
SS_comm_class2d_classes                  XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_class2d_pmd                      XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_lbin_nr_pool                     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_lbin_abinit3d_clean2d_rank_thresh    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_lbin_abinit3d_rank_thresh            XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_lbin_abinit3d_pmd                    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
wait_sec                                 180                           180 
maxtime_hr                               96                            96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
GTF_lbin_abinit3d_wait_prev_proc      XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
has_exited                            0                             0 
GTF_lbin_abinit3d_do_limit_parts      XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
has_all_parts                         0                             0 
has_larger_nr_parts                   0                             0 
has_required_nr_parts                 0                             0 
do_cls2d_cycle                        0                             0 
SS_comm_lbin_do_preread_images        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_lbin_abinit3d_do_run_C1           XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
GTF_lbin_abinit3d_prev_proc_exited    XXX_SSE_REPLACE_SAMPLE_XXX                                                         XXX_SSE_REPLACE_SAMPLE_XXX 
GTF_lbin_abinit3d_in_parts_star       XXX_SSE_REPLACE_SAMPLE_XXX                                                         XXX_SSE_REPLACE_SAMPLE_XXX 
split_parts                           Schemes/050_GTF_AbInitReconst3D/050010_Select_split_parts/particles_split1.star    Schemes/050_GTF_AbInitReconst3D/050010_Select_split_parts/particles_split1.star 
selected_parts                        ""                                                                                 "" 
cls2d_cycle_parts_temp                Schemes/050_GTF_AbInitReconst3D/050030_Select_clean2d_parts/particles.star         Schemes/050_GTF_AbInitReconst3D/050030_Select_clean2d_parts/particles.star 
cls2d_cycle_parts                     ""                                                                                 "" 
GTF_lbin_abinit3d_sym_name            XXX_SSE_REPLACE_SAMPLE_XXX                                                         XXX_SSE_REPLACE_SAMPLE_XXX 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_prev_proc_exited           bool=file_exists      has_exited               GTF_lbin_abinit3d_prev_proc_exited    undefined 
HAS_all_parts                  bool=file_exists      has_all_parts            GTF_lbin_abinit3d_in_parts_star       undefined 
INIT_selected_parts            string=set            selected_parts           GTF_lbin_abinit3d_in_parts_star       undefined 
COUNT_parts                    float=count_images    cur_nr_parts             GTF_lbin_abinit3d_in_parts_star       particles 
HAS_parts_increased            bool=gt               has_larger_nr_parts      cur_nr_parts                          pre_nr_parts 
SET_pre_nr_parts               float=set             pre_nr_parts             cur_nr_parts                          undefined 
HAS_required_nr_parts          bool=ge               has_required_nr_parts    cur_nr_parts                          GTF_lbin_abinit3d_min_nr_parts 
UPDATE_selected_parts_cls2d    string=set            selected_parts           split_parts                           undefined 
CHECK_max_cls2d_cycles         bool=le               do_cls2d_cycle           cur_cls2d_cycles                      GTF_lbin_abinit3d_clean2d_cycles_max 
INIT_cls2d_cycle_parts         string=set            cls2d_cycle_parts        selected_parts                        undefined 
INCR_cur_cls2d_cycles          float=plus            cur_cls2d_cycles         cls2d_cycle_incr                      cur_cls2d_cycles 
UPDATE_cls2d_cycle_parts       string=set            cls2d_cycle_parts        cls2d_cycle_parts_temp                undefined 
WAIT                           wait                  undefined                wait_sec                              undefined 
EXIT_maxtime                   exit_maxtime          undefined                maxtime_hr                            undefined 
EXIT                           exit                  undefined                undefined                             undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
050010_Select_split_parts       050010_Select_split_parts       new            0 
050020_Class2D_EM               050020_Class2D_EM               new            0 
050030_Select_clean2d_parts     050030_Select_clean2d_parts     new            0 
050040_Class2D_EM               050040_Class2D_EM               new            0 
050050_Select_abinit3d_parts    050050_Select_abinit3d_parts    new            0 
050060_InitialModel             050060_InitialModel             new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                            HAS_all_parts                   1    EXIT_maxtime                 GTF_lbin_abinit3d_wait_prev_proc 
EXIT_maxtime                    HAS_prev_proc_exited            0    undefined                    undefined 
HAS_prev_proc_exited            WAIT                            1    HAS_all_parts                has_exited 
HAS_all_parts                   WAIT                            1    INIT_selected_parts          has_all_parts 
INIT_selected_parts             INIT_cls2d_cycle_parts          1    COUNT_parts                  GTF_lbin_abinit3d_do_limit_parts 
COUNT_parts                     HAS_parts_increased             0    undefined                    undefined 
HAS_parts_increased             WAIT                            1    SET_pre_nr_parts             has_larger_nr_parts 
SET_pre_nr_parts                HAS_required_nr_parts           0    undefined                    undefined 
HAS_required_nr_parts           WAIT                            1    050010_Select_split_parts    has_required_nr_parts 
050010_Select_split_parts       UPDATE_selected_parts_cls2d     0    undefined                    undefined 
UPDATE_selected_parts_cls2d     INIT_cls2d_cycle_parts          0    undefined                    undefined 
INIT_cls2d_cycle_parts          CHECK_max_cls2d_cycles          0    undefined                    undefined 
CHECK_max_cls2d_cycles          050040_Class2D_EM               1    050020_Class2D_EM            do_cls2d_cycle 
050020_Class2D_EM               050030_Select_clean2d_parts     0    undefined                    undefined 
050030_Select_clean2d_parts     UPDATE_cls2d_cycle_parts        0    undefined                    undefined 
UPDATE_cls2d_cycle_parts        INCR_cur_cls2d_cycles           0    undefined                    undefined 
INCR_cur_cls2d_cycles           CHECK_max_cls2d_cycles          0    undefined                    undefined 
050040_Class2D_EM               050050_Select_abinit3d_parts    0    undefined                    undefined 
050050_Select_abinit3d_parts    050060_InitialModel             0    undefined                    undefined 
050060_InitialModel             EXIT                            0    undefined                    undefined 
