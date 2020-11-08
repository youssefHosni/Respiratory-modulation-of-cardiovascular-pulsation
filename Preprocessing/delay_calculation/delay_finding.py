from scipy import signal
import numpy as np
from scipy.stats import spearmanr
import matplotlib.pyplot as plt


def find_delay(resp_MREG_data,MREG_data,belt_data):
    
    corr_map_belt_resp=np.empty(np.shape(resp_MREG_data)[0:3]) 
    corr_map_belt_MREG=np.empty(np.shape(MREG_data)[0:3]) 
    delay_map_belt_resp=np.empty(np.shape(resp_MREG_data)[0:3])
    delay_map_belt_MREG=np.empty(np.shape(MREG_data)[0:3])
    
    
    for i in range(np.shape(resp_MREG_data)[0]):
        for j in range(np.shape(resp_MREG_data)[1]):
            for k in range(np.shape(resp_MREG_data)[2]):
                corr_map_belt_resp[i,j,k]=max(signal.correlate(belt_data,resp_MREG_data[i,j,k,0:len(belt_data)],method='auto',mode='same'))
                corr_map_belt_MREG[i,j,k]=max(signal.correlate(belt_data,MREG_data[i,j,k,0:len(belt_data)],method='auto',mode='same'))
                delay_map_belt_resp[i,j,k]=np.argmax(signal.correlate(belt_data,resp_MREG_data[i,j,k,0:len(belt_data)],method='auto',mode='same'))
                delay_map_belt_MREG[i,j,k]=np.argmax(signal.correlate(belt_data,MREG_data[i,j,k,0:len(belt_data)],method='auto',mode='same'))
                
    return corr_map_belt_MREG,corr_map_belt_resp,delay_map_belt_MREG,delay_map_belt_resp





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
        print(y1.shape)
        print(y2.shape)
        delay=lag_finder(y1,y2,sr)
        corrected_signal=fraction_time_shifting(np.squeeze(y2),delay)
        
        
        
        plt.figure()
        plt.title(plot_title)
        plt.plot(time,y1,label=label1)
        plt.plot(time,(max(y1)/max(corrected_signal))*corrected_signal,label=label2)
        plt.legend()
        cala_corr,_=spearmanr(y1,corrected_signal)
        #print('The correlation between ' + label1 + ' and ' + label2 + 'is : %f ' % calc_corr)
        
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
        delay=lag_finder(y1,y2,sr)
        corrected_signal=fraction_time_shifting(np.squeeze(y2),delay)
        
        plt.figure()
        plt.title(plot_title)
        plt.plot(time,y1,label=label1)
        plt.plot(time,(max(y1)/max(corrected_signal))*corrected_signal,label=label2)
        plt.legend()
        cala_corr,_=spearmanr(y1,corrected_signal)
        #print('The correlation between ' + label1 + ' and  the shifted ' + label2 + 'is : %f ' % calc_corr)
            
        
        


def lag_finder(y1, y2, sr):
    n = len(y1)
    corr = signal.correlate(y1, y2, mode='same') / np.sqrt(signal.correlate(y1, y1, mode='same')[int(n/2)] * signal.correlate(y2, y2, mode='same')[int(n/2)])
    delay_arr = np.linspace(-0.5*n/sr, 0.5*n/sr, n)
    
    
    delay = delay_arr[np.argmax(corr)]
    
    return delay

def fraction_time_shifting(signal,delay):
    
    fs=10
    print_delay=0
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
    if print_delay==1:
        print("The time delay is %f seconds" % delay)
        print("The time delay in samples is %f samples" % tDelayInSamples)
        print("The correction phase shift is %f pi" % (tDelayInSamples))

   
    return shifted_signal
