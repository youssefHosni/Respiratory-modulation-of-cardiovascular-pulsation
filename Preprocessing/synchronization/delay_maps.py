import sys
import numpy as np
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from find_the_delay.delay_finding import lag_finder


def generating_delay_maps(mreg_data,reference_voxel):
    """
    This functions aims to synchronize the MREG resp signal along the  brain voexls with the
    voxel which has the highest correlation with the belt signal
    
    Inputs :
        mreg_resp_data: the comlete brain data for the resp componet data of the MREG signal
    Outputs :
        delay map with the most correlated voxel as a reference
    """
    
    delay_map_all_voxels_max_corr=np.empty(np.shape(mreg_data)[0:3])
    fs=10
    
    for i in range(np.shape(mreg_data)[0]):
        for j in range(np.shape(mreg_data)[1]):
            for k in range(np.shape(mreg_data)[2]):
                voxel_tobe_sync=mreg_data[i,j,k,:]
                delay_map_all_voxels_max_corr[i,j,k]=lag_finder(reference_voxel[:,np.newaxis],voxel_tobe_sync[:,np.newaxis],fs)
                 
    return delay_map_all_voxels_max_corr    
        
