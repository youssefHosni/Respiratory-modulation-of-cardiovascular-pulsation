import os 
import sys
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from representing_the_diff_with_resp_phases import histogram_plotting
from respiratory_phases_interval_extraction.load_data import load_niftiydata



control_path='/data/fmri/Youssef/Data/MREG_data/controls'
AD_path='/data/fmri/Youssef/Data/MREG_data/AD'


main_path=control_path

cardiac_duration_peaks_map_file_name ='cardiac_duration_peaks_all_samples.nii.gz'
cardiac_duration_valleys_map_file_name ='cardiac_duration_valleys_all_samples.nii.gz'

voxel_to_show=[25,25,25]
bins_num=15

cardiac_duration_peaks_map=load_niftiydata(os.path.join(main_path,cardiac_duration_peaks_map_file_name))
cardiac_duration_valleys_map=load_niftiydata(os.path.join(main_path,cardiac_duration_valleys_map_file_name))

cardiac_duration_peaks_voxel=cardiac_duration_peaks_map[voxel_to_show[0],voxel_to_show[1],voxel_to_show[2],:]
cardiac_duration_valleys_voxel=cardiac_duration_valleys_map[voxel_to_show[0],voxel_to_show[1],voxel_to_show[2],:]


histogram_plotting(cardiac_duration_peaks_voxel,bins_num,'cardiac_duration_peaks'+str(voxel_to_show),save_data=0,saving_path="")
histogram_plotting(cardiac_duration_valleys_voxel,bins_num,'cardiac_duration_valleys'+str(voxel_to_show),save_data=0,saving_path="")
    
