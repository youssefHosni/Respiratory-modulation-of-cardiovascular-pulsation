#  Methodology visualization 
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms')
from respiratory_phases_interval_extraction.load_data import load_niftiydata
from synchorization.find_refernce_voxel import find_refernce_voxel
from abnormalities_detection_removing.segment_abnormality import abnormal_segments_detection
from abnormalities_detection_removing.segment_abnormality import abnormal_segments_removing
from filtering.max_min_resp_rate import max_min_rate_calc
from filtering.filters import low_pass_filter
from scipy.interpolate import make_interp_spline
from respiratory_phases_interval_extraction.peak_detector_algorithm import find_peaks_valleys
from respiratory_phases_interval_extraction.save_data import save_nifity_data
from representing_the_differneces_at_different_resp_phases.representing_the_diff_with_resp_phases import insp_exp_regions_3

resp_MREG_data_file_name='resp_ffdm.nii.gz'
cardiac_MREG_data_file_name='fullcard_ffdm.nii.gz'
optical_flow_file_name='optflow-all-m3_lptp6_fullcard_iffdm.nii.gz'
main_path="/data/fmri/Youssef/Data/MREG_data"
data_used="controls"
mask_file_name="/data/fmri/Youssef/codes/analysis/Visualization/masks"
main_path=os.path.join(main_path,data_used,data_used)

refernce_resp_voxel_corrdinates=[20,20,10]
refernce_cardiac_voxels_corrdinates_control_list=[[21,39,20],
                 [21,41,18],
                 [21,36,17],
                 [22,41,18],
                 [21,40,17],
                 [21,37,17],
                 [21,36,18],
                 [21,35,18],
                 [21,40,18],
                 [21,39,17],
                 [21,40,18],
                 [21,41,16],
                 [21,40,16],
                 [21,39,17],
                 [22,40,17],
                 [22,40,18],
                 [22,40,18],
                 [22,39,19],
                 [22,37,15],
                 [21,39,17],
                 [21,39,17],
                 [22,39,15],
                 [21,39,17],
                 [21,40,18],
                 [21,41,17],
                 [21,39,17],
                 ]

  
sample_names=os.listdir(main_path)
sample_names=sorted(sample_names)
if data_used=='controls':
    refernce_cardiac_voxels_corrdinates_list=refernce_cardiac_voxels_corrdinates_control_list

elif data_used=='AD':
    refernce_cardiac_voxels_corrdinates_AD_list=find_refernce_voxel(sample_names,method='automatic',main_path=main_path,mreg_data_file_name=cardiac_MREG_data_file_name,refernce_voxel=[21,39,17],new_refernce_voxel=[],plot_results=0)
    refernce_cardiac_voxels_corrdinates_list=refernce_cardiac_voxels_corrdinates_AD_list

segment_time_length=32
min_allowed_resp_rate=8
max_allowed_resp_rate=20

min_allowed_heart_rate=60
max_allowed_heart_rate=100


resp_signal_filtering=1
remove_segment_abnormality=0
remove_cycle_abnormality=1
filter_order=8

new_voxel=([22,20,18],[22,20,28],[23,22,31],[11,34,29])

old_voxel=([22,32,32],[21,34,29],[22,38,28],[22,41,26])


selected_voxels=new_voxel
for i in range(len(sample_names)):
    
    if i >0:
        break
    
    [mreg_resp_data,mreg_resp_affine,mreg_resp_header]=load_niftiydata(os.path.join(main_path,sample_names[i],resp_MREG_data_file_name))
    [mreg_cardiac_data,mreg_cardiac_affine,mreg_cardiac_header]=load_niftiydata(os.path.join(main_path,sample_names[i],cardiac_MREG_data_file_name))
    [optical_flow,optical_flow_affine,optical_flow_header]=load_niftiydata(os.path.join(main_path,sample_names[i],optical_flow_file_name))
    
    #[mreg_data,mreg_affine,mreg_header]=load_niftiydata(os.path.join(main_path,sample_names[i],mreg_data_file_name))    
    refernce_voxel_resp_siganl=mreg_resp_data[refernce_resp_voxel_corrdinates[0],refernce_resp_voxel_corrdinates[1],refernce_resp_voxel_corrdinates[2],:]
    refernce_voxel_cardiac_siganl=mreg_cardiac_data[int(refernce_cardiac_voxels_corrdinates_list[i][0]),int(refernce_cardiac_voxels_corrdinates_list[i][1]),int(refernce_cardiac_voxels_corrdinates_list[i][2]),:]
    
        
    if resp_signal_filtering ==1:
        min_BR,max_BR=max_min_rate_calc(refernce_voxel_resp_siganl,segment_time_length)
        hp_wc=min_BR/60
        lp_wc=max_BR/60
        filtered_resp_signal=low_pass_filter(refernce_voxel_resp_siganl,lp_wc,filter_order)
        refernce_voxel_resp_siganl=filtered_resp_signal
    
    
    if remove_segment_abnormality==1:
        abnormal_segments_index=abnormal_segments_detection(refernce_voxel_resp_siganl,segment_time_length,min_allowed_resp_rate,max_allowed_resp_rate)
        if abnormal_segments_index!=[]:
            refernce_voxel_resp_siganl=abnormal_segments_removing(refernce_voxel_resp_siganl,abnormal_segments_index,segment_time_length,os.path.join(main_path,sample_names[i]),save_data=0)
            mreg_cardiac_data=abnormal_segments_removing(mreg_cardiac_data,abnormal_segments_index,segment_time_length,os.path.join(main_path,sample_names[i]),save_data=0)
            refernce_voxel_cardiac_siganl=mreg_cardiac_data[int(refernce_cardiac_voxels_corrdinates_list[i][0]),int(refernce_cardiac_voxels_corrdinates_list[i][1]),int(refernce_cardiac_voxels_corrdinates_list[i][2]),:]

