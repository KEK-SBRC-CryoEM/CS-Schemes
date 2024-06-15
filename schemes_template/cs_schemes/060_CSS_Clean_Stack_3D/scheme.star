
# version 30001 

data_scheme_general 

_rlnSchemeName                       Schemes/060_CSS_Clean_Stack_3D/ 
_rlnSchemeCurrentNodeName            WAIT 


# version 30001 

data_scheme_floats 

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
cur_nr_parts                               0                             0 
pre_nr_parts                               0                             0 
CSS_lbin_center3d_min_nr_parts             XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_clean2d_cycles_max       XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
cur_cls2d_cycles                           1                             1 
cls2d_cycle_incr                           1                             1 
SS_comm_class2d_classes                    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_class2d_pmd                        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_lbin_nr_pool                       XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_clean2d_rank_thresh      XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_class3d_conts_max        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_class3d_iter_step        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_class3d_offset_factor    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
cls3d_cont_incr                            1                             1 
cur_cls3d_conts                            1                             1 
cls3d_cont_iter                            0                             0 
cls3d_offset_range_default                 5                             5 
cls3d_offset_step_default                  1                             1 
cls3d_offset_factor_step                   2                             2 
cls3d_cont_offset_factor                   0                             0 
cls3d_cont_offset_range                    0                             0 
cls3d_cont_offset_step                     0                             0 
CSS_lbin_center3d_class3d_lpf              XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_class3d_classes          XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_optimal_pmd                        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_lbin_angpix                        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_postproc_adhoc_lpf       XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
wait_sec                                   180                           180 
maxtime_hr                                 96                            96 


# version 30001 

data_scheme_bools 

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
SS_comm_wait_prev_proc                       XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
has_exited                                   0                             0 
has_all_parts                                0                             0 
has_larger_nr_parts                          0                             0 
has_required_nr_parts                        0                             0 
CSS_lbin_center3d_do_limit_parts             0                             0 
do_cls2d_cycle                               0                             0 
SS_comm_lbin_do_preread_images               XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
do_cls3d_cont                                0                             0 
CSS_lbin_center3d_class3d_use_mask3d         XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_class3d_do_fast_subsets    XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_refine3d_use_mask3d        XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 


# version 30001 

data_scheme_strings 

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
prev_proc_exited                        Schemes/050_GTF_AbInitReconst3D/RELION_JOB_EXIT_SUCCESS                           Schemes/050_GTF_AbInitReconst3D/RELION_JOB_EXIT_SUCCESS 
CSS_lbin_center3d_parts_star            Schemes/030_GTF_Create_Stack/030060_Select_rm_bars_xy/particles.star              Schemes/030_GTF_Create_Stack/030060_Select_rm_bars_xy/particles.star 
split_parts                             Schemes/060_CSS_Clean_Stack_3D/060010_Select_split_parts/particles_split1.star    Schemes/060_CSS_Clean_Stack_3D/060010_Select_split_parts/particles_split1.star 
selected_parts                          ""                                                                                "" 
SS_comm_lbin_ref3d_path                 XXX_SSE_REPLACE_SAMPLE_XXX                                                        XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_lbin_ref3d_name                 XXX_SSE_REPLACE_SAMPLE_XXX                                                        XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_lbin_mask3d_path                XXX_SSE_REPLACE_SAMPLE_XXX                                                        XXX_SSE_REPLACE_SAMPLE_XXX 
SS_comm_lbin_mask3d_name                XXX_SSE_REPLACE_SAMPLE_XXX                                                        XXX_SSE_REPLACE_SAMPLE_XXX 
imported_ref3d                          Schemes/060_CSS_Clean_Stack_3D/060040_Import_ref3d/$$SS_comm_lbin_ref3d_name      Schemes/060_CSS_Clean_Stack_3D/060040_Import_ref3d/$$SS_comm_lbin_ref3d_name 
imported_mask3d                         Schemes/060_CSS_Clean_Stack_3D/060050_Import_mask3d/$$SS_comm_lbin_mask3d_name    Schemes/060_CSS_Clean_Stack_3D/060050_Import_mask3d/$$SS_comm_lbin_mask3d_name 
mask3d_ref3d                            ""                                                                                "" 
mask3d_cls3d                            ""                                                                                "" 
CSS_lbin_center3d_class3d_cont_stars    XXX_SSE_REPLACE_SAMPLE_XXX                                                        XXX_SSE_REPLACE_SAMPLE_XXX 
cls2d_cycle_parts_temp                  Schemes/060_CSS_Clean_Stack_3D/060030_Select_clean2d_parts/particles.star         Schemes/060_CSS_Clean_Stack_3D/060030_Select_clean2d_parts/particles.star 
cls2d_cycle_parts                       ""                                                                                "" 
cls3d_cont_data_name                    ""                                                                                "" 
cls3d_cont_data_path                    ""                                                                                "" 
cls3d_cont_data_path_temp               Schemes/060_CSS_Clean_Stack_3D/060060_Class3D/$$cls3d_cont_data_name              Schemes/060_CSS_Clean_Stack_3D/060060_Class3D/$$cls3d_cont_data_name 
CSS_lbin_center3d_class3d_parts_star    XXX_SSE_REPLACE_SAMPLE_XXX                                                        XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_class3d_sym           XXX_SSE_REPLACE_SAMPLE_XXX                                                        XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_lbin_center3d_refine3d_sym_name     XXX_SSE_REPLACE_SAMPLE_XXX                                                        XXX_SSE_REPLACE_SAMPLE_XXX 
particles                               particles                                                                         particles 


