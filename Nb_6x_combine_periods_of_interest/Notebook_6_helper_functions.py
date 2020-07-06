#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:21:38 2020

@author: gilmandelbaum
"""
import pandas as pd
from pathlib import Path
import pickle

"""
How notebook 6s work:

Each notebook 6 can run stand alone with a seq_str up until Nb5, including. 
So for example, if the seq_str for the analysis is 0a1b2a3b4abcde5a6c7a , 
notebook 6c will use the notebook 5 output object with the name 0a1b2a3b4abcde5a.

If there are multiple notebooks 6 and you are running 
the first version of the notebook 6 notebook 5 will be loaded. 
For example, if the seq_str is 0a1b2a3b4abcde5a6bec7a , 
and we are running notebook 6b. 
Notebook 6b will load notebook 5 output object with the name 0a1b2a3b4abcde5a.

However, if If there are multiple notebooks 6 and you are not running 
the first version of the notebook 6, the previous notebook 6 will be loaded. 
For example, if the seq_str is 0a1b2a3b4abcde5a6bec7a , and we are running notebook 6e. 
Notebook 6e will load notebook 6 output object with the name 0a1b2a3b4abcde5a6b.
"""


def load_data_obj_general(data_dir_output,mouse,data_day,date,HowManyBack,seq_str,Nb_name,Nb5):
    seq_until_Nb5= seq_str[:seq_str.index('6')]
    print ("seq_until_Nb5:"+" "+seq_until_Nb5)
    Nb6s_to_run = seq_str[seq_str.index("6"):seq_str.index("7")]
    print ("Nb6s_to_run:"+" "+Nb6s_to_run)
    #this means that there is only one version. 
    
    if (len(Nb6s_to_run) == 2) or (Nb6s_to_run[1] ==  Nb_name[-1]): 
        print ("first notebook")
        #so you load notebook5. 
        
        
        #finds its path: 
        root = Path(data_dir_output+"/"+mouse+"/"+data_day+'/'+str(HowManyBack)+"_Back")
        d = mouse+"_"+date+"Notebook_5_"+Nb5+"_"+"seq"+seq_until_Nb5+'.pickle'
        my_path = root / d 
        
        #open the object: 
        fileToOpen = open(my_path, 'rb')
        PhotoData_perTrial_channels = pickle.load(fileToOpen)
        print ("loaded:"+str(my_path))
        return (PhotoData_perTrial_channels)
            
    else: 
        #this means that you are not running the first one in the seq of notebook 6s. 
        #so you need to load a notebook 6. 
        print ("not first notebook")
        seq_6s_before_this_notebook = Nb6s_to_run[0:Nb6s_to_run.index(Nb_name[-1])]
        #print (seq_6s_before_this_notebook)
        seq_until_prev_Nb = seq_until_Nb5+seq_6s_before_this_notebook
        #print (seq_until_prev_Nb)
        
        #finds its path: 
        root = Path(data_dir_output+"/"+mouse+"/"+data_day+'/'+str(HowManyBack)+"_Back")
        d = mouse+"_"+date+"Notebook_6_"+seq_6s_before_this_notebook[-1]+"_"+"seq"+seq_until_prev_Nb+'.pickle'
        my_path = root / d 
        
        #open the object: 
        fileToOpen = open(my_path, 'rb')
        PhotoData_perTrial_channels = pickle.load(fileToOpen)
        print ("loaded seq"+str(my_path))
        return (PhotoData_perTrial_channels)

     
      
        
"""
getting the seq for the notebook
"""


def seq_for_this_nb (seq_str,Nb_name):
    
    seq_until_Nb5= seq_str[:seq_str.index('6')]
    Nb6s_to_run = seq_str[seq_str.index("6"):seq_str.index("7")]
    
    if (len(Nb6s_to_run) == 2) or (Nb6s_to_run[1] ==  Nb_name[-1]):
        seq_for_this_nb = seq_until_Nb5+"6"+Nb6s_to_run[1]
    else: 
        seq_6s_with_this_notebook = Nb6s_to_run[0:(Nb6s_to_run.index(Nb_name[-1])+1)]
        seq_for_this_nb = seq_until_Nb5+seq_6s_with_this_notebook
    print (seq_for_this_nb)
    return (seq_for_this_nb)



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