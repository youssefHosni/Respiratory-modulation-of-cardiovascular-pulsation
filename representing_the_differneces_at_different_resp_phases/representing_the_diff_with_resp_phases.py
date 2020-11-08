import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from respiratory_phases_interval_extraction.load_data import load_niftiydata
from respiratory_phases_interval_extraction.save_data import save_nifity_data
from respiratory_phases_interval_extraction.save_data import save_numeric_data
import os
import numpy as np
import nolds
from respiratory_phases_interval_extraction.peak_detector_algorithm import find_peaks_valleys

def resp_phases_loc_points(refernce_signal,min_allowed_resp_rate,max_allowed_resp_rate):
    """
    get the index loc points (peaks,valleys,max_der,min_der) of the 1_D i  input signal 
    """
    peaks_index,valleys_index =find_peaks_valleys(refernce_signal,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)
    max_der_index=[]
    min_der_index=[]
    resp_der=np.gradient(refernce_signal)
    if peaks_index[0]< valleys_index[0]:
        for i in range(len(peaks_index)-1):
            start_index=peaks_index[i]
            end_index=peaks_index[i+1]
            der_one_cycle=resp_der[start_index:end_index]
            max_der_index=np.append(max_der_index,np.argmax(der_one_cycle)+start_index)
            min_der_index=np.append(min_der_index,np.argmin(der_one_cycle)+start_index)
    
    elif peaks_index[0]> valleys_index[0]:

        for i in range(len(valleys_index)-1):
        
            start_index=valleys_index[i]
            end_index=valleys_index[i+1]
            der_one_cycle=resp_der[start_index:end_index]
            max_der_index=np.append(max_der_index,np.argmax(der_one_cycle)+start_index)
            min_der_index=np.append(min_der_index,np.argmin(der_one_cycle)+start_index)  

    return peaks_index,valleys_index,max_der_index,min_der_index

def cardiac_data_resp_lock_points(refernce_voxel_resp_siganl,refernce_voxel_cardiac_siganl,cardiac_signal,data_affine,data_header,min_allowed_resp_rate,max_allowed_resp_rate,min_allowed_heart_rate,max_allowed_heart_rate,save_data,main_path,sample_name,save_seperate_file,mean_calc,tolerance):
        
        """
        get the cardiac data at a certain respiratory loc points
        """
        if tolerance!=0:
            cardiac_signal_resp_peaks_lock_folder_name='cardiac_data_resp_peaks_lock_point_'+str(tolerance)+'s_tolerance'
            cardiac_signal_resp_valleys_lock_folder_name='cardiac_data_resp_valleys_lock_point_'+str(tolerance)+'s_tolerance'
            cardiac_signal_resp_max_der_lock_folder_name='cardiac_data_resp_max_der_lock_point_'+str(tolerance)+'s_tolerance'
            cardiac_signal_resp_min_der_lock_folder_name='cardiac_data_resp_min_der_lock_point_'+str(tolerance)+'s_tolerance'
            
            cardiac_signal_resp_peaks_lock_file_name='cardiac_data_resp_peaks_lock_point_map_'+str(tolerance)+'s_tolerance.nii.gz'
            cardiac_signal_resp_valleys_lock_file_name='cardiac_data_resp_valleys_lock_point_map_'+str(tolerance)+'s_tolerance.nii.gz'
            cardiac_signal_resp_max_der_lock_file_name='cardiac_data_resp_max_der_lock_point_map_'+str(tolerance)+'s_tolerance.nii.gz'
            cardiac_signal_resp_min_der_lock_file_name='cardiac_data_resp_min_der_lock_point_map_'+str(tolerance)+'s_tolerance.nii.gz'

        else:
            cardiac_signal_resp_peaks_lock_folder_name='cardiac_data_resp_peaks_lock_point_'
            cardiac_signal_resp_valleys_lock_folder_name='cardiac_data_resp_valleys_lock_point_'
            cardiac_signal_resp_max_der_lock_folder_name='cardiac_data_resp_max_der_lock_point_'
            cardiac_signal_resp_min_der_lock_folder_name='cardiac_data_resp_min_der_lock_point_'
            
            cardiac_signal_resp_peaks_lock_file_name='cardiac_data_resp_peaks_lock_point_map.nii.gz'
            cardiac_signal_resp_valleys_lock_file_name='cardiac_data_resp_valleys_lock_point_map.nii.gz'
            cardiac_signal_resp_max_der_lock_file_name='cardiac_data_resp_max_der_lock_point_map.nii.gz'
            cardiac_signal_resp_min_der_lock_file_name='cardiac_data_resp_min_der_lock_point_map.nii.gz'


        resp_peaks_index,resp_valleys_index =find_peaks_valleys(refernce_voxel_resp_siganl,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)
        cardiac_peaks_index,cardiac_valleys_index =find_peaks_valleys(refernce_voxel_cardiac_siganl,main_path='',sample_name='',plot_results=1,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_heart_rate,upper_RRPm=max_allowed_heart_rate)
        
    
        cardiac_valleys_index=np.append(cardiac_valleys_index,np.append(cardiac_valleys_index+tolerance/2,cardiac_valleys_index-tolerance/2))
        
        cardiac_data_resp_peaks_index=(np.where(np.in1d(cardiac_valleys_index,resp_peaks_index))[0])
        cardiac_data_resp_valleys_index=(np.where(np.in1d(cardiac_valleys_index,resp_valleys_index))[0])
        
        cardiac_data_resp_peaks_lock_point_map=cardiac_signal[:,:,:,cardiac_data_resp_peaks_index]
        cardiac_data_resp_valleys_lock_point_map=cardiac_signal[:,:,:,cardiac_data_resp_valleys_index]
            
        max_der_index=[]
        min_der_index=[]
        resp_der=np.gradient(refernce_voxel_resp_siganl)
        if resp_peaks_index[0]< resp_valleys_index[0]:
            for i in range(len(resp_peaks_index)-1):
                start_index=resp_peaks_index[i]
                end_index=resp_peaks_index[i+1]
                der_one_cycle=resp_der[start_index:end_index]
                max_der_index=np.append(max_der_index,np.argmax(der_one_cycle)+start_index)
                min_der_index=np.append(min_der_index,np.argmin(der_one_cycle)+start_index)
        
        elif resp_peaks_index[0]> resp_valleys_index[0]:

            for i in range(len(resp_valleys_index)-1):
            
                start_index=resp_valleys_index[i]
                end_index=resp_valleys_index[i+1]
                der_one_cycle=resp_der[start_index:end_index]
                max_der_index=np.append(max_der_index,np.argmax(der_one_cycle)+start_index)
                min_der_index=np.append(min_der_index,np.argmin(der_one_cycle)+start_index)  
    
        cardiac_data_resp_max_der_index=(np.where(np.in1d(cardiac_valleys_index,max_der_index))[0])
        cardiac_data_resp_min_der_index=(np.where(np.in1d(cardiac_valleys_index,min_der_index))[0])
        
        cardiac_data_resp_max_der_lock_point_map=cardiac_signal[:,:,:,cardiac_data_resp_max_der_index]
        cardiac_data_resp_min_der_lock_point_map=cardiac_signal[:,:,:,cardiac_data_resp_min_der_index]
        
        if save_data==1:
           save_nifity_data(os.path.join(main_path,sample_name,cardiac_signal_resp_peaks_lock_file_name),cardiac_data_resp_peaks_lock_point_map,data_affine,data_header)
           save_nifity_data(os.path.join(main_path,sample_name,cardiac_signal_resp_valleys_lock_file_name),cardiac_data_resp_valleys_lock_point_map,data_affine,data_header)
           save_nifity_data(os.path.join(main_path,sample_name,cardiac_signal_resp_max_der_lock_file_name),cardiac_data_resp_max_der_lock_point_map,data_affine,data_header)
           save_nifity_data(os.path.join(main_path,sample_name,cardiac_signal_resp_min_der_lock_file_name),cardiac_data_resp_min_der_lock_point_map,data_affine,data_header)

        if save_seperate_file==1:
           save_nifity_data(os.path.join(main_path,cardiac_signal_resp_peaks_lock_folder_name,sample_name+'peaks.nii.gz'),cardiac_data_resp_peaks_lock_point_map,data_affine,data_header)
           save_nifity_data(os.path.join(main_path,cardiac_signal_resp_valleys_lock_folder_name,sample_name+'valleys.nii.gz'),cardiac_data_resp_valleys_lock_point_map,data_affine,data_header)
           save_nifity_data(os.path.join(main_path,cardiac_signal_resp_max_der_lock_folder_name,sample_name+'max_der.nii.gz'),cardiac_data_resp_max_der_lock_point_map,data_affine,data_header)
           save_nifity_data(os.path.join(main_path,cardiac_signal_resp_min_der_lock_folder_name,sample_name+'min_der.nii.gz'),cardiac_data_resp_min_der_lock_point_map,data_affine,data_header)
        
        if mean_calc==1:
            
            mean_map_cardiac_data_resp_peak_lock_point=np.mean(cardiac_data_resp_peaks_lock_point_map,3)
            mean_map_cardiac_data_resp_valley_lock_point=np.mean(cardiac_data_resp_valleys_lock_point_map,3)
            mean_map_cardiac_data_resp_max_der_lock_point=np.mean(cardiac_data_resp_max_der_lock_point_map,3)
            mean_map_cardiac_data_resp_min_der_lock_point=np.mean(cardiac_data_resp_min_der_lock_point_map,3)
            
            save_nifity_data(os.path.join(main_path,cardiac_signal_resp_peaks_lock_folder_name,'average_each_sample',sample_name+'peaks_mean.nii.gz'),mean_map_cardiac_data_resp_peak_lock_point,data_affine,data_header)
            save_nifity_data(os.path.join(main_path,cardiac_signal_resp_valleys_lock_folder_name,'average_each_sample',sample_name+'valleys_mean.nii.gz'),mean_map_cardiac_data_resp_valley_lock_point,data_affine,data_header)
            save_nifity_data(os.path.join(main_path,cardiac_signal_resp_max_der_lock_folder_name,'average_each_sample',sample_name+'max_der_mean_.nii.gz'),mean_map_cardiac_data_resp_max_der_lock_point,data_affine,data_header)
            save_nifity_data(os.path.join(main_path,cardiac_signal_resp_min_der_lock_folder_name,'average_each_sample',sample_name+'min_der_mean.nii.gz'),mean_map_cardiac_data_resp_min_der_lock_point,data_affine,data_header)
            
        return
            



    