# version 30001 

data_scheme_operators 

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
HAS_prev_proc_exited               bool=file_exists      has_exited                                 prev_proc_exited                           undefined 
HAS_all_parts                      bool=file_exists      has_all_parts                              CSS_lbin_center3d_parts_star               undefined 
INIT_selected_parts                string=set            selected_parts                             CSS_lbin_center3d_parts_star               undefined 
COUNT_parts                        float=count_images    cur_nr_parts                               CSS_lbin_center3d_parts_star               particles 
HAS_parts_increased                bool=gt               has_larger_nr_parts                        cur_nr_parts                               pre_nr_parts 
SET_pre_nr_parts                   float=set             pre_nr_parts                               cur_nr_parts                               undefined 
HAS_required_nr_parts              bool=ge               has_required_nr_parts                      cur_nr_parts                               CSS_lbin_center3d_min_nr_parts 
UPDATE_selected_parts_cls2d        string=set            selected_parts                             split_parts                                undefined 
INIT_cls2d_cycle_parts             string=set            cls2d_cycle_parts                          selected_parts                             undefined 
CHECK_max_cls2d_cycles             bool=le               do_cls2d_cycle                             cur_cls2d_cycles                           CSS_lbin_center3d_clean2d_cycles_max 
UPDATE_cls2d_cycle_parts           string=set            cls2d_cycle_parts                          cls2d_cycle_parts_temp                     undefined 
INCR_cur_cls2d_cycles              float=plus            cur_cls2d_cycles                           cls2d_cycle_incr                           cur_cls2d_cycles 
UPDATE_selected_parts_cls3d        string=set            selected_parts                             cls2d_cycle_parts                          undefined 
SET_mask3d_class3d                 string=set            mask3d_cls3d                               imported_mask3d                            undefined 
INIT_cls3d_cont_iter               float=set             cls3d_cont_iter                            CSS_lbin_center3d_class3d_iter_step        undefined 
INIT_cls3d_cont_offset_factor      float=set             cls3d_cont_offset_factor                   CSS_lbin_center3d_class3d_offset_factor    undefined 
ROUND_cls3d_cont_offset_factor     float=round           CSS_lbin_center3d_class3d_offset_factor    CSS_lbin_center3d_class3d_offset_factor    undefined 
UPDATE_cls3d_cont_offset_range     float=mult            cls3d_cont_offset_range                    cls3d_offset_range_default                 CSS_lbin_center3d_class3d_offset_factor 
UPDATE_cls3d_cont_offset_step      float=mult            cls3d_cont_offset_step                     cls3d_offset_step_default                  CSS_lbin_center3d_class3d_offset_factor 
INCR_cur_cls3d_conts               float=plus            cur_cls3d_conts                            cls3d_cont_incr                            cur_cls3d_conts 
CHECK_max_cls3d_conts              bool=le               do_cls3d_cont                              cur_cls3d_conts                            CSS_lbin_center3d_class3d_conts_max 
UPDATE_cls3d_cont_data_name        string=nth_word       cls3d_cont_data_name                       CSS_lbin_center3d_class3d_cont_stars       cur_cls3d_conts 
UPDATE_cls3d_cont_data_path        string=set            cls3d_cont_data_path                       cls3d_cont_data_path_temp                  undefined 
UPDATE_cls3d_cont_iter             float=plus            cls3d_cont_iter                            cls3d_cont_iter                            CSS_lbin_center3d_class3d_iter_step 
UPDATE_cls3d_cont_offset_factor    float=divide          CSS_lbin_center3d_class3d_offset_factor    CSS_lbin_center3d_class3d_offset_factor    cls3d_offset_factor_step 
SET_mask3d_refine3d                string=set            mask3d_ref3d                               imported_mask3d                            undefined 
WAIT                               wait                  undefined                                  wait_sec                                   undefined 
EXIT_maxtime                       exit_maxtime          undefined                                  maxtime_hr                                 undefined 
EXIT                               exit                  undefined                                  undefined                                  undefined 


