# Notebook 2:
sync neural data and behavior data.  
input: behavior data per state transition, neural data. 
output: a df with the neural data synced to the beh data. In addition there is a column that is called Real_nTrials which 
corresponds to the consumption of the previous trial until the choice of the next trial (see X for full explanation of what 
that means). The name of this df is mouse_dateNotebook_2_label.pickle 

2_a: 4 channel photometry notebook. Resampling occurs per trial using the scipy.signal resample function. 

2_b: 4 channel photometry notebook. Resampling occurs per session basis using the scipy.signal resample function. 
