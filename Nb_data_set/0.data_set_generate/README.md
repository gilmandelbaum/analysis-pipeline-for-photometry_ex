# 0.data set generate

**0.data_set_generate_data_object_data_trial.ipynb:**
generates one object in a .pickle fomat as a list. Each entry to that list is a data trial df that is importad from the output of notebook 0a in the processing pipeline. 

**1.data_set_generate_data_object_photometry_raw_traces.ipynb:**
photometry traces that are directly from the tdt system. 

**2.data_set_generate_data_object_photometry_after_down_sampling.ipynb:**
generates one object in a .pickle fomat that that has the structure:
[Session number] [df with the photometry data after it with processed and downsampled]

**3.data_set_generate_data_object_photometry_after_processing.ipynb:**
generates one object in a .pickle fomat that that has the structure:
[Session number][Right or left side of the brain][ipsi or contra response][trial type]{period}.




