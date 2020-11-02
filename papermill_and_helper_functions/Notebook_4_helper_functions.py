
import pandas as pd 


#function that adds a flag for notebook 4_a: 

def tag_period(beh_photo_align, period_name, states_list):
    

    Period_rows_list = []

    for states in states_list:
        state_start = states[0]
        state_end = states[1]
        Period_rows_list.append(beh_photo_align.loc[(beh_photo_align['iState_start'] == state_start) & (beh_photo_align['iState_end'] == state_end)])
        
    Period_rows = pd.concat(Period_rows_list)
    Period_rows = Period_rows.sort_index()
    
    Period_rows[period_name]=Period_rows['Real_nTrials']
    Period_df = pd.DataFrame(Period_rows[period_name])
    return Period_df



#function that adds a flag for notebook 4_b: 
    
def tag_period_from_previousTrial(beh_photo_align, period_name, states_list):
    Period_rows_list = []

    for states in states_list:
        state_start = states[0]
        state_end = states[1]
        Period_rows_list.append(beh_photo_align.loc[(beh_photo_align['iState_start'] == state_start) & (beh_photo_align['iState_end'] == state_end)])
        
    Period_rows = pd.concat(Period_rows_list)
    Period_rows = Period_rows.sort_index()
    
    Period_rows[period_name+'_fromPrevTrial']=Period_rows['Real_nTrials']
    Period_df = pd.DataFrame(Period_rows[period_name+'_fromPrevTrial'])+1
    return Period_df


#function that adds a flag for notebook 4_e: 
    
def tag_ENLp(beh_photo_align,state_ENLp):
    rows_list = []
    for state in state_ENLp:
        state_start = state[0]
        state_end = state[1]
        
        rows_list.append(beh_photo_align.loc[(beh_photo_align['iState_start'] == state_start) & (beh_photo_align['iState_end'] == state_end)])
    
    #take only first two state transitions. In the standard case that would be 29 to 32 and 29 to 30. 
    firstCon = rows_list[0]
    SecondCon = rows_list[1]
    #make a data frame with the data: 
    frames = [firstCon,SecondCon]
    dfEnlPeBins = pd.concat(frames)
    
    #sort data frame: 
    dfEnlPeBins = dfEnlPeBins.sort_index()
    #take the diff on the Real_nTrials column 
    diffReal_nTrials = dfEnlPeBins["Real_nTrials"].diff()
    
    #make a new column: 
    dfEnlPeBins["diffENLp"] = diffReal_nTrials
    #take only the first ENLP:
    dfEnlPeBins = dfEnlPeBins.loc[dfEnlPeBins["diffENLp"] !=0]
    #tak only ENLP that occured 250ms from the start of the trial 
    dfEnlPeBins = dfEnlPeBins.loc[dfEnlPeBins["iOccurrence"] >50]
    
    #make a dataframe from what is left: 
    dfEnlPeBins = pd.DataFrame(dfEnlPeBins["Real_nTrials"])
    
    #change column header name: 
    dfEnlPeBins = dfEnlPeBins.rename(columns={"Real_nTrials": "firstENLp"})
    
    return(dfEnlPeBins)


















