FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data

cd /data/fmri/Youssef/Data/MREG_data/controls

fsleyes -b -ls 24 -vl 172 270 126 ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 50  \
diff_insp_region1_2_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_insp_region2_3_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_insp_region3_4_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_exp_region1_2_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_exp_region2_3_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_exp_region3_4_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_insp_exp_region4_1_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 


diff_insp_region1_2_flow_mean-vectors_subj-avg.nii.gz

cd /data/fmri/Youssef/Data/MREG_data/controls

fsleyes -b -ls 24 -vl 172 270 126 ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 50  \
diff_insp_region1_2_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_insp_region2_3_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_insp_region3_4_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \

diff_exp_region1_2_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_exp_region2_3_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
diff_exp_region3_4_flow_mean-vectors_subj-avg.nii.gz -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 





fsleyes -b -ls 24 -vl 172 270 126 ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 50 \
diff_insp_region1_2_flow_mean-speed_subj-avg.nii.gz -dr 0.05 0.3 -cm red-yellow -un -nc blue-lightblue -in spline \
diff_insp_region2_3_flow_mean-speed_subj-avg.nii.gz -dr 0.05 0.3 -cm red-yellow -un -nc blue-lightblue -in spline \
diff_insp_region3_4_flow_mean-speed_subj-avg.nii.gz -dr 0.0 0.3 -cm red-yellow -un -nc blue-lightblue -in spline \
diff_insp_exp_region4_1_flow_mean-speed_subj-avg.nii.gz -dr 0.05 0.3 -cm red-yellow -un -nc blue-lightblue -in spline \
diff_exp_region1_2_flow_mean-speed_subj-avg.nii.gz -dr 0.05 0.3 -cm red-yellow -un -nc blue-lightblue -in spline \
diff_exp_region2_3_flow_mean-speed_subj-avg.nii.gz -dr 0.05 0.3 -cm red-yellow -un -nc blue-lightblue -in spline \
diff_exp_region3_4_flow_mean-speed_subj-avg.nii.gz -dr 0.05 0.3 -cm red-yellow -un -nc blue-lightblue -in spline \


fsleyes -b -ls 24 -vl 172 270 126 ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 50 \
 /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp_region1.nii.gz   -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
 /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp_region2.nii.gz   -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
 /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp_region3.nii.gz   -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
 /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_insp_region4.nii.gz   -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
 /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp_region1.nii.gz   -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
 /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp_region2.nii.gz   -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
 /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp_region3.nii.gz   -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
 /data/fmri/Youssef/Data/MREG_data/controls/flow_mean_vectors_exp_region4.nii.gz   -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 




fsleyes -b -ls 24 -vl 172 270 126 ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 50 \
/data/fmri/Youssef/Data/MREG_data/controls/diff_insp_region3_4_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
/data/fmri/Youssef/Data/MREG_data/controls/diff_insp_region2_3_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
/data/fmri/Youssef/Data/MREG_data/controls/diff_insp_region1_2_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
/data/fmri/Youssef/Data/MREG_data/controls/diff_insp_exp_region4_1_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \

			

/data/fmri/Youssef/Data/MREG_data/controls/diff_exp_region3_4_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
/data/fmri/Youssef/Data/MREG_data/controls/diff_exp_region2_3_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \
/data/fmri/Youssef/Data/MREG_data/controls/diff_exp_region1_2_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 1000 \









: '
for data_used in "controls" "AD" ; do 
for i in {1..4} ; do  

cd "$main_path/$data_used"

fsleyes render -S -b -of insp_region${i}_mean-vectors_lq.png -sz 1920 640 ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 100  -b 40 -c 60  flow_mean_vectors_insp_region${i}.nii.gz  -ot linevector -b 65 -c 85  -lw 2 -ld -nu -ls 500
fsleyes render -S -b -of exp_region${i}_mean-vectors_lq.png -sz 1920 640 ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 100  -b 40 -c 60  flow_mean_vectors_exp_region${i}.nii.gz  -ot linevector -b 65 -c 85  -lw 2 -ld -nu -ls 500

#fsleyes render -S -b -ls 24 -vl 172 270 126 -of ${data_used}_mean_speed_region${i}_lq.png ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 50 mean_speed_insp_region${i}_all_samples.nii.gz -dr 0.2 0.5 -cm red-yellow -un -nc blue-lightblue -in spline 
#fsleyes render -S -b -ls 24 -vl 172 270 126 -of ${data_used}_mean_speed_region${i}_lq.png ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 50 mean_speed_exp_region${i}_all_samples.nii.gz -dr 0.2 0.5 -cm red-yellow -un -nc blue-lightblue -in spline 


done
done
'

fsleyes -b -ls 24 -vl 172 270 126 ${FSLDIR}/data/standard/MNI152_T1_0.5mm -a 50 \
/data/fmri/Youssef/Data/MREG_data/diff_con_AD_insp_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 \
/data/fmri/Youssef/Data/MREG_data/diff_con_AD_exp_flow_mean-vectors_subj-avg.nii.gz  -ot linevector -b 60 -c 80 -lw 2 -ld -nu -ls 2000 

			

