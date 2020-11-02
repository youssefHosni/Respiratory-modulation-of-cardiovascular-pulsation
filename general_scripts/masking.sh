FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH
fslmaths /data/fmri/Youssef/MNI152_T1_4mm.nii.gz -mul /data/fmri/Youssef/4mm_brain_mask_bin.nii.gz /data/fmri/Youssef/MNI152_T1_4mm_masked.nii.gz