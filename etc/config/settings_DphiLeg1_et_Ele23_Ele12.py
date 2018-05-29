#############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'passL1T'  : '(passL1T  == 1)',
    'passEtLeg1' :  '(passEtLeg1 == 1)',
    'passClusterShapeLeg1' : '(passClusterShapeLeg1 == 1)',
    'passHELeg1' : '(passHELeg1 ==1)',
    'passEcalIsoLeg1' : '(passEcalIsoLeg1 ==1)',
    'passPixelMatchLeg1' : '(passPixelMatchLeg1 == 1)',
    'passOneOEMinusOneOPLeg1' : '(passOneOEMinusOneOPLeg1 == 1)',
    'passDetaLeg1' : '(passDetaLeg1 == 1)',
    'passDphiLeg1' : '(passDphiLeg1 == 1)',
    }
baseOutDir = 'results/Ele23_Ele12/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples

tnpTreeDir = 'tnpEleTrig' # tree name of the input root files 

samplesDef = {
    'data'   : tnpSamples.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v_performance['data_Run2017_HLT_v13'].clone(),
    'data_1'   : tnpSamples.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v_performance['data_Run2017_HLT_v14'].clone(),
    'data_2'   : tnpSamples.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v_performance['data_Run2017_HLT_v15'].clone(),
    'data_3'   : tnpSamples.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v_performance['data_Run2017_HLT_v16'].clone(),
    'data_4'   : tnpSamples.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v_performance['data_Run2017_HLT_v17'].clone(),
    'mcNom'  : tnpSamples.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v_performance['DY_powheg_M50_120'].clone(),
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
samplesDef['data'  ].set_cut('run >= 299368 && run <= 299649')
samplesDef['data_1'  ].set_cut('run >= 300079 && run <= 300817')
samplesDef['data_2'  ].set_cut('run >= 301046 && run <= 302019')
samplesDef['data_3'  ].set_cut('run >= 302026 && run <= 302494')
samplesDef['data_4'  ].set_cut('run >= 302509 && run <= 306460')

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

   { 'var' : 'probe_sc_eta' , 'type': 'abs_float', 'bins': [0.0, 1.479, 2.5] },
   { 'var' : 'probe_sc_et' , 'type': 'float', 'bins': [10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 27.0, 28.5, 30.0, 35.0, 40.0, 45.0, 50.0,60.0,70.0,80.0,100.0, 150.0, 200.0, 250.0] },

]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut

cutBase   = 'tag_sc_et > 35 && abs(tag_sc_eta) < 2.1 && passL1T == 1 && passEtLeg1 == 1 && passClusterShapeLeg1 == 1&& passHELeg1 == 1 && passEcalIsoLeg1 == 1 && passPixelMatchLeg1 == 1 && passOneOEMinusOneOPLeg1 == 1 && passDetaLeg1 == 1'

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
        
