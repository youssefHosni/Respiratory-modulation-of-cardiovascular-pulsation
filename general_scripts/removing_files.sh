source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data
main_path_controls=/data/fmri/Youssef/Data/MREG_data/controls/controls
main_path_AD=/data/fmri/Youssef/Data/MREG_data/AD/AD


for data_used in  "AD"
do
for j in "$main_path/$data_used/$data_used"/*	
do 
cd $j

rm ffdm.nii.gz

done 
done
