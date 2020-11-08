FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

cd /data/fmri/Youssef/Data/MREG_data/controls

fslmaths  merged_mean_opt_flow_speed.nii.gz  -Tmean mean_speed_all_samples.nii.gz  

fslmaths  merged_mean_X.nii.gz -Tmean mean_X_all_samples.nii.gz    

fslmaths  merged_mean_Y.nii.gz -Tmean mean_Y_all_samples.nii.gz    

fslmaths  merged_mean_Z.nii.gz -Tmean mean_Z_all_samples.nii.gz    

fslmerge -t flow_mean_vectors.nii.gz   mean_X_all_samples.nii.gz  mean_Y_all_samples.nii.gz  mean_Z_all_samples.nii.gz
fslmaths flow_mean_vectors.nii.gz -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  masked_flow_mean_vectors.nii.gz


fslmaths  merged_mean_opt_flow_speed_insp.nii.gz  -Tmean mean_speed_all_samples_insp.nii.gz  

fslmaths  merged_mean_X_insp.nii.gz -Tmean mean_X_all_samples_insp.nii.gz    

fslmaths  merged_mean_Y_insp.nii.gz -Tmean mean_Y_all_samples_insp.nii.gz    

fslmaths  merged_mean_Z_insp.nii.gz -Tmean mean_Z_all_samples_insp.nii.gz    

fslmerge -t flow_mean_vectors_insp.nii.gz   mean_X_all_samples_insp.nii.gz  mean_Y_all_samples_insp.nii.gz  mean_Z_all_samples_insp.nii.gz
fslmaths flow_mean_vectors_insp.nii.gz -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  masked_flow_mean_vectors_insp.nii.gz


fslmaths /data/fmri/Youssef/Data/MREG_data/controls/merged_mean_opt_flow_speed_exp.nii.gz -Tmean /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_exp.nii.gz    

fslmaths /data/fmri/Youssef/Data/MREG_data/controls/merged_mean_X_exp.nii.gz  -Tmean  /data/fmri/Youssef/Data/MREG_data/controls/mean_X_all_samples_exp.nii.gz  

fslmaths /data/fmri/Youssef/Data/MREG_data/controls/merged_mean_Y_exp.nii.gz -Tmean /data/fmri/Youssef/Data/MREG_data/controls/mean_Y_all_samples_exp.nii.gz    

fslmaths /data/fmri/Youssef/Data/MREG_data/controls/merged_mean_Z_exp.nii.gz  -Tmean /data/fmri/Youssef/Data/MREG_data/controls/mean_Z_all_samples_exp.nii.gz   


fslmerge -t flow_mean_vectors_exp.nii.gz   mean_X_all_samples_exp.nii.gz  mean_Y_all_samples_exp.nii.gz  mean_Z_all_samples_exp.nii.gz
fslmaths flow_mean_vectors_exp.nii.gz -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  masked_flow_mean_vectors_exp.nii.gz

cd /data/fmri/Youssef/Data/MREG_data/AD


fslmaths  merged_mean_opt_flow_speed_insp.nii.gz  -Tmean mean_speed_all_samples_insp.nii.gz  

fslmaths  merged_mean_X_insp.nii.gz -Tmean mean_X_all_samples_insp.nii.gz    

fslmaths  merged_mean_Y_insp.nii.gz -Tmean mean_Y_all_samples_insp.nii.gz    

fslmaths  merged_mean_Z_insp.nii.gz -Tmean mean_Z_all_samples_insp.nii.gz    

fslmerge -t flow_mean_vectors_insp.nii.gz   mean_X_all_samples_insp.nii.gz  mean_Y_all_samples_insp.nii.gz  mean_Z_all_samples_insp.nii.gz
fslmaths flow_mean_vectors_insp.nii.gz -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  masked_flow_mean_vectors_insp.nii.gz


fslmaths merged_mean_opt_flow_speed_exp.nii.gz -Tmean mean_speed_all_samples_exp.nii.gz    

