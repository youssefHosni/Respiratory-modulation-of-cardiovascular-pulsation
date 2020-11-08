source /data/fmri/Folder/Anaconda3/anaconda3/bin/activate
FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data
main_path_controls=/data/fmri/Youssef/Data/MREG_data/controls/controls
main_path_AD=/data/fmri/Youssef/Data/MREG_data/AD/AD
optflow=optflow-all-m3_lptp6_fullcard_iffdm.nii.gz
optflow_exp=optflow-all-m3_lptp6_fullcard_iffdm_exp.nii.gz
optflow_insp=optflow-all-m3_lptp6_fullcard_iffdm_insp.nii.gz



for data_used in "controls" "AD"
do
for j in "$main_path/$data_used/$data_used"/*	
do 

cd $j 

`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i optflow_insp_region1_3.nii.gz `
`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i optflow_insp_region2_3.nii.gz `
`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i optflow_insp_region3_3.nii.gz `


`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i optflow_exp_region1_3.nii.gz `
`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i optflow_exp_region2_3.nii.gz `
`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i optflow_exp_region3_3.nii.gz `




: '
optflow_file_path="$j"/"$optflow"
optflow_insp_file_path="$j"/"$optflow_insp"
optflow_exp_file_path="$j"/"$optflow_exp"


`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i $optflow_file_path `
`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i $optflow_insp_file_path `
`python3 /data/fmri/Youssef/codes/algorithms/fmri_optic_flow_master/fmri_optic_flow_master/vectors2speed.py   -i $optflow_exp_file_path `
'

done
done


