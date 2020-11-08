FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data

for data_used in "controls" "AD" ; do 
for i in {1..4} ; do  

cd "$main_path/$data_used"

: '
fslmaths merged_mean_speed_insp_region${i}.nii.gz  -Tmean  mean_speed_insp_region${i}_all_samples.nii.gz 
fslmaths merged_mean_speed_exp_region${i}.nii.gz  -Tmean  mean_speed_exp_region${i}_all_samples.nii.gz

fslmaths merged_optflow_insp_region${i}_X_mean.nii.gz  -Tmean mean_optflow_insp_region${i}_X_all_samples.nii.gz   
fslmaths merged_optflow_insp_region${i}_Y_mean.nii.gz  -Tmean mean_optflow_insp_region${i}_Y_all_samples.nii.gz   
fslmaths merged_optflow_insp_region${i}_Z_mean.nii.gz  -Tmean mean_optflow_insp_region${i}_Z_all_samples.nii.gz   

fslmaths merged_optflow_exp_region${i}_X_mean.nii.gz  -Tmean mean_optflow_exp_region${i}_X_all_samples.nii.gz   
fslmaths merged_optflow_exp_region${i}_Y_mean.nii.gz  -Tmean mean_optflow_exp_region${i}_Y_all_samples.nii.gz   
fslmaths merged_optflow_exp_region${i}_Z_mean.nii.gz  -Tmean mean_optflow_exp_region${i}_Z_all_samples.nii.gz   


fslmerge -t flow_mean_vectors_insp_region${i}.nii.gz   mean_optflow_insp_region${i}_X_all_samples.nii.gz  mean_optflow_insp_region${i}_Y_all_samples.nii.gz  mean_optflow_insp_region${i}_Z_all_samples.nii.gz
fslmerge -t flow_mean_vectors_exp_region${i}.nii.gz    mean_optflow_exp_region${i}_X_all_samples.nii.gz  mean_optflow_exp_region${i}_Y_all_samples.nii.gz  mean_optflow_exp_region${i}_Z_all_samples.nii.gz
'

fslmaths flow_mean_vectors_exp_region${i}.nii.gz -sub flow_mean_vectors_insp_region${i}.nii.gz   diff_exp_insp_region${i}_flow_mean-vectors_subj-avg.nii.gz
fslmaths mean_speed_exp_region${i}_all_samples.nii.gz -sub mean_speed_insp_region${i}_all_samples.nii.gz   diff_exp_insp_region${i}_flow_mean-speed_subj-avg.nii.gz

done 

fslmaths flow_mean_vectors_insp_region1.nii.gz -sub flow_mean_vectors_insp_region2.nii.gz   diff_insp_region1_2_flow_mean-vectors_subj-avg.nii.gz
fslmaths flow_mean_vectors_insp_region2.nii.gz -sub flow_mean_vectors_insp_region3.nii.gz   diff_insp_region2_3_flow_mean-vectors_subj-avg.nii.gz
fslmaths flow_mean_vectors_insp_region3.nii.gz -sub flow_mean_vectors_insp_region4.nii.gz   diff_insp_region3_4_flow_mean-vectors_subj-avg.nii.gz

fslmaths flow_mean_vectors_insp_region4.nii.gz -sub flow_mean_vectors_exp_region1.nii.gz   diff_insp_exp_region4_1_flow_mean-vectors_subj-avg.nii.gz

fslmaths flow_mean_vectors_exp_region1.nii.gz -sub flow_mean_vectors_exp_region2.nii.gz   diff_exp_region1_2_flow_mean-vectors_subj-avg.nii.gz
fslmaths flow_mean_vectors_exp_region2.nii.gz -sub flow_mean_vectors_exp_region3.nii.gz   diff_exp_region2_3_flow_mean-vectors_subj-avg.nii.gz
fslmaths flow_mean_vectors_exp_region3.nii.gz -sub flow_mean_vectors_exp_region4.nii.gz   diff_exp_region3_4_flow_mean-vectors_subj-avg.nii.gz


fslmaths mean_speed_insp_region1_all_samples.nii.gz -sub mean_speed_insp_region2_all_samples.nii.gz   diff_insp_region1_2_flow_mean-speed_subj-avg.nii.gz
fslmaths mean_speed_insp_region2_all_samples.nii.gz -sub mean_speed_insp_region3_all_samples.nii.gz   diff_insp_region2_3_flow_mean-speed_subj-avg.nii.gz
fslmaths mean_speed_insp_region3_all_samples.nii.gz -sub mean_speed_insp_region4_all_samples.nii.gz   diff_insp_region3_4_flow_mean-speed_subj-avg.nii.gz

fslmaths mean_speed_insp_region4_all_samples.nii.gz -sub mean_speed_exp_region1_all_samples.nii.gz   diff_insp_exp_region4_1_flow_mean-speed_subj-avg.nii.gz

fslmaths mean_speed_exp_region1_all_samples.nii.gz -sub mean_speed_exp_region2_all_samples.nii.gz   diff_exp_region1_2_flow_mean-speed_subj-avg.nii.gz
fslmaths mean_speed_exp_region2_all_samples.nii.gz -sub mean_speed_exp_region3_all_samples.nii.gz   diff_exp_region2_3_flow_mean-speed_subj-avg.nii.gz
fslmaths mean_speed_exp_region3_all_samples.nii.gz -sub mean_speed_exp_region4_all_samples.nii.gz   diff_exp_region3_4_flow_mean-speed_subj-avg.nii.gz

done 

for i in {1..4} ; do  

fslmaths /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_insp_region${i}.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp_region${i}.nii.gz   /data/fmri/Youssef/Data/MREG_data/diff_insp_region${i}_flow_mean-vectors_subj-avg.nii.gz
fslmaths /data/fmri/Youssef/Data/MREG_data/AD/flow_mean_vectors_exp_region${i}.nii.gz -sub /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp_region${i}.nii.gz   /data/fmri/Youssef/Data/MREG_data/diff_exp_region${i}_flow_mean-vectors_subj-avg.nii.gz

done





