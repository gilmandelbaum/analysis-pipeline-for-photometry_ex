#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:18:35 2020

@author: gilmandelbaum
"""

import pickle
import pandas as pd 

def add_pickles (Tags):
    add_pickle = []
    for i in range(len(Tags)):
        tag = Tags[i]+".pickle"
        add_pickle.append(tag)
    return (add_pickle)



def combine_processed_data_and_tags (Tags,processed_data,root):
    Tags_pickles = add_pickles (Tags)
    
    for i in range(len(Tags_pickles)):
        d = Tags_pickles[i]
        my_path = root / d 
        fileToOpen = open(my_path, 'rb')
        processed_data[Tags[i]] = pickle.load(fileToOpen)
        
    return processed_data


def tag_Pre_Post_Periods(beh_photo_align, NumberOfBins_PrePost):
    
    pre_post_AllPeriods =[]

    
    for period in beh_photo_align.loc[:, 'Reward_NoReward_tag':].columns:
        diff= pd.DataFrame(beh_photo_align[period].fillna(0).diff())
        pre_period_list =[]
        post_period_list = []
        for trial in beh_photo_align['Real_nTrials'].unique()[1:]:
            try:
                index_start = diff[diff[period] == trial].index[0]
            
                index_end = diff[diff[period] == -trial].index[0]-1 #-1 because the actual end is the last bin that is tagges (!=0)

                pre_period = beh_photo_align[index_start-NumberOfBins_PrePost: index_start]
                post_period = beh_photo_align[index_end+1: NumberOfBins_PrePost+index_end+1]

                
                #Make df with column = period, values = trial, index = from pre_period/post_period
            
                df_pre = pd.DataFrame(index= pre_period.index, columns= ['pre_'+period])
                df_pre = df_pre.fillna(trial)
                
                df_post = pd.DataFrame(index= post_period.index, columns= ['post_'+period])
                df_post = df_post.fillna(trial)                
            
                
                pre_period_list.append(df_pre)
                post_period_list.append(df_post)
            except: #Error appears when it tries to get info from last trial 
                pass
            
        pre_period_alltrials = pd.concat(pre_period_list)
        post_period_alltrials = pd.concat(post_period_list)
        
        

        pre_post_AllPeriods.append(pre_period_alltrials)
        pre_post_AllPeriods.append(post_period_alltrials)
        
    
    df_PrePost= pd.concat(pre_post_AllPeriods, axis=1)
       
    df_final = pd.concat([beh_photo_align, df_PrePost], axis=1)  
    
    return df_final



def behavPhoto_split(aligned_behav_photo, listofTrial_RIC_LIC):
    total=[]
    for rl in listofTrial_RIC_LIC:
        rl_l=[]
        for ic in rl:
            ic_l=[]
            for combo in ic:
                periods_dic={}
                #iterate over new flags so we create dictionary with all periods
                for period in aligned_behav_photo.loc[:, 'Real_nTrials':].columns:
                    periods_dic[period] = aligned_behav_photo[aligned_behav_photo[period].isin(combo)]
                ic_l.append(periods_dic)                
            rl_l.append(ic_l)
        total.append(rl_l)
    return total 


def drop_columns(beh_photo):
    total= []
    side = 'R'
    for rl in beh_photo:
        rl_l=[]
        for ic in rl:
            ic_l=[]
            for combo in ic:
                period_dic = {}
                if side == 'R':
                    for period_str, period_value in combo.items():
                        period_dic[period_str]=period_value.drop(['d1 L', 'd2 L'], axis='columns')
                           
                    ic_l.append(period_dic)
                elif side == 'L':
                    for period_str, period_value in combo.items():
                        period_dic[period_str]=period_value.drop(['d1 R', 'd2 R'], axis='columns')
                    ic_l.append(period_dic)
                
            rl_l.append(ic_l)
        total.append(rl_l)
        side = 'L'
    return total



def get_photodata_perTrial_df_secondStep(combo, channel_list): #this has the trials in columns
  
    combo_dict = dict()
    try:
        for key, value in combo.items():
            period_str = key
            period_data = value
            #print(period_str)
            total_ntrials_df=[]
            ntrials = period_data[period_str].unique()

            for i in ntrials:
                total_ntrials_df.append(period_data[period_data[period_str]==i])
                #print(i)       
            channel_dict = dict()        
            for trial_i in range(0, len(total_ntrials_df)):
                trial = total_ntrials_df[trial_i]
                ntrial = ntrials[trial_i]

                for channel in channel_list:
                    new_df = pd.DataFrame(trial[channel]).reset_index(drop=True)                 
                    new_df.columns = [ntrial]            
                    try:
                        channel_dict[channel].append(new_df)
                    except:
                        channel_dict[channel]= [new_df]                    
            df_photo_df_list = []
            for key, value in channel_dict.items():     
                df_photo_allTrials_OneChannel = pd.concat(value, axis=1)
                df_photo_df_list.append(df_photo_allTrials_OneChannel) 
            try:
                df_photo_AllTrials_AllChannels = pd.concat(df_photo_df_list, axis=1, keys= channel_list)
                combo_dict[period_str] = df_photo_AllTrials_AllChannels
            except:
                combo_dict[period_str]= df_photo_AllTrials_AllChannels[0:0]
    except:
        pass
    return combo_dict



def get_photodata_perTrial_df_firstStep(data):
    channel_list_R = ['d1 R', 'd2 R']
    channel_list_L = ['d1 L', 'd2 L']
    BehPhoto = data.copy()
    final_list = []
    side = 'R'
    for rl in BehPhoto:
        rl_list = []
        if side == 'R':
            channel_list = channel_list_R
        elif side == 'L':
            channel_list = channel_list_L
        for ic in rl:
            ic_list =[]
            for combo in ic:
                ic_list.append(get_photodata_perTrial_df_secondStep(combo, channel_list))
            rl_list.append(ic_list)
        final_list.append(rl_list)
        
        side = 'L'
        
    return final_list    


def get_specificTime_fromPeriod(photo_data_RL_IC_tt, Period, NumberOfBins, Start_from_where):
    
    for rl in photo_data_RL_IC_tt:
        for ic in rl:
            for combo_dic in ic:
                try:
                    photo_data = combo_dic[Period]
                    if Start_from_where == 'end':
                        photo_data_UpSideDown = photo_data.iloc[::-1] #here i switch the order of rows. The last become the first ones and viceversa. 
                        #Nans at photo_data_UpSideDown are at the top so here we put them down
                        photo_data_UpSideDown = photo_data_UpSideDown.apply(lambda x: pd.Series(x.dropna().values))
                        #get from the end means that the first chunk will be taken (because it is up side down)
                        SpecificTime_photo_data = photo_data_UpSideDown[:NumberOfBins]
                        #Now Original order has to be restored  (but it will start with other bins because we just the last chunk)
                        SpecificTime_photo_data = SpecificTime_photo_data.iloc[::-1]
                        SpecificTime_photo_data = SpecificTime_photo_data.reset_index(drop=True)
                        str_name = 'last'
                    elif Start_from_where == 'start':
                        SpecificTime_photo_data = photo_data[:NumberOfBins]
                        str_name = 'first'
                    #df is incorporated to dictionary as a new period.
                    key_new_period = str_name+'_'+str(NumberOfBins)+'_bins_'+Period
                    combo_dic[key_new_period] = SpecificTime_photo_data
                    
                except KeyError: #No data for that trialtype
                    
                    pass 
                
    return photo_data_RL_IC_tt