fslmaths merged_mean_X_exp.nii.gz  -Tmean  mean_X_all_samples_exp.nii.gz  

fslmaths merged_mean_Y_exp.nii.gz -Tmean mean_Y_all_samples_exp.nii.gz    

fslmaths merged_mean_Z_exp.nii.gz  -Tmean mean_Z_all_samples_exp.nii.gz   


fslmerge -t flow_mean_vectors_exp.nii.gz   mean_X_all_samples_exp.nii.gz  mean_Y_all_samples_exp.nii.gz  mean_Z_all_samples_exp.nii.gz
fslmaths flow_mean_vectors_exp.nii.gz -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  masked_flow_mean_vectors_exp.nii.gz

cd /data/fmri/Youssef/Data/MREG_data/controls

fslmaths /data/fmri/Youssef/Data/MREG_data/controls/merged_mean_speed_insp_region1.nii.gz  -Tmean  /data/fmri/Youssef/Data/MREG_data/controls/mean_all_samples_speed_insp_region1

fslmaths merged_mean_speed_insp_region1.nii.gz -Tmean mean_all_samples_speed_insp_region1.nii.gz  

fslmaths merged_mean_speed_insp_region2.nii.gz  -Tmean  merged_mean_all_samples_speed_insp_region2.nii.gz
fslmaths merged_mean_speed_insp_region3.nii.gz  -Tmean  merged_mean_all_samples_speed_insp_region3.nii.gz
fslmaths merged_mean_speed_insp_region4.nii.gz  -Tmean  merged_mean_all_samples_speed_insp_region4.nii.gz

fslmaths merged_mean_speed_exp_region1.nii.gz  -Tmean merged_mean_all_samples_speed_exp_region1.nii.gz
fslmaths merged_mean_speed_exp_region2.nii.gz  -Tmean merged_mean_all_samples_speed_exp_region2.nii.gz
fslmaths merged_mean_speed_exp_region3.nii.gz  -Tmean merged_mean_all_samples_speed_exp_region3.nii.gz
fslmaths merged_mean_speed_exp_region4.nii.gz  -Tmean merged_mean_all_samples_speed_exp_region4.nii.gz

fslmerge -t flow_mean_vectors_exp.nii.gz   mean_X_all_samples_exp.nii.gz  mean_Y_all_samples_exp.nii.gz  mean_Z_all_samples_exp.nii.gz
fslmaths flow_mean_vectors_exp.nii.gz -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  masked_flow_mean_vectors_exp.nii.gz


# Differnce 
# Magntiude 

#con-con
fslmaths /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz    /data/fmri/Youssef/Data/MREG_data/controls/diff_con_exp_insp_flow_mean-speed_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_exp.nii.gz -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz    /data/fmri/Youssef/Data/MREG_data/controls/diff_con_insp_exp_flow_mean-speed_subj-avg.nii.gz

# AD-AD

fslmaths /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/AD/diff_AD_exp_insp_flow_mean-speed_subj-avg.nii.gz

fslmaths /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/AD/diff_AD_insp_exp_flow_mean-speed_subj-avg.nii.gz


# AD-con
fslmaths /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_AD_con_exp_flow_mean-speed_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_AD_con_insp_flow_mean-speed_subj-avg.nii.gz

fslmaths /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_con_AD_exp_flow_mean-speed_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_con_AD_insp_flow_mean-speed_subj-avg.nii.gz



fslmaths /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_AD_con_exp_insp_flow_mean-speed_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_AD_con_insp_exp_flow_mean-speed_subj-avg.nii.gz


fslmaths /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_con_AD_exp_insp_flow_mean-speed_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/controls/mean_speed_all_samples_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/mean_speed_all_samples_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_con_AD_insp_exp_flow_mean-speed_subj-avg.nii.gz



# vectors

# con-con

cd /data/fmri/Youssef/Data/MREG_data/controls

