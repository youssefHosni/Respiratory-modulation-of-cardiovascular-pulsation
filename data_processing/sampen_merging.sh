# calculate the mean for differnet nifity files found in different directories
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data


for data_used in  "controls" "AD"
do
counter=0
for j in "$main_path/$data_used/$data_used"/*	
do 

cd $j 



if [[ $counter -eq 0 ]] 
then 

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_duration_peaks_sampen.nii.gz    cardiac_duration_peaks_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_duration_valleys_sampen.nii.gz     cardiac_duration_valleys_sampen.nii.gz

else 


fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_duration_peaks_sampen.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_duration_peaks_sampen.nii.gz       cardiac_duration_peaks_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_duration_valleys_sampen.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_cardiac_duration_valleys_sampen.nii.gz      cardiac_duration_valleys_sampen.nii.gz




fi	
counter=$((counter+1))



done
done 

