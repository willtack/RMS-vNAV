#!/bin/bash
dataDir='/home/will/Projects/hd_motion_correction/first2/first_data'
files=$(find ${dataDir} -type f | grep _t1.nii.gz)

for f in ${files}; do
   outname=$(basename $f .nii.gz | cut -d '_' -f 1,2)
   echo $outname
   run_first_all -i $f -o ${outname} -s L_Accu,L_Amyg,L_Hipp,L_Pall,L_Puta,L_Thal,R_Accu,R_Amyg,R_Caud,R_Hipp,R_Pall,R_Puta,R_Thal;
done
