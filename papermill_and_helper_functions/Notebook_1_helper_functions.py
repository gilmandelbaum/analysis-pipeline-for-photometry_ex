#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:45:51 2020

@author: gilmandelbaum
"""
import itertools



"""
split the data frame into 4 data frame. 
[[[R.i],[R.c]], [[L.i],[L.c]]] 
the structure of the list is Right side IPSI CONTRA Left side IPSI CONTRA. 
"""

def separate_between_RIC_LIC_blocks(df): 
    R_L_List= []
    
    for n in ['R', 'L']:
        BlocksIpsilat= df[df["direction"]==n]
        BlocksContralat= df[df["direction"]!=n]
        R_L_List.append([BlocksIpsilat, BlocksContralat])
        
    
    return R_L_List 



"""
function that only works with one back and two back. 

"""  

def get_combination_previous_trial(df,HowManyBack):
    #1= reward. 2=non rewarded (HowManyBack*2 is the amount of previous trials that we will look at).
    combinations =list(itertools.product([2,1], repeat=HowManyBack*2))
    
    total=[]
    
    for rl in df:
        rl_l=[]
        for ic in rl:
            ic_l=[]   
            for i in combinations:
                if HowManyBack==2:
                    ic_l.append(ic[(ic['-2_r'] == i[0]) & (ic['-2_d']==i[1])& (ic['-1_r']==i[2])& (ic['-1_d']==i[3])])
                elif HowManyBack==1:
                    ic_l.append(ic[(ic['-1_r'] == i[0]) & (ic['-1_d']==i[1])])

            rl_l.append(ic_l)  
        total.append(rl_l)
    return total ####for one back total structure is: [Right or Left][Ipsi or Contra][22,21,12,11]..



"""
get lists of the trial numbers that correspond to the different trial types
"""

def get_nTrials_tt(data):
    total= []
    for rl in data:
        rl_l=[]
        for ic in rl:
            ic_l=[]
            for i in ic:
                ic_l.append(i.index)
                
            rl_l.append(ic_l)
            
        total.append(rl_l)
    return total 



"""
for notebook 1_b and 1_C: 
"""

def divide_withWithout_ENLp_noCuep(df_trial, ENLp):

    if ENLp== 'noENLp':
        noENLp_df= df_trial[df_trial['n_ENL']==1]
        noENLpnoCuep_df= noENLp_df[noENLp_df['n_Cue']==1]
        return noENLpnoCuep_df

    elif ENLp== 'withENLp':

        ENLp_df= df_trial[df_trial['n_ENL']>1]
        return ENLp_df




"""
for notebook 1_d:
"""

def get_nTrials_tt_boot_strap(data):
    total= []
    for rl in data:
        rl_l=[]
        for ic in rl:
            ic_l=[]
            for i,trial_df in enumerate (ic):  
                #print (i)
                if i ==0: #lose_switch
                    trial_df = trial_df.sample(n = 30, replace = True)     
                elif i ==3: #win stay
                    trial_df = trial_df.sample(n = 100, replace = True) 
                ic_l.append(trial_df.index)
            rl_l.append(ic_l)
        total.append(rl_l)
    return total

