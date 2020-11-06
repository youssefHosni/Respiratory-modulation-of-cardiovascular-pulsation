The codes here are used to obtain the number of voxels that fill in each cortical and subcortical structure for each of the  two hemispheres the left and the right.

First the file create_4mm_structure.sh is used to obtain the cortical and subcortical structure and convert them from 1mm to 4mm and save them, this file is important if 
your  data is in 4mm else, you should ignore it. 

To run the codes you should use the file run.sh and give it the input file and the path of this file and change the path of the cortical and subcortical structures storing file from the restof the code.

The output will be for text files for each input file, which are the following the number of left side voxels per cortical structure, per sub cortcal structure, and the same for the right side voxels.