def flow_speed(cardiac_data,cardiac_affine,cardiac_header,refernce_resp_signal,resp_peaks_index,resp_valleys_index,flow_speed_insp_exp,flow_speed_max_min_der,save_data,main_path,sample_name,save_seperate_file,flow_speed_seperate_files):
        
        """
        calculate the flow speed at resp loc points
        """
        
        file_name_insp=flow_speed_seperate_files['flow_speed_insp']
        file_name_exp=flow_speed_seperate_files['flow_speed_exp']
        file_name_max_der=flow_speed_seperate_files['flow_speed_max_der']
        file_name_min_der=flow_speed_seperate_files['flow_speed_min_der']
            
        flow_speed_insp_map=np.empty((cardiac_data.shape[0],cardiac_data.shape[1],cardiac_data.shape[2]))
        flow_speed_exp_map=np.empty((cardiac_data.shape[0],cardiac_data.shape[1],cardiac_data.shape[2]))
        flow_speed_max_der_map=np.empty((cardiac_data.shape[0],cardiac_data.shape[1],cardiac_data.shape[2]))
        flow_speed_min_der_map=np.empty((cardiac_data.shape[0],cardiac_data.shape[1],cardiac_data.shape[2]))        
        
        if flow_speed_max_min_der==1:
            max_der_index=[]
            min_der_index=[]
            resp_der=np.gradient(refernce_resp_signal)
            if resp_peaks_index[0]< resp_valleys_index[0]:
                
                for i in range(len(resp_peaks_index)-1):
                    start_index=resp_peaks_index[i]
                    end_index=resp_peaks_index[i+1]
                    der_one_cycle=resp_der[start_index:end_index]
                    max_der_index=np.append(max_der_index,np.argmax(der_one_cycle)+start_index)
                    min_der_index=np.append(min_der_index,np.argmin(der_one_cycle)+start_index)
            
            elif resp_peaks_index[0]> resp_valleys_index[0]:
 
                for i in range(len(resp_valleys_index)-1):
                
                    start_index=resp_valleys_index[i]
                    end_index=resp_valleys_index[i+1]
                    der_one_cycle=resp_der[start_index:end_index]
                    max_der_index=np.append(max_der_index,np.argmax(der_one_cycle)+start_index)
                    min_der_index=np.append(min_der_index,np.argmin(der_one_cycle)+start_index)
            
            
            
        for i in range(cardiac_data.shape[0]):
            for j in range(cardiac_data.shape[1]):
                for k in range(cardiac_data.shape[2]):
                    
                    cardiac_voxel_signal=cardiac_data[i,j,k,:]
                    cardiac_peaks,cardiac_valleys=find_peaks_valleys(cardiac_voxel_signal,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=0,lower_RRPm=0,upper_RRPm=0)
                    if flow_speed_insp_exp==1:
                        flow_speed_insp=len(np.where(np.in1d(cardiac_valleys, resp_peaks_index))[0])
                        flow_speed_exp=len(np.where(np.in1d(cardiac_valleys, resp_valleys_index))[0])
                        flow_speed_insp_map[i,j,k]=flow_speed_insp
                        flow_speed_exp_map[i,j,k]=flow_speed_exp
                    
                    
                    if flow_speed_max_min_der==1:
                        flow_speed_max_der=len(np.where(np.in1d(cardiac_valleys, max_der_index))[0])
                        flow_speed_min_der=len(np.where(np.in1d(cardiac_valleys, min_der_index))[0])
                        flow_speed_max_der_map[i,j,k]=flow_speed_max_der
                        flow_speed_min_der_map[i,j,k]=flow_speed_min_der
                        
                    
        
        if save_data==1:
          if save_seperate_file==0:
              ## if save in seperate file ==1 this means save the flow speed in seperate file other tham the sample file 
              #this is done so as to be used in randomize test.if it is =2 then both of them will done , saving data in
              # in seperate files and in the sample files
            if flow_speed_insp_exp==1:
                save_nifity_data(os.path.join(main_path,sample_name,'flow_speed_map_insp.nii.gz'),flow_speed_insp_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,sample_name,'flow_speed_map_exp.nii.gz'),flow_speed_exp_map,cardiac_affine,cardiac_header)            
            if flow_speed_max_min_der==1:
                save_nifity_data(os.path.join(main_path,sample_name,'flow_speed_max_der_map.nii.gz'),flow_speed_max_der_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,sample_name,'flow_speed_min_der_map.nii.gz'),flow_speed_min_der_map,cardiac_affine,cardiac_header)            
          elif save_seperate_file==1:
            if flow_speed_insp_exp==1:
                save_nifity_data(os.path.join(main_path,file_name_insp,sample_name[0:len(sample_name)-12]+'flow_speed_map_insp.nii.gz'),flow_speed_insp_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,file_name_exp,sample_name[0:len(sample_name)-12]+'flow_speed_map_exp.nii.gz'),flow_speed_exp_map,cardiac_affine,cardiac_header)            
            if flow_speed_max_min_der==1:
                save_nifity_data(os.path.join(main_path,file_name_max_der,sample_name[0:len(sample_name)-12]+'flow_speed_max_der_map.nii.gz'),flow_speed_max_der_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,file_name_min_der,sample_name[0:len(sample_name)-12]+'flow_speed_min_der_map.nii.gz'),flow_speed_min_der_map,cardiac_affine,cardiac_header)            
          
          elif save_seperate_file==2:
            if flow_speed_insp_exp==1:
                save_nifity_data(os.path.join(main_path,file_name_insp,sample_name[0:len(sample_name)-12]+'flow_speed_map_insp.nii.gz'),flow_speed_insp_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,file_name_exp,sample_name[0:len(sample_name)-12]+'flow_speed_map_exp.nii.gz'),flow_speed_exp_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,sample_name,'flow_speed_map_insp.nii.gz'),flow_speed_insp_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,sample_name,'flow_speed_map_exp.nii.gz'),flow_speed_exp_map,cardiac_affine,cardiac_header)         
            if flow_speed_max_min_der==1:
                save_nifity_data(os.path.join(main_path,file_name_max_der,sample_name[0:len(sample_name)-12]+'flow_speed_max_der_map.nii.gz'),flow_speed_max_der_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,file_name_min_der,sample_name[0:len(sample_name)-12]+'flow_speed_min_der_map.nii.gz'),flow_speed_min_der_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,sample_name,'flow_speed_max_der_map.nii.gz'),flow_speed_max_der_map,cardiac_affine,cardiac_header)            
                save_nifity_data(os.path.join(main_path,sample_name,'flow_speed_min_der_map.nii.gz'),flow_speed_min_der_map,cardiac_affine,cardiac_header)            
                         
              
            
def histogram_plotting(data,bins_num,title,save_data,saving_path):
        """
        plot histograms for the giving data
        """
        plt.figure()    
        zero_index=np.where(data==0)
        data=np.delete(data,zero_index)
        mu=np.mean(data)
        sigma=np.std(data)
        n,bins,patches=plt.hist(data,bins=bins_num ,density=True, facecolor='g',alpha=0.75)
        plt.grid(True)
        y = mlab.normpdf(bins, mu, sigma)
        plt.plot(bins, y, 'r--')
        plt.title(title+' $\mu=$'+str(mu)+', $\sigma=15$'+str(sigma))
        plt.xlabel('Durations in sec')
        plt.ylabel('magnitude')
        if save_data==1:    
            plt.savefig(os.path.join(saving_path))

def thresholding(input_data,threshold_limit):
    abnormal_duration_index=np.where(input_data>threshold_limit)
    if len((abnormal_duration_index))>1:
        input_data[abnormal_duration_index[0],abnormal_duration_index[1],abnormal_duration_index[2],abnormal_duration_index[3]]=0
    else:
        input_data[abnormal_duration_index]=0
    
    return input_data 
    
    