optical_flow_mean=np.mean(optical_flow[:,:,:,:,0:9],axis=4)
optical_flow_x_dir= np.mean(optical_flow[:,:,:,0,0:9],axis=3)
optical_flow_y_dir= np.mean(optical_flow[:,:,:,1,0:9],axis=3)
optical_flow_z_dir= np.mean(optical_flow[:,:,:,2,0:9],axis=3)
speed=np.sqrt(optical_flow_mean[:,:,:,0]**2+optical_flow_mean[:,:,:,1]**2+optical_flow_mean[:,:,:,2]**2)



time=np.linspace(0,len(refernce_voxel_resp_siganl)/10,len(refernce_voxel_resp_siganl))

plt.plot(time[0:10],mreg_cardiac_data[selected_voxels[0][0],selected_voxels[0][1],selected_voxels[0][2],0:10],'r',label="first")
plt.plot(time[0:10],mreg_cardiac_data[selected_voxels[1][0],selected_voxels[1][1],selected_voxels[1][2],0:10],'b',label="second")
plt.plot(time[0:10],2*mreg_cardiac_data[selected_voxels[2][0],selected_voxels[2][1],selected_voxels[2][2],0:10],'g',label="third")
plt.plot(time[0:10],2*mreg_cardiac_data[selected_voxels[3][0],selected_voxels[3][1],selected_voxels[3][2],0:10],'m',label="fourth")

plt.legend()
plt.figure()


plt.plot(time[0:50],optical_flow[selected_voxels[0][0],selected_voxels[0][1],selected_voxels[0][2],0,0:50],'g',label="L-R")
plt.plot(time[0:50],optical_flow[selected_voxels[1][0],selected_voxels[1][1],selected_voxels[1][2],1,0:50],'k',label="A-P")
plt.plot(time[0:50],optical_flow[selected_voxels[2][0],selected_voxels[2][1],selected_voxels[2][2],2,0:50],'m',label="S-P")
plt.legend()
plt.figure()


new_length=len(time)*10
time_new=np.linspace(0,time[-1],new_length)

y1=mreg_cardiac_data[selected_voxels[0][0],selected_voxels[0][1],selected_voxels[0][2],:]
y2=mreg_cardiac_data[selected_voxels[1][0],selected_voxels[1][1],selected_voxels[1][2],:]
y3=mreg_cardiac_data[selected_voxels[2][0],selected_voxels[2][1],selected_voxels[2][2],:]
y4=mreg_cardiac_data[selected_voxels[3][0],selected_voxels[3][1],selected_voxels[3][2],:]/1.5

spl1 = make_interp_spline(time, y1, k=3)
spl2 = make_interp_spline(time, y2, k=3)
spl3 = make_interp_spline(time, y3, k=3)
spl4 = make_interp_spline(time, y4, k=3)
y1_new=spl1(time_new)
y2_new=spl2(time_new)
y3_new=spl3(time_new)
y4_new=spl4(time_new)


_,valleys_y1 =find_peaks_valleys(y1_new,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)
_,valleys_y2=find_peaks_valleys(y2_new,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)
_,valleys_y3 =find_peaks_valleys(y3_new,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)
_,valleys_y4 =find_peaks_valleys(y4_new,main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=1,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)



plt.xlabel("Time(s)")
plt.ylabel("Respiration(a.u)")

