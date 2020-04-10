#
# Calculate Dice coefficients for pairs of within session scans
# and consolidate data into a couple csvs

import nipype.algorithms.metrics as metrics
import numpy as np
import pandas as pd
import os

labels = [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 24, 26, 28, 30, 31, 41, 42, 43, 44, 46, 47, 49, 50, 51, 52, 53, 54, 58, 60, 62, 63, 77, 85, 251, 252, 253, 254, 255]

data_dir = os.path.join('/','home','will','Projects','RMS','data')
# initialize dictionary that will make it easy to visualize avg dice, etc. by subject
data_dict = {'subject': [], 'mode': [], 'dice': [], 'jaccard': []}
rois_dict = {'labels': labels} # for visualizing data by ROI
roi_df = pd.DataFrame(data=rois_dict)

for subdir, dirs, files in os.walk(data_dir):
    # get lists of the passive and active segmentation files for this subject
    passive_list = [f for f in files if "passive" in f and 'aseg.nii' in f]
    active_list = [f for f in files if "active" in f and 'aseg.nii' in f]
    subject = subdir.split('/')[-1] # subject name is the last element in the path
    print(subject)
    for list in passive_list, active_list:
        if len(list) > 1: # make sure list isn't empty
            # determine the mode and the two relevant images
            mode = list[0].split("_")[4]
            vol1 = os.path.join(subdir, list[0])
            vol2 = os.path.join(subdir, list[1])
            # Run Overlap analysis and store outputs
            overlap = metrics.Overlap(volume1=vol1,volume2=vol2,vol_units='mm')
            res=overlap.run()
            dice = res.outputs.dice
            jaccard = res.outputs.jaccard
            roi_di = res.outputs.roi_di
            # append outputs to first dictionary
            data_dict['subject'].append(subject)
            data_dict['mode'].append(mode)
            data_dict['dice'].append(dice)
            data_dict['jaccard'].append(jaccard)
            # append the list of DF
            if len(roi_di) == 43: # should be 43 regions. dims need to be = for concatenation
                roi_df[subject+'_'+ mode] = roi_di

# create dataframe from first dict and save both dfs to csvs
print(data_dict)
df = pd.DataFrame(data=data_dict)
csv_file = df.to_csv(os.path.join(data_dir, '..', 'dice', 'dice3.csv'), index=False)
csv_file2 = roi_df.to_csv(os.path.join(data_dir, '..', 'rois', 'rois3.csv'))
