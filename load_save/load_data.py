import scipy.io
import numpy as np
import nibabel as nib


def load_npydata(data_path):
    return np.load(data_path)

def load_matdata(data_path,data_type):

    dummy_signal= scipy.io.loadmat(data_path)
    if data_type=='resampled':
        dummy_signal=dummy_signal['z']
    elif data_type=='original':
        dummy_signal=dummy_signal['y']
    dummy_signal=dummy_signal.astype(np.float64)  
    dummy_signal=(dummy_signal-np.mean(dummy_signal))/np.std(dummy_signal)
    return dummy_signal

def load_niftiydata(data_path):
    data=nib.load(data_path)
    data_affine=data.affine
    data_header=data.header
    data=data.get_data() 
    return data, data_affine, data_header