plt.plot(time[0:19],refernce_voxel_resp_siganl[400:419],'r')
plt.plot(time[18:40],refernce_voxel_resp_siganl[418:440],'c')
plt.plot(time[39:60],refernce_voxel_resp_siganl[439:460],'r')
plt.plot(time[58:79],refernce_voxel_resp_siganl[458:479],'c')
#plt.plot(time[0+79:19+79],refernce_voxel_resp_siganl[400+79:419+79],'r')
#plt.plot(time[18+79:40+79],refernce_voxel_resp_siganl[418+79:440+79],'c')

plt.figure()
plt.xlabel("Time(s)")
plt.ylabel("Respiration(a.u)")

x1=6
x2=4

plt.plot(time[0:7],refernce_voxel_resp_siganl[400:407],':',color='darkred',linewidth=x2)

plt.plot(time[6:13],refernce_voxel_resp_siganl[406:413],':',color='red',linewidth=x2)

plt.plot(time[12:20],refernce_voxel_resp_siganl[412:420],':',color='darkorange',linewidth=x2)

plt.plot(time[19:26],refernce_voxel_resp_siganl[419:426],':',color="cyan",linewidth=x2)

plt.plot(time[25:33],refernce_voxel_resp_siganl[425:433],':',color="blueviolet",linewidth=x2)

plt.plot(time[32:40],refernce_voxel_resp_siganl[432:440],':',color="magenta",linewidth=x1)
plt.savefig(os.path.join(mask_file_name,"resp_regions_plots","region6.png"))



plt.savefig(os.path.join(mask_file_name,"respiratory_sigal_phases.png"))

plt.savefig(os.path.join(mask_file_name,"respiratory_sigal_phases.png"))
plt.figure()

resp_peaks_index,resp_valleys_index =find_peaks_valleys(refernce_voxel_resp_siganl[400:439],main_path='',sample_name='',plot_results=0,interval_duration_calc=0,save_results=0,abnormal_cycle_removing=0,lower_RRPm=min_allowed_resp_rate,upper_RRPm=max_allowed_resp_rate)

insp_index,exp_index=insp_exp_regions_3(refernce_voxel_resp_siganl[400:439],resp_peaks_index,resp_valleys_index)



# plotting cardiac signal for certain voxels 
plt.xlabel("Time(s)")
plt.ylabel("MREG(a.u)")
plt.plot(time_new[0:100],y1_new[0:100],"r",label="A")
plt.plot(time_new[valleys_y1][0],y1_new[valleys_y1][0],"or")

plt.plot(time_new[0:100],y2_new[0:100],"b",label="B")
plt.plot(time_new[valleys_y2][0],y2_new[valleys_y2][0],"ob")

plt.plot(time_new[0:100],y3_new[0:100],"g",label="C")
plt.plot(time_new[valleys_y3][0],y3_new[valleys_y3][0],"og")

plt.plot(0.1+time_new[0:100],y4_new[0:100],"m",label="D")
plt.plot(0.1+time_new[valleys_y4][0],y4_new[valleys_y4][0],"om")
plt.legend()

plt.savefig(os.path.join(mask_file_name,"cardiac_sigal.png"))
plt.figure()



# printing brain mask of all zeros and just a certain voxel to be one 
mask1=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
mask2=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
mask3=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
mask4=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))


mask1[selected_voxels[0][0],selected_voxels[0][1],selected_voxels[0][2]]=1
mask2[selected_voxels[1][0],selected_voxels[1][1],selected_voxels[1][2]]=1            
mask3[selected_voxels[2][0],selected_voxels[2][1],selected_voxels[2][2]]=1            
mask4[selected_voxels[3][0],selected_voxels[3][1],selected_voxels[3][2]]=1


save_nifity_data(os.path.join(mask_file_name,"mask1.nii.gz"),mask1,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"mask2.nii.gz"),mask2,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"mask3.nii.gz"),mask3,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"mask4.nii.gz"),mask4,mreg_cardiac_affine,mreg_cardiac_header)

optical_flow_masked=optical_flow_mean
speed_masked=speed*(mask1+mask2+mask3+mask4)


optical_flow_x_dir_masked=(mask1+mask2+mask3+mask4)*optical_flow_x_dir
optical_flow_y_dir_masked=(mask1+mask2+mask3+mask4)*optical_flow_y_dir
optical_flow_z_dir_masked=(mask1+mask2+mask3+mask4)*optical_flow_z_dir


save_nifity_data(os.path.join(mask_file_name,"X_dir_masked.nii.gz"),optical_flow_x_dir_masked,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"Y_dir_masked.nii.gz"),optical_flow_y_dir_masked,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"Z_dir_masked.nii.gz"),optical_flow_z_dir_masked,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"optical_flow_masked.nii.gz"),optical_flow_masked,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"speed_masked.nii.gz"),speed_masked,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"speed.nii.gz"),speed,optical_flow_affine,optical_flow_header)



