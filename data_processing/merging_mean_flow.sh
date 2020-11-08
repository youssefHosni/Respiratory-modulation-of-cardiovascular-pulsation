FSLDIR=/data/fmri/Folder/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

main_path=/data/fmri/Youssef/Data/MREG_data
mean_speed=optflow-all-m3_lptp6_fullcard_iffdm_mean-speed.nii.gz
mean_X=optflow-all-m3_lptp6_fullcard_iffdm_mean-X.nii.gz
mean_Y=optflow-all-m3_lptp6_fullcard_iffdm_mean-Y.nii.gz
mean_Z=optflow-all-m3_lptp6_fullcard_iffdm_mean-Z.nii.gz


mean_speed_insp=optflow-all-m3_lptp6_fullcard_iffdm_insp_mean-speed.nii.gz
std_speed_insp=optflow-all-m3_lptp6_fullcard_iffdm_insp_speed_std.nii.gz
sampen_speed_insp=optflow-all-m3_lptp6_fullcard_iffdm_insp_speed_sampen.nii.gz
mean_X_insp=optflow-all-m3_lptp6_fullcard_iffdm_insp_mean-X.nii.gz
mean_Y_insp=optflow-all-m3_lptp6_fullcard_iffdm_insp_mean-Y.nii.gz
mean_Z_insp=optflow-all-m3_lptp6_fullcard_iffdm_insp_mean-Z.nii.gz

mean_speed_exp=optflow-all-m3_lptp6_fullcard_iffdm_exp_mean-speed.nii.gz
std_speed_exp=optflow-all-m3_lptp6_fullcard_iffdm_exp_speed_std.nii.gz
sampen_speed_exp=optflow-all-m3_lptp6_fullcard_iffdm_exp_speed_sampen.nii.gz
mean_X_exp=optflow-all-m3_lptp6_fullcard_iffdm_exp_mean-X.nii.gz
mean_Y_exp=optflow-all-m3_lptp6_fullcard_iffdm_exp_mean-Y.nii.gz
mean_Z_exp=optflow-all-m3_lptp6_fullcard_iffdm_exp_mean-Z.nii.gz

mean_speed_resp_peaks=optflow_lptp6_fullcard_iffdm_speed_resp_peaks_mean.nii.gz
mean_speed_resp_valleys=optflow_lptp6_fullcard_iffdm_speed_resp_valleys_mean.nii.gz
mean_speed_resp_max_der=optflow_lptp6_fullcard_iffdm_speed_resp_max_der_mean.nii.gz
mean_speed_resp_min_der=optflow_lptp6_fullcard_iffdm_speed_resp_min_der_mean.nii.gz


mean_speed_resp_min_der_tol=optflow_lptp6_iffdm_speed_min_der_tol_mean.nii.gz
mean_speed_resp_max_der_tol=optflow_lptp6_iffdm_speed_max_der_tol_mean.nii.gz
mean_speed_exp_valleys_tol=optflow_lptp6_iffdm_speed_exp_valleys_tol_mean.nii.gz
mean_speed_exp_peaks_tol=optflow_lptp6_iffdm_speed_exp_peaks_tol_mean.nii.gz
mean_speed_insp_valleys_tol=optflow_lptp6_iffdm_speed_insp_valleys_tol_mean.nii.gz
mean_speed_insp_peaks_tol=optflow_lptp6_iffdm_speed_insp_peaks_tol_mean.nii.gz


mean_speed_insp_sampen=optflow_iffdm_insp_speed_sampen_mean.nii.gz
mean_speed_exp_sampen=optflow_iffdm_exp_speed_sampen_mean.nii.gz


counter=0


