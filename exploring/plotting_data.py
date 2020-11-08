plotting the data using differnt methods.
import sys
import numpy as np
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from respiratory_phases_interval_extraction.load_data import load_npydata
from respiratory_phases_interval_extraction.load_data import load_niftiydata
from respiratory_phases_interval_extraction.save_data import save_nifity_data
from respiratory_phases_interval_extraction.save_data import save_numeric_data
from respiratory_phases_interval_extraction.load_data import load_matdata
from max_min_resp_rate import segmeantation_and_BR
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from numpy import cov
from scipy.stats import shapiro
import scipy.io as sio

def load_plot(main_path,sample_name,file_name,data_type,title):
    full_path=os.path.join(main_path,sample_name,file_name)
    if data_type== 'mat':
        signal=load_matdata(full_path,'resampled')
        if signal.shape[0]==1:
            signal=signal.transpose()
        time=np.linspace(0,np.size(signal)/10,np.size(signal))
        plt.plot(time,signal)
        plt.title(title)
        plt.xlabel('time in sec')
        plt.ylabel('signal magnitudde')
    elif data_type=='nifity':
        signal,signal_affine,signal_header=load_niftiydata(full_path)
        time=np.linspace(0,np.shape(signal)[3]/10,np.shape(signal)[3])
        plt.plot(time,signal[22,20,10,:])
        plt.title(title)
        plt.xlabel('time in sec')
        plt.ylabel('signal magnitudde')
    return signal   

def  plot_spectogram(input_signal):
    plt.figure()
    f, t, Sxx = signal.spectrogram(input_signal, 10, return_onesided=False)
    plt.pcolormesh(t, np.fft.fftshift(f), np.fft.fftshift(Sxx, axes=0))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')


def frequency_component(input_signal,title):
    f_s=10
    freq_mag= fftpack.fft(input_signal)
    freqs = fftpack.fftfreq(len(input_signal)) * f_s
    fig, ax = plt.subplots()
    ax.stem(freqs, np.abs(freq_mag))
    ax.set_xlabel('Frequency in Hertz [Hz]')
    ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
    ax.set_title(title)
    ax.set_xlim(-f_s / 2, f_s / 2)
    ax.set_ylim(-5, 110)



def corr_delay_calc(input_signal1,input_signal2,method,plot_title,label1,label2):
    """
   This functions take two signal and find the corrleation and the delay between them and 
   shift signal 2 to be synch with signal 1.
    
   input_signal1: should be the signal that i  will compare the signals to 
   input_signal2 :the one that will be shifted after that.
   
   method :
       1: Pad the shorter signal with zero 
       2: Remove the extra samples from the longer signal
       plot title: The title of the plot
       Label1: label of the input signal one.
       Label2: label of the input signal two.
    """
    input_signal1=input_signal1[:,np.newaxis]
    input_signal2=input_signal2[:,np.newaxis]
    if method ==1:
        if len(input_signal1)<len(input_signal2):
            zeros_padding=np.zeros((abs(len(input_signal1)-len(input_signal2)),1))
            y1=np.vstack((input_signal1,zeros_padding))
            y2=input_signal2
          
        elif  len(input_signal1)>len(input_signal2):
            zeros_padding=np.zeros((abs(len(input_signal1)-len(input_signal2)),1))
            y1=input_signal1
            y2=np.vstack((input_signal2,zeros_padding))
            print ('signal 1  is longer signal 2')
            print(input_signal1.shape)
            print(input_signal2.shape)
        else:
            y1=input_signal1
            y2=input_signal2
        
       
        sr=10
        time=np.linspace(0,len(y1)/sr,len(y1))
        delay,corr,calc_corr=lag_finder(y1,y2,sr)
        corrected_signal=fraction_shifting(np.squeeze(y2),delay)
        
        
        
        plt.figure()
        plt.title(plot_title)
        plt.plot(time,y1,label=label1)
        plt.plot(time,(max(y1)/max(corrected_signal))*corrected_signal,label=label2)
        plt.legend()
        cala_corr,_=spearmanr(y1,corrected_signal)
        print('The correlation between ' + label1 + ' and ' + label2 + 'is : %f ' % calc_corr)
        
    elif method==2:
        if len(input_signal2)>len(input_signal1):
            y1= input_signal1
            y2=input_signal2[0:len(input_signal1)]
        
        elif  len(input_signal2)<len(input_signal1):
            y1=input_signal1[0:len(input_signal2)]
            y2=input_signal2
        else:
            y1=input_signal1
            y2=input_signal2
        
        sr=10
        time=np.linspace(0,len(y1)/sr,len(y1))
        delay,corr,calc_corr=lag_finder(y1,y2,sr)
        corrected_signal=fraction_shifting(np.squeeze(y2),delay)
        
        plt.figure()
        plt.title(plot_title)
        plt.plot(time,y1,label=label1)
        plt.plot(time,(max(y1)/max(corrected_signal))*corrected_signal,label=label2)
        plt.legend()
        cala_corr,_=spearmanr(y1,corrected_signal)
        print('The correlation between ' + label1 + ' and  the shifted ' + label2 + 'is : %f ' % calc_corr)
            
        
        

