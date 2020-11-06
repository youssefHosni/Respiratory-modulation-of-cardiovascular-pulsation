#!/bin/bash

# Start fsl
source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH


# iterating through all the files 

for data_used in "cortical" "subcortical"
do
main_path=/data/fmri/Youssef/codes/analysis/masks/${data_used}_structure/${data_used}_areas_1mm
echo $main_path
cd $main_path 

for j in *
do
echo $j
# Resample to 4 mm standard space (from 1mm)

flirt -in $j -ref /data/fmri/Youssef/codes/analysis/masks/ref_4mm.nii.gz -applyisoxfm 4 -out /data/fmri/Youssef/codes/analysis/masks/${data_used}_structure/${data_used}_areas_4mm/$j
# Select areas with at least 30% probability

fslmaths /data/fmri/Youssef/codes/analysis/masks/${data_used}_structure/${data_used}_areas_4mm/$j -thr 30 -bin /data/fmri/Youssef/codes/analysis/masks/${data_used}_structure/${data_used}_areas_4mm_30_bin/$j

done 
done
