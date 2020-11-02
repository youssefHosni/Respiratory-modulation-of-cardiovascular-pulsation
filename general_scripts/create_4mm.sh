#!/bin/bash

# Start fsl
source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH


# Resample to 4 mm standard space (from 1mm)

flirt -in /data/fmri/Youssef/MNI152_T1_1mm_brain.nii.gz -ref /data/fmri/Youssef/codes/analysis/masks/ref_4mm.nii.gz -applyisoxfm 4 -out /data/fmri/Youssef/MNI152_T1_4mm_brain_new.nii.gz