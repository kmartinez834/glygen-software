#!/usr/bin/python
import os,sys
import glob
import csv
import json
from optparse import OptionParser
import tarfile


#######################################
def main():

    medline_dir = "/data/projects/glygen/downloads/ncbi"       
    file_list = glob.glob(medline_dir+"/medline_txt/*")

    dup_list = []
    file_num = 0
    for file in file_list:
        with open(file, 'r') as in_file:
            infile = in_file.readlines()
            if (len(infile)) < 5:
                dup_list.append(file) 

        file_num += 1
        #print (f'Checked {file_num}/{len(file_list)} files')
            
    #print (len(dup_list))
    print (dup_list)

if __name__ == '__main__':
    main()

