import os

path_to_file = './Locations_on_railway.txt'

with open(path_to_file) as f:
    contents = f.readlines()


for i in range(1,len(contents)):
    Command_line = 'LiCSBAS_cum2tstxt.py' + ' -g ' + str(contents[i].split('\t')[0]) + '/' + str(contents[i].split('\t')[1]) + ' -i ' + 'TS_GEOCml/cum.h5'
    #print(Command_line)
    os.system(Command_line)


