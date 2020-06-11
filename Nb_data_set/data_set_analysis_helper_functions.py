#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:37:22 2020

@author: gilmandelbaum
"""
from pathlib import Path
import pickle
import pandas as pd 

"""
laoding functions
"""


def generate_date_(Date):
    return('20'+str(Date)[:2]+'_'+str(Date)[2:4]+'_'+str(Date)[4:6])

def generate_name_and_date(Date,Mouse):
    return ('20'+str(Date)[:2]+'_'+str(Date)[2:4]+'_'+str(Date)[4:6]+'__'+Mouse)

def extract_data_set(Mouse_Date_FileName,data_dir,HowManyBack,seq_str):   
    
    version_nb6_to_import = seq_str[:seq_str.index('7')][-1]
    
    PhotoData_perTrial_channels_list = []
    counter = 1 
    
    #generate 3 lists.
    l_mouse = list(Mouse_Date_FileName["Mouse"]) 
    l_date_ = list(Mouse_Date_FileName.apply(lambda x: generate_date_(x["Date"]),axis=1))  
    l_date_and_name = list(Mouse_Date_FileName.apply(lambda x: generate_name_and_date(x["Date"],x["Mouse"]),axis=1))
    
    numer_of_sessions_dataset = len(l_mouse)
    
    for (mouse, date_, date_and_name) in zip(l_mouse, l_date_, l_date_and_name):
        
        print ("session number"+" "+str(counter)+" "+"was imported (out of"+" "+str(numer_of_sessions_dataset)+")")
        root = Path(data_dir+"/"+mouse+"/"+date_and_name+'/'+str(HowManyBack)+"_Back")
        d = mouse+"_"+date_+"Notebook_6_"+version_nb6_to_import+"_"+'seq'+seq_str[:seq_str.index('7')]+'.pickle'
        my_path = root / d 
        print (my_path)
        
        # open a file, where you stored the pickled data
        fileToOpen = open(my_path, 'rb')
        # load the pickle: 
        PhotoData_perTrial_channels = pickle.load(fileToOpen)
        
        counter += 1 
                
        PhotoData_perTrial_channels_list.append(PhotoData_perTrial_channels)
        
    return PhotoData_perTrial_channels_list



"""
used in data_set_plots_ic_and_sessions_combined
""" 

#etract the mean from a given session. Choice of right or left side, trial type, period to plot, 
#and the cell type. 
#gives back both the ipsi next and the contra next as a tuple  
def extract_rl_tt_period_celltype_mean_session(PhotoData_perTrial_channels,rl,tt,period,cell_type):
    
    #number_of_trials = len(PhotoData_perTrial_channels[rl][0][tt][period][cell_type].columns)
    
    mean_ipsi_next = PhotoData_perTrial_channels[rl][0][tt][period][cell_type].mean(axis=1)
    mean_contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type].mean(axis=1)
    
    #sem_ipsi_next = (PhotoData_perTrial_channels[rl][0][tt][period][cell_type].std(axis=1))/(number_of_trials**0.5)
    #sem_contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type].std(axis=1)/(number_of_trials**0.5)
    
    #return (mean_ipsi_next,sem_ipsi_next,mean_contra_next,sem_contra_next,number_of_trials)
    return (mean_ipsi_next,mean_contra_next)



def extract_rl_tt_period_celltype_mean_data_set (PhotoData_perTrial_channels_list,rl,tt,period,cell_type):
    df_ipsi_next = pd.DataFrame ()
    df_contra_next = pd.DataFrame ()
    for PhotoData_perTrial_channels in PhotoData_perTrial_channels_list:
        mean_ipsi_contra_next = extract_rl_tt_period_celltype_mean_session(PhotoData_perTrial_channels,rl,tt,period,cell_type)
        df_ipsi_next = pd.concat([df_ipsi_next,mean_ipsi_contra_next[0]],axis=1)
        df_contra_next = pd.concat([df_contra_next,mean_ipsi_contra_next[1]],axis=1)
    return df_ipsi_next, df_contra_next


    
    
    
    
    
    
    
    
    