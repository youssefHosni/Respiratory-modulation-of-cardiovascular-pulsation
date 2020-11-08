from numpy.random import randn
from numpy.random import seed
from numpy import cov
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from scipy.stats import shapiro


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
        delay = delay_arr[np.argmin(corr)]
   
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

# seed random number generator
seed(1)
# prepare data
time=np.linspace(0,10,1000)
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)
# calculate covariance matrix
covariance = cov(data1, data2)
print(covariance)

corr, _ = pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr)

data1=data1[:,np.newaxis]
data2=data2[:,np.newaxis]
delay,corr,spearman_corr=lag_finder(data1,data2,10)


#############################################################################3

plt.plot(time,data1,'c')
plt.plot(time,data2,'r')


data2_shifted=np.vstack((data2[100:len(data2),:],np.zeros((100,1))))
delay,corr,calc_corr=lag_finder(data1,data2_shifted,10)


plt.plot(time,data1,'c')
plt.plot(time,data2_shifted,'r')


corrected_data2=fraction_shifting(np.squeeze(data2),delay)

plt.figure()
plt.plot(time,data1,'c')
plt.plot(time,corrected_data2,'r')
