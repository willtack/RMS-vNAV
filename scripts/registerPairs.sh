#!/bin/bash
#
# Use mri_label2vol to transform labels into MNI space
#
#

dataDir='/home/will/Projects/RMS/data'
mniDir='/home/will/Projects/RMS/mni'

for subdir in ${dataDir}/*; do
  for seg in ${subdir}/*_aseg.mgz; do
    #mode=$(echo $seg | cut -d '_' -f 8)
    fname=$(basename ${seg} | cut -d '.' -f 1)
    # t1name=$(echo $fname | cut -d '_' -f 1-7)

    # use freesurfer space to mni transform to normalize aseg label image
    mri_label2vol --seg ${seg} --reg ${mniDir}/mni152.register.dat \
                  --temp ${mniDir}/mni152.nii.gz \
                  --o ${subdir}/${fname}.mni152.mgz
    # convert the mgz file into .nii
    mri_convert --in_type mgz --out_type nii --out_orientation RAS \
                ${subdir}/${fname}.mni152.mgz ${subdir}/${fname}.mni152.nii
  done
done
