#!/bin/bash
#
# Move T1s from data/justT1s/ to first/ so all the files are at the same level

T1dir="/home/will/Projects/hd_motion_correction/data/justT1s"
firstDir="/home/will/Projects/hd_motion_correction/first2/first_data"
newNameDir="/home/will/Projects/hd_motion_correction/justT1s/newNames"
files=$(find ${T1dir} -type f | grep .nii.gz)

for f in ${files}; do
  #rename
  subno=$(echo $f | cut -d '/' -f 8 | cut -d '_' -f 4)
  type=$(echo $f | cut -d '/' -f 9 | cut -d '_' -f 5)
  acq=$(echo $f | cut -d '/' -f 9 | cut -d '_' -f 7)
  type=${type::-3}
  filename="${type}${acq}_${subno}_t1"
  dirname=$(dirname $f)
  newfile="$dirname/$filename.nii.gz"
  cp $f $newfile
  cp $newfile ${firstDir}/
  rm $newfile
done
