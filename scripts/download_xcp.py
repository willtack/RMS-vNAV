import flywheel
import os
import glob

fw = flywheel.Client() # establish flywheel Client
# Define paths for impt variables
project = fw.lookup('huntington/Pilot_Study')
outdir = os.path.join("/home", "will", "Projects", "hd_motion_correction", "data3")
#freedir = os.path.join("/media", "will", "Data", "freesurfer_subjects")

# retrieve list of relevant analyses
vv = fw.get_analyses("projects", project.id ,"sessions")
recon_list = [fw.get(a.id) for a in vv if "xcp-anat_2020-08-12" in a.label]

for a in recon_list:
    # get subject name for output folder
    sub = fw.get(a.parents.subject)
    print(sub.label)
    subdir = os.path.join(outdir, sub.label)
    os.makedirs(subdir, exist_ok=True)
    for inp in a.inputs:
    # construct file name from info in header
        print(inp.name)
        if '.nii.gz' in inp.name:
            try:
                sd = inp.info['SeriesDescription']
                sn = inp.info['SeriesNumber']
                name = sd +'_'+str(sn)
            except KeyError as e:
                print(e)
                print(sub.label)
                continue
    name = sd +'_'+str(sn)
    # download files
    if len(a.files) > 0: # make sure the analysis has completed successfully
        # make a list with (hopefully) one entry--the file you want
        # can fill in any string for whatever file you want
        zip_folder = [f for f in a.files if '.zip' in f.name]
        # print(zip_folder)
        if len(zip_folder) > 0:
            zip_info = a.get_file_zip_info(zip_folder[0].name)
            print(zip_info)
            try:
                print(name)
                a.download_file_zip_member(zip_folder[0].name, \
                'structural/sub-struct/struc/sub-struct_BrainNormalizedToTemplate.nii.gz', \
                os.path.join(subdir, name+'_T1inMNI.nii.gz'))
                print("Downloading T1 from " + sub.label)
            except Exception as e:
                print(e)
                print(sub.label)
                continue
