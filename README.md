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
For more details see [task description] (https://github.com/gilmandelbaum/analysis-pipeline-for-photometry_ex/blob/master/task_description.md)
