from libPython.tnpClassUtils import tnpSample

### qll stat
eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
ntuple_2017_tnp = '/home/jhkim/TnPFit/samples/' # test for private tnp samples 

HLT_DoubleEle25_CaloIdL_MW_v2 = {
    'data_Run2017C_v3p0' : tnpSample('data_Run2017C_v3p0' , ntuple_2017_tnp + 'data/temp/tnp_data.root', lumi = 1.0),
    'data_Run2017E' : tnpSample('data_Run2017E' , ntuple_2017_tnp + 'data/temp/Run2017E_HLT_DoubleEle25_CaloIdL_MW_v2_Ele35Tag_.root', lumi = 1.0),
    'data_Run2017E_Ele35Tag' : tnpSample('data_Run2017E_Ele35Tag' , ntuple_2017_tnp + 'data/Run2017E_HLT_DoubleEle25_CaloIdL_MW_v2_Ele35Tag.root', lumi = 1.0),
    'data_Run2017F' : tnpSample('data_Run2017F' , ntuple_2017_tnp + 'data/temp/runF/Run2017F_HLT_DoubleEle25_CaloIdL_MW_v2_Ele35Tag_.root', lumi = 1.0),

    'DY_powheg_M50_120' : tnpSample('DY_powheg_M50_120', ntuple_2017_tnp + 'mc/DY_powheg_M_50_120_HLT_DoubleEle25_CaloIdL_MW_v2_UnSeededInfo.root', isMC = True, nEvts = -1),
    'DY_powheg_M50_120_Ele35Tag' : tnpSample('DY_powheg_M50_120_Ele35Tag', ntuple_2017_tnp + 'mc/DY_powheg_M_50_120_HLT_DoubleEle25_CaloIdL_MW_v2_Ele35Tag.root', isMC = True, nEvts = -1),
}

HLT_DoubleEle25_CaloIdL_MW_v2_performance = {
    'data_Run2017_HLT_v3*' : tnpSample('data_Run2017_HLT_v3*' , ntuple_2017_tnp + 'data/temp/Run2017DtoF_HLT_DoubleEle25_CaloIdL_MW_v2_Ele35Tag.root', lumi = 1.0),
    'data_Run2017_HLT_v4*' : tnpSample('data_Run2017_HLT_v4*' , ntuple_2017_tnp + 'data/temp/Run2017DtoF_HLT_DoubleEle25_CaloIdL_MW_v2_Ele35Tag.root', lumi = 1.0),

    'DY_powheg_M50_120_Ele35Tag' : tnpSample('DY_powheg_M50_120_Ele35Tag', ntuple_2017_tnp + 'mc/DY_powheg_M_50_120_HLT_DoubleEle25_CaloIdL_MW_v2_Ele35Tag_MiniAOD.root', isMC = True, nEvts = -1),
}

#HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v_performance = {
#    'data_Run2017_HLT_v13' : tnpSample('data_Run2017_HLT_v13' , ntuple_2017_tnp + 'data/temp/Run2017C_HLT_Ele23_Ele12.root', lumi = 1.0),
#    'data_Run2017_HLT_v14' : tnpSample('data_Run2017_HLT_v14' , ntuple_2017_tnp + 'data/temp/Run2017C_HLT_Ele23_Ele12.root', lumi = 1.0),
#    'data_Run2017_HLT_v15' : tnpSample('data_Run2017_HLT_v15' , ntuple_2017_tnp + 'data/temp/Run2017C_HLT_Ele23_Ele12.root', lumi = 1.0),
#    'data_Run2017_HLT_v16' : tnpSample('data_Run2017_HLT_v16' , ntuple_2017_tnp + 'data/temp/Run2017DtoF_HLT_Ele23_Ele12.root', lumi = 1.0),
#    'data_Run2017_HLT_v17' : tnpSample('data_Run2017_HLT_v17' , ntuple_2017_tnp + 'data/temp/Run2017DtoF_HLT_Ele23_Ele12.root', lumi = 1.0),
#
#    'DY_powheg_M50_120' : tnpSample('DY_powheg_M50_120', ntuple_2017_tnp + 'mc/DY_powheg_M_50_120_HLT_Ele23_Ele23_nonDZ_L1PS_3.root', isMC = True, nEvts = -1),
#}

HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v_performance = {
    #'data_Run2017_HLT_v13' : tnpSample('data_Run2017_HLT_v13' , ntuple_2017_tnp + 'data/SingleElectron_2017/SingleElectron_2017B-F_HLT_Ele23_Ele12.root', lumi = 1.0),
    #'data_Run2017_HLT_v14' : tnpSample('data_Run2017_HLT_v14' , ntuple_2017_tnp + 'data/SingleElectron_2017/SingleElectron_2017B-F_HLT_Ele23_Ele12.root', lumi = 1.0),
    #'data_Run2017_HLT_v15' : tnpSample('data_Run2017_HLT_v15' , ntuple_2017_tnp + 'data/SingleElectron_2017/SingleElectron_2017B-F_HLT_Ele23_Ele12.root', lumi = 1.0),
    #'data_Run2017_HLT_v16' : tnpSample('data_Run2017_HLT_v16' , ntuple_2017_tnp + 'data/SingleElectron_2017/SingleElectron_2017B-F_HLT_Ele23_Ele12.root', lumi = 1.0),
    'data_Run2017_HLT_Commissioning' : tnpSample('data_Run2017_HLT_Commissioning' , ntuple_2017_tnp + 'data/SingleElectron_2017/SingleElectron_2017B-F_HLT_Double.root', lumi = 1.0),
    'data_Run2017_HLT_Nominal WP Pre Oct 5th' : tnpSample('data_Run2017_HLT_Nominal WP Pre Oct 5th' , ntuple_2017_tnp + 'data/SingleElectron_2017/SingleElectron_2017B-F_HLT_Double.root', lumi = 1.0),
    'data_Run2017_HLT_Nominal WP Post Oct 5th' : tnpSample('data_Run2017_HLT_Nominal WP Post Oct 5th' , ntuple_2017_tnp + 'data/SingleElectron_2017/SingleElectron_2017B-F_HLT_Double.root', lumi = 1.0),

    #'DY_powheg_M50_120' : tnpSample('DY_powheg_M50_120', ntuple_2017_tnp + 'mc/DY_powheg_M_50_120_HLT_Ele23_Ele23_nonDZ_L1PS_3.root', isMC = True, nEvts = -1),
    'DY_powheg_M50_120' : tnpSample('DY_powheg_M50_120', ntuple_2017_tnp + 'mc/DY_powheg_M_50_120_MINIAODSIM_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_94X_mc2017_realistic_v10.root', isMC = True, nEvts = -1),
}

