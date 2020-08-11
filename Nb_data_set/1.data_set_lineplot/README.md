# 1.data_set_lineplot
plot the data in a line plot from various periods of interest. One can combine sessions in different ways too. (See explanation below).
You can plot the right hemisphere or the left hemisphere. You can plot the avg across sessions or the avg across mice. 


**data_set_lineplot_avg_of_sessions_papermill.ipynb:**
The papermill is to make changes to the period that is being plotted. 
**avg_of_sessions:**
the line represents the avg of all sessions from all mice. (treating each session as independent).


For example, if the plot is a LS ipsi and combined period 1 is plotted the sequence is: 1 sec before the non reward period, the non rewarded period after the mouse made a choice contra to the recording, last 1 second of ENL period. 


**data_set_lineplot_avg_of_mice_papermill.ipynb:**
The papermill is to make changes to the period that is being plotted. 
This is also where the sessions are assigned to the each mouse. 
**avg_of_mice:**
each thin line represents an avg of sesssions per mouse and the thick line represents the avg across mice. 


### [right_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/right_side_of_the_brain/avg_of_sessions) 
all notebooks below are for the right hemisphere (right side (rs)) and avg of sessions (sess). 

**0.dsl__winall(no_dirc)_loseall(no_dirc)__rs_sess.ipynb:**
plots the wins together (win repeat + win switch) and the loses together (lose repeat + lose switch). 

**1.dsl__ipsinext_vs_contranext__rs_sess.ipynb:**
plots the trials that the next was an ipsi response to the recordings or contra response to the recordings.

**2.dsl__ipsiprevious_vs_contraprevious__rs_sess.ipynb:**
plots the trials that the previous was an ipsi response to the recordings or contra response to the recordings. 

**3.dsl__winall(ipsi_vs_contra_next)_loseall(ipsi_vs_contra_next)__rs_sess.ipynb:**
plots the win or lose trials that the next was an ipsi response to the recordings or contra response to the recordings. 

**4.dsl__winall(ipsi_vs_contra_previous)_loseall(ipsi_vs_contra_previous)__rs_sess.ipynb:**
plots the win or lose trials that the previous was an ipsi response to the recordings or contra response to the recordings. 

**5.dsl__winrepeat(ipsi_vs_contra_next)_loseswitch(ipsi_vs_contra_next)__rs_sess.ipynb:**
plots the win repeat or lose switch trials that the next was an ipsi response to the recordings or contra response to the recordings. 

**6.dsl__winrepeat(ipsi_vs_contra_previous)_loseswitch(ipsi_vs_contra_previous)__rs_sess.ipynb:**
plots the win repeat or lose switch trials that the previous was an ipsi response to the recordings or contra response to the recordings. 


### [right_side_of_the_brain avg across mice](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/1.data_set_lineplot/right_side_of_the_brain/avg_of_mice)


### [left_side_of_the_brain avg across sessions](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/1.data_set_lineplot/left_side_of_the_brain/avg_of_sessions) all notebooks are similar to the right side but with __ls and sess at the end to signify that they are for left hemisphere analysis and avg across sessions. 


### [left_side_of_the_brain avg across mice](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/1.data_set_lineplot/left_side_of_the_brain/avg_of_mice) all notebooks are similar to the right side but with __ls and mice at the end to signify that they are for left hemisphere analysis and avg across mice. 

