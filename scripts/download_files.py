import flywheel
import os
import glob

fw = flywheel.Client() # establish flywheel Client
# Define paths for impt variables
project = fw.lookup('huntington/Pilot_Study')
outdir = os.path.join("/home", "will", "Projects", "hd_motion_correction", "data2")
#freedir = os.path.join("/media", "will", "Data", "freesurfer_subjects")

# retrieve list of relevant analyses
vv = fw.get_analyses("projects", project.id ,"sessions")
recon_list = [fw.get(a.id) for a in vv if "recon-all" in a.label]

for a in recon_list:
    # get subject name for output folder
    sub = fw.get(a.parents.subject)
    print(sub.label)
    subdir = os.path.join(outdir, sub.label)
    os.makedirs(subdir, exist_ok=True)
    # construct file name from info in header
    try:
        sd = a.inputs[0].info['SeriesDescription']
        sn = a.inputs[0].info['SeriesNumber']
        name = sd +'_'+str(sn)
    except KeyError as e:
        print(e)
        print(sub.label)
        continue

    # skip if already downloaded
    # list = glob.glob(os.path.join(subdir,name+'.csv'))
    # print(list)
    # if len(list) > 0:
    #     print("Skipping {0}'s {1}".format(sub.label, name))
    #     continue
    # download files
    if len(a.files) > 0: # make sure the analysis has completed successfully
        # make a list with (hopefully) one entry--the file you want
        # can fill in any string for whatever file you want
        vol_stats_csv = [f for f in a.files if 'T1.nii.gz' in f.name]
        if len(vol_stats_csv) > 0:
            a.download_file(vol_stats_csv[0].name, \
            os.path.join(subdir, name+'_T1.nii.gz'))
            print("Downloading {0} as {1}".format(vol_stats_csv[0].name, name))
