#
#
#
import glob
import os
import subprocess
import pandas as pd

data_dir='/home/will/Projects/hd_motion_correction/first/first_data'
images=os.path.join(data_dir, '*_all_none_firstseg.nii.gz' )
ints = [10,12]
# ints = [10, 12, 13, 17, 18, 26, 49, 50, 51, 52, 53, 54, 58]
rois = ["L_Accu","L_Amyg","L_Hipp","L_Pall","L_Puta","L_Thal","R_Accu","R_Amyg","R_Caud","R_Hipp","R_Pall","R_Puta","R_Thal"]

# initialize dictionary
columns = ['image name'] + ints
dict = {i : [] for i in columns}
print(dict)

image_names = []
for filepath in glob.glob(images):
    filename=os.path.basename(filepath)
    print(filename)
    image_names.append(filename)
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
df.to_csv('../first_volumes3.csv', index=False)
