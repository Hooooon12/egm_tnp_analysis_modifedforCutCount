
### python specific import
import argparse
import os
import sys
import pickle
import shutil

parser = argparse.ArgumentParser(description='tnp EGM fitter')
parser.add_argument('--checkBins'  , action='store_true'  , help = 'check  bining definition')
parser.add_argument('--createBins' , action='store_true'  , help = 'create bining definition')
parser.add_argument('--createHists', action='store_true'  , help = 'create histograms')
parser.add_argument('--createHists_v2', action='store_true'  , help = 'create histograms v2') #### added by me: draw plots using cut and count effciency
parser.add_argument('--sample'     , default='all'        , help = 'create histograms (per sample, expert only)')
parser.add_argument('--altSig'     , action='store_true'  , help = 'alternate signal model fit')
parser.add_argument('--altBkg'     , action='store_true'  , help = 'alternate background model fit')
parser.add_argument('--doFit'      , action='store_true'  , help = 'fit sample (sample should be defined in settings.py)')
parser.add_argument('--mcSig'      , action='store_true'  , help = 'fit MC nom [to init fit parama]')
parser.add_argument('--doPlot'     , action='store_true'  , help = 'plotting')
parser.add_argument('--sumUp'      , action='store_true'  , help = 'sum up efficiencies')
parser.add_argument('--iBin'       , dest = 'binNumber'   , type = int,  default=-1, help='bin number (to refit individual bin)')
parser.add_argument('--flag'       , default = None       , help ='WP to test')
parser.add_argument('--plotX'       , default = None       , help ='x axis of plot to draw') #### added by me: plot type to draw
parser.add_argument('settings'     , default = None       , help = 'setting file [mandatory]')

args = parser.parse_args()

print '===> settings %s <===' % args.settings
importSetting = 'import %s as tnpConf' % args.settings.replace('/','.').split('.py')[0]
print importSetting
exec(importSetting)

### tnp library
import libPython.binUtils  as tnpBiner
import libPython.rootUtils as tnpRoot


if args.flag is None:
    print '[tnpEGM_fitter] flag is MANDATORY, this is the working point as defined in the settings.py'
    sys.exit(0)
    
if not args.flag in tnpConf.flags.keys() :
    print '[tnpEGM_fitter] flag %s not found in flags definitions' % args.flag
    print '  --> define in settings first'
    print '  In settings I found flags: '
    print tnpConf.flags.keys()
    sys.exit(1)

outputDirectory = '%s/%s/%s' % (tnpConf.baseOutDir,args.flag, args.plotX)

print '===>  Output directory: '
print outputDirectory


####################################################################
##### Create (check) Bins
####################################################################
if args.checkBins:
    tnpBins = tnpBiner.createBins(tnpConf.biningDef,tnpConf.cutBase)
    tnpBiner.tuneCuts( tnpBins, tnpConf.additionalCuts )
    for ib in range(len(tnpBins['bins'])):
        print tnpBins['bins'][ib]['name']
        print '  - cut: ',tnpBins['bins'][ib]['cut']
    sys.exit(0)
    
if args.createBins:
    if os.path.exists( outputDirectory ):
            shutil.rmtree( outputDirectory )
    os.makedirs( outputDirectory )
    tnpBins = tnpBiner.createBins(tnpConf.biningDef,tnpConf.cutBase)
    tnpBiner.tuneCuts( tnpBins, tnpConf.additionalCuts )
    pickle.dump( tnpBins, open( '%s/bining.pkl'%(outputDirectory),'wb') )
    print 'created dir: %s ' % outputDirectory
    print 'bining created successfully... '
    print 'Note than any additional call to createBins will overwrite directory %s' % outputDirectory
    sys.exit(0)

tnpBins = pickle.load( open( '%s/bining.pkl'%(outputDirectory),'rb') )


####################################################################
##### Create Histograms
####################################################################
#keyNames = ['data', 'data_1', 'data_2', 'data_3', 'data_4','mcNom','mcAlt','tagSel']
keyNames = ['data', 'data_1', 'data_2','mcNom','mcAlt','tagSel']
#keyNames = ['data', 'mcNom','mcAlt','tagSel']
#for s in tnpConf.samplesDef.keys():
for s in keyNames:
    sample =  tnpConf.samplesDef[s]
    if sample is None: continue
    setattr( sample, 'tree'     ,'%s/fitter_tree' % tnpConf.tnpTreeDir )
    setattr( sample, 'histFile' , '%s/%s_%s_%s.root' % ( outputDirectory , sample.name, args.flag, args.plotX ) )

dataList = []
mcList = []
fOutList = []

