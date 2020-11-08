# sperating vectorss for diffeent optical flow files
source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data

for data_used in "controls" "AD"
do

: '

for j in "$main_path/$data_used/$data_used"/*	
do 

cd $j 

for i in {1..3} ; do  

python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/separate_nifti_dim.py -i optflow_insp_region${i}_3.nii.gz   -d 3 -o X Y Z -t 3

python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/separate_nifti_dim.py -i optflow_exp_region${i}_3.nii.gz   -d 3 -o X Y Z -t 3


fslmaths optflow_insp_region${i}_3_X.nii.gz -Tmean optflow_insp_region${i}_3_X_mean.nii.gz

fslmaths optflow_insp_region${i}_3_Y.nii.gz -Tmean optflow_insp_region${i}_3_Y_mean.nii.gz

fslmaths optflow_insp_region${i}_3_Z.nii.gz -Tmean optflow_insp_region${i}_3_Z_mean.nii.gz



fslmaths optflow_exp_region${i}_3_X.nii.gz -Tmean optflow_exp_region${i}_3_X_mean.nii.gz

fslmaths optflow_exp_region${i}_3_Y.nii.gz -Tmean optflow_exp_region${i}_3_Y_mean.nii.gz

fslmaths optflow_exp_region${i}_3_Z.nii.gz -Tmean optflow_exp_region${i}_3_Z_mean.nii.gz



fslmaths optflow_insp_region${i}_3_X.nii.gz -Tstd optflow_insp_region${i}_3_X_std.nii.gz

fslmaths optflow_insp_region${i}_3_Y.nii.gz -Tstd optflow_insp_region${i}_3_Y_std.nii.gz

fslmaths optflow_insp_region${i}_3_Z.nii.gz -Tstd optflow_insp_region${i}_3_Z_std.nii.gz


fslmaths optflow_exp_region${i}_3_X.nii.gz -Tstd optflow_exp_region${i}_3_X_std.nii.gz

fslmaths optflow_exp_region${i}_3_Y.nii.gz -Tstd optflow_exp_region${i}_3_Y_std.nii.gz

fslmaths optflow_exp_region${i}_3_Z.nii.gz -Tstd optflow_exp_region${i}_3_Z_std.nii.gz

done 
done 

'


for i in {1..3} ; do  

counter=0

for j in "$main_path/$data_used/$data_used"/*	
do 

cd $j 

if [[ $counter -eq 0 ]] 
then 

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_sampen.nii.gz    optflow_insp_region${i}_3_X_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_sampen.nii.gz    optflow_insp_region${i}_3_Y_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_sampen.nii.gz    optflow_insp_region${i}_3_Z_sampen.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_sampen.nii.gz    optflow_exp_region${i}_3_X_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_sampen.nii.gz    optflow_exp_region${i}_3_Y_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_sampen.nii.gz    optflow_exp_region${i}_3_Z_sampen.nii.gz




: '
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_mean.nii.gz    optflow_insp_region${i}_3_X_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_mean.nii.gz    optflow_insp_region${i}_3_Y_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_mean.nii.gz    optflow_insp_region${i}_3_Z_mean.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_mean.nii.gz    optflow_exp_region${i}_3_X_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_mean.nii.gz    optflow_exp_region${i}_3_Y_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_mean.nii.gz    optflow_exp_region${i}_3_Z_mean.nii.gz


fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_std.nii.gz    optflow_insp_region${i}_3_X_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_std.nii.gz    optflow_insp_region${i}_3_Y_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_std.nii.gz    optflow_insp_region${i}_3_Z_std.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_std.nii.gz    optflow_exp_region${i}_3_X_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_std.nii.gz    optflow_exp_region${i}_3_Y_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_std.nii.gz    optflow_exp_region${i}_3_Z_std.nii.gz
'

else 


fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_sampen.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_sampen.nii.gz   optflow_insp_region${i}_3_X_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_sampen.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_sampen.nii.gz   optflow_insp_region${i}_3_Y_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_sampen.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_sampen.nii.gz   optflow_insp_region${i}_3_Z_sampen.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_sampen.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_sampen.nii.gz    optflow_exp_region${i}_3_X_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_sampen.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_sampen.nii.gz    optflow_exp_region${i}_3_Y_sampen.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_sampen.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_sampen.nii.gz    optflow_exp_region${i}_3_Z_sampen.nii.gz
: '

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_mean.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_mean.nii.gz   optflow_insp_region${i}_3_X_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_mean.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_mean.nii.gz   optflow_insp_region${i}_3_Y_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_mean.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_mean.nii.gz   optflow_insp_region${i}_3_Z_mean.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_mean.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_mean.nii.gz    optflow_exp_region${i}_3_X_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_mean.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_mean.nii.gz    optflow_exp_region${i}_3_Y_mean.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_mean.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_mean.nii.gz    optflow_exp_region${i}_3_Z_mean.nii.gz



fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_std.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_X_std.nii.gz   optflow_insp_region${i}_3_X_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_std.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Y_std.nii.gz   optflow_insp_region${i}_3_Y_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_std.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_insp_region${i}_3_Z_std.nii.gz   optflow_insp_region${i}_3_Z_std.nii.gz

fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_std.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_X_std.nii.gz    optflow_exp_region${i}_3_X_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_std.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Y_std.nii.gz    optflow_exp_region${i}_3_Y_std.nii.gz
fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_std.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_exp_region${i}_3_Z_std.nii.gz    optflow_exp_region${i}_3_Z_std.nii.gz
' 




fi	
counter=$((counter+1))


done
done 
done
