import nipype.algorithms.metrics as metrics
import numpy as np
import pandas as pd
import os

data_dir = os.path.join('/','home','will','Projects','RMS','data')
data_dict = {'subject': [], 'mode': [], 'dice': [], 'jaccard': []}

for subdir, dirs, files in os.walk(data_dir):
    passive_list = [f for f in files if "passive" in f and 'nii' in f]
    active_list = [f for f in files if "active" in f and 'nii' in f]
    subject = subdir.split('/')[-1]

    for list in passive_list, active_list:
        if len(list) > 1:
            mode = list[0].split("_")[4]
            vol1 = os.path.join(subdir, list[0])
            vol2 = os.path.join(subdir, list[1])
            overlap = metrics.Overlap(volume1=vol1,volume2=vol2,vol_units='mm')
            res=overlap.run()
            dice = res.outputs.dice
            jaccard = res.outputs.jaccard

            data_dict['subject'].append(subject)
            data_dict['mode'].append(mode)
            data_dict['dice'].append(dice)
            data_dict['jaccard'].append(jaccard)


print(data_dict)

df = pd.DataFrame(data=data_dict)
csv_file = df.to_csv(os.path.join(data_dir,'dice.csv'), index_label='subject')
