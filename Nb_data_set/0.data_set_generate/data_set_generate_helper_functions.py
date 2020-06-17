#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:34:17 2020

@author: gilmandelbaum
"""

from pathlib import Path
import pickle


"""
loading functions
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