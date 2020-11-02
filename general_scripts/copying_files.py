import shutil
import os

main_path_target_controls='/data/fmri/Youssef/Data/MREG_data/controls/controls'

main_path_target_AD='/data/fmri/Youssef/Data/MREG_data/AD/AD'

main_path_original='/data/fmri/zalan/AD'



original_AD_files_name=['20160226_mreg_fa5_1_75comp.ica', 
'20160617_mreg_fa5_1_75comp.ica', 
'20160826_mreg_fa5_1_75comp.ica', 
'20161004_mreg_fa5_1_75comp.ica', 
'20161011_mreg_fa5_1_75comp.ica', 
'20161028_mreg_fa5_1_75comp.ica', 
'20161125_mreg_fa5_1_75comp.ica', 
'20180410_1_FA5_c01.ica', 
'20180417_1_FA5_c01.ica' ,
'20180911_2_FA5_c01.ica' ,
'20180918_1_FA5_c01.ica' ,
'20181002_1_FA5_c01.ica' ,
'20181023_2_FA5_c01.ica' ,
'20181113_1_FA5_c01.ica' ,
'20181120_1_FA5_c01.ica',
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

controls_files_name=[
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

target_AD_files_name=['20160226_mreg_fa5.ica', 
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

file_to_be_copied='optflow-all-m3_lptp6_fullcard_iffdm.nii.gz'

data_tobe_used=['controls','AD']
for data_used in data_tobe_used:
    if data_used=='controls':
        for i in range(len(controls_files_name)): 
            original=os.path.join(main_path_original,controls_files_name[i],file_to_be_copied)
            target=os.path.join(main_path_target_controls,controls_files_name[i],file_to_be_copied)
            shutil.copyfile(original, target)
    elif data_used=='AD':
        for i in range(len(original_AD_files_name)): 
            original=os.path.join(main_path_original,original_AD_files_name[i],file_to_be_copied)
            target=os.path.join(main_path_target_AD,target_AD_files_name[i],file_to_be_copied)
            shutil.copyfile(original, target)