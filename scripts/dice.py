import nipype.algorithms.metrics as metrics
import numpy as np
import pandas as pd
import os

labels = [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 24, 26, 28, 30, 31, 41, 42, 43, 44, 46, 47, 49, 50, 51, 52, 53, 54, 58, 60, 62, 63, 77, 85, 251, 252, 253, 254, 255]

data_dir = os.path.join('/','home','will','Projects','RMS','data')
data_dict = {'subject': [], 'mode': [], 'dice': [], 'jaccard': []}
rois_dict = {'labels': labels}
roi_df = pd.DataFrame(data=rois_dict)

for subdir, dirs, files in os.walk(data_dir):
    passive_list = [f for f in files if "passive" in f and 'mni152.nii' in f]
    active_list = [f for f in files if "active" in f and 'mni152.nii' in f]
    subject = subdir.split('/')[-1]
    print(subject)
    for list in passive_list, active_list:
        if len(list) > 1:
            mode = list[0].split("_")[4]
            vol1 = os.path.join(subdir, list[0])
            vol2 = os.path.join(subdir, list[1])
            overlap = metrics.Overlap(volume1=vol1,volume2=vol2,vol_units='mm')
            res=overlap.run()
            dice = res.outputs.dice
            jaccard = res.outputs.jaccard
            roi_di = res.outputs.roi_di
            data_dict['subject'].append(subject)
            data_dict['mode'].append(mode)
            data_dict['dice'].append(dice)
            data_dict['jaccard'].append(jaccard)
            if len(roi_di) == 43:
                roi_df[subject] = roi_di

print(data_dict)
df = pd.DataFrame(data=data_dict)
csv_file = df.to_csv(os.path.join(data_dir, '..', 'dice2.csv'))
csv_file2 = roi_df.to_csv(os.path.join(data_dir, '..', 'rois.csv'))