if args.createHists:
    #for sampleType in tnpConf.samplesDef.keys():
    for sampleType in keyNames:
        sample =  tnpConf.samplesDef[sampleType]
        if sample is None : continue
        if sampleType == args.sample or args.sample == 'all' :
            print 'creating histogram for sample '
            sample.dump()
            var = { 'name' : 'pair_mass', 'nbins' : 60, 'min' : 60, 'max': 120 }
            if sample.mcTruth:
                var = { 'name' : 'pair_mass', 'nbins' : 60, 'min' : 60, 'max': 120 }
                mcList.append(sample.histFile)
            else:
               dataList.append(sample.histFile)
               print sample.histFile 
               print dataList

            tnpRoot.makePassFailHistograms( sample, tnpConf.flags[args.flag], tnpBins, var )
    # root files with historams are created

    print dataList
    for datumList in dataList :
        print datumList
    
        #### added by me: make efficiency text file using cut and count efficiency 
        info = {
            #'data'        :   outputDirectory + '/data_Run2017E_Ele35Tag_' + args.flag + '_' + args.plotX + '.root',
            'data'        :   datumList,
            'dataNominal' : None,
            'dataAltSig'  : None,
            'dataAltBkg'  : None,
            #'mcNominal'   :  outputDirectory + '/DY_powheg_M50_120_Ele35Tag_' + args.flag + '_' + args.plotX + '.root',
            'mcNominal'   :  mcList[0],
            #'mcNominal'   :  None,
            'mcAlt'       : None,
            'tagSel'      : None
            }
    
        effis = None
        effFileName ='%s/egammaEffi%s.txt' % (outputDirectory, (datumList.split('/')[5]).split('.root')[0])
        fOut = open( effFileName,'w')
        fOutList.append(effFileName)
    
        for ib in range(len(tnpBins['bins'])):
            #effis = tnpRoot.getAllEffi( info, tnpBins['bins'][ib] )
            effis = tnpRoot.getAllNumbers( info, tnpBins['bins'][ib] )
    
            ### formatting assuming 2D bining -- to be fixed        
            v1Range = tnpBins['bins'][ib]['title'].split(';')[1].split('<')
            v2Range = tnpBins['bins'][ib]['title'].split(';')[2].split('<')
            if ib == 0 :
                astr = '### var1 : %s' % v1Range[1]
                print astr
                fOut.write( astr + '\n' )
                astr = '### var2 : %s' % v2Range[1]
                print astr
                fOut.write( astr + '\n' )
    
            astr =  '%+8.3f\t%+8.3f\t%+8.3f\t%+8.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f' % (
                float(v1Range[0]), float(v1Range[2]),
                float(v2Range[0]), float(v2Range[2]),
                effis['data'][0],effis['data'][1],
                effis['mcNominal'  ][0],effis['mcNominal'  ][1],
                effis['dataAltBkg' ][0],
                effis['dataAltSig' ][0],
                effis['mcAlt' ][0],
                effis['tagSel'][0],
                )
            print astr
            fOut.write( astr + '\n' )
        fOut.close()
    ####

    print fOutList
    sys.exit(0)

#### added by me: draw plot
if args.createHists_v2:
    from os import listdir

    #### collect all effi txt files
    fOutList = []
    for s in keyNames:
        sample =  tnpConf.samplesDef[s]
        if sample is None: continue
        temp_ = sample.name

        if temp_.split('_')[0] == 'data' :
           temp_txtFile = outputDirectory + '/' + 'egammaEffidata_' + temp_.split('_')[1] + '_' + temp_.split('_')[2] + '_' + temp_.split('_')[3] + '_' + args.flag + '_' + args.plotX + '.txt'
           fOutList.append(temp_txtFile)
           print temp_txtFile

    print fOutList
    import libPython.EGammaID_scaleFactors as egm_sf

    #if 'nvtx' in args.plotX : egm_sf.draw1Dplot(effFileName, -1., outputDirectory, ['PV','eta'])
    #if 'z' in args.plotX : egm_sf.draw1Dplot(effFileName, -1., outputDirectory, ['z','eta'])
    #if 'eta' in args.plotX :egm_sf.draw1Dplot(effFileName, -1., outputDirectory, ['eta','pt'])
    #if 'phi' in args.plotX :egm_sf.draw1Dplot(effFileName, -1., outputDirectory, ['phi','eta'])
    #if 'et' in args.plotX : egm_sf.draw1Dplot(effFileName, -1., outputDirectory)

    if 'phi' == args.plotX : egm_sf.draw1Dplots(fOutList, -1., outputDirectory, ['phi','eta'])
    if 'eta' == args.plotX : egm_sf.draw1Dplots(fOutList, -1., outputDirectory, ['eta','pt'])
    if 'nvtx' == args.plotX : egm_sf.draw1Dplots(fOutList, -1., outputDirectory, ['PV','eta'])
    if 'et' == args.plotX : egm_sf.draw1Dplots(fOutList, -1., outputDirectory)

    sys.exit(0)
####


####################################################################
##### Actual Fitter
####################################################################
sampleToFit = tnpConf.samplesDef['data']
if sampleToFit is None:
    print '[tnpEGM_fitter, prelim checks]: sample (data or MC) not available... check your settings'
    sys.exit(1)

sampleMC = tnpConf.samplesDef['mcNom']