def lag_finder(y1, y2, sr):
    n = len(y1)
    corr = signal.correlate(y1, y2, mode='same') / np.sqrt(signal.correlate(y1, y1, mode='same')[int(n/2)] * signal.correlate(y2, y2, mode='same')[int(n/2)])
    delay_arr = np.linspace(-0.5*n/sr, 0.5*n/sr, n)
    
    stat1, p1 = shapiro(y1)
    stat2, p2 = shapiro(y2)
    alpha=0.05
    print(p1)
    print(p2)
    if (p1< alpha) and (p2 < alpha):
        calc_corr, _ = spearmanr(y1, y2)
        print('The two data sets are not normally distrubited')                
    
    else:
        calc_corr,_=pearsonr(y1, y2)

    
    if calc_corr>0:
        delay = delay_arr[np.argmax(corr)]
    else:
        delay = delay_arr[np.argmax(corr)]
   
    print('y2 started ' + str(delay) +  ' after y1')    
    plt.figure()
    plt.plot(delay_arr, corr)
    plt.title('Lag: ' + str(np.round(delay, 3)) + ' s')
    plt.xlabel('Lag')
    plt.ylabel('Correlation coeff')
    plt.show()
    return delay,corr,calc_corr
    

def fraction_shifting(signal,delay):
    
    fs=10
    
    # 1. Take the FFT
    fftData = np.fft.fft(signal)
    
    # 2. Construct the phase shift
    
    tDelayInSamples = delay * fs
    N = fftData.shape[0]
    k = np.linspace(0, N-1, N)
    timeDelayPhaseShift = np.exp(((-2*np.pi*1j*k*tDelayInSamples)/(N)) + (tDelayInSamples*np.pi*1j))
    
    # 3. Do the fftshift on the phase shift coefficients
    timeDelayPhaseShift = np.fft.fftshift(timeDelayPhaseShift)
    
    # 4. Multiply the fft data with the coefficients to apply the time shift
    fftWithDelay = np.multiply(fftData, timeDelayPhaseShift)
    
    # 5. Do the IFFT
    shifted_signal = np.fft.ifft(fftWithDelay)
    
    print("The time delay is %f seconds" % delay)
    print("The time delay in samples is %f samples" % tDelayInSamples)
    print("The correction phase shift is %f pi" % (tDelayInSamples))
    
   
    return shifted_signal
  

save_mat=0
main_path='/data/fmri/Youssef/Data/MREG_data/controls'
sample_name='20162211_mreg_fa5.ica'

file_name='puls_data_resampled.mat'
data_type='mat'
finger_signal=load_plot(main_path,sample_name,file_name,data_type,'finger_signal')

plt.figure()



"""
main_path='/data/fmri/Youssef/Data/MREG_data/controls'
sample_name='20161025_mreg_fa5.ica'
file_name='extracted_resp_data.mat'
data_type='mat'
extracted_resp_signal=load_plot(main_path,sample_name,file_name,data_type,'extracted_resp_signal')

plt.figure()
"""

file_name='belt_data_resampled.mat'
data_type='mat'
belt_signal=load_plot(main_path,sample_name,file_name,data_type,'belt_data')

plt.figure()


file_name='resp_ffdm.nii.gz'
data_type='nifity'
resp_signal=load_plot(main_path,sample_name,file_name,data_type,'MREG_Resp_signal')
plt.figure()


file_name='resp_ffdm.nii.gz'
data_type='nifity'
resp_signal=load_plot(main_path,sample_name,file_name,data_type,'MREG_Resp_signal')
plt.figure()

file_name='card_ffdm.nii.gz'
data_type='nifity'
cardiac_signal=load_plot(main_path,sample_name,file_name,data_type,'MREG_cardiac_signal')
plt.figure()


file_name='fullcard_ffdm.nii.gz'
data_type='nifity'
full_cardiac_signal=load_plot(main_path,sample_name,file_name,data_type,'MREG_full_cardiac_signal')
plt.figure()


file_name='fullcard_iffdm.nii.gz'
data_type='nifity'
full_inverted_cardiac_signal=load_plot(main_path,sample_name,file_name,data_type,'MREG__full_inverted_cardiac_signal')
plt.figure()

refernce_cardiac_voxel=cardiac_signal[21,39,17,:]
refernce_full_cardiac_voxel=full_cardiac_signal[21,39,17,:]
refernce_full_inverted_cardiac_voxel=full_inverted_cardiac_signal[21,39,17,:]

