#!/bin/bash

# Start fsl
source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH



while getopts m: option
do
case "${option}"
in
m) main_path=${OPTARG};;
esac
done

cd $main_path
rm -rf $main_path/results
mkdir results

for structure in "cortical" "subcortical"
do 
for side in "left" "right"
do
cd $main_path/"${structure}"/${side}

for j in *
do 

echo "$j"  >> $main_path/results/${structure}_${side}.txt
fslstats  $j     -V  >> $main_path/results/${structure}_${side}.txt

done 
done
done 