# version 30001 

data_scheme_jobs 

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
060010_Select_split_parts      060010_Select_split_parts      new            0 
060020_Class2D_EM              060020_Class2D_EM              new            0 
060030_Select_clean2d_parts    060030_Select_clean2d_parts    new            0 
060040_Import_ref3d            060040_Import_ref3d            new            0 
060050_Import_mask3d           060050_Import_mask3d           new            0 
060060_Class3D                 060060_Class3D                 continue       0 
060070_External_select3d       060070_External_select3d       new            0 
060080_Refine3D_global         060080_Refine3D_global         new            0 
060090_PostProcess_global      060090_PostProcess_global      new            0 


# version 30001 

data_scheme_edges 

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                               HAS_all_parts                      1    EXIT_maxtime                   SS_comm_wait_prev_proc 
EXIT_maxtime                       HAS_prev_proc_exited               0    undefined                      undefined 
HAS_prev_proc_exited               WAIT                               1    HAS_all_parts                  has_exited 
HAS_all_parts                      WAIT                               1    INIT_selected_parts            has_all_parts 
INIT_selected_parts                INIT_cls2d_cycle_parts             1    COUNT_parts                    CSS_lbin_center3d_do_limit_parts 
COUNT_parts                        HAS_parts_increased                0    undefined                      undefined 
HAS_parts_increased                WAIT                               1    SET_pre_nr_parts               has_larger_nr_parts 
SET_pre_nr_parts                   HAS_required_nr_parts              0    undefined                      undefined 
HAS_required_nr_parts              WAIT                               1    060010_Select_split_parts      has_required_nr_parts 
060010_Select_split_parts          UPDATE_selected_parts_cls2d        0    undefined                      undefined 
UPDATE_selected_parts_cls2d        INIT_cls2d_cycle_parts             0    undefined                      undefined 
INIT_cls2d_cycle_parts             CHECK_max_cls2d_cycles             0    undefined                      undefined 
CHECK_max_cls2d_cycles             UPDATE_selected_parts_cls3d        1    060020_Class2D_EM              do_cls2d_cycle 
060020_Class2D_EM                  060030_Select_clean2d_parts        0    undefined                      undefined 
060030_Select_clean2d_parts        UPDATE_cls2d_cycle_parts           0    undefined                      undefined 
UPDATE_cls2d_cycle_parts           INCR_cur_cls2d_cycles              0    undefined                      undefined 
INCR_cur_cls2d_cycles              CHECK_max_cls2d_cycles             0    undefined                      undefined 
UPDATE_selected_parts_cls3d        060040_Import_ref3d                0    undefined                      undefined 
060040_Import_ref3d                060050_Import_mask3d               0    undefined                      undefined 
060050_Import_mask3d               INIT_cls3d_cont_iter               1    SET_mask3d_class3d             CSS_lbin_center3d_class3d_use_mask3d 
SET_mask3d_class3d                 INIT_cls3d_cont_iter               0    undefined                      undefined 
INIT_cls3d_cont_iter               INIT_cls3d_cont_offset_factor      0    undefined                      undefined 
INIT_cls3d_cont_offset_factor      ROUND_cls3d_cont_offset_factor     0    undefined                      undefined 
ROUND_cls3d_cont_offset_factor     UPDATE_cls3d_cont_offset_range     0    undefined                      undefined 
UPDATE_cls3d_cont_offset_range     UPDATE_cls3d_cont_offset_step      0    undefined                      undefined 
UPDATE_cls3d_cont_offset_step      060060_Class3D                     0    undefined                      undefined 
060060_Class3D                     INCR_cur_cls3d_conts               0    undefined                      undefined 
INCR_cur_cls3d_conts               CHECK_max_cls3d_conts              0    undefined                      undefined 
CHECK_max_cls3d_conts              060070_External_select3d           1    UPDATE_cls3d_cont_data_name    do_cls3d_cont 
UPDATE_cls3d_cont_data_name        UPDATE_cls3d_cont_data_path        0    undefined                      undefined 
UPDATE_cls3d_cont_data_path        UPDATE_cls3d_cont_iter             0    undefined                      undefined 
UPDATE_cls3d_cont_iter             UPDATE_cls3d_cont_offset_factor    0    undefined                      undefined 
UPDATE_cls3d_cont_offset_factor    ROUND_cls3d_cont_offset_factor     0    undefined                      undefined 
060070_External_select3d           060080_Refine3D_global             1    SET_mask3d_refine3d            CSS_lbin_center3d_refine3d_use_mask3d 
SET_mask3d_refine3d                060080_Refine3D_global             0    undefined                      undefined 
060080_Refine3D_global             060090_PostProcess_global          0    undefined                      undefined 
060090_PostProcess_global          EXIT                               0    undefined                      undefined 