def histogram_generating(resp_peaks_index,resp_valleys_index,cardiac_data,mreg_data,refernce_voxel_cardiac_siganl,cardiac_affine,cardiac_header,histogram_level,main_path,sample_name,save_data,save_seperate_file,voxel_used):
    
    if len(main_path)==51:
        saving_path=main_path[0:42]
    elif len(main_path)==39:
        saving_path=main_path[0:36]    
    
    cardiac_cycle_duration_resp_valleys=[]
    cardiac_cycle_duration_resp_peaks=[]
    
    mreg_data[mreg_data>1]=1
    mreg_data[mreg_data<=0]=0
    
    cardiac_data=mreg_data*cardiac_data
    
    if voxel_used=='refernce_voxel':
        if len(resp_valleys_index)<=len(resp_peaks_index):
            for_loop_range=len(resp_valleys_index)
        elif  len(resp_valleys_index)>len(resp_peaks_index):
            for_loop_range=len(resp_peaks_index)
        cardiac_peaks,cardiac_valleys=find_peaks_valleys(refernce_voxel_cardiac_siganl,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=60,upper_RRPm=100)
    
        for l in range(for_loop_range):
            if (resp_peaks_index[l]>= max(cardiac_valleys)) or (resp_valleys_index[l]>= max(cardiac_valleys)) :
                break
            cardiac_duration_one_peak=(cardiac_valleys[np.where(cardiac_valleys > resp_peaks_index[l])[0][0]]-cardiac_valleys[np.where(cardiac_valleys <= resp_peaks_index[l])[0][-1]])/10
            cardiac_duration_one_valley=(cardiac_valleys[np.where(cardiac_valleys > resp_valleys_index[l])[0][0]]-cardiac_valleys[np.where(cardiac_valleys <= resp_valleys_index[l])[0][-1]])/10
            cardiac_cycle_duration_resp_peaks=np.append(cardiac_cycle_duration_resp_peaks,cardiac_duration_one_peak)              
            cardiac_cycle_duration_resp_valleys=np.append(cardiac_cycle_duration_resp_valleys,cardiac_duration_one_valley)  
        
        cardiac_cycle_duration_resp_peaks=thresholding(cardiac_cycle_duration_resp_peaks,2)
        cardiac_cycle_duration_resp_valleys=thresholding(cardiac_cycle_duration_resp_valleys,2)
        
        histogram_plotting(cardiac_cycle_duration_resp_peaks,10,'cardiac_cycle_ref_signal_duration_resp_peaks',save_data,os.path.join(main_path,sample_name,'cardiac_duration_refernce_voxel_peaks.png'))    
        histogram_plotting(cardiac_cycle_duration_resp_valleys,10,'cardiac_cycle_ref_signal_duration_resp_valleys',save_data,os.path.join(main_path,sample_name,'cardiac_duration_refernce_voxel_valleys.png'))    
        #return cardiac_cycle_duration_resp_peaks,cardiac_cycle_duration_resp_valleys
    
    elif voxel_used=='all_voxels':
        if len(resp_valleys_index)<=len(resp_peaks_index):
            for_loop_range=len(resp_valleys_index)
        elif  len(resp_valleys_index)>len(resp_peaks_index):
            for_loop_range=len(resp_peaks_index)
            
        cardiac_duration_map_peaks=np.empty((cardiac_data.shape[0],cardiac_data.shape[1],cardiac_data.shape[2],for_loop_range))
        cardiac_duration_map_valleys=np.empty((cardiac_data.shape[0],cardiac_data.shape[1],cardiac_data.shape[2],for_loop_range))
        
        for i in range(cardiac_data.shape[0]):
                for j in range(cardiac_data.shape[1]):
                    for k in range(cardiac_data.shape[2]):
                    
                        cardiac_duration_resp_peak_one_voxel=[]
                        cardiac_duration_resp_valley_one_voxel=[]
                        cardiac_voxel_signal=cardiac_data[i,j,k,:]
                        cardiac_peaks,cardiac_valleys=find_peaks_valleys(cardiac_voxel_signal,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=60,upper_RRPm=100)
    
                        if (len(cardiac_valleys)==0) or (len(cardiac_valleys)==1):
                            if  (histogram_level=="voxel_level")  or (histogram_level=="all_level") :
                                cardiac_duration_map_peaks[i,j,k,:]=0
                                cardiac_duration_map_valleys[i,j,k,:]=0
                            continue
                        
                        for l in range(for_loop_range): 
                            
                            if (resp_peaks_index[l]>= max(cardiac_valleys)) or (resp_valleys_index[l]>= max(cardiac_valleys)) or  (resp_peaks_index[l]<= min(cardiac_valleys)) or (resp_valleys_index[l]<= min(cardiac_valleys)):
                                cardiac_duration_resp_peak_one_voxel=np.append(cardiac_duration_resp_peak_one_voxel,0)
                                cardiac_duration_resp_valley_one_voxel=np.append(cardiac_duration_resp_valley_one_voxel,0)
                                
                            else:
                                
                                cardiac_duration_one_peak=(cardiac_valleys[np.where(cardiac_valleys > resp_peaks_index[l])[0][0]]-cardiac_valleys[np.where(cardiac_valleys <= resp_peaks_index[l])[0][-1]])/10
                                cardiac_duration_one_valley=(cardiac_valleys[np.where(cardiac_valleys > resp_valleys_index[l])[0][0]]-cardiac_valleys[np.where(cardiac_valleys <= resp_valleys_index[l])[0][-1]])/10
                                cardiac_duration_resp_peak_one_voxel=np.append(cardiac_duration_resp_peak_one_voxel,cardiac_duration_one_peak)
                                cardiac_duration_resp_valley_one_voxel=np.append(cardiac_duration_resp_valley_one_voxel,cardiac_duration_one_valley)
                            
                        if  (histogram_level=="voxel_level")  or (histogram_level=="all_level") :
                            cardiac_duration_map_peaks[i,j,k,:]=cardiac_duration_resp_peak_one_voxel
                            cardiac_duration_map_valleys[i,j,k,:]=cardiac_duration_resp_valley_one_voxel
                            
                        
                        
                        cardiac_cycle_duration_resp_peaks=np.append(cardiac_cycle_duration_resp_peaks,cardiac_duration_resp_peak_one_voxel)
                        cardiac_cycle_duration_resp_valleys=np.append(cardiac_cycle_duration_resp_valleys,cardiac_duration_resp_valley_one_voxel)    
        
        
        cardiac_cycle_duration_resp_peaks=thresholding(cardiac_cycle_duration_resp_peaks,2)
        cardiac_cycle_duration_resp_valleys=thresholding(cardiac_cycle_duration_resp_valleys,2)
        cardiac_duration_map_peaks=thresholding(cardiac_duration_map_peaks,2)
        cardiac_duration_map_valleys=thresholding(cardiac_duration_map_valleys,2)
        
        if (histogram_level=="sample_level" or histogram_level=="all_level" ) :
            
            histogram_plotting(cardiac_cycle_duration_resp_peaks,15,'cardiac cycle durations at resp peaks',save_data,os.path.join(main_path,sample_name,'hist_resp_peaks.png'))
            histogram_plotting(cardiac_cycle_duration_resp_valleys,15,'cardiac cycle durations at resp valleys',save_data,os.path.join(main_path,sample_name,'hist_resp_valleys.png'))
            save_numeric_data(os.path.join(main_path,sample_name,'cardiac_cycle_duration_resp_peaks.npy'),cardiac_cycle_duration_resp_peaks)
            save_numeric_data(os.path.join(main_path,sample_name,'cardiac_cycle_duration_resp_valleys.npy'),cardiac_cycle_duration_resp_valleys)
    
        if (((histogram_level=="voxel_level")  or (histogram_level=="all_level")) and (save_data==1)):
            save_nifity_data(os.path.join(main_path,sample_name,'cardiac_duration_map_peaks.nii.gz'),cardiac_duration_map_peaks,cardiac_affine,cardiac_header)
            save_nifity_data(os.path.join(main_path,sample_name,'cardiac_duration_map_valleys.nii.gz'),cardiac_duration_map_valleys,cardiac_affine,cardiac_header)
            if save_seperate_file==1:
                save_nifity_data(os.path.join(saving_path,'cardiac_durations_peaks',sample_name+'_peaks.nii.gz'),cardiac_duration_map_peaks,cardiac_affine,cardiac_header)
                save_nifity_data(os.path.join(saving_path,'cardiac_durations_valleys',sample_name+'_valleys.nii.gz'),cardiac_duration_map_valleys,cardiac_affine,cardiac_header)
    
        
        return cardiac_cycle_duration_resp_peaks,cardiac_cycle_duration_resp_valleys

def resp_phases_index_extraction(resp_peaks_index,resp_valleys_index,data_time_length):
    """
    giving a 1_D resp signal it returns the index of the insp adn expiation 
    """
    insp_duration_total_index=[]
    exp_duration_total_index=[]
    
        
    if len(resp_peaks_index)>=len(resp_valleys_index):
        for_loop_range=len(resp_valleys_index)
    elif len(resp_peaks_index)<len(resp_valleys_index):
        for_loop_range=len(resp_peaks_index)
    
    for i in range(for_loop_range):
        if resp_peaks_index[0]>resp_valleys_index[0]:
            if (i ==0) and (resp_valleys_index[0]>5):
                insp_duration_index=np.arange(5,resp_valleys_index[i])
                insp_duration_total_index=np.append(insp_duration_total_index,insp_duration_index)
                
            insp_duration_index=np.arange(resp_valleys_index[i],resp_peaks_index[i])
            insp_duration_total_index=np.append(insp_duration_total_index,insp_duration_index)
            
            
            
            if i == for_loop_range-1:
                if len(resp_valleys_index)>len(resp_peaks_index):
                    exp_duration_index=np.arange(resp_peaks_index[i],resp_valleys_index[i+1])
                    exp_duration_total_index=np.append(exp_duration_total_index,exp_duration_index)
                    insp_duration_index=np.arange(resp_valleys_index[i+1],data_time_length)
                    insp_duration_total_index=np.append(insp_duration_total_index,insp_duration_index)
                else:
                    exp_duration_index=np.arange(resp_peaks_index[i],data_time_length)
                    exp_duration_total_index=np.append(exp_duration_total_index,exp_duration_index)
            else:
                exp_duration_index=np.arange(resp_peaks_index[i],resp_valleys_index[i+1])
                exp_duration_total_index=np.append(exp_duration_total_index,exp_duration_index)
            
            
        elif resp_peaks_index[0]< resp_valleys_index[0]:         
        
            if (i ==0) and (resp_peaks_index[0]>5):
                exp_duration_index=np.arange(5,resp_peaks_index[i])
                exp_duration_total_index=np.append(exp_duration_total_index,exp_duration_index)

            exp_duration_index=np.arange(resp_peaks_index[i],resp_valleys_index[i])
            exp_duration_total_index=np.append(exp_duration_total_index,exp_duration_index)    
            
            if i == for_loop_range-1:
                if len(resp_peaks_index)>len(resp_valleys_index):
                    insp_duration_index=np.arange(resp_valleys_index[i],resp_peaks_index[i+1])
                    insp_duration_total_index=np.append(insp_duration_total_index,insp_duration_index)
                    exp_duration_index=np.arange(resp_peaks_index[i+1],data_time_length)
                    exp_duration_total_index=np.append(exp_duration_total_index,exp_duration_index)
                else:
                    insp_duration_index=np.arange(resp_valleys_index[i],data_time_length)
                    insp_duration_total_index=np.append(insp_duration_total_index,insp_duration_index)

            else:
                insp_duration_index=np.arange(resp_valleys_index[i],resp_peaks_index[i+1])
                insp_duration_total_index=np.append(insp_duration_total_index,insp_duration_index)
    return insp_duration_total_index,exp_duration_total_index

