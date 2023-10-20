#!/usr/bin/python
import os
import glob
import csv


#search for file name in path
def file_search (row, data_dir):

    search_file, search_path = row[0], row[1]
    folder_contents = glob.glob(data_dir + search_path + "*")
    files = [file.split("/")[-1] for file in folder_contents]
    if search_file in files:
        return
    else:
        print (f"ERROR: {search_file} not found in {data_dir + search_path}")
        return



def main():

    dataset_list = "/data/projects/glygen/generated/misc/files4nathan.csv"
    data_dir = "/data/projects/glygen/"

    with open(dataset_list, "r") as in_file:
        infile = csv.reader(in_file, delimiter=",")
        
        row_count = 0    
        for row in infile:
            row_count += 1
            if row_count == 1: #skip header row
                continue

            else:
                file_search(row, data_dir)

    print (f"Checked {row_count - 1} files")

    
if __name__ == '__main__':
    main()



    