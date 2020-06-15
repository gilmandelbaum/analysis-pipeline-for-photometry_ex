#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:37:22 2020

@author: gilmandelbaum
"""
from pathlib import Path
import pickle
import pandas as pd 
import matplotlib.pyplot as plt

"""
laoding functions
"""


def generate_date_(Date):
    return('20'+str(Date)[:2]+'_'+str(Date)[2:4]+'_'+str(Date)[4:6])

def generate_name_and_date(Date,Mouse):
    return ('20'+str(Date)[:2]+'_'+str(Date)[2:4]+'_'+str(Date)[4:6]+'__'+Mouse)

def extract_data_set(Mouse_Date_FileName,data_to_be_plotted,HowManyBack,seq_str):   
    
    version_nb6_to_import = seq_str[:seq_str.index('7')][-1]
    
    PhotoData_perTrial_channels_data_set = []
    counter = 1 
    
    #generate 3 lists.
    l_mouse = list(Mouse_Date_FileName["Mouse"]) 
    l_date_ = list(Mouse_Date_FileName.apply(lambda x: generate_date_(x["Date"]),axis=1))  
    l_date_and_name = list(Mouse_Date_FileName.apply(lambda x: generate_name_and_date(x["Date"],x["Mouse"]),axis=1))
    
    numer_of_sessions_dataset = len(l_mouse)
    
    for (mouse, date_, date_and_name) in zip(l_mouse, l_date_, l_date_and_name):
        
        print ("session number"+" "+str(counter)+" "+"was imported (out of"+" "+str(numer_of_sessions_dataset)+")")
        root = Path(data_to_be_plotted+"/"+mouse+"/"+date_and_name+'/'+str(HowManyBack)+"_Back")
        d = mouse+"_"+date_+"Notebook_6_"+version_nb6_to_import+"_"+'seq'+seq_str[:seq_str.index('7')]+'.pickle'
        my_path = root / d 
        print (my_path)
        
        # open a file, where you stored the pickled data
        fileToOpen = open(my_path, 'rb')
        # load the pickle: 
        PhotoData_perTrial_channels = pickle.load(fileToOpen)
        
        counter += 1 
                
        PhotoData_perTrial_channels_data_set.append(PhotoData_perTrial_channels)
        
    return PhotoData_perTrial_channels_data_set



"""
used in data_set_plots_ic_and_sessions_combined
""" 

def extract_data_of_interest_ipsi_contra_per_session_helper (PhotoData_perTrial_channels,rl,tt,period,cell_type):
    ipsi_next = PhotoData_perTrial_channels[rl][0][tt][period][cell_type]
    contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type]
    return (ipsi_next,contra_next)
    


def extract_data_of_interest_ipsi_contra_data_set (PhotoData_perTrial_channels_data_set,
                                                   rl,tt,period,cell_type): 
    
    ipsi_contra_data_set = []
    
    for PhotoData_perTrial_channels in PhotoData_perTrial_channels_data_set:
        ipsi_contra = extract_data_of_interest_ipsi_contra_per_session_helper (PhotoData_perTrial_channels,rl,tt,period,cell_type)
        ipsi_contra_data_set.append(ipsi_contra)
        
    return (ipsi_contra_data_set)
    
    
def calculate_mean_data_set (ipsi_contra_data_set):
    
    df_ipsi_next = pd.DataFrame()
    df_contra_next = pd.DataFrame()
    
    for data_ipsi_contra in ipsi_contra_data_set:
        
        mean_ipsi_next = data_ipsi_contra[0].mean(axis=1)
        mean_contra_next = data_ipsi_contra[1].mean(axis=1)
        df_ipsi_next = pd.concat([df_ipsi_next,mean_ipsi_next],axis=1)
        df_contra_next = pd.concat([df_contra_next,mean_contra_next],axis=1)
        
        
    return (df_ipsi_next,df_contra_next)



"""
used in data_set_plots_ic_and_sessions_combined
similar to 7b
"""


def calculate_mean_sem(data_ipsi_contra):
    
    number_of_trials_ipsi_next = len(data_ipsi_contra[0].columns)
    number_of_trials_contra_next = len(data_ipsi_contra[1].columns)
    
    mean_ipsi_next = data_ipsi_contra[0].mean(axis=1)
    mean_contra_next = data_ipsi_contra[1].mean(axis=1)
    
    sem_ipsi_next = data_ipsi_contra[0].std(axis=1)/(number_of_trials_ipsi_next**0.5)
    sem_contra_next = data_ipsi_contra[1].std(axis=1)/(number_of_trials_contra_next**0.5)
    
    
    return (mean_ipsi_next,sem_ipsi_next,mean_contra_next,sem_contra_next,number_of_trials_ipsi_next,number_of_trials_contra_next)
    #in the return - its called trials but its actually sessions. I am just using the same code as notebook 7s so kept it the same.


#make_sem_traces is a function that helps making the sem traces for the plots. 
def make_sem_traces (data_ipsi_contra_mean_sem):
    sem_up_ipsi_next = data_ipsi_contra_mean_sem[0]+data_ipsi_contra_mean_sem[1]/2
    sem_down_ipsi_next = data_ipsi_contra_mean_sem[0]-data_ipsi_contra_mean_sem[1]/2
    
    sem_up_contra_next = data_ipsi_contra_mean_sem[2]+data_ipsi_contra_mean_sem[3]/2
    sem_down_contra_next = data_ipsi_contra_mean_sem[2]-data_ipsi_contra_mean_sem[3]/2
    
    return (sem_up_ipsi_next,sem_down_ipsi_next,sem_up_contra_next,sem_down_contra_next)






#data_ipsi_contra_mean_sem is the output of calculate_mean_sem
#sem_traces is the output of make_sem_traces.


def plot_ipsi_contra_together (data_ipsi_contra_mean_sem,sem_traces,
                               trial_type,period_of_interest,cell_type,y_axis,path_to_plot):
    #number of sessions is the same ipsi and contra. 
    
    plt.plot(data_ipsi_contra_mean_sem[0],linewidth=2, label="ipsi_next"+" "+"("+str(data_ipsi_contra_mean_sem[4])+")")
    plt.plot(data_ipsi_contra_mean_sem[2],linewidth=2, label="contra_next"+" "+"("+str(data_ipsi_contra_mean_sem[4])+")")
    
    plt.plot(sem_traces[0],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem_traces[1],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem_traces[2],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem_traces[3],color='black', linewidth=0.5,alpha=0.8)
    
    # Add legend
    plt.legend(loc='lower left')
    
    
    # Add title and x, y labels
    title = trial_type+"_"+"("+period_of_interest+")"
    plt.title(title, fontsize=16, fontweight='bold')
    plt.suptitle(cell_type, fontsize=16)

    plt.xlabel("time_bins")
    
    #the y axis is defined in the paper mill. This allows to run 7_b with 3a,3b,3c and any future 3s, easliy changing the 
    #the name of the y axis to not cause confusion. 
    plt.ylabel(y_axis)
    plt.savefig(path_to_plot+"/"+"_"+trial_type+cell_type+"_"+period_of_interest+'.pdf')
    plt.show()
    
     
    


    
    
    
    