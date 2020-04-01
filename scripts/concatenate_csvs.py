import pandas as pd
import numpy as np
import os

data_dir = "/home/will/Projects/RMS/data"
df_list = []

# Loop through csvs in directory
for subdir, dirs, files in os.walk(data_dir):
    onlycsvs = [f for f in files if f.endswith(".csv")]
    for csv in onlycsvs:
        mode = csv.split("_")[4]
        no = csv.split("_")[6].split(".")[0]
        df = pd.read_csv(os.path.join(subdir, csv))
        df.insert(1, "Mode", mode +'_'+no)
        df_list.append(df)


master_df = pd.concat(df_list, ignore_index=True)
#master_df.set_index('Measure:volume', drop=True, inplace=True) # change index to subject IDs
master_df.to_csv(os.path.join(data_dir, '..', 'volumes.csv'))
