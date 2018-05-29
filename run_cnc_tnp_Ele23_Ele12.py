import os, sys

NthFilter = sys.argv[1]

#Xaxis = ['eta', 'et', 'phi', 'nvtx']
#Xaxis = ['et','nvtx']
Xaxis = ['nvtx']

if NthFilter == '1':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_L1_' + value + '_Ele23_Ele12.py --flag passL1T --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_L1_' + value + '_Ele23_Ele12.py --flag passL1T --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_L1_' + value + '_Ele23_Ele12.py --flag passL1T --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_L1_' + value + '_Ele23_Ele12.py --flag passL1T --plotX ' + value + ' --createHists_v2')

if NthFilter == '2':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_EtLeg1_' + value + '_Ele23_Ele12.py --flag passEtLeg1 --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_EtLeg1_' + value + '_Ele23_Ele12.py --flag passEtLeg1 --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_EtLeg1_' + value + '_Ele23_Ele12.py --flag passEtLeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_EtLeg1_' + value + '_Ele23_Ele12.py --flag passEtLeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '3':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_ClusterShapeLeg1_' + value + '_Ele23_Ele12.py --flag passClusterShapeLeg1 --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_ClusterShapeLeg1_' + value + '_Ele23_Ele12.py --flag passClusterShapeLeg1 --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_ClusterShapeLeg1_' + value + '_Ele23_Ele12.py --flag passClusterShapeLeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_ClusterShapeLeg1_' + value + '_Ele23_Ele12.py --flag passClusterShapeLeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '4':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_HELeg1_' + value + '_Ele23_Ele12.py --flag passHELeg1 --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_HELeg1_' + value + '_Ele23_Ele12.py --flag passHELeg1 --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_HELeg1_' + value + '_Ele23_Ele12.py --flag passHELeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_HELeg1_' + value + '_Ele23_Ele12.py --flag passHELeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '5':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_EcalIsoLeg1_' + value + '_Ele23_Ele12.py --flag passEcalIsoLeg1 --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_EcalIsoLeg1_' + value + '_Ele23_Ele12.py --flag passEcalIsoLeg1 --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_EcalIsoLeg1_' + value + '_Ele23_Ele12.py --flag passEcalIsoLeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_EcalIsoLeg1_' + value + '_Ele23_Ele12.py --flag passEcalIsoLeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '6':
   for value in Xaxis:
   
       #os.system('python tnpEGM_fitter.py etc/config/settings_PixelMatchLeg1_' + value + '_Ele23_Ele12.py --flag passPixelMatchLeg1 --plotX ' + value + ' --checkBins')
       #os.system('python tnpEGM_fitter.py etc/config/settings_PixelMatchLeg1_' + value + '_Ele23_Ele12.py --flag passPixelMatchLeg1 --plotX ' + value + ' --createBins')
       #os.system('python tnpEGM_fitter.py etc/config/settings_PixelMatchLeg1_' + value + '_Ele23_Ele12.py --flag passPixelMatchLeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_PixelMatchLeg1_' + value + '_Ele23_Ele12.py --flag passPixelMatchLeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '7':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_OneOEMinusOneOPLeg1_' + value + '_Ele23_Ele12.py --flag passOneOEMinusOneOPLeg1 --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_OneOEMinusOneOPLeg1_' + value + '_Ele23_Ele12.py --flag passOneOEMinusOneOPLeg1 --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_OneOEMinusOneOPLeg1_' + value + '_Ele23_Ele12.py --flag passOneOEMinusOneOPLeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_OneOEMinusOneOPLeg1_' + value + '_Ele23_Ele12.py --flag passOneOEMinusOneOPLeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '8':
   for value in Xaxis:
       
       os.system('python tnpEGM_fitter.py etc/config/settings_DetaLeg1_' + value + '_Ele23_Ele12.py --flag passDetaLeg1 --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_DetaLeg1_' + value + '_Ele23_Ele12.py --flag passDetaLeg1 --plotX ' + value + ' --createBins')   
       os.system('python tnpEGM_fitter.py etc/config/settings_DetaLeg1_' + value + '_Ele23_Ele12.py --flag passDetaLeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_DetaLeg1_' + value + '_Ele23_Ele12.py --flag passDetaLeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '9':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_DphiLeg1_' + value + '_Ele23_Ele12.py --flag passDphiLeg1 --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_DphiLeg1_' + value + '_Ele23_Ele12.py --flag passDphiLeg1 --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_DphiLeg1_' + value + '_Ele23_Ele12.py --flag passDphiLeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_DphiLeg1_' + value + '_Ele23_Ele12.py --flag passDphiLeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '10':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_TrackIsoLeg1_' + value + '_Ele23_Ele12.py --flag passTrackIsoLeg1 --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_TrackIsoLeg1_' + value + '_Ele23_Ele12.py --flag passTrackIsoLeg1 --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_TrackIsoLeg1_' + value + '_Ele23_Ele12.py --flag passTrackIsoLeg1 --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_TrackIsoLeg1_' + value + '_Ele23_Ele12.py --flag passTrackIsoLeg1 --plotX ' + value + ' --createHists_v2')
   
if NthFilter == '11':
   for value in Xaxis:
   
       os.system('python tnpEGM_fitter.py etc/config/settings_L1xHLT_' + value + '_Ele23_Ele12.py --flag passL1xHLT --plotX ' + value + ' --checkBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_L1xHLT_' + value + '_Ele23_Ele12.py --flag passL1xHLT --plotX ' + value + ' --createBins')
       os.system('python tnpEGM_fitter.py etc/config/settings_L1xHLT_' + value + '_Ele23_Ele12.py --flag passL1xHLT --plotX ' + value + ' --createHists')
       os.system('python tnpEGM_fitter.py etc/config/settings_L1xHLT_' + value + '_Ele23_Ele12.py --flag passL1xHLT --plotX ' + value + ' --createHists_v2')