def optical_flow_resp_phase_extraction(resp_peaks_index,resp_valleys_index,optical_flow_data,data_affine,data_header,main_path,sample_name):
    
    insp_duration_total_index,exp_duration_total_index= resp_phases_index_extraction(resp_peaks_index,resp_valleys_index,optical_flow_data.shape[4])       
    cardiac_flow_data_insp=np.empty((optical_flow_data.shape[0],optical_flow_data.shape[1],optical_flow_data.shape[2],optical_flow_data.shape[3],len(insp_duration_total_index)))
    cardiac_flow_data_exp=np.empty((optical_flow_data.shape[0],optical_flow_data.shape[1],optical_flow_data.shape[2],optical_flow_data.shape[3],len(exp_duration_total_index)))
       
    cardiac_flow_data_insp[:,:,:,:,]=optical_flow_data[:,:,:,:,insp_duration_total_index.astype(int)]        
    cardiac_flow_data_exp[:,:,:,:,]=optical_flow_data[:,:,:,:,exp_duration_total_index.astype(int)]    
    
    save_nifity_data(os.path.join(main_path,sample_name,'optflow-all-m3_lptp6_fullcard_iffdm_insp.nii.gz'),cardiac_flow_data_insp,data_affine,data_header)
    save_nifity_data(os.path.join(main_path,sample_name,'optflow-all-m3_lptp6_fullcard_iffdm_exp.nii.gz'),cardiac_flow_data_exp,data_affine,data_header)
    

def property_map(input_data,data_affine,data_header,prop,save_data,save_path):
    
    if (prop=="mean") or (prop=="all") :
        mean_map=np.mean(input_data,3)
        if save_data==1:
            save_nifity_data(save_path,mean_map,data_affine,data_header)

    elif prop=="std" or (prop=="all"):
        std_map=np.std(input_data,3)
        if save_data==1:
            save_nifity_data(save_path,std_map,data_affine,data_header)

    elif prop=="cv" or (prop=="all"):  
        cv_map=np.std(input_data,3)/np.mean(input_data,3)
        if save_data==1:
            save_nifity_data(save_path,cv_map,data_affine,data_header)

    elif prop=="sample_entropy" or (prop=="all"):  
        sampen_map=np.empty((input_data.shape[0],input_data.shape[1],input_data.shape[2]))
        for i in range (input_data.shape[0]):
            for j in range(input_data.shape[1]):
                for k in range(input_data.shape[2]):
                    if sum(input_data[i,j,k,:])==0:
                        sampen_map[i,j,k]=0
                    else:
                        sampen_map[i,j,k]=nolds.sampen(input_data[i,j,k,:])
    
        if save_data==1:
            save_nifity_data(save_path,sampen_map,data_affine,data_header)

    
           
def insp_exp_regions_4(resp_signal,resp_peaks_index,resp_valleys_index,min_allowed_resp_rate,max_allowed_resp_rate):

    insp_signal_index,exp_signal_index=resp_phases_index_extraction(resp_peaks_index,resp_valleys_index,len(resp_signal))
    [resp_peaks_index,resp_valleys_index,max_der_index,min_der_index]=resp_phases_loc_points(resp_signal,min_allowed_resp_rate,max_allowed_resp_rate)
    
    #insp_refernce_signal=resp_signal[insp_signal_index.astype(int)]
    #exp_refernce_signal=resp_signal[exp_signal_index.astype(int)]
    #[insp_peaks_index,insp_valleys_index,max_der_index,_]=resp_phases_loc_points(insp_refernce_signal,min_allowed_resp_rate,max_allowed_resp_rate)
    #[exp_peaks_index,exp_valleys_index,_,min_der_index]=resp_phases_loc_points(exp_refernce_signal,min_allowed_resp_rate,max_allowed_resp_rate)
    
    region_1_insp_index=[]
    region_2_insp_index=[]
    region_3_insp_index=[]
    region_4_insp_index=[]       
    region_1_exp_index=[]
    region_2_exp_index=[]
    region_3_exp_index=[]
    region_4_exp_index=[]
    
    for i in range(len((max_der_index))):
        if i!=5:
            continue
        
        if resp_valleys_index[0]<resp_peaks_index[0]:
            insp_1st_half_index=np.arange(resp_valleys_index[i],max_der_index[i])
            insp_2nd_half_index=np.arange(max_der_index[i],resp_peaks_index[i])
        elif resp_valleys_index[0]>resp_peaks_index[0]:
            insp_1st_half_index=np.arange(resp_valleys_index[i],max_der_index[i])
            insp_2nd_half_index=np.arange(max_der_index[i],resp_peaks_index[i+1])
            
        
        
        if len(insp_1st_half_index)%2==0:
            region_1_insp_index=np.append(region_1_insp_index,insp_1st_half_index[0:int(len(insp_1st_half_index)/2)])
            region_2_insp_index=np.append(region_2_insp_index,insp_1st_half_index[int(len(insp_1st_half_index)/2):int(len(insp_1st_half_index))])
        else:
            region_1_insp_index=np.append(region_1_insp_index,insp_1st_half_index[0:int(np.round(len(insp_1st_half_index)/2))])
            region_2_insp_index=np.append(region_2_insp_index,insp_1st_half_index[int(np.round(len(insp_1st_half_index)/2))+1:int(len(insp_1st_half_index))])
            
            
        if len(insp_2nd_half_index)%2==0:
            region_3_insp_index=np.append(region_3_insp_index,insp_2nd_half_index[0:int(len(insp_2nd_half_index)/2)])
            region_4_insp_index=np.append(region_4_insp_index,insp_2nd_half_index[int(len(insp_2nd_half_index)/2):int(len(insp_2nd_half_index))])
        else:
            region_3_insp_index=np.append(region_3_insp_index,insp_2nd_half_index[0:int(np.round(len(insp_2nd_half_index)/2))])
            region_4_insp_index=np.append(region_4_insp_index,insp_2nd_half_index[int(np.round(len(insp_2nd_half_index)/2))+1:int(len(insp_2nd_half_index))])

    for i in range(len((min_der_index))):
        if i!=6:
            continue
        if resp_valleys_index[0]<resp_peaks_index[0]:
            exp_1st_half_index=np.arange(resp_peaks_index[i],min_der_index[i])
            exp_2nd_half_index=np.arange(min_der_index[i],resp_valleys_index[i+1])
        elif resp_valleys_index[0]>resp_peaks_index[0]:
            exp_1st_half_index=np.arange(resp_peaks_index[i],min_der_index[i])
            exp_2nd_half_index=np.arange(min_der_index[i],resp_valleys_index[i])
            
        
        if len(exp_1st_half_index)%2==0:
            region_1_exp_index=np.append(region_1_exp_index,exp_1st_half_index[0:int(len(exp_1st_half_index)/2)])
            region_2_exp_index=np.append(region_2_exp_index,exp_1st_half_index[int(len(exp_1st_half_index)/2):int(len(exp_1st_half_index))])
        else:
            region_1_exp_index=np.append(region_1_exp_index,exp_1st_half_index[0:int(np.round(len(exp_1st_half_index)/2))])
            region_2_exp_index=np.append(region_2_exp_index,exp_1st_half_index[int(np.round(len(exp_1st_half_index)/2))+1:int(len(exp_1st_half_index))])
            
            
        if len(exp_2nd_half_index)%2==0:
            region_3_exp_index=np.append(region_3_exp_index,exp_2nd_half_index[0:int(len(exp_2nd_half_index)/2)])
            region_4_exp_index=np.append(region_4_exp_index,exp_2nd_half_index[int(len(exp_2nd_half_index)/2):int(len(exp_2nd_half_index))])
        else:
            region_3_exp_index=np.append(region_3_exp_index,exp_2nd_half_index[0:int(np.round(len(exp_2nd_half_index)/2))])
            region_4_exp_index=np.append(region_4_exp_index,exp_2nd_half_index[int(np.round(len(exp_2nd_half_index)/2))+1:int(len(exp_2nd_half_index))])
    
    insp_regions_index={"region_1_4_insp_index":region_1_insp_index,"region_2_4_insp_index":region_2_insp_index,"region_3_4_insp_index":region_3_insp_index,"region_4_4_insp_index":region_4_insp_index}
    exp_regions_index={"region_1_4_exp_index":region_1_exp_index,"region_2_4_exp_index":region_2_exp_index,"region_3_4_exp_index":region_3_exp_index,"region_4_4_exp_index":region_4_exp_index}
    
    return insp_regions_index,exp_regions_index