"""

frequency_component(refernce_cardiac_voxel,'cardiac signal')
plt.figure()
frequency_component(refernce_full_cardiac_voxel,'full cardiac signal')
plt.figure()
frequency_component(refernce_full_inverted_cardiac_voxel,'full inverted cardiac signal')
plt.figure()
frequency_component(np.squeeze(finger_signal),'finger_signal')




frequency_component(np.squeeze(belt_signal),'belt_signal')
plt.figure()
frequency_component(np.squeeze(finger_signal),'finger_signal')

plt.figure()
frequency_component(np.squeeze(extracted_resp_signal),'extracted_resp_signal')

plt.figure()
frequency_component(resp_signal[22,20,10,:],'MREG_Resp_signal')
"""

###filtering ranges 

min_br,max_br=segmeantation_and_BR(belt_signal,16,'max_min_breathing_rate')
hp_fc=min_br/60
lp_fc=max_br/60

sos = signal.butter(6, hp_fc, 'hp', fs=10, output='sos')
high_pass_filtered_finger_signal = signal.sosfilt(sos, np.squeeze(finger_signal))
frequency_component(high_pass_filtered_finger_signal,' high passed filterd_finger_signal')
sos = signal.butter(6, lp_fc, 'lp', fs=10, output='sos')
filtered_finger_signal = signal.sosfilt(sos, high_pass_filtered_finger_signal) 
plt.figure()
frequency_component(filtered_finger_signal,'band passed filterd_finger_signal')


sos = signal.butter(6, hp_fc, 'hp', fs=10, output='sos')
high_pass_filtered_belt_signal = signal.sosfilt(sos, np.squeeze(belt_signal))
sos = signal.butter(6, lp_fc, 'lp', fs=10, output='sos')
filtered_belt_signal = signal.sosfilt(sos,high_pass_filtered_belt_signal)
plt.figure()
frequency_component(filtered_belt_signal,'band pass filterd_belt_signal')

sos = signal.butter(6, hp_fc, 'hp', fs=10, output='sos')
high_pass_filtered_mreg_resp_signal = signal.sosfilt(sos, resp_signal[22,20,10,:])
plt.figure()
sos = signal.butter(6, lp_fc, 'lp', fs=10, output='sos')
filtered_mreg_resp_signal = signal.sosfilt(sos,high_pass_filtered_mreg_resp_signal)
frequency_component(filtered_mreg_resp_signal,'filterd_resp_signal')


sos = signal.butter(6, 0.7, 'hp', fs=10, output='sos')
high_pass_filtered_cardiac_finger_signal = signal.sosfilt(sos, np.squeeze(finger_signal))
frequency_component(high_pass_filtered_cardiac_finger_signal,' high passed filterd_finger_signal')
sos = signal.butter(6, 4.5, 'lp', fs=10, output='sos')
filtered_cardiac_finger_signal = signal.sosfilt(sos, high_pass_filtered_cardiac_finger_signal) 
plt.figure()
frequency_component(filtered_cardiac_finger_signal,'band passed filterd_finger_signal')





'''
sos = signal.cheby2(40,20, 0.6, 'hp', fs=10, output='sos')
high_pass_filtered_cardiac_finger_signal = signal.sosfilt(sos, np.squeeze(finger_signal))
frequency_component(high_pass_filtered_finger_signal,' high passed filterd_finger_signal')
sos = signal.cheby2(40,20, 4.8, 'lp', fs=10, output='sos')
filtered_cardiac_finger_signal = signal.sosfilt(sos, high_pass_filtered_cardiac_finger_signal) 
plt.figure()
frequency_component(filtered_cardiac_finger_signal,'band passed filterd_finger_signal')

'''



# save the filtered dat as a mat files so as to check the delay by mmatlab 
if save_mat==1:
    sio.savemat(os.path.join(main_path,sample_name,'filtered_belt_data.mat'),{'data':filtered_belt_signal})
    
    sio.savemat(os.path.join(main_path,sample_name,'filtered_finger_data.mat'),{'data':filtered_finger_signal})
    
    sio.savemat(os.path.join(main_path,sample_name,'filtered_mreg_resp_data.mat'),{'data':filtered_mreg_resp_signal})
