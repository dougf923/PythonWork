


import os
"""
Renames the multiple file within the same directory with appending number
"""
path = 'FixedDT_MC_Logs/'
files = os.listdir(path)



i = 1

for file in files:
	os.rename(path+file, "TC1_F"+str(i)+".ulg")
	i += 1
    



