import flywheel
import os

fw = flywheel.Client()
project = fw.lookup('huntington/Pilot_Study')
outdir = os.path.join("/home", "will", "Projects", "RMS", "data")
freedir = os.path.join("/media", "will", "Data", "freesurfer_subjects")
vv = fw.get_analyses("projects", project.id ,"sessions")
recon_list = [fw.get(a.id) for a in vv if "recon-all" in a.label]

for a in recon_list:
    # construct file name from info in header
    sd = a.inputs[0].info['SeriesDescription']
    sn = a.inputs[0].info['SeriesNumber']
    name = sd +'_'+str(sn)
    # get subject name for output folder
    sub = fw.get(a.parents.subject)
    subdir = os.path.join(outdir, sub.label)
    os.makedirs(subdir, exist_ok=True)
    # download files
    if len(a.files) > 0:
        vol_stats_csv = [f for f in a.files if '.zip' in f.name]
        if len(vol_stats_csv) > 0:
            a.download_file(vol_stats_csv[0].name, \
            os.path.join(subdir, vol_stats_csv[0].name))
            print("Downloading " + vol_stats_csv[0].name)
