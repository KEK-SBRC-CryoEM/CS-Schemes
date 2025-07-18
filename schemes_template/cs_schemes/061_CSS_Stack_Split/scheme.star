
# version 50001

data_scheme_general

_rlnSchemeName                       Schemes/061_CSS_Stack_Split/
_rlnSchemeCurrentNodeName            WAIT
 

# version 50001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
maxtime_hr    96.000000    96.000000 
  wait_sec   180.000000   180.000000 
 

# version 50001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
has_exited            0            0 
 

# version 50001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
CSS_mbin_stack_split_yml  stack_split_scheme.yml  stack_split_scheme.yml
CSS_mbin_result_merge_yml  Schemes/061_CSS_Stack_Split/061010_External_stack_split/merge_setting.yml  Schemes/061_CSS_Stack_Split/061010_External_stack_split/merge_setting.yml

# version 50001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
      EXIT       exit  undefined  undefined  undefined 
      WAIT       wait  undefined   wait_sec  undefined 
 

# version 50001

data_scheme_jobs

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
061010_External_stack_split 061010_External_stack_split        new            0 
061020_External_result_merge 061020_External_result_merge        new            0 
 

# version 50001

data_scheme_edges

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
      WAIT                        061010_External_stack_split     0    undefined    undefined 
061010_External_stack_split       061020_External_result_merge    0    undefined    undefined 
061020_External_result_merge      EXIT                            0    undefined    undefined 

 