"""
time_belt_signal=np.linspace(0,len(filtered_belt_signal)/10,len(filtered_belt_signal))
time_finger_signal=np.linspace(0,len(filtered_finger_signal)/10,len(filtered_finger_signal))
time_mreg_resp_signal=np.linspace(0,len(filtered_mreg_resp_signal)/10,len(filtered_mreg_resp_signal))
time_mreg_cardiac_signal=np.linspace(0,len(refernce_cardiac_voxel)/10,len(refernce_cardiac_voxel))


plt.figure()
plt.title('band passed filtered extracted resp and the  filtered belt signal')
plt.plot(time_finger_signal[0:1000],filtered_finger_signal[0:1000]*2,'c')
plt.plot(time_belt_signal[0:1000],filtered_belt_signal[0:1000],'r')
plt.legend(['band passed','belt signal'])


plt.figure()
starting_point=0
plotting_range=1000
plt.title('filtered finger signal and the  filtered extrated resp signal and belt signal')
plt.plot(time_finger_signal[starting_point:plotting_range],5*filtered_finger_signal[starting_point:plotting_range],label='band passed')
#plt.plot(time_extracted_resp[starting_point:plotting_range],5*filtered_extracted_resp[starting_point:plotting_range],label='ccf')
plt.plot(time_belt_signal[starting_point:plotting_range],filtered_belt_signal[starting_point:plotting_range],label='belt')
plt.legend()



plt.figure()
starting_point=0
ending_point=1000
plt.title('Band passed filtered mreg resp signal and band passed filtered belt data')
plt.plot(time_mreg_resp_signal[starting_point:ending_point],filtered_mreg_resp_signal[starting_point:ending_point],label='mreg_resp')
plt.plot(time_belt_signal[starting_point:ending_point],50*filtered_belt_signal[starting_point:ending_point],label='belt data')
plt.legend()



plt.figure()
starting_point=0
ending_point=1000
plt.title('Band passed filtered mreg resp signal and band passed filtered finger data')
plt.plot(time_mreg_resp_signal[starting_point:ending_point],filtered_mreg_resp_signal[starting_point:ending_point],label='mreg_resp')
plt.plot(time_finger_signal[starting_point:ending_point],50*filtered_finger_signal[starting_point:ending_point],label='belt data')
plt.legend()



# plotting the cardaiac signals with the filtered finger signal
plt.figure()
plt.title('The filtered cardiac mreg signal and filtered finger signal')
plt.plot(time_mreg_cardiac_signal[0:500],-1*refernce_cardiac_voxel[0:500],label='cardiac signal')
plt.plot(time_finger_signal[0:300],100*filtered_cardiac_finger_signal[0:300],label='finger signal')
plt.plot(time_mreg_cardiac_signal[0:300],refernce_full_inverted_cardiac_voxel[0:300],label='full inverted cardiac')
plt.legend()

#plt.plot(time_mreg_cardiac_signal[0:250],refernce_full_cardiac_voxel[0:250],label='full cardiac')
"""


time_belt_signal=np.linspace(0,len(filtered_belt_signal)/10,len(filtered_belt_signal))
time_mreg_resp_signal=np.linspace(0,len(filtered_mreg_resp_signal)/10,len(filtered_mreg_resp_signal))

plt.figure()
starting_point=0
ending_point=1000
plt.title('Band passed filtered mreg resp signal and band passed filtered belt data')
plt.plot(time_mreg_resp_signal[starting_point:ending_point],filtered_mreg_resp_signal[starting_point:ending_point],label='mreg_resp')
plt.plot(time_belt_signal[starting_point:ending_point],50*filtered_belt_signal[starting_point:ending_point],label='belt data')
plt.legend()


#corr_delay_calc(refernce_cardiac_voxel,filtered_cardiac_finger_signal,1,'full inverted cadriac and  band passed [0.7-4] filtered finger signal','cardiac','finger')

#corr_delay_calc(20*filtered_finger_signal,filtered_belt_signal,1,'belt signal and band passed filtered finger signal','finger','belt')

corr_delay_calc(filtered_mreg_resp_signal,filtered_belt_signal,1,'belt signal and band passed filtered mreg resp signal','mreg resp','belt')


"""
################################# trying to extract the RIIV from ppg signal

#### enelope detection method but it didnot work 
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import hilbert

fs=10
t=np.linspace(0,len(filtered_finger_signal)/10,len(filtered_finger_signal))
analytic_signal = hilbert(filtered_finger_signal)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = (np.diff(instantaneous_phase) /(2.0*np.pi) * fs)
fig = plt.figure()
ax0 = fig.add_subplot(211)
ax0.plot(t, filtered_finger_signal, label='signal')
ax0.plot(t, amplitude_envelope, label='envelope')
ax0.set_xlabel("time in seconds")
ax0.legend()
ax1 = fig.add_subplot(212)
ax1.plot(t[1:], instantaneous_frequency)
ax1.set_xlabel("time in seconds")
ax1.set_ylim(0.0, 120.0)


#### using trend decomposition 

from statsmodels.tsa.seasonal import seasonal_decompose
import numpy.fft as fft
series = filtered_finger_signal
freq= fft.fft(series)
result = seasonal_decompose(series, model='additive',freq=(freq.real).any())
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)
"""
