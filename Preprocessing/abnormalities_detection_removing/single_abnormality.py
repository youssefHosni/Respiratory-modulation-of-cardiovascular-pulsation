import numpy as np
import sys 
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')



def abnormal_cycle_detection(refernce_voxel_resp_siganl,peaks_index,valleys_index,lower_RRPm,upper_RRPm):
    """
    This function detect the abnormal breathing cycle index in the peaks and valleys  and retrun the index of the of the data that will be remved 
    Inputs 
        peaks_index
        valleys_index
        lower_RRPm
        upper_RRPm
    Returns:
        peaks_index_abnormal_removed: The peaks index with the index of the abnormal cycles are being removed 
        valleys_index_abnormal_removed: The valleys index with the index of the abnormal cycles are being removed 
    
    """
    
    abnormal_peaks_index=[]
    abnormal_valleys_index=[]
    
    
    
    if (len(peaks_index)!=0) and (len(valleys_index)!=0) :
        
        peaks_value=refernce_voxel_resp_siganl[peaks_index]
        peaks_mean=np.mean(peaks_value)
        valleys_value=refernce_voxel_resp_siganl[valleys_index]
        valleys_mean=np.mean(valleys_value)
        
        peaks_abnormal_value_index=np.where(np.logical_or(peaks_value < peaks_mean/3,peaks_value > peaks_mean*3))[0]
        valleys_abnormal_value_index=np.where(np.logical_or(valleys_value > valleys_mean/3,valleys_value <valleys_mean*3))[0]
        if peaks_abnormal_value_index.size>0:
            peaks_index=np.delete(peaks_index,peaks_abnormal_value_index,0)
        if valleys_abnormal_value_index.size>0:
            valleys_index=np.delete(valleys_index,valleys_abnormal_value_index,0)
        
        if peaks_index[0]<=valleys_index[0]:
            for i in range(len(peaks_index)-1):
                valleys_between_two_peaks_index=np.where(np.logical_and(valleys_index>=peaks_index[i],valleys_index<peaks_index[i+1]))
               
                if len(valleys_between_two_peaks_index[0])==0:
                   abnormal_peaks_index=np.append(abnormal_peaks_index,i+1)
                if len(valleys_between_two_peaks_index[0])==2:
                    abnormal_valleys_index=np.append(abnormal_valleys_index,valleys_between_two_peaks_index[0][1])
                elif len(valleys_between_two_peaks_index[0])>2:
                    abnormal_valleys_index=np.append(abnormal_valleys_index,valleys_between_two_peaks_index[0][1:len(valleys_between_two_peaks_index)])
            
                
            for i in range(len(valleys_index)-1):
                peaks_between_two_valleys_index=np.where(np.logical_and(peaks_index>=valleys_index[i],peaks_index<valleys_index[i+1]))
               
                if len(peaks_between_two_valleys_index[0])==0:
                    abnormal_valleys_index=np.append(abnormal_valleys_index,i+1)
                if len(peaks_between_two_valleys_index[0])==2:
                    abnormal_peaks_index=np.append(abnormal_peaks_index,peaks_between_two_valleys_index[0][1])
                elif len(peaks_between_two_valleys_index[0])>2:
                    abnormal_peaks_index=np.append(abnormal_peaks_index,peaks_between_two_valleys_index[0][1:len(peaks_between_two_valleys_index)])
                     
            """
            if peaks_index[i]> valleys_index[i]:
                abnormal_valleys_index=np.append(abnormal_valleys_index,i)
                #valleys_index=np.delete(valleys_index,i,0)
            if peaks_index[i+1]< valleys_index[i]:
                abnormal_peaks_index=np.append(abnormal_peaks_index,i+1)
                #peaks_index=np.delete(peaks_index,i+1,0)
           
            breathing_durations_in_sec=(peaks_index[i+1]-peaks_index[i])/10
            print(breathing_durations_in_sec)

            if  (breathing_durations_in_sec>=60/lower_RRPm) or (breathing_durations_in_sec<=60/upper_RRPm):    
                #print(breathing_durations_in_sec)
                abnormal_peaks_index=np.append(abnormal_peaks_index,i)
                abnormal_valleys_index=np.append(abnormal_valleys_index,i)
            """ 
        elif valleys_index[0] < peaks_index[0]:
                
                for i in range(len(peaks_index)-1):
                    valleys_between_two_peaks_index=np.where(np.logical_and(valleys_index>=peaks_index[i],valleys_index<peaks_index[i+1]))
                   
                    if len(valleys_between_two_peaks_index[0])==0:
                        abnormal_peaks_index=np.append(abnormal_peaks_index,i+1)
                    elif len(valleys_between_two_peaks_index[0])==2:
                        abnormal_valleys_index=np.append(abnormal_valleys_index,valleys_between_two_peaks_index[0][1])
                    elif len(valleys_between_two_peaks_index[0])>2:
                        abnormal_valleys_index=np.append(abnormal_valleys_index,valleys_between_two_peaks_index[0][1:len(valleys_between_two_peaks_index)])
                
        
                for i in range(len(valleys_index)-1):
                    peaks_between_two_valleys_index=np.where(np.logical_and(peaks_index>=valleys_index[i],peaks_index<valleys_index[i+1]))
                   
                    if len(peaks_between_two_valleys_index[0])==0:
                        abnormal_valleys_index=np.append(abnormal_valleys_index,i+1)
                    elif len(peaks_between_two_valleys_index[0])==2:
                        abnormal_peaks_index=np.append(abnormal_peaks_index,peaks_between_two_valleys_index[0][1])
                    elif len(peaks_between_two_valleys_index[0])>2:
                        abnormal_peaks_index=np.append(abnormal_peaks_index,peaks_between_two_valleys_index[0][1:len(peaks_between_two_valleys_index)])
               
                """
                for i in range(0,len(valleys_index)-1):
                    if peaks_index[i]< valleys_index[i]:
                        abnormal_peaks_index=np.append(abnormal_peaks_index,i)
                        #peaks_index=np.delete(peaks_index,i,0)
                    if valleys_index[i+1]< peaks_index[i]:
                        abnormal_valleys_index=np.append(abnormal_valleys_index,i+1)
                        #valleys_index=np.delete(valleys_index,i+1,0)
                        
                            
                    breathing_durations_in_sec=(valleys_index[i+1]-valleys_index[i])/10
                    print(breathing_durations_in_sec)
                    if  (breathing_durations_in_sec>=60/lower_RRPm) or (breathing_durations_in_sec<=60/upper_RRPm):    
                        
                        abnormal_peaks_index=np.append(abnormal_peaks_index,i)
                        abnormal_valleys_index=np.append(abnormal_valleys_index,i)         
                """
    
           
        
        
        
        
        """
        if len(valleys_index_abnormal_removed)>=len(peaks_index_abnormal_removed):
            for_loop_range=len(peaks_index_abnormal_removed)
        else:    
            for_loop_range=len(valleys_index_abnormal_removed)
            
        for i in range(for_loop_range-1):
          breathing_durations_in_sec=(valleys_index[i+1]-valleys_index[i])/10
          print(breathing_durations_in_sec)
          if  (breathing_durations_in_sec>=60/lower_RRPm) or (breathing_durations_in_sec<=60/upper_RRPm):
                   abnormal_peaks_index=np.append(abnormal_peaks_index,i)
                   abnormal_valleys_index=np.append(abnormal_valleys_index,i)         
        peaks_index_abnormal_removed=np.delete(peaks_index_abnormal_removed,peaks_abnormal_value_index,0)
        valleys_index_abnormal_removed=np.delete(valleys_index_abnormal_removed,valleys_abnormal_value_index,0)
        """           
    
        if np.size(abnormal_peaks_index)>0:
                abnormal_peaks_index=np.unique(abnormal_peaks_index)
                peaks_index=np.delete(peaks_index,abnormal_peaks_index,0) 
        if np.size(abnormal_valleys_index)>0:
                abnormal_valleys_index=np.unique(abnormal_valleys_index)
                valleys_index=np.delete(valleys_index,abnormal_valleys_index,0)
                       
        return peaks_index, valleys_index    
    else:
        return peaks_index, valleys_index
        
        
    

def abnormal_cycle_removing(signal,abnormality_index_total):
     """
     This function remove the abnormal indeices from the signal 
     """
        
     if len(signal.shape)==4:
        single_abnormality_removed_signal=np.delete(signal,abnormality_index_total,3)
     elif  len(signal.shape)==1:
        single_abnormality_removed_signal=np.delete(signal,abnormality_index_total,0)

     return single_abnormality_removed_signal
    
