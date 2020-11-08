import numpy as np
import os 
import sys 
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from respiratory_phases_interval_extraction.save_data import save_numeric_data
from respiratory_phases_interval_extraction.peak_detector_algorithm import find_peaks_valleys

       
def abnormal_segments_detection(input_signal,segment_time,min_allowed_resp_rate,max_allowed_resp_rate):
    """
    This function detect the abnormal segments of the signal which excced a max or is less than a min threshold
    Inputs:
        input_signal: The  signal in which the abnormal segment to be detected
        segmet time: The segemtn in which the breathing rate is checked in 
        min_allowed_resp_rate,max_allowed_resp_rate: The min and max allowed resp rate  
    Outputs:
        abnormal_segemnts_index: The index of the abnormal segments 
        
    """
    
    flag=0
    fs=10
    segment_length=segment_time*fs
    abnormal_segemnts_index=[]
    segments_index=np.arange(0,len(input_signal),segment_length)

    if len(input_signal)>segments_index[-1]:
        flag=1
    
    for i in range(len(segments_index)):
        if i==len(segments_index)-1:
            if flag==1:
                segments_index=np.append(segments_index,len(input_signal)-1)
            else :
                return abnormal_segemnts_index
                
        data_segment=input_signal[segments_index[i]:segments_index[i+1]]
        peaks_index,valleys_index=find_peaks_valleys(data_segment,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=0,lower_RRPm=0,upper_RRPm=0)
        breathing_rate=len(peaks_index)/(segment_time/60)        
        
        if (breathing_rate > max_allowed_resp_rate) or (breathing_rate < min_allowed_resp_rate)  :
            abnormal_segemnts_index=np.append(abnormal_segemnts_index,segments_index[i])
      
        
        
        return abnormal_segemnts_index
    



   
def abnormal_segments_removing(signal,abnormalities_index,segment_time_length,data_path,save_data):
    """
    This functions delete the abnormal segments from the signal
    Inputs:
        signal:  The signal from which the abnormal segemntss will be removed
        abnormalities_index: The index of the segment an dthe given the segment length , the remocved part indeiceies will be calculated
        data_path: data path at which the indicies to be removed removed from the data is saved 
        save_dadta:The data to be saved or not 
        
    """
    
    abnormalities_total_index=[]
    fs=10
    for i in range(len(abnormalities_index)):
        abnormalities_total_index=np.append(abnormalities_total_index,np.arange(abnormalities_index[i],abnormalities_index[i]+segment_time_length*fs))
    if len(signal.shape)==4:
        abnormal_segment_removed_signal=np.delete(signal,abnormalities_total_index,3)
    elif  len(signal.shape)==1:
        abnormal_segment_removed_signal=np.delete(signal,abnormalities_total_index,0)

    if save_data==1:
        save_numeric_data(os.path.join(data_path,'segment_abnormality_index,npy'),abnormalities_index)
     

    return abnormal_segment_removed_signal
