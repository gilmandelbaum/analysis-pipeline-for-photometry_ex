#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:56:12 2020

@author: gilmandelbaum
"""

import matplotlib.pyplot as plt

"""
for 7b. 
get the mean of trials from the right or the left side of the brain. 
get it from a specific trial type 
get it from a specific period of interest 
get a specific cell type 
"""

def extract_data_of_interest_ipsi_contra_per_session (PhotoData_perTrial_channels,rl,tt,period,cell_type):
    ipsi_next = PhotoData_perTrial_channels[rl][0][tt][period][cell_type]
    contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type]
    return (ipsi_next,contra_next)
    
def calculate_mean_sem(data_ipsi_contra):
    
    number_of_trials_ipsi = len(data_ipsi_contra[0].columns)
    number_of_trials_contra = len(data_ipsi_contra[1].columns)
    
    mean_ipsi_next = data_ipsi_contra[0].mean(axis=1)
    mean_contra_next = data_ipsi_contra[1].mean(axis=1)
    
    sem_ipsi_next = data_ipsi_contra[0].std(axis=1)/(number_of_trials_ipsi**0.5)
    sem_contra_next = data_ipsi_contra[1].std(axis=1)/(number_of_trials_contra**0.5)
    
    
    return (mean_ipsi_next,sem_ipsi_next,mean_contra_next,sem_contra_next,number_of_trials_ipsi,number_of_trials_contra)


"""
for 7b.
"""

def make_sem_traces (data_ipsi_contra_mean_sem):
    sem_up_ipsi_next = data_ipsi_contra_mean_sem[0]+data_ipsi_contra_mean_sem[1]/2
    sem_down_ipsi_next = data_ipsi_contra_mean_sem[0]-data_ipsi_contra_mean_sem[1]/2
    
    sem_up_contra_next = data_ipsi_contra_mean_sem[2]+data_ipsi_contra_mean_sem[3]/2
    sem_down_contra_next = data_ipsi_contra_mean_sem[2]-data_ipsi_contra_mean_sem[3]/2
    
    return (sem_up_ipsi_next,sem_down_ipsi_next,sem_up_contra_next,sem_down_contra_next)



def plot_ipsi_contra_together (data_ipsi_contra_mean_sem,sem_traces,
                               trial_type,cell_type,y_axis,path_to_plot):

    plt.plot(data_ipsi_contra_mean_sem[0],linewidth=2, label="ipsi_next"+" "+"("+str(data_ipsi_contra_mean_sem[4])+")")
    plt.plot(data_ipsi_contra_mean_sem[2],linewidth=2, label="contra_next"+" "+"("+str(data_ipsi_contra_mean_sem[5])+")")
    
    plt.plot(sem_traces[0],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem_traces[1],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem_traces[2],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem_traces[3],color='black', linewidth=0.5,alpha=0.8)
    
    # Add legend
    plt.legend(loc='lower left')
    
    # Add title and x, y labels
    plt.title(trial_type, fontsize=16, fontweight='bold')
    plt.suptitle(cell_type, fontsize=16)

    plt.xlabel("time_bins")

    #the y axis is defined in the paper mill. This allows to run 7_b with 3a,3b,3c and any future 3s, easliy changing the 
    #the name of the y axis to not cause confusion. 
    plt.ylabel(y_axis)
    plt.savefig(path_to_plot+"_"+trial_type+cell_type+'.pdf')
    plt.show()
    
     
    
    
    
    
    
    
    
    