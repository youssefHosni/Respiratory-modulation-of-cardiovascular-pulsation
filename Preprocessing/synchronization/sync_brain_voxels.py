import numpy as np
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from find_the_delay.delay_finding import fraction_time_shifting




def sync_brain_voxels(mreg_data,ref_voxel_signal,delay_map,signal_type):
    
    """
    This function sync the brain voxels with a refernce voxel and it's inputs are :
        mreg_data: The mreg data in which the voxels will be sync 
        ref_voxel_signal: The refernce voxel signal with which the voxels will be sync with
        delay_map: Delay between th evoxels and the refernce voxel 
        signal_type: "Resp" or "cardiac" as the condition is differnet between both of them  
    return :
        mreg_data: it is the input mreg daata with the voxels that needs to be synchronize synchronized        
    
    The condition for the cardiac signal is 0.15s and for the res signal is 0.2s , This could be change based on the 
    physiological information    

    
    """
    
    if signal_type=='cardiac':
        condition_satisfed_indices=np.where((delay_map>-0.15) & (delay_map<0.15))
    elif signal_type=='resp':
         condition_satisfed_indices=np.where((delay_map>-0.2) & (delay_map<0.2))
   
    for i in range(len(condition_satisfed_indices[0])):
        delayed_data=mreg_data[condition_satisfed_indices[0][i], condition_satisfed_indices[1][i], condition_satisfed_indices[2][i],:]
        delay=delay_map[condition_satisfed_indices[0][i],condition_satisfed_indices[1][i],condition_satisfed_indices[2][i]]
        corrected_data=fraction_time_shifting(delayed_data,delay)   
        mreg_data[condition_satisfed_indices[0][i],condition_satisfed_indices[1][i],condition_satisfed_indices[2][i],:]=corrected_data
        
    return mreg_data
    
    
