#!/bin/bash

thisfolder=$(pwd)
sub=passive9
template=~/Gears/lingua-map/masks/mni152.nii.gz
t1brain=tmp19815/tmpBrainExtractionBrain.nii.gz 


antsRegistration --dimensionality 3 --float 0 \
	--output [$thisfolder/${sub}_to_mni_,$thisfolder/${sub}_Warped.nii.gz] \
	--interpolation Linear \
	--winsorize-image-intensities [0.005,0.995] \
	 --use-histogram-matching 0 \
	--initial-moving-transform [$template,$t1brain,1] \
        --transform Rigid[0.1]  \
	--metric MI[$template,$t1brain,1,32,Regular,0.25] \
	--convergence [1000x500x250x100,1e-6,10] \
	--shrink-factors 8x4x2x1 \
	--smoothing-sigmas 3x2x1x0vox\
	 --transform Affine[0.1] \
	--metric MI[$template,$t1brain,1,32,Regular,0.25] \
	--convergence [1000x500x250x100,1e-6,10] \
	 --shrink-factors 8x4x2x1 \
	--smoothing-sigmas 3x2x1x0vox \
	--transform SyN[0.1,3,0] \
	--metric CC[$template,$t1brain,1,4] \
	--convergence [100x70x50x20,1e-6,10] \
	--shrink-factors 8x4x2x1 \
	--smoothing-sigmas 3x2x1x0vox


