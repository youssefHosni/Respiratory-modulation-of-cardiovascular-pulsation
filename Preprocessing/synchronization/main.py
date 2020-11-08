import os
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')

from respiratory_phases_interval_extraction.load_data import load_niftiydata
from respiratory_phases_interval_extraction.save_data import save_numeric_data
from delay_maps import generating_delay_maps
controls_path='/data/fmri/Youssef/Data/MREG_data/controls'
resp_MREG_data_file_name='resp_ffdm.nii.gz'
cardiac_MREG_data_file_name='card_ffdm.nii.gz'
save_data=1

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


refernce_voxels_list=[[21,39,20],
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



counter=0
sync_resp=1
sync_cardiac=0
for sample_name in sample_names:
    
    
    [mreg_resp_data,_,_]=load_niftiydata(os.path.join(controls_path,sample_name,resp_MREG_data_file_name))
    [mreg_cardiac_data,_,_]=load_niftiydata(os.path.join(controls_path,sample_name,cardiac_MREG_data_file_name))
    mreg_resp_ref_voxel=mreg_resp_data[22,20,10,:]
    mreg_cardiac_ref_voxel=mreg_cardiac_data[refernce_voxels_list[counter][0],refernce_voxels_list[counter][1],refernce_voxels_list[counter][2],:]
    
        
    data_path=os.path.join(controls_path,sample_name)
    if sync_resp==1:
        delay_map_all_voxels_max_corr  =generating_delay_maps(mreg_resp_data,mreg_resp_ref_voxel)
    
        if save_data==1:
            save_numeric_data(os.path.join(data_path,'delay_map_resp_with_reference_voxel.npy'),delay_map_all_voxels_max_corr)
    
    elif sync_cardiac==1:
        delay_map_all_voxels_max_corr  =generating_delay_maps(mreg_cardiac_data,mreg_cardiac_ref_voxel)
    
        if save_data==1:
            save_numeric_data(os.path.join(data_path,'delay_map_cardiac_with_reference_voxel.npy'),delay_map_all_voxels_max_corr)
    
    


    counter=counter+1
