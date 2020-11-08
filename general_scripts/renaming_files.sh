# renaming files 

main_path=/data/fmri/Youssef/Data/MREG_data

for data_used in "controls" "AD"
do
for j in "$main_path/$data_used/$data_used"/*	
do 



mv "$j"/"optflow_insp_region1_mean.nii.gz"  "$j"/"optflow_speed_insp_region1_mean.nii.gz"
mv "$j"/"optflow_insp_region2_mean.nii.gz"  "$j"/"optflow_speed_insp_region2_mean.nii.gz"
mv "$j"/"optflow_insp_region3_mean.nii.gz"  "$j"/"optflow_speed_insp_region3_mean.nii.gz"
mv "$j"/"optflow_insp_region4_mean.nii.gz"  "$j"/"optflow_speed_insp_region4_mean.nii.gz"

mv "$j"/"optflow_exp_region1_mean.nii.gz"  "$j"/"optflow_speed_exp_region1_mean.nii.gz"
mv "$j"/"optflow_exp_region2_mean.nii.gz"  "$j"/"optflow_speed_exp_region2_mean.nii.gz"
mv "$j"/"optflow_exp_region3_mean.nii.gz"  "$j"/"optflow_speed_exp_region3_mean.nii.gz"
mv "$j"/"optflow_exp_region4_mean.nii.gz"  "$j"/"optflow_speed_exp_region4_mean.nii.gz"

done 
done
