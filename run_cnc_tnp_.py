import os, sys

#for i in range(1, 11) : 
for i in range(1, 10) : 

    command = 'python run_cnc_tnp_Ele23_Ele12.py ' + str(i) + ' >& filter_' + str(i) + '.log &' 
    os.system(command)
    print command
