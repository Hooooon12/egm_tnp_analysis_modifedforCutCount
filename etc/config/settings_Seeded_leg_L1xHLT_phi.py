#############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'passSeededL1xHLT'  : '(passHLT  == 1) && (passL1T  == 1)',
    'passL1T'  : '(passL1T  == 1)',
    'passHE'  : '(passSeededHE  == 1)',
    'passSie'  : '(passSeededClusterShape  == 1)',
    'passPM'  : '(passSeededPM  == 1)',
    'passSeededS2'  : '(passHLT  == 1)',
    }
baseOutDir = 'results/test/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples

tnpTreeDir = 'tnpEleTrig' # tree name of the input root files 

samplesDef = {
    'data'   : tnpSamples.HLT_DoubleEle25_CaloIdL_MW_v2_performance['data_Run2017_HLT_v3*'].clone(),
    'data_1'   : tnpSamples.HLT_DoubleEle25_CaloIdL_MW_v2_performance['data_Run2017_HLT_v4*'].clone(),
    'mcNom'  : tnpSamples.HLT_DoubleEle25_CaloIdL_MW_v2['DY_powheg_M50_120_Ele35Tag'].clone(),
    'mcAlt'  : None,
    'tagSel' : None,
}
## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.HLT_DoubleEle25_CaloIdL_MW_v2['data_Run2017F'] )
#samplesDef['data'].add_sample( tnpSamples.ICHEP2016['data_2016_runD_ele'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 304333')
samplesDef['data'  ].set_cut('run >= 302026 && run <= 305377')
samplesDef['data_1'  ].set_cut('run >= 305405 && run <= 306126')

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph_ele')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 33  && tag_Ele_nonTrigMVA > 0.90')

## set MC weight, simple way (use tree weight) 
weightName = 'totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'probe_sc_eta' , 'type': 'float', 'bins': [-2.5,-1.479, 0.0, 1.479, 2.5] },
   { 'var' : 'probe_sc_phi' , 'type': 'float', 'bins': [ -3.15, -2.4, -1.8, -1.2, -0.6, 0., 0.6, 1.2, 1.8, 2.4, 3.15] }, # X axis
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut

cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && probe_sc_et > 30'

#cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && probe_sc_et > 30 && passL1T  == 1'
#cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && passL1T  == 1'

#cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && probe_sc_et > 30 && passL1T  == 1 && passSeededHE  == 1'
#cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && passL1T  == 1 && passSeededHE  == 1'

#cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && probe_sc_et > 30 && passL1T  == 1 && passSeededHE  == 1 && passSeededClusterShape  == 1'
#cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && passL1T  == 1 && passSeededHE  == 1 && passSeededClusterShape  == 1'

#cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && probe_sc_et > 30 && passL1T  == 1 && passSeededHE  == 1 && passSeededClusterShape  == 1 && passSeededPM == 1'
#cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && passL1T  == 1 && passSeededHE  == 1 && passSeededClusterShape  == 1 && passSeededPM  == 1'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
}

#### or remove any additional cut (default)
additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, 0, 1]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
