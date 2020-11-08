import os
import numpy as np
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from respiratory_phases_interval_extraction.load_data import load_niftiydata
from respiratory_phases_interval_extraction.save_data import save_nifity_data



def cardiac_durations_properties_map(cardiac_duration_map,mean_calc,std_calc):
    cardiac_duration_mean_map=np.empty((cardiac_duration_map.shape[0],cardiac_duration_map.shape[1],cardiac_duration_map.shape[2]))
    cardiac_duration_std_map=np.empty((cardiac_duration_map.shape[0],cardiac_duration_map.shape[1],cardiac_duration_map.shape[2]))
    #cardiac_duration_cv_map=np.empty((cardiac_duration_map.shape[0],cardiac_duration_map.shape[1],cardiac_duration_map.shape[2]))

    for i in range (cardiac_duration_map.shape[0]):
        for j in range(cardiac_duration_map.shape[1]):
            for k in range(cardiac_duration_map.shape[2]):
                if mean_calc==1:
                    cardiac_duration_mean_map[i,j,k]=np.mean(cardiac_duration_map[i,j,k,:])
                if std_calc==1:
                    cardiac_duration_std_map[i,j,k]=np.std(cardiac_duration_map[i,j,k,:])
                #cardiac_duration_cv_map[i,j,k]=np.std(cardiac_duration_map[i,j,k,:])/np.mean(cardiac_duration_map[i,j,k,:])
                
    return (cardiac_duration_mean_map,cardiac_duration_std_map)
    

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



control_path='/data/fmri/Youssef/Data/MREG_data/controls'
AD_path='/data/fmri/Youssef/Data/MREG_data/AD'

mreg_data_file_name='ffdm.nii.gz'
cardiac_duration_peaks_folder_name='cardiac_durations_peaks'
cardiac_duration_valleys_folder_name='cardiac_durations_valleys'

cadriac_duration_mean_peak_folder='cardiac_duration_mean_peaks'
cadriac_duration_mean_valley_folder='cardiac_duration_mean_valleys'

cadriac_duration_std_peak_folder='cardiac_duration_std_peaks'
cadriac_duration_std_valley_folder='cardiac_duration_std_valleys'

cadriac_duration_cv_peak_folder='cardiac_duration_cv_peaks'
cadriac_duration_cv_valley_folder='cardiac_duration_cv_valleys'

data_used='controls'

if data_used=='AD':
    main_path=AD_path
    samples_name=AD_sample_names
    original_data_path='/data/fmri/Youssef/Data/MREG_data/AD/AD'
elif data_used=='controls':
    main_path=control_path
    samples_name=control_sample_names
    original_data_path='/data/fmri/Youssef/Data/MREG_data/controls/controls'
    
cardiac_duration_peak_file_names=os.listdir(os.path.join(main_path,cardiac_duration_peaks_folder_name))
cardiac_duration_valley_file_names=os.listdir(os.path.join(main_path,cardiac_duration_valleys_folder_name))

cardiac_duration_peak_file_names=np.sort(cardiac_duration_peak_file_names)
cardiac_duration_valley_file_names=np.sort(cardiac_duration_valley_file_names)

mean_calc=0
std_calc=1
mean_map_saving=mean_calc
std_map_saving=std_calc
cv_map_saving=0


for i in range(len(cardiac_duration_valley_file_names)):
  
    sample_name=samples_name[i]
    
    [cardiac_duration_map_peaks,peaks_affine,peaks_header]=load_niftiydata(os.path.join(main_path,cardiac_duration_peaks_folder_name,cardiac_duration_peak_file_names[i]))
    [cardiac_duration_map_valleys,valleys_affine,valleys_header]=load_niftiydata(os.path.join(main_path,cardiac_duration_valleys_folder_name,cardiac_duration_valley_file_names[i]))
    
    [_,mreg_data_affine,mreg_data_header]=load_niftiydata(os.path.join(original_data_path,sample_name,mreg_data_file_name))
    
    [cardiac_duration_mean_map_peak,cardiac_duration_std_map_peak]= cardiac_durations_properties_map(cardiac_duration_map_peaks,mean_calc,std_calc)
    [cardiac_duration_mean_map_valley,cardiac_duration_std_map_valley]= cardiac_durations_properties_map(cardiac_duration_map_valleys,mean_calc,std_calc)

    if mean_map_saving==1:
        save_nifity_data(os.path.join(main_path,cadriac_duration_mean_peak_folder,sample_name+'mean_peaks.nii.gz'),cardiac_duration_mean_map_peak,peaks_affine,peaks_header)
        save_nifity_data(os.path.join(main_path,cadriac_duration_mean_valley_folder,sample_name+'mean_valleys.nii.gz'),cardiac_duration_mean_map_valley,valleys_affine,valleys_header)
    elif std_map_saving==1:
        save_nifity_data(os.path.join(main_path,cadriac_duration_std_peak_folder,sample_name+'std_peaks.nii.gz'),cardiac_duration_std_map_peak,peaks_affine,peaks_header)
        save_nifity_data(os.path.join(main_path,cadriac_duration_std_valley_folder,sample_name+'std_valleys.nii.gz'),cardiac_duration_std_map_valley,valleys_affine,valleys_header)       
    
    """
    elif cv_map_saving==1:
        save_nifity_data(os.path.join(main_path,cadriac_duration_cv_peak_folder,sample_name+'cv_peaks.nii.gz'),cardiac_duration_cv_map_peak,mreg_data_affine,mreg_data_header)
        save_nifity_data(os.path.join(main_path,cadriac_duration_cv_valley_folder,sample_name+'cv_valleys.nii.gz'),cardiac_duration_cv_map_valley,mreg_data_affine,mreg_data_header)
    """   
