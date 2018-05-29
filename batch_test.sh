#!/bin/sh
#$ -S /bin/bash 

cd /share_home/jhkim/TnPFit/egm_tnp_analysis
python tnpEGM_fitter.py etc/config/settings_L1xHLT_nvtx_Ele23_Ele12.py --flag passL1xHLT --plotX nvtx --checkBins
