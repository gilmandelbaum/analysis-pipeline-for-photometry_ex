
# Nb_data_set (Data set analysis)

The structure of the data analysis folders are: 
name of analysis-->seq to be analyzed-->type of analysis-->period analyzed.


[0.data set generate:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/0.data_set_generate)
generating data set of interest from photometry signal or trial data to use for analysis. 

[1.data_set_lineplot:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/1.data_set_lineplot)
Various types of line plots. Notebookes can also run with a papermill to plot different periods of interest one after the other. 

[2.data_set_calculate:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations)
Per session. Extracting features (numbers!) from the traces per session, i.e. each sessions is avg and represented by one number. 

[3.data_set_correlations:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/3.data_set_correlations)
Per trial. Extracting features (numbers!) from the traces and from the behavior to see if they are correlated. Each trial is treated independently. 

[4.data_set_full_session_trace_plots:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/4.data_set_full_session_trace_plots)
Plot a part of the session with a horizontal line which defines a specific state, for example, the choice lick.

[5.data_set_counters:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/5.data_set_counters)
counting various aspects of data set. For example nubmer of trials, or number of licks. 