fslmaths flow_mean_vectors_exp.nii.gz  -sub flow_mean_vectors_insp.nii.gz   -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz    /data/fmri/Youssef/Data/MREG_data/controls/diff_flow_mean_con_exp_insp-vectors_subj-avg.nii.gz
fslmaths flow_mean_vectors_insp.nii.gz  -sub flow_mean_vectors_exp.nii.gz   -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz    /data/fmri/Youssef/Data/MREG_data/controls/diff_flow_mean_con_insp_exp-vectors_subj-avg.nii.gz

# AD-AD
cd /data/fmri/Youssef/Data/MREG_data/AD

fslmaths flow_mean_vectors_exp.nii.gz  -sub flow_mean_vectors_insp.nii.gz   -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz    /data/fmri/Youssef/Data/MREG_data/AD/diff_flow_mean_AD_exp_insp-vectors_subj-avg.nii.gz
fslmaths flow_mean_vectors_insp.nii.gz  -sub flow_mean_vectors_exp.nii.gz   -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz    /data/fmri/Youssef/Data/MREG_data/AD/diff_flow_mean_AD_insp_exp-vectors_subj-avg.nii.gz


# AD-con

fslmaths /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_AD_con_exp_flow_mean-vectors_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_AD_con_insp_flow_mean-vectors_subj-avg.nii.gz

fslmaths /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_con_AD_exp_flow_mean-vectors_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_con_AD_insp_flow_mean-vectors_subj-avg.nii.gz



fslmaths /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_AD_con_exp_insp_flow_mean-vectors_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_AD_con_insp_exp_flow_mean-vectors_subj-avg.nii.gz


fslmaths /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_insp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_con_AD_exp_insp_flow_mean-vectors_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_exp.nii.gz  -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/diff_con_AD_insp_exp_flow_mean-vectors_subj-avg.nii.gz

# VECTOR MAGNITUDES
cd /data/fmri/Youssef/Data/MREG_data/controls

fslmaths diff_flow_mean_con_exp_insp-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/controls/diff_flow_mean_con_exp_insp-vectors_mag_subj-avg.nii.gz
fslmaths diff_flow_mean_con_insp_exp-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz  /data/fmri/Youssef/Data/MREG_data/controls/diff_flow_mean_con_insp_exp-vectors_mag_subj-avg.nii.gz

cd /data/fmri/Youssef/Data/MREG_data/AD

fslmaths diff_flow_mean_AD_exp_insp-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/AD/diff_flow_mean_AD_exp_insp-vectors_mag_subj-avg.nii.gz
fslmaths diff_flow_mean_AD_insp_exp-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/AD/diff_flow_mean_AD_insp_exp-vectors_mag_subj-avg.nii.gz

cd /data/fmri/Youssef/Data/MREG_data

fslmaths diff_AD_con_exp_flow_mean-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/diff_AD_con_exp_flow_mean-vectors_subj-mag.nii.gz

fslmaths diff_AD_con_insp_flow_mean-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/diff_AD_con_insp_flow_mean-vectors_subj-mag.nii.gz

fslmaths diff_con_AD_exp_flow_mean-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/diff_con_AD_exp_flow_mean-vectors_subj-mag.nii.gz

fslmaths diff_con_AD_insp_flow_mean-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/diff_con_AD_insp_flow_mean-vectors_subj-mag.nii.gz

fslmaths diff_AD_con_exp_insp_flow_mean-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/diff_AD_con_exp_insp_flow_mean-vectors_subj-mag.nii.gz

fslmaths diff_AD_con_insp_exp_flow_mean-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/diff_AD_con_insp_exp_flow_mean-vectors_subj-mag.nii.gz

fslmaths diff_AD_con_insp_exp_flow_mean-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/diff_AD_con_insp_exp_flow_mean-vectors_subj-mag.nii.gz

fslmaths diff_con_AD_insp_exp_flow_mean-vectors_subj-avg.nii.gz  -sqr -Tmean -mul 3 -sqrt -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/Data/MREG_data/diff_con_AD_insp_exp_flow_mean-vectors_subj-mag.nii.gz

                        




