import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import os 


def find_intial_Bl(input_signal):
    min_index=np.where(input_signal==min(input_signal))
    max_index=np.where(input_signal==max(input_signal))
    min_max_index=np.append(min_index,max_index)
    BL=np.mean(np.delete(input_signal,min_max_index))
    return BL

def load_data(data_path):

    dummy_signal= scipy.io.loadmat(data_path)
    dummy_signal=dummy_signal['z'][0]
    dummy_signal=dummy_signal.astype(np.float64)  
    dummy_signal=(dummy_signal-np.mean(dummy_signal))/np.std(dummy_signal)
    return dummy_signal





def find_peaks(dummy_signal,main_path,file_name):
        
    HT=max(dummy_signal)/10
    DT=min(dummy_signal)/10
    BL=find_intial_Bl(dummy_signal)
    VD=True
    PD=False
    BL_vector=[]
    peaks_index=[0]
    valleys_index=[0]
    peaks_value=[]
    valleys_value=[]
    mh_dist_peak=0
    mh_dist_valley=0
    temp=1
    j=0
    mh_dist_compare_to_peaks=3
    mh_dist_compare_to_valleys=3
    mh_dist_peak_detected=[]
    mh_dist_valley_detected=[]
    
    #This just to convert the data into 
    #doubles as it was just uint so it cannot have any negative values and overfitting 
    #occurs when subtracting form it
    
    for i in range(len(dummy_signal)):
        
        if temp==0:
            if i!=j:   
                continue 
            else:
                temp=1
               
        
        if len(peaks_index)>5:
            #last_100_peak_index=peaks_index[-11:-1]
            last_100_peak_index=peaks_index
            last_100_peak_heigh=dummy_signal[last_100_peak_index]
            HT = np.mean(last_100_peak_heigh) *0.1
            mh_dist_peak=np.sqrt((dummy_signal[i]-np.mean(last_100_peak_heigh))**2/np.std(last_100_peak_heigh))
            mh_dist_peak_detected=np.append(mh_dist_peak_detected,mh_dist_peak)
            mh_dist_compare_to_peaks=np.mean(mh_dist_peak_detected)*4
        if len(valleys_index)>5:
            #last_100_valley_index=valleys_index[-11:-1]
            last_100_valley_index=valleys_index
            last_100_valley_heigh=dummy_signal[last_100_valley_index]
            DT = np.mean(last_100_valley_heigh)*0.1
            mh_dist_valley=np.sqrt((dummy_signal[i]-np.mean(last_100_valley_heigh))**2/np.std(last_100_valley_heigh))
            mh_dist_valley_detected=np.append(mh_dist_valley_detected,mh_dist_valley)
            mh_dist_compare_to_valleys=np.mean(mh_dist_valley_detected)*4
        if (i >0) and (i <len(dummy_signal)-1):
         
            if (np.sign(dummy_signal[i-1]-dummy_signal[i])!=np.sign(dummy_signal[i]-dummy_signal[i+1])):    
                if np.sign(dummy_signal[i]-dummy_signal[i+1]) ==0 :
                   
                    flag=1
                    j=i+2
                    while flag==1:
                         
                        if j>len(dummy_signal)-2:
                            break
                        
                        if abs(dummy_signal[j])> abs(dummy_signal[i]):
                            flag=0
                            temp=0
                        elif  abs(dummy_signal[j])< abs(dummy_signal[i]):
                            flag=0
                       
                        
                        else :
                            j=j+1
                
                
                
                if  (dummy_signal[i]< BL) and ((dummy_signal[i]<=DT)) and (mh_dist_valley<mh_dist_compare_to_valleys) and (PD==True) and (VD==False)  :
                    valleys_index=np.append(valleys_index,i)
                    valleys_value=np.append(valleys_value,dummy_signal[i])
                    BL_vector=[]
                    VD=True
                    PD=False
                    
                    
                elif  (dummy_signal[i]> BL) and (dummy_signal[i]>HT) and (mh_dist_peak<mh_dist_compare_to_peaks) and (VD==True) and (PD==False) and (np.sign(dummy_signal[i-1]-dummy_signal[i])!=np.sign(dummy_signal[i]-dummy_signal[i+1])) :
                    peaks_index=np.append(peaks_index,i)
                    peaks_value=np.append(peaks_value,dummy_signal[i])
                    BL_vector=np.append(BL_vector,dummy_signal[i])
                    BL=np.mean(BL_vector)
                    PD=True
                    VD=False
    
                else:
                    BL_vector=np.append(BL_vector,dummy_signal[i])
                    BL=np.mean(BL_vector)
            
        else:
            if  (dummy_signal[i]< BL) and ((dummy_signal[i]<=DT)) and (mh_dist_valley<1.7) and (PD==True) and (VD==False):
                valleys_index=np.append(valleys_index,i)
                valleys_value=np.append(valleys_value,dummy_signal[i])
                BL_vector=[]
                VD=True
                PD=False
                mh_dist_valley_detected=np.append(mh_dist_valley_detected,mh_dist_valley)
    
                
            elif  (dummy_signal[i]> BL) and (dummy_signal[i]>HT) and (mh_dist_peak<1.7) and (VD==True) and (PD==False) :
                peaks_index=np.append(peaks_index,i)
                peaks_value=np.append(peaks_value,dummy_signal[i])
                BL_vector=np.append(BL_vector,dummy_signal[i])
                BL=np.mean(BL_vector)
                PD=True
                VD=False
                mh_dist_peak_detected=np.append(mh_dist_peak_detected,mh_dist_peak)
    
                
            else:
                BL_vector=np.append(BL_vector,dummy_signal[i])
                BL=np.mean(BL_vector)
          
       
        
        
    ##### Plotting the results ######
    plt.figure()
    plt.title(file_name)
    peaks_index=peaks_index[1:len(peaks_index)]
    valleys_index=valleys_index[1:len(valleys_index)]
    time=np.linspace(0,len(dummy_signal)/10,len(dummy_signal))
    plt.plot(time,dummy_signal)
    plt.scatter(peaks_index/10,peaks_value)
    plt.scatter(valleys_index/10,valleys_value)
    
    
    ###### Calculating the inspiration and expiration interval and durations 
    expiration_intervals=[]
    inspiration_intervals=[]
    inspiration_durations=[]
    expiration_durations=[]
    
    if len(valleys_index)>len(peaks_index):
       smaller_length =len(peaks_index)
    else:
       smaller_length =len(valleys_index)
    
    for i in range(smaller_length-1):
        expiration_intervals=np.append(expiration_intervals,np.append(valleys_index[i],peaks_index[i+1]))
        inspiration_intervals=np.append(inspiration_intervals,np.append(peaks_index[i],valleys_index[i]))

    for i in range(0,len(inspiration_intervals),2):
        inspiration_durations=np.append(inspiration_durations,inspiration_intervals[i+1]-inspiration_intervals[i])
    for i in range(0,len(expiration_intervals),2):
        expiration_durations=np.append(expiration_durations,expiration_intervals[i+1]-expiration_intervals[i])    
   
    breathing_durations_in_sec=(inspiration_durations+expiration_durations)/10
    
    np.save(os.path.join(main_path,file_name,'breathing_durations_in_sec.dat'),breathing_durations_in_sec)
    np.save(os.path.join(main_path,file_name,'inspiration_intervals.dat'),inspiration_intervals)
    np.save(os.path.join(main_path,file_name,'expiration_intervals.dat'),expiration_intervals)
    
    
    #### Removing the abnormal intervals from inspiration and expiration 
    
    upper_RRPm=15  # 15 beats per min , which mean that the duration for one cycle is 4 sec
    lower_RRPm=8    # 8 beats per min , which mean that the duration for one cycle is 7.5 sec

    abnormality_index=np.where(np.logical_or((breathing_durations_in_sec>=60/lower_RRPm) , (breathing_durations_in_sec<=60/upper_RRPm))  )    
    abnormality_index=np.append(2*abnormality_index[0],2*abnormality_index[0]+1)  
    inspiration_intervals_abnormality_removed=np.delete(inspiration_intervals,abnormality_index)
    expiration_intervals_abnormality_removed=np.delete(expiration_intervals,abnormality_index)
    
    inspiration_durations_abnormality_removed=[]
    expiration_durations_abnormality_removed=[]
    for i in range(0,len(inspiration_intervals_abnormality_removed),2):
        inspiration_durations_abnormality_removed=np.append(inspiration_durations_abnormality_removed,inspiration_intervals_abnormality_removed[i+1]-inspiration_intervals_abnormality_removed[i])
    for i in range(0,len(expiration_intervals_abnormality_removed),2):
        expiration_durations_abnormality_removed=np.append(expiration_durations_abnormality_removed,expiration_intervals_abnormality_removed[i+1]-expiration_intervals_abnormality_removed[i])    
      
        
    breathing_durations_in_sec_abnormality_removed=(inspiration_durations_abnormality_removed+expiration_durations_abnormality_removed)/10
    np.save(os.path.join(main_path,file_name,'inspiration_intervals__abnormality_removed.dat'),inspiration_intervals_abnormality_removed)
    np.save(os.path.join(main_path,file_name,'expiration_intervals__abnormality_removed.dat'),expiration_intervals_abnormality_removed)
    
    return breathing_durations_in_sec,inspiration_intervals,inspiration_durations,peaks_index,valleys_index,expiration_intervals,expiration_durations
    
    
    return 
def main():
    main_path='/data/fmri/Youssef/Data/MREG_data/controls'
    file_names=os.listdir(main_path)
    data_file_name='belt_data_resampled.mat'
    if np.size(file_names)>1:
        for file_name in file_names:
            if file_name=='info'  or file_name=='missing_data':
                continue
            else:
                data_path=os.path.join(main_path,file_name,data_file_name)
                data=load_data(data_path)
                breathing_durations_in_sec,inspiration_intervals,inspiration_durations,peaks_index,valleys_index,expiration_intervals,expiration_durations=find_peaks(data,main_path,file_name)
    else:
        data_path=os.path.join(main_path,file_names,data_file_name)
        data=load_data(data_path)
        breathing_durations_in_sec,inspiration_intervals,inspiration_durations,peaks_index,valleys_index,expiration_intervals,expiration_durations=find_peaks(data,main_path,file_names)
        
    return breathing_durations_in_sec,inspiration_intervals,inspiration_durations,peaks_index,valleys_index,expiration_intervals,expiration_durations
    
    
    
    
    
breathing_durations_in_sec,inspiration_intervals,inspiration_durations,peaks_index,valleys_index,expiration_intervals,expiration_durations=main()    
    
    
    
    
