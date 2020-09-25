import flywheel

fw = flywheel.Client()

project = fw.lookup('huntington/Pilot_Study')
gear = fw.lookup('gears/fmriprep-fwheudiconv/0.3.4_20.0.7')
license_file = project.get_file('freesurfer_license.txt')


for ses in project.sessions():
    sublabel = fw.get(ses.parents['subject']).label
    if sublabel == 'gonzalez_alegre_pilot_16':
            continue
    if "test" in sublabel:
        shortlabel = 'pilot_' + sublabel[-4:]
    else:
        shortlabel = 'pilot_' + sublabel[-2:]
    acq_list = [ acq for acq in ses.acquisitions() if "RMS" in acq.label]
    print(len(acq_list))
    for acq in acq_list:
        print("acq: " + acq.label)
        container = fw.get(acq.id)
        t1 = None
        for file in container.files:
            if "rms_series" in file.name:
                t1 = file
                print("T1: " + t1.name)
            elif '.nii.gz' in file.name:
                t1 = file
                print("T1: " + t1.name)
        if t1 is not None:
            print('Running analysis for {}'.format(sublabel))
            inputs = {'t1w_anatomy': t1, 'freesurfer_license': license_file}
            config = {"anat_only":True, "skip_bids_validation":True, "output_spaces": "MNI152NLin2009cAsym anat", "skip_bids_validation": False,  "fs_no_reconall": True}
            #analysis_id = gear.run(analysis_label='fprep-anat_2020-08-04_WT', config=config, inputs=inputs, destination=ses)
            #print(analysis_id)
