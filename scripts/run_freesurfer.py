import flywheel

fw = flywheel.Client()

project = fw.lookup('huntington/Pilot_Study')
gear = fw.lookup('gears/freesurfer-recon-all')
license_string = 'william.tackett@pennmedicine.upenn.edu\
                39492\
                *Cze83ZRK81rI\
                FSB/TAmun94lg'

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
        print(acq.label)
        container = fw.get(acq.id)
        for file in container.files:
            if '.nii.gz' in file.name:
                t1 = file
                print(t1.name)
        if t1 is not None:
            print('Running analysis for {}'.format(sublabel))
            inputs = {'anatomical': t1}
            config = {'freesurfer_license': license_string, 'subject_id': shortlabel}
            analysis_id = gear.run(analysis_label='recon-all_2020-03-26_WT', config=config, inputs=inputs, destination=ses)
            print(analysis_id)
