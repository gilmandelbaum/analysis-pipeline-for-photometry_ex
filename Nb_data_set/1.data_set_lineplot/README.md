# 1.data_set_lineplot
plot the data in a line plot from various periods of interest. One can combine sessions in different ways too. (See explanation below).

**papermill_data_set_lineplot_(ic_together).ipynb:**
to run the data_set_lineplot_(ic_together) notebook. The papermill is to make changes to the period that is being plotted. 
ipsi and contra in the plots refers to the next trial.
For example, if the plot is a LS ipsi and combined period 1 is plotted the sequence is: 1 sec before the non reward period, the non rewarded period after the mouse made a choice contra to the recording, last 1 second of ENL period. 

### [right_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/right_side_of_the_brain) 
all notebooks below are for the right hemisphere. 

**0.dsl__winall(no_dirc)_loseall(no_dirc)__rs.ipynb:**

**1.dsl__winall(ipsi_vs_contra)_loseall(ipsi_vs_contra)__rs.ipynb:**

**2.dsl__ipsinext(winall_vs_loseall)_contranext(winall_vs_loseall)__rs.ipynb:** 

**data_set_lineplot_win_or_lose_trial_right_side.ipynb:**
plots the wins together ipsi vs contra (win repeat + win switch) and the loses together ipsi vs contra (lose repeat + lose switch). 

**data_set_lineplot_win_and_lose_trial_right_side.ipynb:**
plots the wins and loses together ipsi on the next.
plots the wins and loses together contra on the next.


**3.dsl__winrepeat(ipsi_vs_contra)_loseswitch(ipsi_vs_contra)__rs.ipynb**
plots similar to [7b](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/Nb_7x_plots/Notebook_7_b.ipynb) 
but for a data set: it takes the avg from each session and makes a line plot of the avg of all the sessions from the right hemisphere.





### [left_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/left_side_of_the_brain)
all notebooks below are for the left hemisphere. 

**data_set_lineplot_ic_together_left_side.ipynb:**
plots similar to 
[7c](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/Nb_7x_plots/Notebook_7_c.ipynb) 
but for a data set: it takes the avg from each session and makes a line plot of the avg of all the sessions from the left hemisphere. 

**data_set_lineplot_win_or_lose_trial_left_side.ipynb:**
plots the wins together ipsi vs contra (win repeat + win switch) and the loses together ipsi vs contra (lose repeat + lose switch) 
