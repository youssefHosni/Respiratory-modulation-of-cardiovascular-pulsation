#!/bin/bash

# masking and thresholding the file that would like to calculate the signifcant voxels in

# open fsl 
source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH


while getopts m:i:o: option
do
case "${option}"
in
m) main_path=${OPTARG};;
i) input_file=${OPTARG};;
o) output_file=${OPTARG};;
esac
done




mask_file=/data/fmri/Youssef/4mm_brain_mask_bin.nii.gz
mask_left=/data/fmri/Youssef/4mm_brain_mask_left_bin.nii.gz
mask_right=/data/fmri/Youssef/4mm_brain_mask_right_bin.nii.gz
output_left="${output_file%.nii.gz}_left.nii.gz"
output_right="${output_file%.nii.gz}_right.nii.gz"

cd $main_path
fslmaths  $input_file -thr 0.95  $output_file
fslmaths  $output_file -mul $mask_file  $output_file
fslmaths  $output_file -mul $mask_left  $output_left
fslmaths  $output_file -mul $mask_right  $output_right

