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

def extract_rl_tt_period_celltype_mean(PhotoData_perTrial_channels,rl,tt,period,cell_type):
    
    number_of_trials = len(PhotoData_perTrial_channels[rl][0][tt][period][cell_type].columns)
    
    mean_ipsi_next = PhotoData_perTrial_channels[rl][0][tt][period][cell_type].mean(axis=1)
    mean_contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type].mean(axis=1)
    
    sem_ipsi_next = (PhotoData_perTrial_channels[rl][0][tt][period][cell_type].std(axis=1))/(number_of_trials**0.5)
    sem_contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type].std(axis=1)/(number_of_trials**0.5)
    
    
    return (mean_ipsi_next,sem_ipsi_next,mean_contra_next,sem_contra_next,number_of_trials)


"""
for 7b.
"""

def calculate_sem (data):
    sem_up_ipsi_next = data[0]+data[1]/2
    sem_down_ipsi_next = data[0]-data[1]/2
    
    sem_up_contra_next = data[2]+data[3]/2
    sem_down_contra_next = data[2]-data[3]/2
    
    return (sem_up_ipsi_next,sem_down_ipsi_next,sem_up_contra_next,sem_down_contra_next)



def plot_ipsi_contra_together (data,sem,trial_type,cell_type,y_axis,path_to_plot):

    plt.plot(data[0],linewidth=2, label="ipsi_next"+" "+"("+str(data[4])+")")
    plt.plot(data[2],linewidth=2, label="contra_next"+" "+"("+str(data[4])+")")
    
    plt.plot(sem[0],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem[1],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem[2],color='black', linewidth=0.5,alpha=0.8)
    plt.plot(sem[3],color='black', linewidth=0.5,alpha=0.8)
    
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
    
     