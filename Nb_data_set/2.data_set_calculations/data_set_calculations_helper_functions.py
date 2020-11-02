#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:41:24 2020

@author: gilmandelbaum
"""
import pandas as pd 

def extract_data_of_interest_ipsi_contra_per_session_helper (PhotoData_perTrial_channels,
                                                             rl,
                                                             tt,
                                                             period,
                                                             cell_type):
    
    try:
        ipsi_next = PhotoData_perTrial_channels[rl][0][tt][period][cell_type]
    except KeyError:
        period
        ipsi_next = pd.DataFrame()
    
    try:    
        contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type]
    except  KeyError:
        period
        contra_next = pd.DataFrame()
        
    return (ipsi_next,contra_next)




def extract_data_of_interest_ipsi_contra_data_set (PhotoData_perTrial_channels_data_set,
                                                   rl,tt,period,cell_type): 
    
    ipsi_contra_data_set = []
    
    for PhotoData_perTrial_channels in PhotoData_perTrial_channels_data_set:
        ipsi_contra = extract_data_of_interest_ipsi_contra_per_session_helper (PhotoData_perTrial_channels,rl,tt,period,cell_type)
        ipsi_contra_data_set.append(ipsi_contra)
        
    return (ipsi_contra_data_set)
    
