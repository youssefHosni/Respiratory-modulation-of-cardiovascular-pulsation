data_path='/data/fmri/Youssef/Data/MREG_data/controls/';
sample_name='20180626_3_FA5_c01.ica/';
filtered_belt_file_name='filtered_belt_data.mat';
filtered_finger_file_name='filtered_finger_data.mat';
filtered_mreg_resp_file_name='filtered_mreg_resp_data.mat';

belt_signal=load([data_path sample_name filtered_belt_file_name]);
finger_signal=load([data_path sample_name filtered_finger_file_name]);
mreg_resp_signal=load([data_path sample_name filtered_mreg_resp_file_name]);
Fs=10;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 % calculate the delay between the filtered belt signal and filtered resp signal of voxel [22,20,10]
[corr,lags]=xcorr(mreg_resp_signal.data,belt_signal.data);
[max_corr_value,max_corr_index]=max(corr);
delay_belt_mreg=lags(max_corr_index)/Fs

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% calculate the delay between the filtered belt signal and the filtered
% finger signal
[corr,lags]=xcorr(finger_signal.data,belt_signal.data);
[max_corr_value,max_corr_index]=max(corr);
delay_belt_finger=lags(max_corr_index)/Fs

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% calculate the delay between the filtered belt signal and filtered reps
% signal of voxel[22,20,10]
[corr,lags]=xcorr(finger_signal.data,mreg_resp_data.data);
[max_corr_value,max_corr_index]=max(corr);
delay_finger_resp=lags(max_corr_index)/Fs