Moriond17_80X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eosWinter17 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph_Spring16_reHLT.root',
                                       isMC = True, nEvts = -1 ),
    'DY_madgraph_Winter17' : tnpSample('DY_madgraph_Winter17', 
                                       eosWinter17 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph_Moriond17.root',
                                       isMC = True, nEvts = 48652793 ),
    'DYee_powheg_Winter17' : tnpSample('DYee_powheg_Winter17', 
                                       eosWinter17 + 'mc/TnPTree_DYToEE_NNPDF30_13TeV-powheg-pythia8_DYToEE_powheg_Moriond17.root',
                                       isMC = True, nEvts = 49986588 ),
    'DY_amcatnlo_Winter17' : tnpSample('DY_amcatnlo_Winter17', 
                                       eosWinter17 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_DYToLL_mcAtNLO_Moriond17.root',
                                       isMC = True, nEvts = 28968252 ),
    'Wj_madgraph_Winter17' : tnpSample('Wj_madgraph_Winter17', 
                                       eosWinter17 + 'mc/TnPTree_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_WJets_madgraph_Moriond17.root',
                                       isMC = True, nEvts = 29048609 ),

    'data_Run2016B' : tnpSample('data_Run2016B' , eosWinter17 + 'data/TnPTree_SingleElectron_2016rereco_RunB.root' , lumi = 5.767 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , eosWinter17 + 'data/TnPTree_SingleElectron_2016rereco_RunC.root' , lumi = 2.646 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , eosWinter17 + 'data/TnPTree_SingleElectron_2016rereco_RunD.root' , lumi = 4.353 ),
    'data_Run2016E' : tnpSample('data_Run2016E' , eosWinter17 + 'data/TnPTree_SingleElectron_2016rereco_RunE.root' , lumi = 3.985 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , eosWinter17 + 'data/TnPTree_SingleElectron_2016rereco_RunF.root' , lumi = 3.160 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , eosWinter17 + 'data/TnPTree_SingleElectron_2016rereco_RunG.root' , lumi = 7.539 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , eosWinter17 + 'data/TnPTree_SingleElectron_2016prompt_RunH.root' , lumi = 8.762 ),

    

    ### AOD TnP for RECO scale factors
    'DY_madgraph_Winter17_rec' : tnpSample('DY_madgraph_Winter17_rec'  , 
                                           eosDirREC + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph_Winter2017.root',
                                           isMC = True, nEvts = 49748967),
    'DY_amcatnlo_Winter17_rec' : tnpSample('DY_amcatnlo_Winter17_rec'  , 
                                           eosDirREC + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_DYToLL_mcAtNLO_Winter2017.root',
                                           isMC = True, nEvts = 28658054),    
    'data_Run2016B_rec' : tnpSample('data_Run2016B_rec', eosDirREC + 'data/TnPTree_SingleElectron_2016rereco_RunB.root', lumi = 5.899),
    'data_Run2016C_rec' : tnpSample('data_Run2016C_rec', eosDirREC + 'data/TnPTree_SingleElectron_2016rereco_RunC.root', lumi = 2.646),
    'data_Run2016D_rec' : tnpSample('data_Run2016D_rec', eosDirREC + 'data/TnPTree_SingleElectron_2016rereco_RunD.root', lumi = 4.353),
    'data_Run2016E_rec' : tnpSample('data_Run2016E_rec', eosDirREC + 'data/TnPTree_SingleElectron_2016rereco_RunE.root', lumi = 4.050),
    'data_Run2016F_rec' : tnpSample('data_Run2016F_rec', eosDirREC + 'data/TnPTree_SingleElectron_2016rereco_RunF.root', lumi = 3.160),
    'data_Run2016G_rec' : tnpSample('data_Run2016G_rec', eosDirREC + 'data/TnPTree_SingleElectron_2016rereco_RunG.root', lumi = 7.391),
    'data_Run2016H_rec' : tnpSample('data_Run2016H_rec', eosDirREC + 'data/TnPTree_SingleElectron_2016prompt_RunH.root', lumi = 8.762),
    }

Moriond17_80X_prompt = {
    'DY_madgraph' : tnpSample('DY_madgraph', eosDir1 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph.root', 
                              isMC = True, nEvts = 33584160 ),
    'data_Run2016B' : tnpSample('data_Run2016B' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunB.root' , lumi = -1 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunC.root' , lumi = -1 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunD.root' , lumi = -1 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunF.root' , lumi = -1 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunG.root' , lumi = -1 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunH.root' , lumi = -1 ),
    }



### for this round eleIDs, phoIDs, trigger trees are included in the same file
eosDir = 'eos/cms/store/group/phys_egamma/tnp/80X/76Xids/AllIDs_v0/'
Ichep2016_80X = {
    'DY_amcatnlo' : tnpSample('DY_amcatnlo', eosDir+'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_DYToLL_mcAtNLO.root', isMC = True, nEvts = 28696958 ),
    'DY_madgraph' : tnpSample('DY_madgraph', eosDir+'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root'           , isMC = True, nEvts = 44716638 ),
    'Wjets'       : tnpSample('Wjets'      , eosDir+'mc/TnPTree_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_WJets_madgraph.root' , isMC = True, nEvts = 28062407 ),
    'ttbar'       : tnpSample('ttbar'      , eosDir+'mc/TnPTree_TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ttbar_madgraph.root'     , isMC = True, nEvts = 10215131 ),
    'data_Run2016B' : tnpSample('data_Run2016B' , eosDir+'data/TnPTree_SingleElectron_Run2016B.root' , lumi = 5.884 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , eosDir+'data/TnPTree_SingleElectron_Run2016C.root' , lumi = 2.646 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , eosDir+'data/TnPTree_SingleElectron_Run2016D.root' , lumi = 4.353 ),
}

