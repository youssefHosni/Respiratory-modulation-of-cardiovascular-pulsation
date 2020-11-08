import numpy as np
import nibabel as nib


def save_numeric_data(data_path,data):
    np.save(data_path,data)
    return 

def save_nifity_data(data_path,data,data_affine,data_header):
    nifity_img = nib.Nifti1Image(data,data_affine, data_header)
    nib.save (nifity_img,data_path)
    return
