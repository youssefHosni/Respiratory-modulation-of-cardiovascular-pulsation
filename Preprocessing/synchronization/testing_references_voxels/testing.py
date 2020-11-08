import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
from max_min_resp_rate import segmeantation_and_BR
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0,'/data/fmri/Youssef/codes/algorithms ')
from find_the_delay.delay_finding import corr_delay_calc


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


def testing_ref_voxel (signal1,signal2,title,label1,label2):
    
    
    min_br,max_br=segmeantation_and_BR(signal1)
    hp_fc=min_br/60
    lp_fc=max_br/60
    sos = signal.butter(6, hp_fc, 'hp', fs=10, output='sos')
    high_pass_filtered_signal1 = signal.sosfilt(sos, np.squeeze(signal1))
    sos = signal.butter(6, lp_fc, 'lp', fs=10, output='sos')
    filtered_signal1 = signal.sosfilt(sos,high_pass_filtered_signal1)
    plt.figure()
    
    sos = signal.butter(6, hp_fc, 'hp', fs=10, output='sos')
    high_pass_filtered_signal2 = signal.sosfilt(sos, signal2)
    plt.figure()
    sos = signal.butter(6, lp_fc, 'lp', fs=10, output='sos')
    filtered_mreg_resp_signal = signal.sosfilt(sos,high_pass_filtered_signal2)
    
    corr_delay_calc(filtered_mreg_resp_signal,filtered_signal1,1,title,label1,label2)
    
    
