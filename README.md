# Photometry_analysis pipeline 

This package is the second (of many!) to support the analysis of a 
project in the Sabatini Lab at Harvard Medical School in which we try to 
better understand how the brain allows us to decide what to do next.

It uses jupyter noteboooks and each stage of the pipeline can be run stand-alone 
or as part of work flow controlled by one "master jupyter notebook" that uses 
the [papermill](https://papermill.readthedocs.io/en/latest/) library to control all the notebooks in the pipeline. 

This package is written to analyze photometry experiments. 
The goal was to write a pipeline that allows for others in the lab to write there own notebooks and add them to the pipeline.  

The choice of notebook will determine what pipeline/analysis will be executed. 
If specific output data structures already exist based on previous runs of the pipeline the "master jupyter notebook" will 
recognize those data structures and only run what is needed to complete the new analyses. 
This saves lots of time and allows to efficiently explore the data.


The design of this behavioral task for mice was inspired by operant conditioning behavioral tasks. 
For more details see [task description](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/task_description.md)


# photometry_analysis


# Notebook 0:
processing of the photometry signal pre analysis notebook - prepare to define what each trial was. 
input: mouse_dataTrial_label.xlsx (each row is a trial). 
output: mouse_dateNotebook_0_a.pickle. The output is the same df as mouse_dataTrial_label with additional columns that will aid in the analysis. 
0_a: standard analysis 


# Notebook 1:
Each notebook 1 gives a different list of trial numbers with the same general structure of output: 
The number of trial: R/L, IPSI/CONTRA, TrialType. 
input: the output of notebook 0_a. 
output: a list of lists called mouse_dateNotebook_1_label.pickle 

1_a: get all trials (with ENLp and with CUEp)

1_b: get no ENLp, no CUEp trials. 

1_c: get ENLp. 


# Notebook 2:
sync neural data and behavior data.  
input: behavior data per state transition, neural data. 
output: a df with the neural data synced to the beh data. In addition there is a column that is called Real_nTrials which 
corresponds to the consumption of the previous trial until the choice of the next trial (see X for full explanation of what 
that means). The name of this df is mouse_dateNotebook_2_label.pickle 

2_a: 4 channel photometry notebook. 



# Notebook 3:
processing neural data 
input: notebook 2 
output: same as notebook 2 but with neural data processed. 

3_a: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline.  

3_b: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline.  Z score on full session. 

3_c: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline and 10 seconds Z score sliding window. 


# Notebook 4:
Flagging periods of interest in order to generate neural epochs of interest. 
input: Notebook 2  
output: .pickle that has a data frame with two columns. The first column is the bin number and the second column is the trial number. 

4_a: Reward_NoReward_tag: consumption or no rewarded period. 

4_b: ENL_tag: enforced non lick period task. 

4_c: Cue_to_Sel_tag: the period of the cue and the response time. 

4_d: Cue_to_Sel_fromPrevTrial_tag: cue to the selection from the previous trial. 

4_e: tags the first ENL period penalty time and only if it happened after 500ms into the ENL period. 


# Notebook 5:
input: notebook 1 (list of trial types of interest), notebook 3 (processed neural data). It also uses the flags that were generated in notebook 4s
Notebook 5 also needs [Tags], [Timing], [Start_or_end] which are all set in the papermill notebook. 
output: list that is [R/L][IPSI/CONTRA][trial type][period]. Also a list_of_tags in a csv file. 

5_a: splits as described above. 


# Notebook 6:
adds combination of periods together from notebook 5. 
input: notebook 5. 
output: same structure as notebook 5 but with an added period combining periods. 

6_a: key 'combined_periods_1'. combining 1 sec pre-consumption lick, 3 sec rewarded or non rewarded period and 1 sec ENL period before the cue. 




######

# Notebook 7:

7_a: empty
7_b: plots the mean of the ipsi and contra trials in win stay lose switch conditions from the right hemisphere. 