def insp_exp_regions_3(resp_signal,resp_peaks_index,resp_valleys_index):

    insp_signal_index,exp_signal_index=resp_phases_index_extraction(resp_peaks_index,resp_valleys_index,len(resp_signal))
    
    #insp_refernce_signal=resp_signal[insp_signal_index.astype(int)]
    #exp_refernce_signal=resp_signal[exp_signal_index.astype(int)]
    #[insp_peaks_index,insp_valleys_index,max_der_index,_]=resp_phases_loc_points(insp_refernce_signal,min_allowed_resp_rate,max_allowed_resp_rate)
    #[exp_peaks_index,exp_valleys_index,_,min_der_index]=resp_phases_loc_points(exp_refernce_signal,min_allowed_resp_rate,max_allowed_resp_rate)
    
    region_1_3_insp_index=[]
    region_2_3_insp_index=[]
    region_3_3_insp_index=[]
    
    region_1_3_exp_index=[]
    region_2_3_exp_index=[]
    region_3_3_exp_index=[]
    
    if len(resp_peaks_index)> len(resp_valleys_index):
        for_loop_range= len(resp_peaks_index)-1
    elif len(resp_peaks_index)< len(resp_valleys_index):
        for_loop_range= len(resp_valleys_index)-1
    else:
        for_loop_range=len(resp_valleys_index)-1
    for i in range(for_loop_range):
        if resp_valleys_index[0]<resp_peaks_index[0]:
            
            insp_range=resp_peaks_index[i]-resp_valleys_index[i]
            exp_range= resp_valleys_index[i+1]-resp_peaks_index[i]
            
            region_1_3_insp_index=np.append(region_1_3_insp_index,np.arange(resp_valleys_index[i],resp_valleys_index[i]+np.round((insp_range/3))))
            region_2_3_insp_index=np.append(region_2_3_insp_index,np.arange(resp_valleys_index[i]+np.round(insp_range/3),resp_valleys_index[i]+np.round(insp_range*2/3)))
            region_3_3_insp_index=np.append(region_3_3_insp_index,np.arange(resp_valleys_index[i]+np.round(insp_range*2/3),resp_peaks_index[i]))
            
            
            
            region_1_3_exp_index=np.append(region_1_3_exp_index,np.arange(resp_peaks_index[i],resp_peaks_index[i]+np.round((exp_range/3))))
            region_2_3_exp_index=np.append(region_2_3_exp_index,np.arange(resp_peaks_index[i]+np.round(exp_range/3),resp_peaks_index[i]+np.round(exp_range*2/3)))
            region_3_3_exp_index=np.append(region_3_3_exp_index,np.arange(resp_peaks_index[i]+np.round(exp_range*2/3),resp_valleys_index[i+1]))
            
            
            if len(resp_valleys_index) > len(resp_peaks_index) :
                if i == for_loop_range-1:
                    exp_range= resp_valleys_index[i+1]-resp_peaks_index[i]
                    region_1_3_exp_index=np.append(region_1_3_exp_index,np.arange(resp_peaks_index[i],resp_peaks_index[i]+np.round((exp_range/3))))
                    region_2_3_exp_index=np.append(region_2_3_exp_index,np.arange(resp_peaks_index[i]+np.round(exp_range/3),resp_peaks_index[i]+np.round(exp_range*2/3)))
                    region_3_3_exp_index=np.append(region_3_3_exp_index,np.arange(resp_peaks_index[i]+np.round(exp_range*2/3),resp_valleys_index[i+1]))
   
    
                    
                    

        elif resp_valleys_index[0]>resp_peaks_index[0]:
            insp_range=resp_peaks_index[i+1]-resp_valleys_index[i]
            exp_range= resp_valleys_index[i]-resp_peaks_index[i]
            region_1_3_insp_index=np.append(region_1_3_insp_index,np.arange(resp_valleys_index[i],resp_valleys_index[i]+np.round(insp_range/3)))
            region_2_3_insp_index=np.append(region_2_3_insp_index,np.arange(resp_valleys_index[i]+np.round(insp_range/3),resp_valleys_index[i]+np.round(insp_range*2/3)))
            region_3_3_insp_index=np.append(region_3_3_insp_index,np.arange(resp_valleys_index[i]+np.round(insp_range*2/3),resp_peaks_index[i+1]))
            
            region_1_3_exp_index=np.append(region_1_3_exp_index,np.arange(resp_peaks_index[i],resp_peaks_index[i]+np.round(exp_range/3)))
            region_2_3_exp_index=np.append(region_2_3_exp_index,np.arange(resp_peaks_index[i]+np.round(exp_range/3),resp_peaks_index[i]+np.round(exp_range*2/3)))
            region_3_3_exp_index=np.append(region_3_3_exp_index,np.arange(resp_peaks_index[i]+np.round(exp_range*2/3),resp_valleys_index[i]))
            
            if len(resp_valleys_index) < len(resp_peaks_index) :
                if i == for_loop_range-1:
                    insp_range=resp_peaks_index[i+1]-resp_valleys_index[i]
                    region_1_3_insp_index=np.append(region_1_3_insp_index,np.arange(resp_valleys_index[i],resp_valleys_index[i]+np.round(insp_range/3)))
                    region_2_3_insp_index=np.append(region_2_3_insp_index,np.arange(resp_valleys_index[i]+np.round(insp_range/3),resp_valleys_index[i]+np.round(insp_range*2/3)))
                    region_3_3_insp_index=np.append(region_3_3_insp_index,np.arange(resp_valleys_index[i]+np.round(insp_range*2/3),resp_peaks_index[i+1]))
            
    insp_regions_index={"region_1_3_insp_index":region_1_3_insp_index,"region_2_3_insp_index":region_2_3_insp_index,"region_3_3_insp_index":region_3_3_insp_index}
    exp_regions_index={"region_1_3_exp_index":region_1_3_exp_index,"region_2_3_exp_index":region_2_3_exp_index,"region_3_3_exp_index":region_3_3_exp_index}

    return insp_regions_index,exp_regions_index


def optical_flow_resp_regions(optflow_data,data_affine,data_header,save_data,data_path,regions_number,resp_signal,resp_peaks_index,resp_valleys_index,min_allowed_resp_rate,max_allowed_resp_rate,min_allowed_heart_rate,max_allowed_heart_rate):
    
    if regions_number=="3":
        insp_regions_index,exp_regions_index=insp_exp_regions_3(resp_signal,resp_peaks_index,resp_valleys_index)
        
        region_1_3_insp_index=insp_regions_index["region_1_3_insp_index"]    
        region_2_3_insp_index=insp_regions_index["region_2_3_insp_index"]    
        region_3_3_insp_index=insp_regions_index["region_3_3_insp_index"]    
        region_1_3_exp_index=insp_regions_index["region_1_3_exp_index"]    
        region_2_3_exp_index=insp_regions_index["region_2_3_exp_index"]    
        region_3_3_exp_index=insp_regions_index["region_3_3_exp_index"]   
        opflow_insp_region1_3=optflow_data[:,:,:,:,region_1_3_insp_index.astype(int)]
        opflow_insp_region2_3=optflow_data[:,:,:,:,region_2_3_insp_index.astype(int)]
        opflow_insp_region3_3=optflow_data[:,:,:,:,region_3_3_insp_index.astype(int)]
    
        opflow_exp_region1_3=optflow_data[:,:,:,:,region_1_3_exp_index.astype(int)]
        opflow_exp_region2_3=optflow_data[:,:,:,:,region_2_3_exp_index.astype(int)]
        opflow_exp_region3_3=optflow_data[:,:,:,:,region_3_3_exp_index.astype(int)]
    
        if save_data==1:
        
            save_nifity_data(os.path.join(data_path,'optflow_insp_region1_3.nii.gz'),opflow_insp_region1_3,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_insp_region2_3.nii.gz'),opflow_insp_region2_3,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_insp_region3_3.nii.gz'),opflow_insp_region3_3,data_affine,data_header)
            
            save_nifity_data(os.path.join(data_path,'optflow_exp_region1_3.nii.gz'),opflow_exp_region1_3,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_exp_region2_3.nii.gz'),opflow_exp_region2_3,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_exp_region3_3.nii.gz'),opflow_exp_region3_3,data_affine,data_header)

        
    elif regions_number=="4":  
        
        insp_regions_index,exp_regions_index =insp_exp_regions_4(resp_signal,resp_peaks_index,resp_valleys_index,min_allowed_resp_rate,max_allowed_resp_rate)
        region_1_4_insp_index=insp_regions_index["region_1_4_insp_index"]    
        region_2_4_insp_index=insp_regions_index["region_2_4_insp_index"]    
        region_3_4_insp_index=insp_regions_index["region_3_4_insp_index"]  
        region_4_4_insp_index=insp_regions_index["region_4_4_insp_index"]  
        region_1_4_exp_index=insp_regions_index["region_1_4_exp_index"]    
        region_2_4_exp_index=insp_regions_index["region_2_4_exp_index"]    
        region_3_4_exp_index=insp_regions_index["region_3_4_exp_index"]  
        region_4_4_exp_index=insp_regions_index["region_4_4_exp_index"]
        
        region_1_4_insp_index=insp_regions_index["region_1_4_insp_index"]    
        region_2_4_insp_index=insp_regions_index["region_2_4_insp_index"]    
        region_3_4_insp_index=insp_regions_index["region_3_4_insp_index"]    
        region_4_4_insp_index=insp_regions_index["region_4_4_insp_index"]    
        
        region_1_4_exp_index=insp_regions_index["region_1_4_exp_index"]    
        region_2_4_exp_index=insp_regions_index["region_2_4_exp_index"]    
        region_3_4_exp_index=insp_regions_index["region_3_4_exp_index"]    
        region_3_4_exp_index=insp_regions_index["region_4_4_exp_index"]    
            
        
        opflow_insp_region1=optflow_data[:,:,:,:,region_1_4_insp_index.astype(int)]
        opflow_insp_region2=optflow_data[:,:,:,:,region_2_4_insp_index.astype(int)]
        opflow_insp_region3=optflow_data[:,:,:,:,region_3_4_insp_index.astype(int)]
        opflow_insp_region4=optflow_data[:,:,:,:,region_4_4_insp_index.astype(int)]
    
        opflow_exp_region1=optflow_data[:,:,:,:,region_1_4_exp_index.astype(int)]
        opflow_exp_region2=optflow_data[:,:,:,:,region_2_4_exp_index.astype(int)]
        opflow_exp_region3=optflow_data[:,:,:,:,region_3_4_exp_index.astype(int)]
        opflow_exp_region4=optflow_data[:,:,:,:,region_4_4_exp_index.astype(int)]


        if save_data==1:
        
            save_nifity_data(os.path.join(data_path,'optflow_insp_region1.nii.gz'),opflow_insp_region1,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_insp_region2.nii.gz'),opflow_insp_region2,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_insp_region3.nii.gz'),opflow_insp_region3,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_insp_region4.nii.gz'),opflow_insp_region4,data_affine,data_header)
            
            save_nifity_data(os.path.join(data_path,'optflow_exp_region1.nii.gz'),opflow_exp_region1,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_exp_region2.nii.gz'),opflow_exp_region2,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_exp_region3.nii.gz'),opflow_exp_region3,data_affine,data_header)
            save_nifity_data(os.path.join(data_path,'optflow_exp_region4.nii.gz'),opflow_exp_region4,data_affine,data_header)


