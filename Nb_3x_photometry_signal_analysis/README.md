# Notebook 3:
processing neural data 
input: notebook 2 
output: same as notebook 2 but with neural data processed. 

3_a: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline.  

3_b: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline.  Z score on full session. 

3_c: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline and 10 seconds Z score sliding window.

3_d: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline.  Z score on full session. Smoothing using 1 sec sliding window with avg. 

3_e: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline.  Z score on full session. Take the derivative of that. not yet working. 

3_f: df/f using a Sliding window of 10 seconds and 10 percentile to calculate baseline.  deconvovle signal. For more info: https://caiman.readthedocs.io/en/master/core_functions.html 

3_g: df/f using a Sliding window of 10 seconds and 1 percentile to calculate baseline.

3_h: df/f using a Sliding window of 10 seconds and 1 percentile to calculate baseline. Smoothing using 1 sec sliding window with avg. 

3_i: df/f using a Sliding window of 10 seconds and 1 percentile to calculate baseline. Smoothing using 150ms sliding window with avg. 

3_j: df/f using a Sliding window of 10 seconds and 0.5 percentile to calculate baseline. Smoothing using 1 sec sliding window with avg for d1 and 250ms for d2. Z score on that and add the value 2. 

3_k: df/f using a Sliding window of 10 seconds and 0.5 percentile to calculate baseline. Smoothing using 1 sec sliding window with avg for d1 and 250ms for d2. Z score. 

3_l: Normalize with sliding window of 2 min. Smoothing using 500ms sliding window with avg for d1 and 250ms for d2. 
