"""
This code is used to find the refence voxel in the caridac data 

"""



import sys
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from respiratory_phases_interval_extraction.load_data import load_niftiydata
import os
import numpy as np
import matplotlib.pyplot as plt
import heapq

controls_path='/data/fmri/Youssef/Data/MREG_data/controls'
AD_path='/data/fmri/Youssef/Data/MREG_data/AD'
cardiac_mreg_file_name='fullcard_ffdm.nii.gz'

control_sample_names=[
'20160614_fa5_75comp.ica',
'20161025_mreg_fa5.ica',
'20161111_mreg_fa5.ica', 
'20161122_mreg_fa5_2.ica' ,
'20161216_mreg_fa5.ica',
'20170110_mreg_fa5.ica',
'20170117_mreg_fa5.ica',
'20170124_mreg_fa5.ica',
'20170124_mreg_fa5_2.ica', 
'20170221_mreg_fa5.ica',
'20180515_FA5_c0_1.ica',
'20180530_1_FA5_c01.ica',
'20180605_2_FA5_c01.ica',
'20180606_1_FA5_c01.ica',
'20180612_1_FA5_c01.ica',
'20180612_2_FA5_c01.ica',
'20180613_1_FA5_c01.ica',
'20180613_2_FA5_c01.ica',
'20180619_2_FA5_c01.ica',
'20180626_1_FA5_c01.ica',
'20180626_3_FA5_c01.ica',
'20181219_2_FA5_c01.ica',
'20190108_1_FA5_c01.ica',
'20190109_2_FA5_c01.ica',
'20190109_3_FA5_c01.ica',
'20190605_3_FA5_c01.ica' ]

AD_sample_names=['20160226_mreg_fa5.ica', 
'20160617_mreg_fa5.ica' ,
'20160826_mreg_fa5.ica' ,
'20161004_mreg_fa5.ica' ,
'20161011_mreg_fa5.ica' ,
'20161028_mreg_fa5.ica' ,
'20161125_mreg_fa5.ica' ,
'20180410_1_FA5_c01.ica',
'20180417_1_FA5_c01.ica' ,
'20180911_2_FA5_c01.ica' ,
'20180918_1_FA5_c01.ica' ,
'20181002_1_FA5_c01.ica',
'20181023_2_FA5_c01.ica',
'20181113_1_FA5_c01.ica' ,
'20181120_1_FA5_c01.ica' ,
'20181204_3_FA5_c01.ica' ,
'20181204_4_FA5_c01.ica' ,
'20181205_3_FA5_c01.ica' ,
'20181205_4_FA5_c01.ica' ,
'20181211_2_FA5_c01.ica' ,
'20181212_2_FA5_c01.ica' ,
'20181218_1_FA5_c01.ica' ,
'20181218_2_FA5_c01.ica' ,
'20190122_2_FA5_c01.ica' ,
'20190122_3_FA5_c01.ica' ,
'20190402_3_FA5_c01.ica' ,
'20190409_1_FA5_c01.ica' ,
'20190417_1_FA5_c01.ica' ,
'20190423_2_FA5_c01.ica' ,
'20190430_1_FA5_c01.ica' ,
'20190507_2_FA5_c01.ica',
]

refernce_voxel= '21,39,17'

refernce_voxels_control=[
                 '21,39,20',
                 '21,41,18',
                 '21,36,17',
                 '22,41,18',
                 '21,40,17',
                 '21,37,17',
                 '21,36,18',
                 '21,35,18',
                 '21,40,18',
                 '21,39,17',
                 '21,40,18',
                 '21,41,16',
                 '21,40,16',
                 '21,39,17',
                 '22,40,17',
                 '22,40,18',
                 '22,40,18',
                 '22,39,19',
                 '22,37,15',
                 '21,39,17',
                 '21,39,17',
                 '22,39,15',
                 '21,39,17',
                 '21,40,18',
                 '21,41,17',
                 '21,39,17',
        ]


