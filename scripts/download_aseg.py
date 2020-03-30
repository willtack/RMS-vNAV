import flywheel
import os

fw = flywheel.Client()
project = fw.lookup('huntington/Pilot_Study')
outdir = os.path.join("/home", "will", "Projects", "RMS", "data")
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
    shortlabel = 'pilot_' + sub.label[-2:]
    # download files
    if len(a.files) > 0:
        zip_folder = [f for f in a.files if '.zip' in f.name]
        if len(zip_folder) > 0:
            a.download_file_zip_member(zip_folder[0].name, \
            shortlabel+'/mri/aseg.mgz', os.path.join(subdir, name+'_aseg.mgz'))
            print("Downloading " + shortlabel + "'s " + name + '_aseg.mgz')