def voxel_wise_cardiac_rate(mreg_cardiac,resp_signal,resp_peaks_index,resp_valleys_index,max_allowed_heart_rate,min_allowed_heart_rate,save_data,data_path,data_affine,data_header):
     
     """
     calculate the voxel wise cardiac rate per each respiratory region
     Output: The output is six nii.gz maps each represent the voxel wise cardiac rate map for each respiratory region.
     """
     
     insp_regions_index,exp_regions_index=insp_exp_regions_3(resp_signal,resp_peaks_index,resp_valleys_index)
     
     region_1_3_insp_index=insp_regions_index["region_1_3_insp_index"]    
     region_2_3_insp_index=insp_regions_index["region_2_3_insp_index"]    
     region_3_3_insp_index=insp_regions_index["region_3_3_insp_index"]    
     
     region_1_3_exp_index=exp_regions_index["region_1_3_exp_index"]    
     region_2_3_exp_index=exp_regions_index["region_2_3_exp_index"]    
     region_3_3_exp_index=exp_regions_index["region_3_3_exp_index"]
     
     starting_index_region1_insp_cycles=np.where(region_1_3_insp_index[1:len(region_1_3_insp_index)]-region_1_3_insp_index[0:-1]>1)
     starting_index_region1_insp_cycles=np.append(0,starting_index_region1_insp_cycles+np.ones((1,len(starting_index_region1_insp_cycles))))
     starting_index_region1_insp_cycles=starting_index_region1_insp_cycles.astype(int)
     starting_index_region1_insp_cycles=region_1_3_insp_index[starting_index_region1_insp_cycles]
     
     starting_index_region2_insp_cycles=np.where(region_2_3_insp_index[1:len(region_2_3_insp_index)]-region_2_3_insp_index[0:-1]>1)
     starting_index_region2_insp_cycles=np.append(0,starting_index_region2_insp_cycles+np.ones((1,len(starting_index_region2_insp_cycles))))
     starting_index_region2_insp_cycles=starting_index_region2_insp_cycles.astype(int)
     starting_index_region2_insp_cycles=region_2_3_insp_index[starting_index_region2_insp_cycles]

     
     starting_index_region3_insp_cycles=np.where(region_3_3_insp_index[1:len(region_3_3_insp_index)]-region_3_3_insp_index[0:-1]>1)
     starting_index_region3_insp_cycles=np.append(0,starting_index_region3_insp_cycles+np.ones((1,len(starting_index_region3_insp_cycles))))
     starting_index_region3_insp_cycles=starting_index_region3_insp_cycles.astype(int)
     starting_index_region3_insp_cycles=region_3_3_insp_index[starting_index_region3_insp_cycles]

     
     starting_index_region1_exp_cycles=np.where(region_1_3_exp_index[1:len(region_1_3_exp_index)]-region_1_3_exp_index[0:-1]>1)
     starting_index_region1_exp_cycles=np.append(0,starting_index_region1_exp_cycles+np.ones((1,len(starting_index_region1_exp_cycles))))
     starting_index_region1_exp_cycles=starting_index_region1_exp_cycles.astype(int)
     starting_index_region1_exp_cycles=region_1_3_exp_index[starting_index_region1_exp_cycles]

    
     starting_index_region2_exp_cycles=np.where(region_2_3_exp_index[1:len(region_2_3_exp_index)]-region_2_3_exp_index[0:-1]>1)
     starting_index_region2_exp_cycles=np.append(0,starting_index_region2_exp_cycles+np.ones((1,len(starting_index_region2_exp_cycles))))
     starting_index_region2_exp_cycles=starting_index_region2_exp_cycles.astype(int)
     starting_index_region2_exp_cycles=region_2_3_exp_index[starting_index_region2_exp_cycles]

     
     starting_index_region3_exp_cycles=np.where(region_3_3_exp_index[1:len(region_3_3_exp_index)]-region_3_3_exp_index[0:-1]>1)
     starting_index_region3_exp_cycles=np.append(0,starting_index_region3_exp_cycles+np.ones((1,len(starting_index_region3_exp_cycles))))
     starting_index_region3_exp_cycles=starting_index_region3_exp_cycles.astype(int)
     starting_index_region3_exp_cycles=region_3_3_exp_index[starting_index_region3_exp_cycles]

     
     starting_index_all_regions=np.hstack((starting_index_region1_insp_cycles,starting_index_region2_insp_cycles,starting_index_region3_insp_cycles,starting_index_region1_exp_cycles,starting_index_region2_exp_cycles,starting_index_region3_exp_cycles))
     starting_index_all_regions=sorted(starting_index_all_regions)
     starting_index_all_regions=np.array(starting_index_all_regions)
     
     if starting_index_region1_insp_cycles[0]<starting_index_region1_exp_cycles[0]: 
         """
         calcuting the indicies of each region in the starting_index_all_regions, so getting the index of each regions elements in this array 
         """
         
         region_1_insp_index=np.arange(0,len(starting_index_region3_exp_cycles)*6,6)
         region_2_insp_index=np.arange(1,len(starting_index_region3_exp_cycles)*6,6)
         region_3_insp_index=np.arange(2,len(starting_index_region3_exp_cycles)*6,6)

         region_1_exp_index=np.arange(3,len(starting_index_region3_exp_cycles)*6,6)
         region_2_exp_index=np.arange(4,len(starting_index_region3_exp_cycles)*6,6)
         region_3_exp_index=np.arange(5,len(starting_index_region3_exp_cycles)*6,6)
     
     else:
         
         region_1_exp_index=np.arange(0,len(starting_index_region3_insp_cycles)*6,6)
         region_2_exp_index=np.arange(1,len(starting_index_region3_insp_cycles)*6,6)
         region_3_exp_index=np.arange(2,len(starting_index_region3_insp_cycles)*6,6)

         region_1_insp_index=np.arange(3,len(starting_index_region3_insp_cycles)*6,6)
         region_2_insp_index=np.arange(4,len(starting_index_region3_insp_cycles)*6,6)
         region_3_insp_index=np.arange(5,len(starting_index_region3_insp_cycles)*6,6)


         
     cardiac_rate_insp_region1=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],len(starting_index_region1_insp_cycles)))
     cardiac_rate_insp_region2=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],len(starting_index_region2_insp_cycles)))
        
     cardiac_rate_exp_region1=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],len(starting_index_region1_exp_cycles)))
     cardiac_rate_exp_region2=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],len(starting_index_region2_exp_cycles)))
     
     if starting_index_region1_insp_cycles[0]<starting_index_region1_exp_cycles[0]: 
         cardiac_rate_exp_region3=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],len(starting_index_region3_exp_cycles)-1))
         cardiac_rate_insp_region3=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],len(starting_index_region3_insp_cycles)))
     else:
         cardiac_rate_insp_region3=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],len(starting_index_region3_insp_cycles)-1))
         cardiac_rate_exp_region3=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],len(starting_index_region3_exp_cycles)))
     
     
     for i in range(mreg_cardiac.shape[0]):
         for j in range(mreg_cardiac.shape[1]):
             for k in range (mreg_cardiac.shape[2]):
                      peaks_index,valleys_index =find_peaks_valleys(mreg_cardiac[i,j,k,:],main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_heart_rate,upper_RRPm=max_allowed_heart_rate)
                      
                      if valleys_index!=[]:
                          
                          common_values= valleys_index[np.where(np.in1d(valleys_index,starting_index_all_regions))[0]]
                          common_values_valleys_index=np.where(np.in1d(valleys_index,common_values))
                          common_values_region_index=np.where(np.in1d(starting_index_all_regions,common_values))
                          common_values_region_index=np.array(common_values_region_index)
                          valleys_index=np.delete(valleys_index,common_values_valleys_index,0)
                          valleys_starting_regions_index=sorted(np.hstack((starting_index_all_regions,valleys_index)))
                          valleys_starting_regions_index=np.array(valleys_starting_regions_index)
                          
                          starting_index_all_regions_new=np.where(np.in1d(valleys_starting_regions_index,starting_index_all_regions))[0]
                          starting_index_all_regions_old=np.arange(0,len(starting_index_all_regions))
                          
                          differnce=starting_index_all_regions_new-starting_index_all_regions_old
                          cardiac_duration_all_regions= differnce[1:len(differnce)]-differnce[0:len(differnce)-1]
                          
                          if common_values_region_index!=[]:
                            cardiac_duration_all_regions[(common_values_region_index-1)]=cardiac_duration_all_regions[common_values_region_index-1]+1    
                           
                          if starting_index_region1_insp_cycles[0]<starting_index_region1_exp_cycles[0]: 
                            
                            cardiac_rate_insp_region1[i,j,k,:] = cardiac_duration_all_regions[region_1_insp_index]/ (starting_index_all_regions[region_2_insp_index]-starting_index_all_regions[region_1_insp_index])                        
                            cardiac_rate_insp_region2[i,j,k,:] = cardiac_duration_all_regions[region_2_insp_index]/ (starting_index_all_regions[region_3_insp_index]-starting_index_all_regions[region_2_insp_index])  
                            cardiac_rate_insp_region3[i,j,k,:] = cardiac_duration_all_regions[region_3_insp_index]/ (starting_index_all_regions[region_1_exp_index]-starting_index_all_regions[region_3_insp_index])
                            
                            cardiac_rate_exp_region1[i,j,k,:] = cardiac_duration_all_regions[region_1_exp_index]/ (starting_index_all_regions[region_2_exp_index]-starting_index_all_regions[region_1_exp_index])                        
                            cardiac_rate_exp_region2[i,j,k,:] = cardiac_duration_all_regions[region_2_exp_index]/ (starting_index_all_regions[region_3_exp_index]-starting_index_all_regions[region_2_exp_index])  
                            cardiac_rate_exp_region3[i,j,k,:] = cardiac_duration_all_regions[region_3_exp_index[0:len(region_3_exp_index)-1]]/ (starting_index_all_regions[region_1_insp_index[1:len(region_1_insp_index)]]-starting_index_all_regions[region_3_exp_index[0:len(region_3_exp_index)-1]])
                                  
                          else:
                            cardiac_rate_exp_region1[i,j,k,:] = cardiac_duration_all_regions[region_1_exp_index]/ (starting_index_all_regions[region_2_exp_index]-starting_index_all_regions[region_1_exp_index])                        
                            cardiac_rate_exp_region2[i,j,k,:] = cardiac_duration_all_regions[region_2_exp_index]/ (starting_index_all_regions[region_3_exp_index]-starting_index_all_regions[region_2_exp_index])  
                            cardiac_rate_exp_region3[i,j,k,:] = cardiac_duration_all_regions[region_3_exp_index]/ (starting_index_all_regions[region_1_insp_index]-starting_index_all_regions[region_3_exp_index])
                            
                            cardiac_rate_insp_region1[i,j,k,:] = cardiac_duration_all_regions[region_1_insp_index]/ (starting_index_all_regions[region_2_insp_index]-starting_index_all_regions[region_1_insp_index])                        
                            cardiac_rate_insp_region2[i,j,k,:] = cardiac_duration_all_regions[region_2_insp_index]/ (starting_index_all_regions[region_3_insp_index]-starting_index_all_regions[region_2_insp_index])  
                            cardiac_rate_insp_region3[i,j,k,:] = cardiac_duration_all_regions[region_3_insp_index[0:len(region_3_insp_index)-1]]/ (starting_index_all_regions[region_1_exp_index[1:len(region_1_exp_index)]]-starting_index_all_regions[region_3_insp_index[0:len(region_3_insp_index)-1]])
                      else:
                          cardiac_rate_insp_region1[i,j,k,:]=np.zeros((len(starting_index_region1_insp_cycles)))
                          cardiac_rate_insp_region2[i,j,k,:]=np.zeros((len(starting_index_region2_insp_cycles)))
                          
                        
                          cardiac_rate_exp_region1[i,j,k,:]=np.zeros((len(starting_index_region1_exp_cycles)))
                          cardiac_rate_exp_region2[i,j,k,:]=np.zeros((len(starting_index_region2_exp_cycles)))
                         
                          if starting_index_region1_insp_cycles[0]<starting_index_region1_exp_cycles[0]: 
                              cardiac_rate_insp_region3[i,j,k,:]=np.zeros((len(starting_index_region3_insp_cycles)))    
                              cardiac_rate_exp_region3[i,j,k,:]=np.zeros((len(starting_index_region3_exp_cycles)-1))
                          elif starting_index_region1_insp_cycles[0]> starting_index_region1_exp_cycles[0]:
                              cardiac_rate_insp_region3[i,j,k,:]=np.zeros((len(starting_index_region3_insp_cycles)-1))    
                              cardiac_rate_exp_region3[i,j,k,:]=np.zeros((len(starting_index_region3_exp_cycles)))
                        
     if save_data==1:  
              save_nifity_data(os.path.join(data_path,'cardiac_rate_map_insp_region1.nii.gz'),cardiac_rate_insp_region1,data_affine,data_header)
              save_nifity_data(os.path.join(data_path,'cardiac_rate_map_insp_region2.nii.gz'),cardiac_rate_insp_region2,data_affine,data_header)
              save_nifity_data(os.path.join(data_path,'cardiac_rate_map_insp_region3.nii.gz'),cardiac_rate_insp_region3,data_affine,data_header)
        
              save_nifity_data(os.path.join(data_path,'cardiac_rate_map_exp_region1.nii.gz'),cardiac_rate_exp_region1,data_affine,data_header)
              save_nifity_data(os.path.join(data_path,'cardiac_rate_map_exp_region2.nii.gz'),cardiac_rate_exp_region2,data_affine,data_header)
              save_nifity_data(os.path.join(data_path,'cardiac_rate_map_exp_region3.nii.gz'),cardiac_rate_exp_region3,data_affine,data_header)
     
         
                                          
                        
                      
         
                 
                 
