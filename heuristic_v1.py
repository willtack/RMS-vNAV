import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

# structurals
t1_passive_1 = create_key(
    'sub-{subject}/ses-{session}/anat/sub-{subject}_{session}_acq-passive_run-01_T1w')
t1_passive_2 = create_key(
    'sub-{subject}/ses-{session}/anat/sub-{subject}_{session}_acq-passive_run-02_T1w')
t1_passiveRMS_1 = create_key(
    'sub-{subject}/ses-{session}/anat/sub-{subject}_{session}_acq-passiveRMS_run-01_T1w')
t1_passiveRMS_2 = create_key(
    'sub-{subject}/ses-{session}/anat/sub-{subject}_{session}_acq-passiveRMS_run-02_T1w')
t1_active_1 = create_key(
    'sub-{subject}/ses-{session}/anat/sub-{subject}_{session}_acq-active_run-01_T1w')
t1_active_2 = create_key(
    'sub-{subject}/ses-{session}/anat/sub-{subject}_{session}_acq-active_run-02_T1w')
t1_activeRMS_1 = create_key(
    'sub-{subject}/ses-{session}/anat/sub-{subject}_{session}_acq-activeRMS_run-01_T1w')
t1_activeRMS_2 = create_key(
    'sub-{subject}/ses-{session}/anat/sub-{subject}_{session}_acq-activeRMS_run-02_T1w')

# ASL scans
asl = create_key(
     'sub-{subject}/ses-{session}/perf/sub-{subject}_{session}_asl')
m0 = create_key(
    'sub-{subject}/ses-{session}/perf/sub-{subject}_{session}_m0scan')
mean_perf = create_key(
    'sub-{subject}/ses-{session}/perf/sub-{subject}_{session}_mean-perfusion')

def infotodict(seqinfo):

    last_run = len(seqinfo)

    info = {t1_passive_1:[], t1_passive_2:[], t1_passiveRMS_1:[], t1_passiveRMS_2:[],
            t1_active_1:[], t1_active_2:[], t1_activeRMS_1:[], t1_activeRMS_2:[],
            asl:[], m0:[], mean_perf:[]}

    # This function accomodates both runs
    def get_both_series(key1, key2, s):
         if len(info[key1]) == 0:
             info[key1].append(s.series_id)
         else:
             info[key2].append(s.series_id)

    # this doesn't need to be a function but using it anyway for aesthetic symmetry
    # with above function
    def get_series(key, s):
            info[key].append(s.series_id)

    for s in seqinfo:
        protocol = s.protocol_name.lower()
        if "passive" in protocol:
            if "rms" not in protocol:
                get_both_series(t1_passive_1, t1_passive_2, s)
            else:
                get_both_series(t1_passiveRMS_1, t1_passiveRMS_2, s)
        elif "active" in protocol:
            if "rms" not in protocol:
                get_both_series(t1_active_1, t1_active_2, s)
            else:
                get_both_series(t1_activeRMS_1, t1_activeRMS_2, s)
        elif "pcasl" in protocol:
            if s.series_description.endswith("_ASL"):
                get_series(asl,s)
            elif s.series_description.endswith("_M0"):
                get_series(m0,s)
            elif s.series_description.endswith("_MeanPerf"):
                get_series(mean_perf,s)

    return info


def AttachToSession():

    NUM_VOLUMES=70
    data = ['label', 'control'] * NUM_VOLUMES
    data = '\n'.join(data)
    data = 'volume_type\n' + data # the data is now a string

    asl_context = {
      'name': 'sub-{subject}/{session}/perf/sub-{subject}_{session}_aslcontext.tsv',
      'data': data,
      'type': 'text/tab-separated-values'
    }

    return asl_context


MetadataExtras = {
   asl: {
   "PulseSequenceType": "3D_SPIRAL",
       "PulseSequenceDetails" : "WIP" ,
       "RepetitionTime":4.5,
       "LabelingType": "PCASL",
       "LabelingDuration": 1.8,
       "PostLabelingDelay": 1.8,
       "BackgroundSuppression": True,
       "BackgroundSuppressionNumberPulses": 2,
       "M0scale":10,
       "M0": 10,
       "LabelingOrientation":"transversal",
       "LabelingDistance":105,
       "LabelingPulseAverageGradient": 10,
       "LabelingPulseMaximumGradient": 80,
       "VascularCrushing": False,
       "PulseDuration": 0.0005,
       "LabelingPulseInterval": 0.00038,
       "PCASLType":"unbalanced",
       "LabelingEfficiency":0.72},

}

IntendedFor = {
    m0: ['{session}/perf/sub-{subject}_{session}_asl.nii.gz'],
}
