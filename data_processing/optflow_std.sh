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

for i in {1..4}
do 

fslmaths optflow_insp_region${i}_speed.nii.gz -Tstd optflow_insp_region${i}_speed_std.nii.gz
fslmaths optflow_exp_region${i}_speed.nii.gz -Tstd optflow_exp_region${i}_speed_std.nii.gz




if [[ $counter -eq 0 ]] 
then 

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_insp_region${i}.nii.gz    optflow_insp_region${i}_speed_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_exp_region${i}.nii.gz     optflow_exp_region${i}_speed_std.nii.gz

else

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_insp_region${i}.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_insp_region${i}.nii.gz    optflow_insp_region${i}_speed_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_exp_region${i}.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_speed_exp_region${i}.nii.gz     optflow_exp_region${i}_speed_std.nii.gz
fi

done

counter=$((counter+1))


done 
done


	
