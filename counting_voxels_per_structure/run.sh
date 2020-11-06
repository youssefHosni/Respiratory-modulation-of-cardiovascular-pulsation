#!/bin/bash
# the input is the "main_path" which has the file you want to count the voxels in and "input_file" which is the file which you want to count the number of signicant voxels in

main_path= 
input_file=

cd /working_dir
bash main.sh -m $main_path -i $input_file 
