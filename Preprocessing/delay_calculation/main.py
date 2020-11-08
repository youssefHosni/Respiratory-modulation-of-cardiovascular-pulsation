import os
from delay_finding import find_delay
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')

from respiratory_phases_interval_extraction.load_data import load_matdata
from respiratory_phases_interval_extraction.load_data import load_niftiydata
from respiratory_phases_interval_extraction.save_data import save_numeric_data

 
controls_path='/data/fmri/Youssef/Data/MREG_data/controls'
file_names=os.listdir(controls_path)
belt_data_file_name='belt_data_resampled.mat'
resp_MREG_data_file_name='resp_ffdm.nii.gz'
MREG_data_file_name='ffdm.nii.gz'

noisy_samples=['20180605_2_FA5_c01.ica' , '20190109_2_FA5_c01.ica' ,'info', 'missing_data','all_samples_calculations','mean_insp','mean_exp']



for file_name in file_names:
    if file_name in noisy_samples:
        continue
    
    belt_data=load_matdata(os.path.join(controls_path,file_name,belt_data_file_name))
    Resp_MREG_data=load_niftiydata(os.path.join(controls_path,file_name,resp_MREG_data_file_name))
    MREG_data=load_niftiydata(os.path.join(controls_path,file_name,MREG_data_file_name))
    corr_map_belt_MREG,corr_map_belt_resp,delay_map_belt_MREG,delay_map_belt_resp=find_delay(Resp_MREG_data,MREG_data,belt_data)
    save_numeric_data(os.path.join(controls_path,file_name,'corr_map_belt_MREG'),corr_map_belt_MREG)
    save_numeric_data(os.path.join(controls_path,file_name,'corr_map_belt_resp'),corr_map_belt_resp)
    save_numeric_data(os.path.join(controls_path,file_name,'delay_map_belt_MREG'),delay_map_belt_MREG)
    save_numeric_data(os.path.join(controls_path,file_name,'delay_map_belt_resp'),delay_map_belt_resp)
    