refernce_cardiac_voxel_coordinates=[21,39,17]
refernce_voxels_list_control=[[21,39,20],
                 [21,41,18],
                 [21,36,17],
                 [22,41,18],
                 [21,40,17],
                 [21,37,17],
                 [21,36,18],
                 [21,35,18],
                 [21,40,18],
                 [21,39,17],
                 [21,40,18],
                 [21,41,16],
                 [21,40,16],
                 [21,39,17],
                 [22,40,17],
                 [22,40,18],
                 [22,40,18],
                 [22,39,19],
                 [22,37,15],
                 [21,39,17],
                 [21,39,17],
                 [22,39,15],
                 [21,39,17],
                 [21,40,18],
                 [21,41,17],
                 [21,39,17],
                 ]

refernce_voxels_AD=['21,40,20',
                    '22,41,17',
                    '22,39,18',
                    '21,41,19',
                    '21,39,17'
                    ]
refernce_voxel_list_AD=[[21,40,20],
                        [22,41,17],
                        [22,39,18],
                        [21,41,19],
                        [21,39,17]
                        ]
sample_names=AD_sample_names
refernce_voxels_list=np.empty((31,),dtype=object)
refernce_voxels=refernce_voxels_AD
main_path=AD_path
sample_index=8
new_refernce_voxel=[21,40,19]



cordinate_change_range=np.linspace(-3,3,7)
automatic_change=0

if automatic_change==1:

    for sample_index in range(len(sample_names)):
        data_path=os.path.join(main_path,sample_names[sample_index],cardiac_mreg_file_name)
        cardiac_mreg_signal,header,affine=load_niftiydata(data_path)
        refernce_cardiac_voxel_21_39_17=cardiac_mreg_signal[21,39,17,:]
    
        sum_abs_diff=[]
        added_number_coordinates=np.empty((len(cordinate_change_range)**3,),dtype=object)
        counter=0
        for i in cordinate_change_range:
            for j in cordinate_change_range:
                for k in cordinate_change_range:
                    refernce_cardiac_voxel=cardiac_mreg_signal[int(refernce_cardiac_voxel_coordinates[0]+i),int(refernce_cardiac_voxel_coordinates[1]+j),int(refernce_cardiac_voxel_coordinates[2]+k),:]
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
        
        refernce_voxels_list[sample_index]=[refernce_cardiac_voxel_coordinates[0]+max_3_diff_corrdiantes[min_corr_index][0],refernce_cardiac_voxel_coordinates[1]+max_3_diff_corrdiantes[min_corr_index][1],refernce_cardiac_voxel_coordinates[2]+max_3_diff_corrdiantes[min_corr_index][2]]
        
          
        plt.figure()
        refernce_cardiac_voxel=cardiac_mreg_signal[int(refernce_voxels_list[sample_index][0]),int(refernce_voxels_list[sample_index][1]),int(refernce_voxels_list[sample_index][2]),:]
    
        time=np.linspace(0,len(refernce_cardiac_voxel)/10,len(refernce_cardiac_voxel))
        
        title=sample_names[sample_index] + ' ' +refernce_voxel+ ' '+ str(refernce_voxels_list[sample_index])
        plt.title(title)
        plt.plot(time,refernce_cardiac_voxel,label=str(refernce_voxels_list[sample_index]))
        plt.plot(time,refernce_cardiac_voxel_21_39_17,label=refernce_voxel)
        plt.legend()
    
    
else:
        data_path=os.path.join(main_path,sample_names[sample_index],cardiac_mreg_file_name)
        cardiac_mreg_signal,header,affine=load_niftiydata(data_path)
        refernce_cardiac_voxel_21_39_17=cardiac_mreg_signal[21,39,17,:]
    
        refernce_cardiac_voxel=cardiac_mreg_signal[int(new_refernce_voxel[0]),int(new_refernce_voxel[1]),int(new_refernce_voxel[2]),:]
    
        plt.figure()
        time=np.linspace(0,len(refernce_cardiac_voxel)/10,len(refernce_cardiac_voxel))
        
        title=sample_names[sample_index] + ' ' +refernce_voxel+ ' '+str(new_refernce_voxel)
        plt.title(title)    
        plt.plot(time,refernce_cardiac_voxel,label=str(new_refernce_voxel))
        plt.plot(time,refernce_cardiac_voxel_21_39_17,label=refernce_voxel)
        plt.legend()
        
