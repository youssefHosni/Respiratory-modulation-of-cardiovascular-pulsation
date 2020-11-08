# calculate the std of the propagation speed at the four respiratory loc points

source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data


for data_used in  "controls"  "AD" 
do
counter=0

for j in "$main_path/$data_used/$data_used"/*	
do 

cd "$j"



fslmaths optflow_lptp6_fullcard_iffdm_speed_resp_max_der.nii.gz   -Tstd std_speed_resp_max_der.nii.gz
fslmaths optflow_lptp6_fullcard_iffdm_speed_resp_min_der.nii.gz   -Tstd std_speed_resp_min_der.nii.gz
fslmaths optflow_lptp6_fullcard_iffdm_speed_resp_peaks.nii.gz     -Tstd std_speed_resp_peaks.nii.gz
fslmaths optflow_lptp6_fullcard_iffdm_speed_resp_valleys.nii.gz   -Tstd std_speed_resp_valleys.nii.gz




if [[ $counter -eq 0 ]] 
then 

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_peaks.nii.gz    	 std_speed_resp_peaks.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_valleys.nii.gz    std_speed_resp_valleys.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_max_der.nii.gz    std_speed_resp_max_der.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_min_der.nii.gz    std_speed_resp_min_der.nii.gz


else

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_peaks.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_peaks.nii.gz        std_speed_resp_peaks.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_valleys.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_valleys.nii.gz     std_speed_resp_valleys.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_max_der.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_max_der.nii.gz     std_speed_resp_max_der.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_min_der.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_resp_min_der.nii.gz     std_speed_resp_min_der.nii.gz

fi
counter=$((counter+1))
done
done



	
