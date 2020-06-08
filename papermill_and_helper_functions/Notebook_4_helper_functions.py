
import pandas as pd 


#fuction that adds a flag for notebook 4_a: 

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


#function that adds a flag for notebook 4_c: 
    
def tag_ENLp(beh_photo_align,state_ENLp):
    rows_list = []
    for state in state_ENLp:
        state_start = state[0]
        state_end = state[1]
        
        rows_list.append(beh_photo_align.loc[(beh_photo_align['iState_start'] == state_start) & (beh_photo_align['iState_end'] == state_end)])
    
    firstCon = rows_list[0]
    SecondCon = rows_list[1]
    frames = [firstCon,SecondCon]
    dfEnlPeBins = pd.concat(frames)
    dfEnlPeBins = dfEnlPeBins.sort_index()
    diffReal_nTrials = dfEnlPeBins["Real_nTrials"].diff()
    dfEnlPeBins["diffENLp"] = diffReal_nTrials
    dfEnlPeBins = dfEnlPeBins.loc[dfEnlPeBins["diffENLp"] !=0]
    dfEnlPeBins = dfEnlPeBins.loc[dfEnlPeBins["iOccurrence"] >50]
    dfEnlPeBins = pd.DataFrame(dfEnlPeBins["Real_nTrials"])
    dfEnlPeBins = dfEnlPeBins.rename(columns={"Real_nTrials": "firstENLp"})
    return(dfEnlPeBins)