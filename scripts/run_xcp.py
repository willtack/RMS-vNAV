import flywheel

fw = flywheel.Client()

project = fw.lookup('huntington/Pilot_Study')
gear = fw.lookup('gears/xcpenginestruc-fw')
design_file = project.get_file('anat-minimal.dsn')


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
            elif '.nii.gz' in file.name and 'mean_square' not in file.name and 'sum_square' not in file.name and 'sqr' not in file.name:
                t1 = file
                print("T1: " + t1.name)
        # if t1:
        #     print(t1.info)
        if t1 is not None and t1.info and t1.info['SeriesNumber'] == 9:
            print('Running analysis for {}'.format(sublabel))
            inputs = {'img': t1, 'designfile': design_file}
            config = {'analysis_type': 'struc'}
            analysis_id = gear.run(analysis_label='xcp-anat_2020-08-04_WT', config=config, inputs=inputs, destination=ses)
            print(analysis_id)