def caculate_the_cardiac_rate(mreg_cardiac,resp_region_index,starting_index_resp_cycles,max_allowed_heart_rate,min_allowed_heart_rate,i,j,k,l):
     """
     cacluate the cardiac rate of a given voxel [i,j,k] within a respiratory region 
     
     Output: cardiac rate for a given voxel within a respiratory region
     
     """
     
     selected_index=resp_region_index[starting_index_resp_cycles[l]:starting_index_resp_cycles[l+1]-1]
     #cardiac_signal_selected_part=mreg_cardiac[i,j,k,selected_index.astype(int)]
     peaks_index,valleys_index =find_peaks_valleys(mreg_cardiac[i,j,k,:],main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_heart_rate,upper_RRPm=max_allowed_heart_rate)
     #cardiac_rate=len(valleys_index)/(len(selected_index)*60/10)
     valleys_index_resp_region=np.where(np.in1d(valleys_index,selected_index))[0]
     if len(valleys_index_resp_region)>1:
        cardiac_duration=valleys_index[valleys_index_resp_region[1]]-valleys_index[valleys_index_resp_region[0]]
     else:
         cardiac_duration=valleys_index[valleys_index_resp_region+1]-valleys_index[valleys_index_resp_region]
     if cardiac_duration.size==0:
         cardiac_duration=0
     return cardiac_duration /10




def cardiac_rate_resp_phase(mreg_cardiac,resp_signal,max_allowed_heart_rate,min_allowed_heart_rate,max_allowed_resp_rate,min_allowed_resp_rate,save_data,data_path,data_affine,data_header):
    """
    caculate the cardiac rate for each phase 
    """
    
    resp_peaks_index,resp_valleys_index =find_peaks_valleys(resp_signal,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_heart_rate,upper_RRPm=max_allowed_heart_rate)
    resp_phases_index=np.append(resp_peaks_index,resp_valleys_index)
    resp_phases_index=np.sort(resp_phases_index)
    

    
    if len(resp_phases_index)%2 != 0:
        resp_phases_index=resp_phases_index[0:len(resp_phases_index)-1]
    
    if resp_peaks_index[0]>resp_valleys_index[0]:
        resp_valleys_index=np.arange(0,len(resp_phases_index),2)
        resp_peaks_index=np.arange(1,len(resp_phases_index),2)
        insp_durations= resp_phases_index[resp_peaks_index]-resp_phases_index[resp_valleys_index]
        exp_durations= resp_phases_index[resp_valleys_index[1:len(resp_valleys_index)]]-resp_phases_index[resp_peaks_index[0:len(resp_peaks_index)-1]]
        cardiac_rate_insp=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],int(len(resp_phases_index)/2)))
        cardiac_rate_exp=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],int(len(resp_phases_index)/2)-1))
        
    elif resp_peaks_index[0] < resp_valleys_index[0]: 
        resp_peaks_index=np.arange(0,len(resp_phases_index),2)
        resp_valleys_index=np.arange(1,len(resp_phases_index),2)
        exp_durations=resp_phases_index[resp_valleys_index]-resp_phases_index[resp_peaks_index]
        insp_durations=resp_phases_index[resp_peaks_index[1:len(resp_peaks_index)]]-resp_phases_index[resp_valleys_index[0:len(resp_valleys_index)-1]]
        cardiac_rate_insp=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],int(len(resp_phases_index)/2)-1))
        cardiac_rate_exp=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],int(len(resp_phases_index)/2)))
    
    
    
   
    old_resp_phases_index=np.arange(0,len(resp_phases_index))
    
    
    for i in range(mreg_cardiac.shape[0]):
         for j in range(mreg_cardiac.shape[1]):
             for k in range (mreg_cardiac.shape[2]):
                     cardiac_peaks_index,cardiac_valleys_index =find_peaks_valleys(mreg_cardiac[i,j,k,:],main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)
                     
                     if cardiac_valleys_index != []:
                         cardiac_valleys_in_resp=np.append(cardiac_valleys_index,resp_phases_index)
                         
                         cardiac_valleys_in_resp=np.sort(cardiac_valleys_in_resp)
                         unique_cardiac_valleys_in_resp,unique_idx,counts=np.unique(cardiac_valleys_in_resp,return_counts=1,return_index=1)
                         new_resp_phases_index=np.where(np.in1d(unique_cardiac_valleys_in_resp,resp_phases_index))[0]
                         
                         repetated_items=np.where(counts>1)
                         repeated_index=unique_idx[repetated_items]
                         repeated_values=cardiac_valleys_in_resp[repeated_index]
                         common_values_index=np.where(np.in1d(resp_phases_index,repeated_values))[0]
                         
                         
                         differnce=new_resp_phases_index-old_resp_phases_index
                         differnce=np.append(differnce[0],differnce[1:len(differnce)]-differnce[0:len(differnce)-1])
                         differnce[common_values_index]+=1
                         
                         cardiac_valleys_insp=differnce[resp_valleys_index]
                         cardiac_valleys_exp=differnce[resp_peaks_index]
                         cardiac_rate_insp[i,j,k,:]=cardiac_valleys_insp[0:len(insp_durations)]/insp_durations
                         cardiac_rate_exp[i,j,k,:]=cardiac_valleys_exp[0:len(exp_durations)]/exp_durations
                         
                     elif cardiac_valleys_index ==[]:
                         cardiac_rate_insp[i,j,k,:]=0
                         cardiac_rate_exp[i,j,k,:]=0
                                 
                 
                 
                 
    if save_data==1:  
         save_nifity_data(os.path.join(data_path,'cardiac_rate_insp.nii.gz'),cardiac_rate_insp,data_affine,data_header)
         save_nifity_data(os.path.join(data_path,'cardiac_rate_exp.nii.gz'),cardiac_rate_exp,data_affine,data_header)
        
                     
                     
    
    return                 



