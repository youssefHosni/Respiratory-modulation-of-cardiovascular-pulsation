from scipy import signal
def low_pass_filter(input_signal,w_c,filter_order):
    ##Butter worth filter 
    sos = signal.butter(filter_order, w_c, 'lp', fs=10, output='sos')
    filtered_signal = signal.sosfilt(sos, input_signal)     
    return filtered_signal

def high_pass_filter(input_signal,w_c,filter_order):
    ##Butter worth filter 
    sos = signal.butter(filter_order, w_c, 'hp', fs=10, output='sos')
    filtered_signal = signal.sosfilt(sos, input_signal)     
    return filtered_signal


def band_pass_filter(input_signal,lp_wc,hp_wc,filter_order):
    sos = signal.butter(filter_order, hp_wc, 'hp', fs=10, output='sos')
    high_pass_filtered_signal = signal.sosfilt(sos, input_signal)
    sos = signal.butter(filter_order, lp_wc, 'lp', fs=10, output='sos')
    band_pass_filtered_signal = signal.sosfilt(sos, high_pass_filtered_signal) 
    return band_pass_filtered_signal
