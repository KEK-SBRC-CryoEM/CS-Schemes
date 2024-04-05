
# version 30001

data_scheme_general

_rlnSchemeName                       Schemes/0_CS_prep/
_rlnSchemeCurrentNodeName            WAIT
 

# version 30001

data_scheme_floats

loop_ 
_rlnSchemeFloatVariableName #1 
_rlnSchemeFloatVariableValue #2 
_rlnSchemeFloatVariableResetValue #3 
CS_Cs                           2.7            2.7 
CS_angpix_mic                   0.83           0.83 
CS_ctf_max_def              20000          20000 
CS_ctf_max_res                  4              4 
CS_ctf_min_def               3000           3000 
CS_dose_per_frame               0.87           0.87 
CS_eer_grouping                 1              1 
CS_first_frame_sum              1              1 
CS_kV                         300            300 
CS_motioncorr_max_motion       80             80 
current_nr_import_movies        0              0
do_at_most                   9999           9999
maxtime_hr                     96             96 
pre_nr_motioncorr_mics          0              0 
wait_sec                      180            180 
 

# version 30001

data_scheme_bools

loop_ 
_rlnSchemeBooleanVariableName #1 
_rlnSchemeBooleanVariableValue #2 
_rlnSchemeBooleanVariableResetValue #3 
has_unprocessed_motioncorr_mics            0            0 
 

# version 30001

data_scheme_strings

loop_ 
_rlnSchemeStringVariableName #1 
_rlnSchemeStringVariableValue #2 
_rlnSchemeStringVariableResetValue #3 
CS_fn_in_raw              Micrographs/*.tif                                          Micrographs/*.tif 
import_movies             Schemes/0_CS_prep/importmovies/movies.star                 Schemes/0_CS_prep/importmovies/movies.star 
motioncor_mics            Schemes/0_CS_prep/motioncorr/corrected_micrographs.star    Schemes/0_CS_prep/motioncorr/corrected_micrographs.star    
selected_motioncor_mics   Schemes/0_CS_prep/select_motioncor_mics/micrographs.star   Schemes/0_CS_prep/select_motioncor_mics/micrographs.star 
CS_fn_mtf                 ""                                                         ""
micrographs               micrographs                                                micrographs 
movies                    movies                                                     movies
ctffind_exe      /efs/em/ctffind-4.1.14-linux64/bin/ctffind                          /efs/em/ctffind-4.1.14-linux64/bin/ctffind
gctf_exe         /efs/em/Gctf_v1.06/bin/Gctf-v1.06_sm_20_cu7.5_x86_64                /efs/em/Gctf_v1.06/bin/Gctf-v1.06_sm_20_cu7.5_x86_64
motioncor2_exe   ""                                                                  ""
python_exe       /efs/em/pyenv/versions/anaconda3-5.3.1/envs/topaz/bin/python        /efs/em/pyenv/versions/anaconda3-5.3.1/envs/topaz/bin/python

# version 30001

data_scheme_operators

loop_ 
_rlnSchemeOperatorName #1 
_rlnSchemeOperatorType #2 
_rlnSchemeOperatorOutput #3 
_rlnSchemeOperatorInput1 #4 
_rlnSchemeOperatorInput2 #5 
COUNT_current_import_movies        float=count_images        current_nr_import_movies           import_movies              movies 
COUNT_pre_motioncorr_mics          float=count_images        pre_nr_motioncorr_mics             motioncor_mics             micrographs 
EXIT_maxtime                       exit_maxtime              undefined                          maxtime_hr                 undefined 
HAS_unprocessed_motioncorr_mics    bool=gt                   has_unprocessed_motioncorr_mics    current_nr_import_movies   pre_nr_motioncorr_mics 
      WAIT                         wait                      undefined                          wait_sec                   undefined 
 

# version 30001

data_scheme_jobs

loop_ 
_rlnSchemeJobNameOriginal #1 
_rlnSchemeJobName #2 
_rlnSchemeJobMode #3 
_rlnSchemeJobHasStarted #4 
   ctffind               ctffind                 continue            0 
importmovies             importmovies            continue            0 
motioncorr               motioncorr              continue            0 
select_motioncor_mics    select_motioncor_mics   continue            0 
 

# version 30001

data_scheme_edges

loop_ 
_rlnSchemeEdgeInputNodeName #1 
_rlnSchemeEdgeOutputNodeName #2 
_rlnSchemeEdgeIsFork #3 
_rlnSchemeEdgeOutputNodeNameIfTrue #4 
_rlnSchemeEdgeBooleanVariable #5 
WAIT                                 EXIT_maxtime                           0  undefined     undefined 
EXIT_maxtime                         importmovies                           0  undefined     undefined 
importmovies                         COUNT_current_import_movies            0  undefined     undefined 
COUNT_current_import_movies          COUNT_pre_motioncorr_mics              0  undefined     undefined 
COUNT_pre_motioncorr_mics            HAS_unprocessed_motioncorr_mics        0  undefined     undefined 
HAS_unprocessed_motioncorr_mics      WAIT                                   1  motioncorr    has_unprocessed_motioncorr_mics 
motioncorr                           select_motioncor_mics                  0  undefined     undefined 
select_motioncor_mics                ctffind                                0  undefined     undefined 
ctffind                              WAIT                                   0  undefined     undefined 
