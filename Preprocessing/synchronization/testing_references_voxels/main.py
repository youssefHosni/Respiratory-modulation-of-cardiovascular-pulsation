import sys

sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from respiratory_phases_interval_extraction.load_data import load_niftiydata
from respiratory_phases_interval_extraction.load_data import load_matdata
import os

from testing import testing_ref_voxel

controls_path='/data/fmri/Youssef/Data/MREG_data/controls'
sample_names=os.listdir(controls_path)
resp_MREG_data_file_name='resp_ffdm.nii.gz'
belt_data_file_name='belt_data_resampled.mat'
non_data_files=['all_samples_calculations','mean_insp','mean_exp','info', 'missing_data']
noisy_belt_data=['24012017_mreg_fa5.ica','20180605_2_FA5_c01.ica','20190109_2_FA5_c01.ica']



for sample_name in sample_names:
    if (sample_name in non_data_files) or (sample_name in noisy_belt_data):
        continue
   
    data_path_belt=os.path.join(controls_path,sample_name,belt_data_file_name)
    data_path_resp_mreg=os.path.join(controls_path,sample_name,resp_MREG_data_file_name)
      
    belt_signal=load_matdata(data_path_belt,'resampled')       
    mreg_resp_data,mreg_resp_affine,mreg_resp_header=load_niftiydata(data_path_resp_mreg)
    if belt_signal.shape[0]==1:
            belt_signal=belt_signal.transpose()
    refernce_resp_voxel=mreg_resp_data[22,20,10,:]    
    title = sample_name +  ' shifted belt signal ' +   'resp refernce voxel'
    testing_ref_voxel(belt_signal,refernce_resp_voxel,title,'resp data','shifted belt data')
