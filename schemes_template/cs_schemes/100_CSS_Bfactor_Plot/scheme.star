
# version 50001

data_scheme_general

_rlnSchemeName                       Schemes/100_CSS_Bfactor_Plot/
_rlnSchemeCurrentNodeName            WAIT
 

# version 50001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CSS_mbin_bfactor_min_nr_parts     XXX_SSE_REPLACE_SAMPLE_XXX     XXX_SSE_REPLACE_SAMPLE_XXX 
CSS_mbin_bfactor_max_nr_parts     XXX_SSE_REPLACE_SAMPLE_XXX    XXX_SSE_REPLACE_SAMPLE_XXX 
maxtime_hr    96.000000    96.000000 
  wait_sec   180.000000   180.000000 
 

# version 50001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
CSS_mbin_bfactor_wait_prev_proc            1            1 
has_exited            0            0 
 

# version 50001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
CSS_mbin_bfactor_prev_proc_exited Schemes/090_CSS_Res_fish_3D/RELION_JOB_EXIT_SUCCESS Schemes/090_CSS_Res_fish_3D/RELION_JOB_EXIT_SUCCESS 
CSS_mbin_bfactor_refine3d_job  XXX_SSE_REPLACE_SAMPLE_XXX  XXX_SSE_REPLACE_SAMPLE_XXX
CSS_mbin_bfactor_postproc_job  XXX_SSE_REPLACE_SAMPLE_XXX  XXX_SSE_REPLACE_SAMPLE_XXX
 

# version 50001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
      EXIT       exit  undefined  undefined  undefined 
EXIT_maxtime exit_maxtime  undefined maxtime_hr  undefined 
HAS_prev_proc_exited bool=file_exists has_exited CSS_mbin_bfactor_prev_proc_exited  undefined 
      WAIT       wait  undefined   wait_sec  undefined 
 

# version 50001

data_scheme_jobs

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
100010_External_bfactor 100010_External_bfactor        new            0 
 

# version 50001

data_scheme_edges

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
      WAIT 100010_External_bfactor            1 EXIT_maxtime CSS_mbin_bfactor_wait_prev_proc 
EXIT_maxtime HAS_prev_proc_exited            0  undefined  undefined 
HAS_prev_proc_exited       WAIT            1 100010_External_bfactor has_exited 
100010_External_bfactor       EXIT            0  undefined  undefined 
 