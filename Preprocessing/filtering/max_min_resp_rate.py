import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from respiratory_phases_interval_extraction.peak_detector_algorithm import find_peaks_valleys
import numpy as np

def max_min_rate_calc(input_signal,segment_time):
    flag=0
    fs=10
    segment_length=segment_time*fs
    min_breathing_rate=1000
    max_breathing_rate=0
    min_allowed_resp_rate=6
    max_allowed_resp_rate=20
    abnormalities_index=[]
    segments_index=np.arange(0,len(input_signal),segment_length)

    if len(input_signal)>segments_index[-1]:
        flag=1
    
    for i in range(len(segments_index)):
        if i==len(segments_index)-1:
            if flag==1:
                segments_index=np.append(segments_index,len(input_signal)-1)
            else :
                return min_breathing_rate,max_breathing_rate
                
                
        data_segment=input_signal[segments_index[i]:segments_index[i+1]]
        peaks_index,valleys_index=find_peaks_valleys(data_segment,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=0,lower_RRPm=8,upper_RRPm=20)
        breathing_rate=len(peaks_index)/(segment_time/60)        
        
        if (breathing_rate > max_allowed_resp_rate) or (breathing_rate < min_allowed_resp_rate)  :
            abnormalities_index=np.append(abnormalities_index,segments_index[i])
        
        if (breathing_rate > max_breathing_rate) and (breathing_rate< max_allowed_resp_rate)  :
            max_breathing_rate=breathing_rate
        if (breathing_rate < min_breathing_rate) and (breathing_rate > min_allowed_resp_rate):
            min_breathing_rate=breathing_rate

    
    return min_breathing_rate,max_breathing_rate
    


