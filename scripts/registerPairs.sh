#!/bin/bash
#
# Make template from each pair of T1s (active/passive) for each subject.
# Then mrilabel2vol each segmentation to that template.
#

dataDir='/home/will/Projects/RMS/data'

label2vol(){
  subdir=$1
  for seg in ${subdir}/*_aseg.mgz; do
    mode=$(echo $seg | cut -d '_' -f 8)
    fname=$(basename ${seg} | cut -d '.' -f 1)
    t1name=$(echo $fname | cut -d '_' -f 1-7)
    tkregister2 --mov  ${subdir}/${t1name}_T1.nii.gz --targ ${subdir}/${mode}_temp.nii.gz \
                --reg ${subdir}/${t1name}_register.dat --noedit --regheader
    mri_label2vol --seg ${seg} --reg ${subdir}/${t1name}_register.dat \
                  --temp ${subdir}/${mode}_temp.nii.gz \
                  --o ${subdir}/${fname}_tempspace.mgz
    mri_convert --in_type mgz --out_type nii --out_orientation RAS \
                ${subdir}/${fname}_tempspace.mgz ${subdir}/${fname}_tempspace.nii
  done
}

for subdir in ${dataDir}/gonzalez_alegre_pilot_05; do
  # there a couple subjects who don't have all four scans; just do the passive pair
  # which both do have. slightly different series numbers too.
  if [ -f ${subdir}/ABCD_T1w_MPR_vNav_passive_RMS_21_T1.nii.gz ]; then
      mri_robust_template --mov ${subdir}/ABCD_T1w_MPR_vNav_passive_RMS_21_T1.nii.gz \
                                ${subdir}/ABCD_T1w_MPR_vNav_passive_RMS_9_T1.nii.gz \
                          --template ${subdir}/passive_temp.nii.gz \
                          --satit
      mri_robust_template --mov ${subdir}/ABCD_T1w_MPR_vNav_active_RMS_24_T1.nii.gz \
                                ${subdir}/ABCD_T1w_MPR_vNav_active_RMS_12_T1.nii.gz \
                          --template ${subdir}/active_temp.nii.gz \
                          --satit

      label2vol $subdir
  else
      mri_robust_template --mov ${subdir}/ABCD_T1w_MPR_vNav_passive_RMS_21_T1.nii.gz \
                              ${subdir}/ABCD_T1w_MPR_vNav_passive_RMS_9_T1.nii.gz \
                          --template ${subdir}/passive_temp.nii.gz \
                          --satit
      label2vol $subdir
   fi
done
