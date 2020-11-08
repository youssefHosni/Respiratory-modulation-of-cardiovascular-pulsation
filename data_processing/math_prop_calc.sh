# calculate the mean for differnet nifity files found in different directories
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data


for data_used in  "controls" "AD"
do

for j in "$main_path/$data_used/$data_used"/*	
do 

cd "$j"



fslmaths cardiac_rate_insp.nii.gz -Tmean  cardiac_rate_insp_mean.nii.gz
fslmaths cardiac_rate_exp.nii.gz -Tmean  cardiac_rate_exp_mean.nii.gz

fslmaths cardiac_rate_insp.nii.gz -Tstd  cardiac_rate_insp_std.nii.gz
fslmaths cardiac_rate_exp.nii.gz -Tstd  cardiac_rate_exp_std.nii.gz



done 


counter=0

for j in "$main_path/$data_used/$data_used"/*	
do 

cd $j 



if [[ $counter -eq 0 ]] 
then 

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_mean.nii.gz    cardiac_rate_insp_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_mean.nii.gz     cardiac_rate_exp_mean.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_std.nii.gz    cardiac_rate_insp_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_std.nii.gz     cardiac_rate_exp_std.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_sampen.nii.gz    cardiac_rate_insp_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_sampen.nii.gz     cardiac_rate_exp_sampen.nii.gz

else 

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_mean.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_mean.nii.gz       cardiac_rate_insp_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_mean.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_mean.nii.gz         cardiac_rate_exp_mean.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_std.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_std.nii.gz         cardiac_rate_insp_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_std.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_std.nii.gz           cardiac_rate_exp_std.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_sampen.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_insp_sampen.nii.gz    cardiac_rate_insp_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_sampen.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_rate_exp_sampen.nii.gz      cardiac_rate_exp_sampen.nii.gz





fi	
counter=$((counter+1))




done
done
