import sys
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from respiratory_phases_interval_extraction.load_data import load_niftiydata
import os
import numpy as np
import matplotlib.pyplot as plt
import heapq

def find_refernce_voxel(sample_names,method,main_path,mreg_data_file_name,refernce_voxel,new_refernce_voxel,plot_results):





    if method=='automatic':
        refernce_voxels_list=np.empty((len(sample_names),),dtype=object)
        cordinate_change_range=np.linspace(-3,3,7)
    
        for sample_index in range(len(sample_names)):
            data_path=os.path.join(main_path,sample_names[sample_index],mreg_data_file_name)
            cardiac_mreg_signal,header,affine=load_niftiydata(data_path)
            refernce_cardiac_voxel_21_39_17=cardiac_mreg_signal[21,39,17,:]
        
            sum_abs_diff=[]
            added_number_coordinates=np.empty((len(cordinate_change_range)**3,),dtype=object)
            counter=0
            for i in cordinate_change_range:
                for j in cordinate_change_range:
                    for k in cordinate_change_range:
                        refernce_cardiac_voxel=cardiac_mreg_signal[int(refernce_voxel[0]+i),int(refernce_voxel[1]+j),int(refernce_voxel[2]+k),:]
                        if len(refernce_cardiac_voxel[refernce_cardiac_voxel>0]) >= len(refernce_cardiac_voxel_21_39_17[refernce_cardiac_voxel_21_39_17>0]):
                            abs_diff=refernce_cardiac_voxel[refernce_cardiac_voxel>0][0:len(refernce_cardiac_voxel_21_39_17[refernce_cardiac_voxel_21_39_17>0])]-refernce_cardiac_voxel_21_39_17[refernce_cardiac_voxel_21_39_17>0]
                        else:
                            abs_diff=refernce_cardiac_voxel[refernce_cardiac_voxel>0]-refernce_cardiac_voxel_21_39_17[refernce_cardiac_voxel_21_39_17>0][0:len(refernce_cardiac_voxel[refernce_cardiac_voxel>0])]                        
                        sum_abs_diff=np.append(sum_abs_diff,sum(abs_diff))
                        added_number_coordinates[counter]=[i,j,k]
                        counter=counter+1
                        
            max_3_diff_index=heapq.nlargest(2, range(len(sum_abs_diff)), sum_abs_diff.take)            
            max_3_diff_corrdiantes=added_number_coordinates[max_3_diff_index]
            sum_max_3_corrdinates=[]
            
            for i in range(len(max_3_diff_corrdiantes)):
                sum_max_3_corrdinates=np.append(sum_max_3_corrdinates,sum(np.abs(max_3_diff_corrdiantes[i])))
            min_corr_index=np.argmin(sum_max_3_corrdinates)
            
            refernce_voxels_list[sample_index]=[refernce_voxel[0]+max_3_diff_corrdiantes[min_corr_index][0],refernce_voxel[1]+max_3_diff_corrdiantes[min_corr_index][1],refernce_voxel[2]+max_3_diff_corrdiantes[min_corr_index][2]]
            
            if plot_results==1:  
                plt.figure()
                refernce_cardiac_voxel=cardiac_mreg_signal[int(refernce_voxels_list[sample_index][0]),int(refernce_voxels_list[sample_index][1]),int(refernce_voxels_list[sample_index][2]),:]
            
                time=np.linspace(0,len(refernce_cardiac_voxel)/10,len(refernce_cardiac_voxel))
                
                title=sample_names[sample_index] + ' ' +str(refernce_voxel)+ ' '+ str(refernce_voxels_list[sample_index])
                plt.title(title)
                plt.plot(time,refernce_cardiac_voxel,label=str(refernce_voxels_list[sample_index]))
                plt.plot(time,refernce_cardiac_voxel_21_39_17,label=refernce_voxel)
                plt.legend()
        return refernce_voxels_list
        
    elif method=='manual':
            data_path=os.path.join(main_path,sample_names[sample_index],mreg_data_file_name)
            cardiac_mreg_signal,header,affine=load_niftiydata(data_path)
            refernce_cardiac_voxel_21_39_17=cardiac_mreg_signal[21,39,17,:]
        
            refernce_cardiac_voxel=cardiac_mreg_signal[int(new_refernce_voxel[0]),int(new_refernce_voxel[1]),int(new_refernce_voxel[2]),:]
            
            if plot_results==1:
                plt.figure()
                time=np.linspace(0,len(refernce_cardiac_voxel)/10,len(refernce_cardiac_voxel))
                
                title=sample_names + ' ' +refernce_voxel+ ' '+str(new_refernce_voxel)
                plt.title(title)    
                plt.plot(time,refernce_cardiac_voxel,label=str(new_refernce_voxel))
                plt.plot(time,refernce_cardiac_voxel_21_39_17,label=refernce_voxel)
                plt.legend()
                
