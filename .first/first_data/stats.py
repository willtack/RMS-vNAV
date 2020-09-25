#
#
#
import glob
import os
import subprocess
import pandas as pd

data_dir='/home/will/Projects/hd_motion_correction/first/first_data'
images=os.path.join(data_dir, '*_all_none_firstseg.nii.gz' )
ints = [10, 12, 13, 17, 18, 26, 49, 50, 51, 52, 53, 54, 58]
rois = ["image name", "L_Thal","L_Puta","L_Pall","L_Hippo","L_Amyg","L_Accu","R_Thal","R_Caud","R_Puta","R_Pall","R_Hippo","R_Amyg","R_Accum"]

# initialize dictionary
columns = ['image name'] + ints
dict = {i : [] for i in columns}
print(dict)

image_names = []
for filepath in glob.glob(images):
    filename = os.path.basename(filepath)
    split = filename.split('_')
    parts = ((split[1], split[0], split[2], split[3], split[4]))
    newname = "_".join(parts)
    print(newname)
    image_names.append(newname)
dict['image name'] = image_names

for int in ints:
    print('')
    print(int)
    volumes_by_roi = []
    lower = int-0.5
    upper = int+0.5
    for filepath in glob.glob(images):
        print(filepath)
        cmd='fslstats {0} -l {1} -u {2} -V'.format(filepath, lower, upper)
        results = subprocess.check_output(cmd, shell=True)
        results_decode=results.decode("utf-8")
        volume = results_decode.split(' ')[0]
        print(volume)
        volumes_by_roi.append(volume)
    dict[int] = volumes_by_roi

print(dict)

df = pd.DataFrame(data=dict)
df.columns = rois
df.to_csv('../first_volumes.csv', index=False)
