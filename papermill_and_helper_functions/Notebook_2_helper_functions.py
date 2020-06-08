#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:31:47 2020

@author: gilmandelbaum
"""
import pandas as pd 
import numpy  as np
import scipy.signal as sp_signal



from pathlib import Path
import pickle
import sys 



"""
load the state transitions
"""

def load_lookup_tables (to_load):
    
    data_dir_input = sys.path[0]
    root = Path(data_dir_input)
    d = to_load+".pickle"
    my_path = root / d 
    fileToOpen = open(my_path, 'rb')
    lookup_table = pickle.load(fileToOpen)
    return (lookup_table)


"""
there are different formats of the behavior_data_states. This is to be sure that the analysis is done on same format
"""

def prepare_behavior_data (behavior_data_states):
    first_column_label = behavior_data_states.columns[0]
    if behavior_data_states[first_column_label][0]>1:
        first_row_fromCurrent_session = behavior_data_states[behavior_data_states[first_column_label]==0]
        behavior_data_states = behavior_data_states[first_row_fromCurrent_session.index[0]:].reset_index(drop=True)
    
    if behavior_data_states[behavior_data_states.columns[-1]][0]<10: 
        behavior_data_states.columns = ["iBlock", "iTrial","iOccurrence", "iState_start", "iState_end", "analog1", "analog2","nTrial"]
    else:
        behavior_data_states.columns = ["nTrial", "iBlock", "iTrial","iOccurrence", "iState_start", "iState_end", "analog1", "analog2"]
    
    return behavior_data_states
    
"""
The goal of the function below is to start the photometry system at a specifc 
trial. 
first step: the photometry sent a signal to the behavior system. cut before that. 
second step: on the first step df, slice a data frame where the behavior system sent a signal to the photometry system. 
the output: we have a data frame that starts with a start of a behavioral trial. 
note: the photometry sync single to the behav systems starts a few seconds after turning on the photo system
"""

def handshake_behav_recording_sys(data):
    #first to be sure the recording system is sending a signal to the behavior
    df1 = data.loc[data[data['toBehSys']==1].index[0]:]
    #second to be sure the behavSys is sending signal to the photometry system at the start of each trial
    df1 = df1.loc[df1[df1['fromBehSys']==0].index[0]:]
    #reset index so it does not carry on the index from the slicing of the original df. 
    df2 = df1.reset_index(drop=True)
    return df2



def define_behavior_data_states(behavior_data_states): 
    #the first trial that the recording system is sending signal to the behavior system. 
    #this first step accounts for the fact that there might be data from a previous session. 
    lowSignal= behavior_data_states[behavior_data_states['analog2']<250.0]
    behavior_data_states_1= behavior_data_states[lowSignal.index[0]:]
    behavior_data_states_1= behavior_data_states_1.reset_index(drop=True)
    
    
    afterPhotoOn= behavior_data_states_1[behavior_data_states_1['analog2']>1000.0]
    behavior_data_states_2= behavior_data_states_1[afterPhotoOn.index[0]:]
    behavior_data_states_2= behavior_data_states_2.reset_index(drop=True)
    
    #start the dataFrame from the start of the next trial 
    Only23= behavior_data_states_2[behavior_data_states_2['iState_start']==23.0]
    behavior_data_states_3 = behavior_data_states_2[Only23.index[0]:]
    #print (behavior_data_states_3)

    #reset index so it does not carry on the index from the slicing of the original df. 
    behavior_data_states_final= behavior_data_states_3.reset_index(drop=True)
    
    return behavior_data_states_final

"""
#get number of bins per trial from the state transition behavioral data (200hz sampling) 
"""

def number_of_bins_beh_data_per_trial(beh_df):     
    trials = beh_df.nTrial.unique() #np array that each number corresponds to a unique trial number. 
    trial_df_list = [] #this is the list that we will populate. 
    
    for i in range(0, len(trials)): 
        ntrial = trials[i]  #ntrial gives the trial number. 
        
        df_nTrial = beh_df[beh_df['nTrial']==ntrial].reset_index(drop=True) #make a dataFrame with that trial. 
        
        df_nTrial_iOccurrence_0 = df_nTrial[df_nTrial['iState_start']==23.0].index[0] 
        df_nTrial = df_nTrial[df_nTrial_iOccurrence_0:]
        
        try:
            df_nTrial_plus1= beh_df[beh_df['nTrial']==ntrial+1].reset_index(drop=True)
            df_nTrial_plus1_iOcurrence_0 = df_nTrial_plus1[df_nTrial_plus1['iState_start']==23.0].index[0]
            df_nTrial_plus1_before_iOcurrence_0 = df_nTrial_plus1[:df_nTrial_plus1_iOcurrence_0]
            trial_df_list.append(len(df_nTrial)+len(df_nTrial_plus1_before_iOcurrence_0))


        except IndexError:
            trial_df_list.append(len(df_nTrial))
        
    return trial_df_list





#get number of bins per trial from the photometry data 
def number_of_bins_photo_data_per_trial(photometry_all_channels_clean):
    photometry_all_channels_clean_diff = photometry_all_channels_clean.diff()
    df_NaN_and_minus_ones = photometry_all_channels_clean_diff.where(photometry_all_channels_clean_diff==-1)
    index_minus_ones_list = df_NaN_and_minus_ones[df_NaN_and_minus_ones['fromBehSys']==-1].index.tolist() 
    
    first_trial_bin_numbers = index_minus_ones_list[0]
    index_minus_ones_list_diff = np.diff(index_minus_ones_list)
    list_of_number_bins_per_trial = np.insert(index_minus_ones_list_diff,0,first_trial_bin_numbers)
    return list_of_number_bins_per_trial


def resample_photoData_and_align_photo_with_beh(beh_binslist, behdf, photo_raw, photo_binslist):
    
    trial_df_list= []
    running = 1 
    
    slice_start_photo = 0
    slice_end_photo = 0
    slice_start_beh = 0
    slice_end_beh = 0
    
    #use beh_binslist to iterate or photo_binslist depending on what is shorter. (this depends what was
    #shutdown first - the photometry system or the behavior system)
    
    if len(photo_binslist) < len(beh_binslist):
        shorterList = len(photo_binslist)
    else: 
        shorterList = len(beh_binslist)
        print (shorterList)
        
    for n_bins in range(0, shorterList):
        
        n_bins_photo = photo_binslist[n_bins]
        n_bins_beh = beh_binslist[n_bins]
                
        slice_end_beh = slice_end_beh+n_bins_beh
        slice_end_photo = slice_end_photo+n_bins_photo
        
        df_photo_trial_chunk = photo_raw[slice_start_photo:slice_end_photo]
        df_beh_trial_chunk = behdf[slice_start_beh:slice_end_beh].reset_index(drop=True)
        
        
        photo_resample = pd.DataFrame(sp_signal.resample(df_photo_trial_chunk[['d2 R', 'd1 R', 'd2 L', 'd1 L']], n_bins_beh))# used to be n_bins_beh*6
        photo_resample.columns = ['d2 R', 'd1 R', 'd2 L', 'd1 L']
     

        df_photo_beh = pd.concat([df_beh_trial_chunk, photo_resample], axis=1)
    
        trial_df_list.append(df_photo_beh)
        
    
        slice_start_photo = slice_start_photo+n_bins_photo
        slice_start_beh = slice_start_beh+n_bins_beh
        #print(running)
        running+=1
    print ("number of trials synced:"+" "+ str(running))
    return pd.concat(trial_df_list)


"""
#define state transitions based on behavioral system, going to be used in tag_real_full_trial function below. 
"""
#ENL
state_ENL = [(23, 29), (29, 30), (30, 30), (30, 32), (32, 33), (33, 33), (33, 29), (30,38)]
state_ENL_and_ENLpenalties = [(29, 30), (29, 32), (30, 30), (30, 32), (31, 32), (32, 33), (33, 33), (33, 29)]
state_ENLp = [(29, 32), (30, 32)]#, (31, 32), (32, 33), (32, 32), (30, 33), (33, 33)]


#Cue and Selection Time
state_Cue_to_Selection = [(38, 39), (38, 41), (39, 39), (39, 41), (41, 42), (42, 42)]+[(39, 47), (47, 48), (48, 48), (48, 49)]


#Selection 
state_SelectRew=[(47,50), (48, 50)]
state_SelectNonRew=[(47, 54), (48, 54)]


#Consumption
state_collectRew=[(53, 53),(50, 51), (51, 51), (51, 52), (52, 53), (53, 61)] 
state_NonRew= [(55, 55), (54, 55), (55, 56)]


states_EndOfTrial_notIdentified= [(61, 82), (82, 62), (62, 63), (55, 61), (63, 78), (78, 66), (66, 75), (58, 61), (58, 58), (75, 16),(63, 20)]
states_StartOfTrial_notIdentified = [(20, 21), (21,14), (14, 24), (24, 25), (25, 27), (27, 23), (16, 20)]
states_FreeRewards = [(63, 93), (93, 94), (94, 94), (94, 95), (95, 96), (96, 96), (96, 20)]
state_TO = [(58, 58)]



def tag_real_full_trial(beh_photo_align):
    
    beh_photo_align = beh_photo_align.reset_index(drop=True)
    Consump_NonRewarded_rows_list = []
    Non_defined_state_list = []
    RestOfBins = beh_photo_align.copy()
    
    for states in state_collectRew+state_NonRew+states_EndOfTrial_notIdentified+states_FreeRewards: #Take out free rewards (after you take the trials)
        state_start = states[0]
        state_end = states[1]
        
        #this state is sometimes aligned with trial n and sometimes to n-1 so to account for this...
        if (state_start, state_end)== (75, 16): 
            Non_defined_state_list.append(beh_photo_align.loc[(beh_photo_align['iState_start'] == state_start) & (beh_photo_align['iState_end'] == state_end)])
        else:   
            Consump_NonRewarded_rows_list.append(beh_photo_align.loc[(beh_photo_align['iState_start'] == state_start) & (beh_photo_align['iState_end'] == state_end)])
        RestOfBins = RestOfBins[~((RestOfBins['iState_start'] == state_start) & (RestOfBins['iState_end'] == state_end))]
        
    Consumption_NonRewarded_rows = pd.concat(Consump_NonRewarded_rows_list)
    Consumption_NonRewarded_rows = Consumption_NonRewarded_rows.sort_index()
    
    Consumption_NonRewarded_rows['R_nTrials_CNR']=Consumption_NonRewarded_rows['nTrial']+1
    Consumption_NonRewarded_df = pd.DataFrame(Consumption_NonRewarded_rows['R_nTrials_CNR'])

    RestOfBins['R_nTrials_RoB']= RestOfBins['nTrial']
    RestOfBins_df = pd.DataFrame(RestOfBins['R_nTrials_RoB'])
    

    
    
    df_Real_nTrials = pd.concat([Consumption_NonRewarded_df, RestOfBins_df], axis= 1)
    
    arr = df_Real_nTrials.values
    df_Real_nTrials['Real_nTrials_1'] = arr[~np.isnan(arr)].astype(int)
    df_Real_nTrials = df_Real_nTrials.drop(['R_nTrials_CNR', 'R_nTrials_RoB'], axis=1)
    
    
    #still accounting for weird state
    Non_defined_state = pd.concat(Non_defined_state_list)
    Non_defined_state = Non_defined_state.sort_index()
    df_prevTrial= df_Real_nTrials[df_Real_nTrials.index.isin(Non_defined_state.index-1)]
    
    df_prevTrial['new_index'] = df_prevTrial.index+1
    
    Non_defined_state_df = df_prevTrial.set_index('new_index')
    Non_defined_state_df.index.name=None
    Non_defined_state_df.columns=['non_defined']
    
    
    df_Real_nTrials = pd.concat([df_Real_nTrials, Non_defined_state_df], axis= 1)
    arr = df_Real_nTrials.values
    df_Real_nTrials['Real_nTrials'] = arr[~np.isnan(arr)].astype(int)
    df_Real_nTrials = df_Real_nTrials.drop(['Real_nTrials_1', 'non_defined'], axis=1)
    
    
    
    
    
    Final_df = pd.concat([beh_photo_align, df_Real_nTrials], axis=1)
    return Final_df


        
