
# data set analysis: 


### data set generate
data_set_generate_data_object: generates one object that has the structure:
[Session number][Right or left side of the brain][ipsi or contra response][trial type]{period}.

data_set_generate_data_object-with bootstrap on sessions.ipynb: generates one object that has the structure:
[Session number][Right or left side of the brain][ipsi or contra response][trial type]{period}. Each mouse is resampled with return and 10 sesssions are taken. 



data_set_generate_data_object-with bootstrap on sessions.ipynb
### lineplot (each session avg contributes one trace. The avg of all those traces are plotted)

papermill_data_set_lineplot_(ic_together): 
to run the data_set_lineplot_(ic_together) notebook. The papermill is to make changes to the period that is being plotted.

data_set_lineplot_(ic_together): 
plots similar to 
[7b](https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/Nb_7x_plots/Notebook_7_b.ipynb) 
but for a data set, i.e., Takes the avg from each session and makes a line plot of the avg of all the sessions. 

