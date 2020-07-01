# Photometry analysis pipeline 

This package is the second (the first one is for [optogenetic experiments](https://github.com/gilmandelbaum/analysis-pipeline-for-optogenetics_ex)) to support the analysis of a project in the [Sabatini Lab](https://sabatini.hms.harvard.edu/) at Harvard Medical School in which we try to better understand how the brain allows us to decide what to do next. 

This package is written to analyze photometry experiments and has 3 major steps: 

1. processing the sessions (all 7 processing steps are controlled from one notebook). 

2. generate the data set 

3. analyze, plot and model the sessions/data set 

The goal was to write a pipeline that allows for others in the lab to write their own notebooks and add them to the pipeline seamlessly.
Also, we wanted to generate rather simple data formats that can easily be shared with others outside the lab  but maintain in them the richeness of the data. 

The choice of which notebook one runs in the processing step will determine what pipeline/analysis will be executed. 
If specific output data structures already exist based on previous runs of the pipeline the "master jupyter notebook" will 
recognize those data structures that are saved and only run what is needed to complete the new analyses. 
This saves lots of time and allows to efficiently explore the data.

The design of this behavioral task for mice was inspired by operant conditioning behavioral tasks. 
For more details see [task description](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/task_description.md)

## For each session the stages of analysis are:

### 1. processing the sessions 
It uses jupyter noteboooks and each stage of the pipeline can be run stand-alone or as part of work flow controlled by one "master jupyter notebook" that uses 
the [papermill](https://papermill.readthedocs.io/en/latest/) library to control all the notebooks in the pipeline. 

Nb stands for notebooks. The number refers to when the notebook will be exected in the pipeline. The x after each number stands for the version of the notebook. For example, one can run a seq of notebooks: 0a1a1d2a4a4b4c5a6a. 

[Nb_0x_pre_analysis](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_0x_pre_analysis)

[Nb_1x_define_trials_of_interest](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_1x_define_trials_of_interest)

[Nb_2x_combine_photometry_behav_data](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_2x_combine_photometry_behav_data)

[Nb_3x_photometry_signal_analysis](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_3x_photometry_signal_analysis)

[Nb_4x_assign_photometry_to_behavioral_states](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_4x_assign_photometry_to_behavioral_states)

[Nb_5x_form_one_structure_with_all_data](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_5x_form_one_structure_with_all_data)

[Nb_6x_combine_periods_of_interest](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_6x_combine_periods_of_interest)

[Nb_7x_plots](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_7x_plots)

all the notebooks run together using a [photometry_papermill.ipynb notebook](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/papermill_and_helper_functions) or can be run stand alone. 

### 2. generate the data set 
After all the session are analyzed there is a second step that generates a unique structure that hold the full [data set](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/0.data_set_generate) of either licks, data of interest per trial, or photometry data from over 20 periods of the trial. 


### 3. analyze the sessions/data set 
The third step is to analyze the [data](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set) 
Currently, you can [plot](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/1.data_set_lineplot) over 20 periods of interest as a line plot and compare trial types/direction of choice and do so for right hemisphere recordings and left hemisphere recordings as well. 
You can also [calculate](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/2.data_set_calculations) and compare various parameters from the photometry signal.
You can also [correlate](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/3.data_set_correlations) between photomotery signals and behavioral events. 


## Acknowledgments


This analysis package was written by Gil Mandelbaum and Maria Diaz Bobillo with the help of [Jeff Markowitz](https://github.com/jmarkow) in the lab of [Bernardo Sabatini](https://sabatini.hms.harvard.edu/) at Harvard Medical School. 
