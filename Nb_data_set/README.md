
# Nb_data_set (Data set analysis)

The structure of the data analysis folders is: 
name of analysis-->seq to be analyzed-->type of analysis-->period analyzed



# [0.data set generate](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/0.data_set_generate)

**data_set_generate_data_object.ipynb:**
generates one object in a .pickle fomat that that has the structure:
[Session number][Right or left side of the brain][ipsi or contra response][trial type]{period}.

**data_set_generate_data_object_data_trial.ipynb:**
generates one object in a .pickle fomat as a list. Each entry to that list is a data trial df that is importad from the output of notebook 0a in the processing pipeline. 

# [1.data_set_lineplot](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_lineplot)
plot the data in a line plot from various periods of interest. One can combine sessions in different ways too. (See explanation below).

**papermill_data_set_lineplot_(ic_together).ipynb:**
to run the data_set_lineplot_(ic_together) notebook. The papermill is to make changes to the period that is being plotted. 
ipsi and contra in the plots refers to the next trial.
For example, if the plot is a LS ipsi and combined period 1 is plotted the sequence is: 1 sec before the non reward period, the non rewarded period after the mouse made a choice contra to the recording, last 1 second of ENL period. 

### [right_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/right_side_of_the_brain) 
all notebooks below are for the right hemisphere. 

**data_set_lineplot_ic_together_right_side.ipynb:**
plots similar to 
[7b](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/Nb_7x_plots/Notebook_7_b.ipynb) 
but for a data set: it takes the avg from each session and makes a line plot of the avg of all the sessions from the right hemisphere. 

### [left_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/left_side_of_the_brain)
all notebooks below are for the left hemisphere. 

**data_set_lineplot_ic_together_left_side.ipynb:**
plots similar to 
[7c](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/Nb_7x_plots/Notebook_7_c.ipynb) 
but for a data set: it takes the avg from each session and makes a line plot of the avg of all the sessions from the left hemisphere. 


# [2.data_set_calculate: (per session)](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations)
extracting features (numbers!) from the traces per session, i.e. each sessions is avg and represented by one number. 

### [right_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/right_side_of_the_brain) 
all notebooks below are for the right hemisphere. 

**data_set_calculations_signal_magnitude_right_side.ipynb:**
calculates the max peak of the photometry signal after choice lick per session per condition. Find the max peak and takes the avg on 100ms around that.


### [left_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/left_side_of_the_brain) 

**data_set_calculations_signal_magnitude_left_side.ipynb:**
calculates the max peak of the photometry signal after choice lick per session per condition. Find the max peak and takes the avg on 100ms around that.
all notebooks below are for the left hemisphere. 


# [3.data_set_correlations: (per trial)](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/3.data_set_correlations)
extracting features (numbers!) from the traces and from the behavior to see if they are correlated. Each trial is treated independently. 

### [right_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/3.data_set_correlations/right_side_of_the_brain) 
all notebooks below are for the right hemisphere. 

**data_set_correlations_rt_vs_signal_magnitude_right_side.ipynb:**
calculates the max peak of the photometry signal after choice lick per trial per in each conidtion along side the response time of the next trial. 
For example,  we can ask if the response time on the switch trial (a few seconds later..) is correlated with the magnitude of signal on the lose trial before. 

**data_set_correlations_rt_vs_AUC_right_side.ipynb:**
calculates the area under the curve photometry signal after choice lick to 2 seconds. along side the response time of the next trial. 
For example,  we can ask if the response time on the switch trial (a few seconds later..) is correlated with the area under the curve on the lose trial before. 

### [left_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/3.data_set_correlations/left_side_of_the_brain) 

**data_set_correlations_rt_vs_signal_magnitude_left_side.ipynb:**
calculates the max peak of the photometry signal after choice lick per trial per in each conidtion along side the response time of the next trial. 
For example,  we can ask if the response time on the switch trial (a few seconds later..) is correlated with the magnitude of signal on the lose trial before. 

**data_set_correlations_rt_vs_AUC_left_side.ipynb:**
calculates the area under the curve photometry signal after choice lick to 2 seconds. along side the response time of the next trial. 
For example,  we can ask if the response time on the switch trial (a few seconds later..) is correlated with the area under the curve on the lose trial before. 


