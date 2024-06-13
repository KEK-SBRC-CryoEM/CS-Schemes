
# version 30001 

data_job 

_rlnJobTypeLabel             relion.ctffind 
_rlnJobIsContinue                       0 
_rlnJobIsTomo                           0 


# version 30001 

data_joboptions_values 

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
input_star_mics             $$SS_comm_motioncorr_mics_star 
use_noDW                    Yes 
do_phaseshift               No 
phase_min                   0 
phase_max                   180 
phase_step                  10 
dast                        100 
use_ctffind4                Yes 
fn_ctffind_exe              XXX_JSE_REPLACE_SYSTEM_XXX 
use_given_ps                Yes 
slow_search                 Yes 
ctf_win                     -1 
box                         512 
resmin                      $$EM_ctffind_fit_res_min 
resmax                      $$EM_ctffind_fit_res_max 
dfmin                       $$GTF_ctffind_search_def_min 
dfmax                       $$GTF_ctffind_search_def_max 
dfstep                      100 
use_gctf                    No 
fn_gctf_exe                 XXX_JSE_REPLACE_SYSTEM_XXX
do_ignore_ctffind_params    No 
do_EPA                      Yes 
other_gctf_args             "" 
gpu_ids                     XXX_JSE_REPLACE_PARALLEL_XXX 
nr_mpi                      XXX_JSE_REPLACE_PARALLEL_XXX 
do_queue                    XXX_JSE_REPLACE_PARALLEL_XXX 
queuename                   020010_CtfFind 
qsub                        XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra1                 XXX_JSE_REPLACE_PARALLEL_XXX 
qsub_extra2                 XXX_JSE_REPLACE_PARALLEL_XXX 
qsubscript                  XXX_JSE_REPLACE_PARALLEL_XXX 
min_dedicated               XXX_JSE_REPLACE_PARALLEL_XXX 
other_args                  XXX_JSE_REPLACE_PARALLEL_XXX 
