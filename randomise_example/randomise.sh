cd /data/fmri/Youssef/codes/analysis/randmoise/optical_flow/sampen_vectors_regions/Three_regions/X_direction/regions_con_AD/region_1_exp
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH


fslmerge -t  merged_sampen_X_exp_con_AD_region1.nii.gz  /data/fmri/Youssef/Data/MREG_data/controls/merged_exp_region1_3_X_sampen.nii.gz /data/fmri/Youssef/Data/MREG_data/AD/merged_exp_region1_3_X_sampen.nii.gz

nohup randomise -i merged_sampen_X_exp_con_AD_region1.nii.gz  -o stat_opt_flow_sampen_X_exp_region1_con_AD_10k -d design_con_AD.mat -t design.con_AD -T -n 10000 >& log2020627-10k.txt &

