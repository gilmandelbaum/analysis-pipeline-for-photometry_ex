# Notebook 6:
adds combination of periods together from notebook 5. 
input: notebook 5. 
output: same structure as notebook 5 but with an added period combining periods. 

How notebook 6s work: 

Each notebook 6 can run stand alone with a seq_str up until Nb5, including. 
So for example, if the seq_str for the analysis is 0a1b2a3b4abcde5a6c7a , notebook 6c will use the notebook 5 output object with the name 0a1b2a3b4abcde5a. 

If there are multiple notebooks 6 and you are running the first version of the notebook 6 notebook 5 will be loaded. 
For example, if the seq_str is 0a1b2a3b4abcde5a6bec7a , and we are running notebook 6b. Notebook 6b will load notebook 5 output object with the name 0a1b2a3b4abcde5a. 

However, if If there are multiple notebooks 6 and you are not running the first version of the notebook 6, the previous notebook 6 will be loaded. 
For example, if the seq_str is 0a1b2a3b4abcde5a6bec7a , and we are running notebook 6e. Notebook 6e will load notebook 6 output object with the name 0a1b2a3b4abcde5a6b. 


6_a: key 'combined_periods_1'. combining 1 sec pre-consumption lick, 3 sec rewarded or non rewarded period and 1 sec ENL period before the cue. 

6_b: key 'combined_periods_2'. combining pre_Cue_to_Sel, Cue_to_Sel and Reward_NoReward. 

6_c: key 'combined_periods_3'. pre_firstENLp_tag, firstENLp_tag, and post_firstENLp_tag. 