eosDir_v0 = 'eos/cms/store/group/phys_egamma/tnp/80X/'
ICHEP2016 = {
    'mc_DY_madgraph_ele' : tnpSample('mc_DY_madgraph_ele', eosDir_v0 + 'Photons_76Xids/elev2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root' ,
                                     isMC = True, nEvts = 36311064 ),
    'mc_DY_amcatnlo_ele' : tnpSample('mc_DY_amcatnlo_ele', eosDir_v0 + 'Photons_76Xids/elev2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
                                     isMC = True, nEvts = 28696958 ),
    'mc_DY_madgraph_pho' : tnpSample('mc_DY_madgraph_pho', eosDir_v0 + 'Photons_76Xids/phov2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root' ,
                                     isMC = True, nEvts = 41253879 ),
    'mc_DY_amcatnlo_pho' : tnpSample('mc_DY_amcatnlo_pho', eosDir_v0 + 'Photons_76Xids/phov2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
                                     isMC = True, nEvts = 28696958 ),
    'mc_Wjets_madgraph_pho' : tnpSample('mc_Wjets_madgraph_pho', eosDir_v0 + 'Photons_76Xids/phov2/mc/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root'        , 
                                        isMC = True, nEvts = 999 ),
    'mc_DY_madgraph_rec' : tnpSample('mc_DY_madgraph_rec', eosDir_v0 + 'RecoSF/RECOv3/mc//TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root'       ,
                                     isMC = True, nEvts = 49877138 ),
    'mc_DY_amcatnlo_rec' : tnpSample('mc_DY_amcatnlo_rec', eosDir_v0 + 'RecoSF/RECOv3/mc//TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root'      , 
                                     isMC = True, nEvts = 28328619 ),
    'data_2016_runB_ele' :  tnpSample('data_2016_runB_ele', eosDir_v0 + 'Photons_76Xids/elev2/data/TnPTree_SingleElectron_2016_RunB.root' , lumi = 5.709 ),
    'data_2016_runC_ele' :  tnpSample('data_2016_runC_ele', eosDir_v0 + 'Photons_76Xids/elev3/data/TnPTree_SingleElectron_2016_RunC.root' , lumi = 2.646 ),
    'data_2016_runD_ele' :  tnpSample('data_2016_runD_ele', eosDir_v0 + 'Photons_76Xids/elev3/data/TnPTree_SingleElectron_2016_RunD.root' , lumi = 4.330 ),
    'data_2016_runB_pho' :  tnpSample('data_2016_runB_pho', eosDir_v0 + 'Photons_76Xids/phov2/data/TnPTree_SingleElectron_2016_RunB.root' , lumi = 5.900 ),
    'data_2016_runC_pho' :  tnpSample('data_2016_runC_pho', eosDir_v0 + 'Photons_76Xids/phov3/data/TnPTree_SingleElectron_2016_RunC.root' , lumi = 2.646 ),
    'data_2016_runD_pho' :  tnpSample('data_2016_runD_pho', eosDir_v0 + 'Photons_76Xids/phov3/data/TnPTree_SingleElectron_2016_RunD.root' , lumi = 4.330 ),
    'data_2016_runB_rec' :  tnpSample('data_2016_runB_rec', eosDir_v0 + 'RecoSF/RECOv3/data//TnPTree_SingleElectron_2016_RunB.root'       , lumi = 5.237 ),
    'data_2016_runC_rec' :  tnpSample('data_2016_runC_rec', eosDir_v0 + 'RecoSF/RECOv4/data//TnPTree_SingleElectron_2016_RunC.root'       , lumi = 2.646 ),
    'data_2016_runD_rec' :  tnpSample('data_2016_runD_rec', eosDir_v0 + 'RecoSF/RECOv5/data//TnPTree_SingleElectron_2016_RunD.root'       , lumi = 4.313 ),
}
