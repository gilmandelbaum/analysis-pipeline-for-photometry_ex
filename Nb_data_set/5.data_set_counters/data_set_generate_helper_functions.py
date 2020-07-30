#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:34:17 2020

@author: gilmandelbaum
"""

from pathlib import Path
import pickle
import pandas as pd 
import tdt
"""
general loading functions
"""

def generate_date_(Date):
    return('20'+str(Date)[:2]+'_'+str(Date)[2:4]+'_'+str(Date)[4:6])

def generate_name_and_date(Date,Mouse):
    return ('20'+str(Date)[:2]+'_'+str(Date)[2:4]+'_'+str(Date)[4:6]+'__'+Mouse)


"""
0.data_set_generate_data_object_data_trial:
"""

def extract_data_object_data_trial(Mouse_Date_FileName,path,HowManyBack):
    data_trial_data_set = []
    counter = 1 
    
    l_mouse = list(Mouse_Date_FileName["mouse"]) 
    l_date_ = list(Mouse_Date_FileName.apply(lambda x: generate_date_(x["date"]),axis=1))  
    l_date_and_name = list(Mouse_Date_FileName.apply(lambda x: generate_name_and_date(x["date"],x["mouse"]),axis=1))
    
    numer_of_sessions_dataset = len(l_mouse)
    
    for (mouse, date_, date_and_name) in zip(l_mouse, l_date_, l_date_and_name):
        print ("session number"+" "+str(counter)+" "+"was imported (out of"+" "+str(numer_of_sessions_dataset)+")")
        root = Path(path+"/"+mouse+"/"+date_and_name+'/'+str(HowManyBack)+"_Back")
        d = mouse+"_"+date_+"Notebook_0_a"+'.pickle'
        my_path = root / d 
        
        fileToOpen = open(my_path, 'rb')
        # load the pickle: 
        data_trial = pickle.load(fileToOpen)
        counter += 1       
        data_trial_data_set.append(data_trial)  
    
    return data_trial_data_set

"""
1.data_set_generate_data_object_photometry_raw_traces
"""


def reading_in_photometryData_all_Channels(photometry_data):
    
    photometry_all_channels_d = {}
    photometry_all_channels_d["d2 R"]=photometry_data.streams.grn1.data 
    photometry_all_channels_d["d1 R"]=photometry_data.streams.red1.data 
    
    
    photometry_all_channels_d["d2 L"]=photometry_data.streams.grn2.data 
    photometry_all_channels_d["d1 L"]=photometry_data.streams.red2.data 
    
    photometry_all_channels= pd.DataFrame(data=photometry_all_channels_d)
    
    return (photometry_all_channels)


def extract_data_object_photometry_raw_traces(Mouse_Date_FileName,path_to_import,path_to_save):   

    l_mouse = list(Mouse_Date_FileName["mouse"]) 
    l_photo_day = list(Mouse_Date_FileName["file name"]) 

    raw_photo_data_per_trial_channels_data_set = []
    counter = 1 
    
    
    numer_of_sessions_dataset = len(l_mouse)
    
    for (mouse, photo_day) in zip(l_mouse, l_photo_day):
        print ("session number"+" "+str(counter)+" "+"was imported (out of"+" "+str(numer_of_sessions_dataset)+")")
        
        photometry_data = tdt.read_block(path_to_import+"/"+mouse+"/"+photo_day)
        photometry_data = reading_in_photometryData_all_Channels(photometry_data)
        raw_photo_data_per_trial_channels_data_set.append(photometry_data)
        
        counter += 1 
        
    return raw_photo_data_per_trial_channels_data_set


"""
2.data_set_generate_data_object_photometry_after_down_sampling
"""

def extract_data_object_photometry_after_down_sampling(Mouse_Date_FileName,path,version_of_notebook_2_3,HowManyBack):
    version_of_notebook_3 = version_of_notebook_2_3[-1]
    PhotoData_perTrial_channels_data_set = []
    counter = 1 
    
    l_mouse = list(Mouse_Date_FileName["mouse"]) 
    l_date_ = list(Mouse_Date_FileName.apply(lambda x: generate_date_(x["date"]),axis=1))  
    l_date_and_name = list(Mouse_Date_FileName.apply(lambda x: generate_name_and_date(x["date"],x["mouse"]),axis=1))
    
    numer_of_sessions_dataset = len(l_mouse)
    
    for (mouse, date_, date_and_name) in zip(l_mouse, l_date_, l_date_and_name):
        print ("session number"+" "+str(counter)+" "+"was imported (out of"+" "+str(numer_of_sessions_dataset)+")")
        root = Path(path+"/"+mouse+"/"+date_and_name+'/'+str(HowManyBack)+"_Back")
        d = mouse+"_"+date_+"Notebook_3_"+version_of_notebook_3+"_seq"+version_of_notebook_2_3+'.pickle'
        print (d)
        my_path = root / d 
        
        fileToOpen = open(my_path, 'rb')
        # load the pickle: 
        PhotoData_perTrial_channels = pickle.load(fileToOpen)
        counter += 1       
        PhotoData_perTrial_channels_data_set.append(PhotoData_perTrial_channels)  
    
    return PhotoData_perTrial_channels_data_set



"""
3.data_set_generate_data_object_photometry_after_processing
"""


def extract_data_object_photometry_after_processing(Mouse_Date_FileName,path,HowManyBack,seq_str):   
    
    version_nb6_to_import = seq_str[:seq_str.index('7')][-1]
    
    PhotoData_perTrial_channels_data_set = []
    counter = 1 
    
    #generate 3 lists.
    l_mouse = list(Mouse_Date_FileName["mouse"]) 
    l_date_ = list(Mouse_Date_FileName.apply(lambda x: generate_date_(x["date"]),axis=1))  
    l_date_and_name = list(Mouse_Date_FileName.apply(lambda x: generate_name_and_date(x["date"],x["mouse"]),axis=1))
    
    numer_of_sessions_dataset = len(l_mouse)
    
    for (mouse, date_, date_and_name) in zip(l_mouse, l_date_, l_date_and_name):
        
        print ("session number"+" "+str(counter)+" "+"was imported (out of"+" "+str(numer_of_sessions_dataset)+")")
        root = Path(path+"/"+mouse+"/"+date_and_name+'/'+str(HowManyBack)+"_Back")
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
4.data_set_generate_data_object_data_lick
"""




