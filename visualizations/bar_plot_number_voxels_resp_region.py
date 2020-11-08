# Data visualization 
import numpy as np
import matplotlib.pyplot as plt

def bar_plot(resp_regions,signifacant_voxels,x_label,y_label,saving_path):
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.bar(resp_regions,signifacant_voxels)
    plt.savefig(saving_path)
    
    return 


x=   ["insp_1","insp_2","ins_3","exp_1","exp_2","exp_3"] 

signifacant_voxels=np.array([193,7394,11,4241,0,4715])

x_label="The respiratory regions"
y_label="Number of significant voxels"    
saving_path="/data/fmri/Youssef/Presentations and meeting reports/mean_cardiac_rate/siginficant_voxels_bar_plot.png"
bar_plot(x,signifacant_voxels,x_label,y_label,saving_path)
    
