#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:21:38 2020

@author: gilmandelbaum
"""
import pandas as pd

#for notebook 6a: 

def combine_periods_1(photo_data):
#Combines: -1secPreConsumption + Consumption + last_sec_ENL + Cue
    for rl in photo_data:
        for ic in rl:
            for combo_dict in ic:
                try:
                    #Periods:
                    Pre_RewNonRew = combo_dict['pre_Reward_NoReward_tag']
                    first_600_bins_Reward_NoReward = combo_dict['first_600_bins_Reward_NoReward_tag']
                    last_200_bins_ENL = combo_dict['last_200_bins_ENL_tag'] #should i make this more general? how can i do it?
                    #first_bins_Cue_to_Sel = combo_dict['first_15_bins_Cue_to_Sel']
                    combined_periods = pd.concat([Pre_RewNonRew, first_600_bins_Reward_NoReward , last_200_bins_ENL])
                    combined_periods = combined_periods.reset_index(drop=True)
                    combo_dict['combined_periods_1']= combined_periods
                    print ("periodsCombined")
                except KeyError:
                    pass
                    print ("no new key")
    return photo_data





def combine_periods_2(photo_data):
#Combines: -1secPreConsumption + Consumption + last_sec_ENL + Cue
    for rl in photo_data:
        for ic in rl:
            for combo_dict in ic:
                try:
                    #Periods:
                    pre_Cue_to_Sel = combo_dict['pre_Cue_to_Sel_tag']
                    Cue_to_Sel = combo_dict['Cue_to_Sel_tag']
                    Reward_NoReward = combo_dict['Reward_NoReward_tag'] #should i make this more general? how can i do it?
                    #first_bins_Cue_to_Sel = combo_dict['first_15_bins_Cue_to_Sel']
                    combined_periods = pd.concat([pre_Cue_to_Sel, Cue_to_Sel , Reward_NoReward])
                    combined_periods = combined_periods.reset_index(drop=True)
                    combo_dict['combined_periods_2']= combined_periods
                    print ("periodsCombined")
                except KeyError:
                    pass
                    print ("no new key")
    return photo_data




def combine_periods_3(photo_data):
#Combines: -1secPreConsumption + Consumption + last_sec_ENL + Cue
    for rl in photo_data:
        for ic in rl:
            for combo_dict in ic:
                try:
                    #Periods:
                    pre_firstENLp_tag = combo_dict['pre_firstENLp_tag']
                    firstENLp_tag = combo_dict['firstENLp_tag']
                    post_firstENLp_tag = combo_dict['post_firstENLp_tag'] #should i make this more general? how can i do it?
                    #first_bins_Cue_to_Sel = combo_dict['first_15_bins_Cue_to_Sel']
                    combined_periods = pd.concat([pre_firstENLp_tag, firstENLp_tag , post_firstENLp_tag])
                    combined_periods = combined_periods.reset_index(drop=True)
                    combo_dict['combined_periods_3']= combined_periods
                    print ("periodsCombined")
                except KeyError:
                    pass
                    print ("no new key")
    return photo_data