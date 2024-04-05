
# version 30001

data_scheme_general

_rlnSchemeName                       Schemes/11_CS_Create_Stack/
_rlnSchemeCurrentNodeName            WAIT
 

# version 30001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CS_cryolo_threshold        0.1             0.1 
CS_ctf_maxres              6.0             6.0 
CS_mics_box              252             252
CS_mics_box_0o95         240             240 
CS_min_nr_parts       200000          800000
CS_min_nr_mics          2000            2000 
CS_parts_box              84              84 
CS_parts_x_coods_max    5634            5634 
CS_parts_x_coods_min     126             126 
CS_parts_y_coods_max    3966            3966 
CS_parts_y_coods_min     126             126 
current_nr_mics            0               0
current_nr_parts           0               0 
maxtime_hr                96              96
prev_nr_mics               0               0
wait_sec                 180             180  


# version 30001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
CS_limit_mics          1            1
has_ctffind            0            0
has_larger_nr_mics     0            0
has_required_nr_mics   0            0
has_required_nr_parts  0            0
limit_mics             0            0



# version 30001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
CS_ctf_mics             Schemes/0_CS_prep/ctffind/micrographs_ctf.star                                  Schemes/0_CS_prep/ctffind/micrographs_ctf.star
selected_ctf_mics       Schemes/11_CS_Create_Stack/0101_Select_mic/micrographs.star                     Schemes/11_CS_Create_Stack/0101_Select_mic/micrographs.star
selected_rm_bars_parts  Schemes/11_CS_Create_Stack/0302_Select_rm_bars_xy/particles.star                Schemes/11_CS_Create_Stack/0302_Select_rm_bars_xy/particles.star
split_mics              Schemes/11_CS_Create_Stack/0102_Select_split_stack_mics/micrographs_split1.star Schemes/11_CS_Create_Stack/0102_Select_split_stack_mics/micrographs_split1.star
all_mics                Schemes/11_CS_Create_Stack/0101_Select_mic/micrographs.star                     Schemes/11_CS_Create_Stack/0101_Select_mic/micrographs.star
mics_import             undefined                                      undefined
micrographs             micrographs                                    micrographs 
particles               particles                                      particles 
python_exe          /efs/em/pyenv/versions/anaconda3-5.3.1/envs/topaz/bin/python  /efs/em/pyenv/versions/anaconda3-5.3.1/envs/topaz/bin/python
cryolo_repo         /efs/em/crYOLO                                                /efs/em/crYOLO
cryolo_exe          /efs/em/crYOLO/gtf_relion4_run_cryolo_system.sh               /efs/em/crYOLO/gtf_relion4_run_cryolo_system.sh


# version 30001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
EXIT                   exit                 undefined              undefined               undefined 
EXIT_maxtime           exit_maxtime         undefined              maxtime_hr              undefined 
HAS_ctffind            bool=file_exists     has_ctffind            CS_ctf_mics             undefined
COUNT_mics             float=count_images   current_nr_mics        selected_ctf_mics       micrographs 
HAS_mics_increased     bool=gt              has_larger_nr_mics     current_nr_mics         prev_nr_mics 
SET_prev_nr_mics       float=set            prev_nr_mics           current_nr_mics         undefined
HAS_required_nr_mics   bool=ge              has_required_nr_mics   current_nr_mics         CS_min_nr_mics
LIMIT_nr_mics          bool=set             limit_mics             CS_limit_mics           undefined
SET_split_mics         string=set           mics_import            split_mics              undefined
SET_all_mics           string=set           mics_import            all_mics                undefined
COUNT_parts            float=count_images   current_nr_parts       selected_rm_bars_parts  particles
HAS_required_nr_parts  bool=ge              has_required_nr_parts  current_nr_parts        CS_min_nr_parts
WAIT                   wait                 undefined              wait_sec                undefined
 

# version 30001

data_scheme_jobs

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4  
0101_Select_mic                   0101_Select_mic                  continue       0
0102_Select_split_stack_mics      0102_Select_split_stack_mics     continue       0 
0200_External_cryolo              0200_External_cryolo             continue       0 
0300_Extract                      0300_Extract                     continue       0 
0301_Select_rm_bars_x             0301_Select_rm_bars_x            continue       0 
0302_Select_rm_bars_xy            0302_Select_rm_bars_xy           continue       0
0303_Select_split_stack_parts     0303_Select_split_stack_parts    new            0 


# version 30001

data_scheme_edges

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                              EXIT_maxtime                     0  undefined                     undefined 
EXIT_maxtime                      HAS_ctffind                      0  undefined                     undefined 
HAS_ctffind                       WAIT                             1  0101_Select_mic               has_ctffind 
0101_Select_mic                   COUNT_mics                       0  undefined                     undefined
COUNT_mics                        HAS_mics_increased               0  undefined                     undefined 
HAS_mics_increased                WAIT                             1  SET_prev_nr_mics              has_larger_nr_mics
SET_prev_nr_mics                  HAS_required_nr_mics             0  undefined                     undefined
HAS_required_nr_mics              WAIT                             1  LIMIT_nr_mics                 has_required_nr_mics
LIMIT_nr_mics                     SET_all_mics                     1  0102_Select_split_stack_mics  limit_mics
0102_Select_split_stack_mics      SET_split_mics                   0  undefined                     undefined
SET_split_mics                    0200_External_cryolo             0  undefined                     undefined
SET_all_mics                      0200_External_cryolo             0  undefined                     undefined
0200_External_cryolo              0300_Extract                     0  undefined                     undefined 
0300_Extract                      0301_Select_rm_bars_x            0  undefined                     undefined 
0301_Select_rm_bars_x             0302_Select_rm_bars_xy           0  undefined                     undefined 
0302_Select_rm_bars_xy            COUNT_parts                      0  undefined                     undefined
COUNT_parts                       HAS_required_nr_parts            0  undefined                     undefined 
HAS_required_nr_parts             WAIT                             1  0303_Select_split_stack_parts has_required_nr_parts
0303_Select_split_stack_parts     EXIT                             0  undefined                     undefined