if sampleMC is None:
    print '[tnpEGM_fitter, prelim checks]: MC sample not available... check your settings'
    sys.exit(1)
for s in tnpConf.samplesDef.keys():
    sample =  tnpConf.samplesDef[s]
    if sample is None: continue
    setattr( sample, 'mcRef'     , sampleMC )
    setattr( sample, 'nominalFit', '%s/%s_%s.nominalFit.root' % ( outputDirectory , sample.name, args.flag ) )
    setattr( sample, 'altSigFit' , '%s/%s_%s.altSigFit.root'  % ( outputDirectory , sample.name, args.flag ) )
    setattr( sample, 'altBkgFit' , '%s/%s_%s.altBkgFit.root'  % ( outputDirectory , sample.name, args.flag ) )



### change the sample to fit is mc fit
if args.mcSig :
    sampleToFit = tnpConf.samplesDef['mcNom']

if  args.doFit:
    sampleToFit.dump()
    for ib in range(len(tnpBins['bins'])):
        if (args.binNumber >= 0 and ib == args.binNumber) or args.binNumber < 0:
            if args.altSig:                 
                tnpRoot.histFitterAltSig(  sampleToFit, tnpBins['bins'][ib], tnpConf.tnpParAltSigFit )
            elif args.altBkg:
                tnpRoot.histFitterAltBkg(  sampleToFit, tnpBins['bins'][ib], tnpConf.tnpParAltBkgFit )
            else:
                tnpRoot.histFitterNominal( sampleToFit, tnpBins['bins'][ib], tnpConf.tnpParNomFit )

    args.doPlot = True
     
####################################################################
##### dumping plots
####################################################################
if  args.doPlot:
    fileName = sampleToFit.nominalFit
    fitType  = 'nominalFit'
    if args.altSig : 
        fileName = sampleToFit.altSigFit
        fitType  = 'altSigFit'
    if args.altBkg : 
        fileName = sampleToFit.altBkgFit
        fitType  = 'altBkgFit'
        
    plottingDir = '%s/plots/%s/%s' % (outputDirectory,sampleToFit.name,fitType)
    if not os.path.exists( plottingDir ):
        os.makedirs( plottingDir )
    shutil.copy('etc/inputs/index.php.listPlots','%s/index.php' % plottingDir)

    for ib in range(len(tnpBins['bins'])):
        if (args.binNumber >= 0 and ib == args.binNumber) or args.binNumber < 0:
            tnpRoot.histPlotter( fileName, tnpBins['bins'][ib], plottingDir )

    print ' ===> Plots saved in <======='
#    print 'localhost/%s/' % plottingDir


####################################################################
##### dumping egamma txt file 
####################################################################
if args.sumUp:
    sampleToFit.dump()
    info = {
        'data'        : sampleToFit.histFile,
        'dataNominal' : sampleToFit.nominalFit,
        'dataAltSig'  : sampleToFit.altSigFit ,
        'dataAltBkg'  : sampleToFit.altBkgFit ,
        'mcNominal'   : sampleToFit.mcRef.histFile,
        'mcAlt'       : None,
        'tagSel'      : None
        }

    if not tnpConf.samplesDef['mcAlt' ] is None:
        info['mcAlt'    ] = tnpConf.samplesDef['mcAlt' ].histFile
    if not tnpConf.samplesDef['tagSel'] is None:
        info['tagSel'   ] = tnpConf.samplesDef['tagSel'].histFile

    effis = None
    effFileName ='%s/egammaEffi.txt' % outputDirectory 
    fOut = open( effFileName,'w')
    
    for ib in range(len(tnpBins['bins'])):
        effis = tnpRoot.getAllEffi( info, tnpBins['bins'][ib] )

        ### formatting assuming 2D bining -- to be fixed        
        v1Range = tnpBins['bins'][ib]['title'].split(';')[1].split('<')
        v2Range = tnpBins['bins'][ib]['title'].split(';')[2].split('<')
        if ib == 0 :
            astr = '### var1 : %s' % v1Range[1]
            print astr
            fOut.write( astr + '\n' )
            astr = '### var2 : %s' % v2Range[1]
            print astr
            fOut.write( astr + '\n' )
            
        astr =  '%+8.3f\t%+8.3f\t%+8.3f\t%+8.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f' % (
            float(v1Range[0]), float(v1Range[2]),
            float(v2Range[0]), float(v2Range[2]),
            effis['dataNominal'][0],effis['dataNominal'][1],
            effis['mcNominal'  ][0],effis['mcNominal'  ][1],
            effis['dataAltBkg' ][0],
            effis['dataAltSig' ][0],
            effis['mcAlt' ][0],
            effis['tagSel'][0],
            )
        print astr
        fOut.write( astr + '\n' )
    fOut.close()

    print 'Effis saved in file : ',  effFileName
    import libPython.EGammaID_scaleFactors as egm_sf
    egm_sf.doEGM_SFs(effFileName,sampleToFit.lumi)