"""

def cardiac_rate_resp_phase(mreg_cardiac,resp_signal,max_allowed_heart_rate,min_allowed_heart_rate,max_allowed_resp_rate,min_allowed_resp_rate,save_data,data_path,data_affine,data_header):
    caculate the cardiac rate for each phase 
 
    
    resp_peaks_index,resp_valleys_index =find_peaks_valleys(resp_signal,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)
    resp_phases_index=np.append(resp_peaks_index,resp_valleys_index)
    resp_phases_index=np.sort(resp_phases_index)
    
    exp_first=0
    insp_first=0
    if resp_peaks_index[0]< resp_valleys_index[0]:
        exp_first=1
        
    else:
        insp_first=1
    
    if len(resp_phases_index)%2 != 0:
        resp_phases_index=resp_phases_index[0:len(resp_phases_index)-1]
        
    cardiac_rate_insp=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],int(len(resp_phases_index)/2)))
    cardiac_rate_exp=np.empty((mreg_cardiac.shape[0],mreg_cardiac.shape[1],mreg_cardiac.shape[2],int(len(resp_phases_index)/2)))
    
    for i in range(mreg_cardiac.shape[0]):
         for j in range(mreg_cardiac.shape[1]):
             for k in range (mreg_cardiac.shape[2]):
                 counter =0
                 if sum(mreg_cardiac[i,j,k,:])==0:
                         cardiac_rate_insp[i,j,k,:]=0
                         cardiac_rate_exp[i,j,k,:]=0
                         continue
                 for l in range (0,len(resp_phases_index),2):     
                     
                     if exp_first==1:
                         selected_exp_index= np.arange(resp_phases_index[i],resp_phases_index[i+1])
                         selected_insp_index=np.arange(resp_phases_index[i+1],resp_phases_index[i+2])
                     elif insp_first==1:
                         selected_insp_index= np.arange(resp_phases_index[i],resp_phases_index[i+1])
                         selected_exp_index=np.arange(resp_phases_index[i+1],resp_phases_index[i+2])
                          
                     cardiac_peaks_index,cardiac_valleys_index =find_peaks_valleys(mreg_cardiac[i,j,k,:],main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_heart_rate,upper_RRPm=max_allowed_heart_rate)
                     cardiac_rate_insp_voxel=np.sum(np.in1d(cardiac_valleys_index,selected_insp_index))/len(selected_insp_index)
                     cardiac_rate_exp_voxel=np.sum(np.in1d(cardiac_valleys_index,selected_exp_index))/len(selected_exp_index)
                     cardiac_rate_insp[i,j,k,counter]=cardiac_rate_insp_voxel
                     cardiac_rate_exp[i,j,k,counter]=cardiac_rate_exp_voxel
                     counter+=1
    
    
    if save_data==1:  
         save_nifity_data(os.path.join(data_path,'cardiac_rate_insp.nii.gz'),cardiac_rate_insp,data_affine,data_header)
         save_nifity_data(os.path.join(data_path,'cardiac_rate_exp.nii.gz'),cardiac_rate_exp,data_affine,data_header)
        
                     
                     
    
    return     
"""            
                 
def summing_niffity_file(samples_name,data_path,file_name,file_saving_name):
    summed_data=np.zeros((45,54,45))
    for sample_name in samples_name:
        [input_data,input_data_affine,input_data_header]=load_niftiydata(os.path.join(data_path,sample_name,file_name))
        summed_data=summed_data+input_data
    save_nifity_data(os.path.join(data_path,file_saving_name),summed_data,input_data_affine,input_data_header)    
    return        
    

def mean_map(input_data,input_data_affine,input_data_header,cycle_index,main_path,sample_name,file_name,save_data):
    last_index=np.sum(cycle_index)
    mean_map=np.empty(np.shape(input_data)[0:3])
    for i in range(np.shape(input_data)[0]):
        for j in range (np.shape(input_data)[1]):
            for k in range(np.shape(input_data)[2]):
                mean_map[i,j,k]=np.mean(input_data[i,j,k,0:int(last_index)])
    if save_data==1:
        
        save_nifity_data(os.path.join(main_path,sample_name,file_name),mean_map,input_data_affine,input_data_header)
    
    
    return mean_map



def CV_map(input_data,cycle_index):
    last_index=np.sum(cycle_index)
    cv_map=np.empty(np.shape(input_data)[0:3])
    for i in range(np.shape(input_data)[0]):
        for j in range (np.shape(input_data)[1]):
            for k in range(np.shape(input_data)[2]):
                if np.mean(input_data[i,j,k,0:int(last_index)])==0:
                    cv_map[i,j,k]=0        
                else:    
                    
                    cv_map[i,j,k]=np.std(input_data[i,j,k,0:int(last_index)])/np.mean(input_data[i,j,k,0:int(last_index)])
    
    
    return cv_map



def mean_over_samples(data_new,data_old,counter):
    data_new=data_new+data_old
    counter=counter+1
    return data_new , counter 

"""


main_path='/data/fmri/Youssef/Data/MREG_data/controls'
file_names=os.listdir(main_path)

cardiac_ffdm_inspiration_file_name='cardic_ffdm_inspiration_phase.nii.gz'
cardiac_ffdm_expiration_file_name='cardic_ffdm_expiration_phase.nii.gz'

insp_cycles_index_file_name='insp_cycle_start_index.npy'
exp_cycles_index_file_name='exp_cycle_start_index.npy'

output_file_insp_mean='mean_insp'
output_file_exp_mean='mean_exp'

mean_cardiac_insp_map_file_name='mean_cardiac_insp_map.nii.gz'
mean_cardiac_exp_map_file_name='mean_cardiac_exp_map.nii.gz'
noisy_samples=['mean_insp','mean_exp','20180605_2_FA5_c01.ica' , '20190109_2_FA5_c01.ica' ,'info', 'missing_data','all_samples_calculations']


counter_insp=-1
counter_exp=-1


for file_name in file_names:
    
    if file_name in noisy_samples:
        continue    

    
    cardiac_ffdm_inspiration,cardiac_ffdm_inspiration_affine,cardiac_ffdm_inspiration_header=load_niftiydata(os.path.join(main_path,file_name,cardiac_ffdm_inspiration_file_name))
    
    cardiac_ffdm_expiration,cardiac_ffdm_expiration_affine,cardiac_ffdm_expiration_header=load_niftiydata(os.path.join(main_path,file_name,cardiac_ffdm_expiration_file_name))
    
    insp_cycle_index=load_npydata(os.path.join(main_path,file_name,insp_cycles_index_file_name))
    exp_cycle_index=load_npydata(os.path.join(main_path,file_name,exp_cycles_index_file_name))
    
    ### getting a mean map for each sample and save it in a niffiy file

    mean_cardiac_insp_map=mean_map(cardiac_ffdm_inspiration,insp_cycle_index)
    mean_cardiac_exp_map=mean_map(cardiac_ffdm_expiration,exp_cycle_index)
    
    save_nifity_data(os.path.join(main_path,output_file_insp_mean,file_name+'mean_cardiac_insp_map.nii.gz'),mean_cardiac_insp_map,cardiac_ffdm_inspiration_affine,cardiac_ffdm_inspiration_header)
    save_nifity_data(os.path.join(main_path,output_file_exp_mean,file_name+'mean_cardiac_exp_map.nii.gz'),mean_cardiac_exp_map,cardiac_ffdm_expiration_affine,cardiac_ffdm_expiration_header)
    
    
    CV_cardiac_insp_map=CV_map(cardiac_ffdm_inspiration,insp_cycle_index)
    CV_cardiac_exp_map=CV_map(cardiac_ffdm_expiration,exp_cycle_index)
    
    save_nifity_data(os.path.join(main_path,file_name,'CV_cardiac_insp_map.nii.gz'),CV_cardiac_insp_map,cardiac_ffdm_inspiration_affine,cardiac_ffdm_inspiration_header)
    save_nifity_data(os.path.join(main_path,file_name,'CV_cardiac_exp_map.nii.gz'),CV_cardiac_exp_map,cardiac_ffdm_expiration_affine,cardiac_ffdm_expiration_header)
    
    
    mean_cardiac_insp_map,mean_cardiac_insp_map_affine,mean_cardiac_insp_map_header=load_niftiydata(os.path.join(main_path,file_name,mean_cardiac_insp_map_file_name))
    mean_cardiac_exp_map,mean_cardiac_exp_map_affine,mean_cardiac_exp_map_header=load_niftiydata(os.path.join(main_path,file_name,mean_cardiac_exp_map_file_name))
    
    
    if (counter_insp==-1) and (counter_exp==-1) :
        old_data_insp=mean_cardiac_insp_map
        old_data_exp=mean_cardiac_exp_map
        counter_insp=0
        counter_exp=0
        continue
    
    old_data_insp,counter_insp=mean_over_samples(mean_cardiac_insp_map,old_data_insp,counter_insp)
    old_data_exp,counter_exp=mean_over_samples(mean_cardiac_exp_map,old_data_exp,counter_exp)
    print(counter_exp)
    print(counter_insp)
    
mean_over_samples_insp=old_data_insp/counter_insp
mean_over_samples_exp=old_data_exp/counter_exp
save_nifity_data(os.path.join(main_path,'all_samples_calculations','mean_over_samples_insp.nii.gz'),mean_over_samples_insp,mean_cardiac_insp_map_affine,mean_cardiac_insp_map_header)
save_nifity_data(os.path.join(main_path,'all_samples_calculations','mean_over_samples_exp.nii.gz'),mean_over_samples_exp,mean_cardiac_exp_map_affine,mean_cardiac_exp_map_header)
     
"""
   
    
