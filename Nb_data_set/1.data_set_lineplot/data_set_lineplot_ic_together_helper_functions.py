
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
used to load data photometry: 
""" 

def extract_data_of_interest_ipsi_contra_per_session_helper (PhotoData_perTrial_channels,rl,tt,period,cell_type):
    try: 
        ipsi_next = PhotoData_perTrial_channels[rl][0][tt][period][cell_type]
        contra_next = PhotoData_perTrial_channels[rl][1][tt][period][cell_type]
        print ("full")
    except:
        ipsi_next = pd.DataFrame()
        contra_next = pd.DataFrame()
        print ("empty")
    return (ipsi_next,contra_next)
    


def extract_data_of_interest_ipsi_contra_data_set (PhotoData_perTrial_channels_data_set,
                                                   rl,tt,period,cell_type): 
    
    ipsi_contra_data_set = []
    
    for PhotoData_perTrial_channels in PhotoData_perTrial_channels_data_set:
        ipsi_contra = extract_data_of_interest_ipsi_contra_per_session_helper (PhotoData_perTrial_channels,rl,tt,period,cell_type)
        ipsi_contra_data_set.append(ipsi_contra)
        
    return (ipsi_contra_data_set) 



