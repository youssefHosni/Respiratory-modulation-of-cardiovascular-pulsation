#!/bin/bash
#  generate text file that will get the number o voxels that fill in each cortical and subcortical structures

FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

cd /data/fmri/Youssef/codes/analysis/masks/scripts
chmod +x masking_thresholding.sh


while getopts m:i:o: option
do
case "${option}"
in
m) main_path=${OPTARG};;
i) input_file=${OPTARG};;
o) output_file=${OPTARG};;
esac
done

output_file="${input_file%.nii.gz}_thre_masked.nii.gz"


bash masking_thresholding.sh -m $main_path  -i $input_file -o  $output_file

bash masking_structures.sh -m $main_path  -i $output_file 

bash counting_roi_voxel.sh -m $main_path
 
  