# virtual mask an d save it 

virtual_mask1=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
virtual_mask2=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
virtual_mask3=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
virtual_mask4=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))

virtual_mask5=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
virtual_mask6=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
virtual_mask7=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))
virtual_mask8=np.zeros((mreg_cardiac_data.shape[0],mreg_cardiac_data.shape[1],mreg_cardiac_data.shape[2]))



virtual_mask1[21:23,10:12,22:24]=1
virtual_mask2[21:23,16:18,26:28]=1
virtual_mask3[21:23,22:24,29:31]=1
virtual_mask4[21:23,28:30,31:33]=1

virtual_mask5[21:23,31:33,31:33]=1
virtual_mask6[21:23,34:36,29:31]=1
virtual_mask7[21:23,37:39,27:29]=1
virtual_mask8[21:23,40:42,25:27]=1





save_nifity_data(os.path.join(mask_file_name,"virtual_mask1.nii.gz"),virtual_mask1,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"virtual_mask2.nii.gz"),virtual_mask2,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"virtual_mask3.nii.gz"),virtual_mask3,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"virtual_mask4.nii.gz"),virtual_mask4,mreg_cardiac_affine,mreg_cardiac_header)


save_nifity_data(os.path.join(mask_file_name,"virtual_mask5.nii.gz"),virtual_mask5,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"virtual_mask6.nii.gz"),virtual_mask6,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"virtual_mask7.nii.gz"),virtual_mask7,mreg_cardiac_affine,mreg_cardiac_header)
save_nifity_data(os.path.join(mask_file_name,"virtual_mask8.nii.gz"),virtual_mask8,mreg_cardiac_affine,mreg_cardiac_header)


# optical seperate masked files

time1 = np.where(optical_flow[selected_voxels[0][0],selected_voxels[0][1],selected_voxels[0][2],0,:]!=0)[0][0]
time2 = np.where(optical_flow[selected_voxels[1][0],selected_voxels[1][1],selected_voxels[1][2],0,:]!=0)[0][2]
time3 = np.where(optical_flow[selected_voxels[2][0],selected_voxels[2][1],selected_voxels[2][2],0,:]!=0)[0][5]



optical_flow_1=optical_flow[:,:,:,:,time1]
optical_flow_2=optical_flow[:,:,:,:,time2]
optical_flow_3=optical_flow[:,:,:,:,time3]

speed_1=np.sqrt(optical_flow_1[:,:,:,0]**2+optical_flow_1[:,:,:,1]**2+optical_flow_1[:,:,:,2]**2)
speed_2=np.sqrt(optical_flow_2[:,:,:,0]**2+optical_flow_2[:,:,:,1]**2+optical_flow_2[:,:,:,2]**2)
speed_3=np.sqrt(optical_flow_3[:,:,:,0]**2+optical_flow_3[:,:,:,1]**2+optical_flow_3[:,:,:,2]**2)



optical_flow_mask1=np.zeros_like(optical_flow_1)
optical_flow_mask1[selected_voxels[0][0],selected_voxels[0][1],selected_voxels[0][2],:]=1
optical_flow_1_masked= optical_flow_1*optical_flow_mask1

optical_flow_mask2=np.zeros_like(optical_flow_2)
optical_flow_mask2[selected_voxels[1][0],selected_voxels[1][1],selected_voxels[1][2],:]=1
optical_flow_2_masked= optical_flow_1*optical_flow_mask2

optical_flow_mask3=np.zeros_like(optical_flow_3)
optical_flow_mask3[selected_voxels[2][0],selected_voxels[2][1],selected_voxels[2][2],:]=1
optical_flow_3_masked= optical_flow_1*optical_flow_mask3



save_nifity_data(os.path.join(mask_file_name,"optical_flow_1.nii.gz"),optical_flow_1,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"optical_flow_2.nii.gz"),optical_flow_2,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"optical_flow_3.nii.gz"),optical_flow_3,optical_flow_affine,optical_flow_header)


save_nifity_data(os.path.join(mask_file_name,"optical_flow_1_masked.nii.gz"),optical_flow_1_masked,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"optical_flow_2_masked.nii.gz"),optical_flow_2_masked,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"optical_flow_3_masked.nii.gz"),optical_flow_3_masked,optical_flow_affine,optical_flow_header)

save_nifity_data(os.path.join(mask_file_name,"speed_1.nii.gz"),speed_1,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"speed_2.nii.gz"),speed_2,optical_flow_affine,optical_flow_header)
save_nifity_data(os.path.join(mask_file_name,"speed_3.nii.gz"),speed_3,optical_flow_affine,optical_flow_header)
