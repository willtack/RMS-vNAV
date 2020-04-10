#!/bin/bash
#
# Convert mgz to nii
#
#

dataDir='/home/will/Projects/RMS/data'
mniDir='/home/will/Projects/RMS/mni'

for subdir in ${dataDir}/*; do
  for seg in ${subdir}/*_aseg.mgz; do
    fname=$(basename ${seg} | cut -d '.' -f 1)
    # convert the mgz file into .nii
    mri_convert --in_type mgz --out_type nii --out_orientation RAS \
                ${subdir}/${fname}.mgz ${subdir}/${fname}.nii
  done
done
