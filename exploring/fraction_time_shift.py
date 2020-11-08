import numpy as np
import matplotlib.pyplot as plt

f1 = 1.8
f2 = 2.6
#try tDelay = .02002 and tDelay = .0205
tDelay = .0205 #seconds
samples = 1024 #number of samples in the time interval
tstart = 0.0
tend = 1.0

# create a waveform to use for the time shifting
samplePeriod = (tend - tstart) / (samples)
print("\nThe sampling period is %f seconds" % samplePeriod)
print("The time delay is %f seconds" % tDelay)
tDelayInSamples = tDelay / samplePeriod
print("The time delay in samples is %f samples" % tDelayInSamples)
timeList = np.linspace(tstart, tend, samples)
waveform = np.sin(2 * np.pi * f1 * timeList) + np.sin(2 * np.pi * f2 * timeList)

# do the time shifting

fftOut = np.fft.fft(waveform)
N = fftOut.shape[0]
k = np.linspace(0, N-1, N)
phaseShiftFunction = np.exp((-2*np.pi*1j*k*tDelayInSamples)/(N))
fftWithDelay = np.multiply(fftOut, phaseShiftFunction)
waveform2 = np.fft.ifft(fftWithDelay)

plots = 1
plt.subplot(plots, 1, 1)
plt.plot(waveform)
plt.plot(waveform2)
plt.show()
