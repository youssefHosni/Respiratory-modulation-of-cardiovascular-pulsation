#!/bin/bash

# Start fsl and Anaconda enviroment
source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH



while getopts m:i: option
do
case "${option}"
in
m) main_path=${OPTARG};;
i) input_file=${OPTARG};;
esac
done

input_left="${input_file%.nii.gz}_left.nii.gz"
input_right="${input_file%.nii.gz}_right.nii.gz"


for selected_structure in "cortical" "subcortical"
do 
for side in "left" "right"
do 

# make two directories inside each other 
mkdir -p $main_path/${selected_structure}/${side}

structure_path=/data/fmri/Youssef/codes/analysis/masks/${selected_structure}_structure/${selected_structure}_areas_4mm_30_bin
cd $structure_path

for j in *
do 

fslmaths  $main_path/"${input_file%.nii.gz}_${side}.nii.gz" -mul $j  $main_path/${selected_structure}/${side}/$j

done
done 
done 