for data_used in  "AD" "controls"
do
counter=0
for j in "$main_path/$data_used/$data_used"/*	
do 	

	mean_speed_file_path="$j"/"$mean_speed"
	mean_X_file_path="$j"/"$mean_X"
	mean_Y_file_path="$j"/"$mean_Y"
	mean_Z_file_path="$j"/"$mean_Z"
		

	mean_speed_insp_file_path="$j"/"$mean_speed_insp"	
	std_speed_insp_file_path="$j"/"$std_speed_insp"	
	sampen_speed_insp_file_path="$j"/"$sampen_speed_insp"	
	
	mean_X_insp_file_path="$j"/"$mean_X_insp"
	mean_Y_insp_file_path="$j"/"$mean_Y_insp"
	mean_Z_insp_file_path="$j"/"$mean_Z_insp"
	
	mean_speed_exp_file_path="$j"/"$mean_speed_exp"
	std_speed_exp_file_path="$j"/"$std_speed_exp"
	sampen_speed_exp_file_path="$j"/"$sampen_speed_exp"	
	
	mean_X_exp_file_path="$j"/"$mean_X_exp"
	mean_Y_exp_file_path="$j"/"$mean_Y_exp"
	mean_Z_exp_file_path="$j"/"$mean_Z_exp"

	#speed mean at differnet resp loc points 
	
	mean_speed_resp_peaks_file_path="$j"/"$mean_speed_resp_peaks"
	mean_speed_resp_valleys_file_path="$j"/"$mean_speed_resp_valleys"
	mean_speed_resp_max_der_file_path="$j"/"$mean_speed_resp_max_der"
	mean_speed_resp_min_der_file_path="$j"/"$mean_speed_resp_min_der"
	
	#speed mean at differnet resp phases loc points withh two samples tolerance
	
	mean_speed_resp_min_der_tol_file_path="$j"/"$mean_speed_resp_min_der_tol"
	mean_speed_resp_max_der_tol_file_path="$j"/"$mean_speed_resp_max_der_tol"
	mean_speed_insp_peaks_tol_file_path="$j"/"$mean_speed_insp_peaks_tol"
	mean_speed_insp_valleys_tol_file_path="$j"/"$mean_speed_insp_valleys_tol"
	mean_speed_exp_peaks_tol_file_path="$j"/"$mean_speed_exp_peaks_tol"
	mean_speed_exp_valleys_tol_file_path="$j"/"$mean_speed_exp_valleys_tol"
	

	mean_optflow_speed_insp_region1_file_path="$j"/"optflow_speed_insp_region1_mean.nii.gz"
	mean_optflow_speed_insp_region2_file_path="$j"/"optflow_speed_insp_region2_mean.nii.gz"
	mean_optflow_speed_insp_region3_file_path="$j"/"optflow_speed_insp_region3_mean.nii.gz"
	mean_optflow_speed_insp_region4_file_path="$j"/"optflow_speed_insp_region4_mean.nii.gz"
	

	mean_optflow_speed_exp_region1_file_path="$j"/"optflow_speed_exp_region1_mean.nii.gz"
	mean_optflow_speed_exp_region2_file_path="$j"/"optflow_speed_exp_region2_mean.nii.gz"
	mean_optflow_speed_exp_region3_file_path="$j"/"optflow_speed_exp_region3_mean.nii.gz"
	mean_optflow_speed_exp_region4_file_path="$j"/"optflow_speed_exp_region4_mean.nii.gz"

	mean_speed_insp_sampen_file_path="$j"/"$mean_speed_insp_sampen"
	mean_speed_exp_sampen_file_path="$j"/"$mean_speed_exp_sampen"
	

	sampen_speed_exp_region1_file_path="$j"/"optflow_iffdm_exp_region1_speed_sampen.nii.gz"
	sampen_speed_insp_region1_file_path="$j"/"optflow_iffdm_insp_region1_speed_sampen.nii.gz"

	sampen_speed_exp_region2_file_path="$j"/"optflow_iffdm_exp_region2_speed_sampen.nii.gz"
	sampen_speed_insp_region2_file_path="$j"/"optflow_iffdm_insp_region2_speed_sampen.nii.gz"

	sampen_speed_exp_region3_file_path="$j"/"optflow_iffdm_exp_region3_speed_sampen.nii.gz"
	sampen_speed_insp_region3_file_path="$j"/"optflow_iffdm_insp_region3_speed_sampen.nii.gz"

	sampen_speed_exp_region4_file_path="$j"/"optflow_iffdm_exp_region4_speed_sampen.nii.gz"
	sampen_speed_insp_region4_file_path="$j"/"optflow_iffdm_insp_region4_speed_sampen.nii.gz"



	if [[ $counter -eq 0 ]] 
	then 
	
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region1.nii.gz     $sampen_speed_exp_region1_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region2.nii.gz     $sampen_speed_exp_region2_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region3.nii.gz     $sampen_speed_exp_region3_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region4.nii.gz     $sampen_speed_exp_region4_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region1.nii.gz    $sampen_speed_insp_region1_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region2.nii.gz    $sampen_speed_insp_region2_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region3.nii.gz    $sampen_speed_insp_region3_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region4.nii.gz    $sampen_speed_insp_region4_file_path

	
	: '
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_sampen.nii.gz    $mean_speed_insp_sampen_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_sampen.nii.gz    $mean_speed_exp_sampen_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region1.nii.gz    $mean_optflow_speed_insp_region1_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region2.nii.gz    $mean_optflow_speed_insp_region2_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region3.nii.gz    $mean_optflow_speed_insp_region3_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region4.nii.gz    $mean_optflow_speed_insp_region4_file_path

	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region1.nii.gz    $mean_optflow_speed_exp_region1_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region2.nii.gz    $mean_optflow_speed_exp_region2_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region3.nii.gz    $mean_optflow_speed_exp_region3_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region4.nii.gz    $mean_optflow_speed_exp_region4_file_path

	
	#speed mean at differnet resp phases loc points withh two samples tolerance

	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_min_der_tol.nii.gz    $mean_speed_resp_min_der_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_max_der_tol.nii.gz    $mean_speed_resp_max_der_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_peaks_tol.nii.gz      $mean_speed_insp_peaks_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_valleys_tol.nii.gz    $mean_speed_insp_valleys_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_peaks_tol.nii.gz       $mean_speed_exp_peaks_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_valleys_tol.nii.gz     $mean_speed_exp_valleys_tol_file_path


	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_peaks.nii.gz    $mean_speed_resp_peaks_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_valleys.nii.gz  $mean_speed_resp_valleys_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_max_der.nii.gz       $mean_speed_resp_max_der_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_min_der.nii.gz       $mean_speed_resp_min_der_file_path
	
	
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_opt_flow_speed_insp.nii.gz  $sampen_speed_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_opt_flow_speed_exp.nii.gz  $sampen_speed_exp_file_path

		

	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_opt_flow_speed_insp.nii.gz  $std_speed_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_opt_flow_speed_exp.nii.gz  $std_speed_exp_file_path
	
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed.nii.gz  $mean_speed_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X.nii.gz  $mean_X_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y.nii.gz  $mean_Y_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z.nii.gz  $mean_Z_file_path
		
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed_insp.nii.gz  $mean_speed_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X_insp.nii.gz  $mean_X_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y_insp.nii.gz  $mean_Y_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z_insp.nii.gz  $mean_Z_insp_file_path
	
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed_exp.nii.gz  $mean_speed_exp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X_exp.nii.gz  $mean_X_exp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y_exp.nii.gz  $mean_Y_exp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z_exp.nii.gz  $mean_Z_exp_file_path
	'
		

	else

	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region1.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region1.nii.gz     $sampen_speed_exp_region1_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region2.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region2.nii.gz     $sampen_speed_exp_region2_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region3.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region3.nii.gz     $sampen_speed_exp_region3_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region4.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_exp_region4.nii.gz     $sampen_speed_exp_region4_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region1.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region1.nii.gz    $sampen_speed_insp_region1_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region2.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region2.nii.gz    $sampen_speed_insp_region2_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region3.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region3.nii.gz    $sampen_speed_insp_region3_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region4.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_sampen_speed_insp_region4.nii.gz    $sampen_speed_insp_region4_file_path

	: '
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_sampen.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_sampen.nii.gz    $mean_speed_insp_sampen_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_sampen.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_sampen.nii.gz    $mean_speed_exp_sampen_file_path

	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region1.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region1.nii.gz    $mean_optflow_speed_insp_region1_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region2.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region2.nii.gz    $mean_optflow_speed_insp_region2_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region3.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region3.nii.gz  $mean_optflow_speed_insp_region3_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region4.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_region4.nii.gz  $mean_optflow_speed_insp_region4_file_path

	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region1.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region1.nii.gz    $mean_optflow_speed_exp_region1_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region2.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region2.nii.gz $mean_optflow_speed_exp_region2_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region3.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region3.nii.gz $mean_optflow_speed_exp_region3_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region4.nii.gz   /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_region4.nii.gz $mean_optflow_speed_exp_region4_file_path


	#speed mean at differnet resp phases loc points withh two samples tolerance

	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_min_der_tol.nii.gz     /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_min_der_tol.nii.gz   $mean_speed_resp_min_der_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_max_der_tol.nii.gz    /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_max_der_tol.nii.gz    $mean_speed_resp_max_der_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_peaks_tol.nii.gz     /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_peaks_tol.nii.gz       $mean_speed_insp_peaks_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_valleys_tol.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_insp_valleys_tol.nii.gz      $mean_speed_insp_valleys_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_peaks_tol.nii.gz    /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_peaks_tol.nii.gz          $mean_speed_exp_peaks_tol_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_valleys_tol.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_exp_valleys_tol.nii.gz        $mean_speed_exp_valleys_tol_file_path


	
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_peaks.nii.gz     /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_peaks.nii.gz   $mean_speed_resp_peaks_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_valleys.nii.gz  /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_resp_valleys.nii.gz  $mean_speed_resp_valleys_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_max_der.nii.gz      /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_max_der.nii.gz        $mean_speed_resp_max_der_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_min_der.nii.gz     /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_speed_min_der.nii.gz         $mean_speed_resp_min_der_file_path

	
	
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_opt_flow_speed_insp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_opt_flow_speed_insp.nii.gz  $std_speed_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_opt_flow_speed_exp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_std_opt_flow_speed_exp.nii.gz  $std_speed_exp_file_path
		
	
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed.nii.gz  $mean_speed_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X.nii.gz  $mean_X_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y.nii.gz  $mean_Y_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z.nii.gz  $mean_Z_file_path
		

	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed_insp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed_insp.nii.gz  $mean_speed_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X_insp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X_insp.nii.gz  $mean_X_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y_insp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y_insp.nii.gz  $mean_Y_insp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z_insp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z_insp.nii.gz  $mean_Z_insp_file_path
	
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed_exp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_opt_flow_speed_exp.nii.gz  $mean_speed_exp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X_exp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_X_exp.nii.gz  $mean_X_exp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y_exp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Y_exp.nii.gz  $mean_Y_exp_file_path
	fslmerge -t /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z_exp.nii.gz /data/fmri/Youssef/Data/MREG_data/$data_used/merged_mean_Z_exp.nii.gz  $mean_Z_exp_file_path
	'



	fi
	counter=$((counter+1))

done
done 





