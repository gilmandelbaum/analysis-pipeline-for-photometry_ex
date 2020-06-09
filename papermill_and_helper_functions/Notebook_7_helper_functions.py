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
    mean_ipsi_next = PhotoData_perTrial_channels[rl][0][tt][period][cell_type].mean(axis=1)
    mean_contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type].mean(axis=1)
    number_of_trials = len(PhotoData_perTrial_channels[rl][0][tt][period][cell_type].columns)
    return (mean_ipsi_next,mean_contra_next,number_of_trials)
"""
for 7b.
"""


def plot_ipsi_contra_together (data,trial_type,cell_type,y_axis,path_to_plot):

    plt.plot(data[0], label="ipsi_next"+" "+"("+str(data[2])+")")
    plt.plot(data[1], label="contra_next"+" "+"("+str(data[2])+")")

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
    
     