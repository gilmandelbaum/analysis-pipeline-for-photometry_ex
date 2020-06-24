
# Nb_data_set (Data set analysis)

The structure of the data analysis folders is: 
name of analysis-->seq to be analyzed-->type of analysis-->period analyzed



# [0.data set generate](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/0.data_set_generate)

**data_set_generate_data_object.ipynb:**
generates one object in a .pickle fomat that that has the structure:
[Session number][Right or left side of the brain][ipsi or contra response][trial type]{period}.


# [data_set_lineplot](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_lineplot)
plot the data in a line plot from various periods of interest. One can combine sessions in different ways too. (See explanation below).

**papermill_data_set_lineplot_(ic_together).ipynb:**
to run the data_set_lineplot_(ic_together) notebook. The papermill is to make changes to the period that is being plotted.

### [right_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/right_side_of_the_brain) 
all notebooks below are for the right hemisphere. 

**data_set_lineplot_ic_together_right_side.ipynb:**
plots similar to 
[7b](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/Nb_7x_plots/Notebook_7_b.ipynb) 
but for a data set: it takes the avg from each session and makes a line plot of the avg of all the sessions from the right hemisphere. 

### [left_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/left_side_of_the_brain)
all notebooks below are for the left hemisphere. 

**data_set_lineplot_ic_together_right_side.ipynb:**
plots similar to 
[7c](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/Nb_7x_plots/Notebook_7_c.ipynb) 
but for a data set: it takes the avg from each session and makes a line plot of the avg of all the sessions from the left hemisphere. 


# [data_set_calculate:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations)
extracting features (numbers!) from the traces 

### [right_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/right_side_of_the_brain) 
all notebooks below are for the right hemisphere. 




### [left_side_of_the_brain:](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/tree/master/Nb_data_set/data_set_calculations/left_side_of_the_brain) 
all notebooks below are for the left hemisphere. 
