import os
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')

from respiratory_phases_interval_extraction.load_data import load_niftiydata
from respiratory_phases_interval_extraction.load_data import load_npydata
import numpy as np
import matplotlib.pyplot as plt
from find_the_delay.delay_finding import fraction_time_shifting

controls_path='/data/fmri/Youssef/Data/MREG_data/controls'
resp_MREG_data_file_name='resp_ffdm.nii.gz'
cardiac_MREG_data_file_name='card_ffdm.nii.gz'
cardiac_delays_file_name='delay_map_cardiac_with_reference_voxel.npy'
resp_delays_file_name='delay_map_resp_with_reference_voxel.npy'


sample_names=[
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

refernce_resp_voxel=[22,20,10]
refernce_cardiac_voxels_list=[[21,39,20],
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


[mreg_resp_data,_,_]=load_niftiydata(os.path.join(controls_path,sample_names[0],resp_MREG_data_file_name))
[mreg_cardiac_data,_,_]=load_niftiydata(os.path.join(controls_path,sample_names[0],cardiac_MREG_data_file_name))

cardiac_delay_map_with_ref_voxel=load_npydata(os.path.join(controls_path,sample_names[0],cardiac_delays_file_name)) 

resp_delay_map_with_ref_voxel=load_npydata(os.path.join(controls_path,sample_names[0],resp_delays_file_name)) 



### For the cardiac signal 
x=np.where((cardiac_delay_map_with_ref_voxel>-0.15) & (cardiac_delay_map_with_ref_voxel<0.15))
condition_index=1000
delayed_data=mreg_cardiac_data[x[0][condition_index],x[1][condition_index],x[2][condition_index],:]
delay=cardiac_delay_map_with_ref_voxel[x[0][condition_index],x[1][condition_index],x[2][condition_index]]
corrected_data=fraction_time_shifting(delayed_data,delay)
time=np.linspace(0,(mreg_cardiac_data.shape[3])/10,mreg_cardiac_data.shape[3])
refrnce_cardiac_data=mreg_cardiac_data[refernce_cardiac_voxels_list[0][0],refernce_cardiac_voxels_list[0][1],refernce_cardiac_voxels_list[0][2],:]
plt.plot(time[0:350],2*corrected_data[0:350],label='delayed_data');plt.plot(time[0:350],refrnce_cardiac_data[0:350],label='refernce_data');plt.legend()

"""
####for the respiratory signal 

x=np.where((resp_delay_map_with_ref_voxel>-0.2) & (resp_delay_map_with_ref_voxel<0.2))
condition_index=1009
delayed_resp_data=mreg_resp_data[x[0][condition_index],x[1][condition_index],x[2][condition_index],:]
delay_resp=resp_delay_map_with_ref_voxel[x[0][condition_index],x[1][condition_index],x[2][condition_index]]
corrected_resp_data=fraction_time_shifting(delayed_resp_data,delay_resp)
time=np.linspace(0,(mreg_resp_data.shape[3])/10,mreg_resp_data.shape[3])
refrnce_resp_data=mreg_resp_data[refernce_resp_voxel[0],refernce_resp_voxel[1],refernce_resp_voxel[2],:]
plt.plot(time[0:350],corrected_resp_data[0:350],label='delayed_data');plt.plot(time[0:350],refrnce_resp_data[0:350],label='refernce_data');plt.legend()

"""
