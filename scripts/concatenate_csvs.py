#
# For concatenating the {sub}_aseg_stats_vol_mm3.csv files that
# Freesurfer produces.

import pandas as pd
import numpy as np
import os

data_dir = "/home/will/Projects/RMS/data"
df_list = []

# Loop through csvs in directory
for subdir, dirs, files in os.walk(data_dir):
    onlycsvs = [f for f in files if f.endswith(".csv")]
    for csv in onlycsvs:
        mode = csv.split("_")[4] # determine whether it's active/passive from filename
        no = csv.split("_")[6].split(".")[0] # determine series number from filename
        df = pd.read_csv(os.path.join(subdir, csv)) # read the csv into dataframe
        df.insert(1, "Mode", mode +'_'+no) # insert a column specifying Mode
        df_list.append(df)


# concatenate the list of subject-wise dataframes into one large dataframe and save as csv
master_df = pd.concat(df_list, ignore_index=True)
#master_df.set_index('Measure:volume', drop=True, inplace=True) # change index to subject IDs
master_df.to_csv(os.path.join(data_dir, '..', 'volumes.csv'))
