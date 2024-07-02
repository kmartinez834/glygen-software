#!/usr/bin/python

'''
This file will remove line breaks from values and convert carbbank.txt to a json file

Example:
{
    "1": {
        "CC": "CCSD:42034",
        "AU": "Albersheim P; Darvill A; Augur C; Cheong JJ; Eberhard S; Hahn MG;Marfa V; Mohnen D; O'Neill MA; Spiro MD; York WS",
        "TI": "Oligosaccharins: Oligosaccharide regulatory molecules",
        "CT": "Acc Chem Res (1992) 25: 77-83",
        "SC": "1",
        "BS": "(GS) Phytophthora megasperma, (OT) cell wall, (*) f.sp. glycinea",
        "SB": "Westra B",
        "DA": "06-12-1995",
        "FC": "5bc58ff3",
        "SI": "CBank:15402"
    }'''


import os
import glob
import csv
import json
import re
import csv

def main():

    entry_dict = {}

    src_file = "/data/projects/glygen/downloads/carbbank/current/carbbank.txt"

    with open(src_file, "r", encoding = 'latin-1') as in_file:
        infile = in_file.readlines()
        
        record_num = 0
        prev_line = ""
        new_record = False
        for line in infile:
            line = line.strip("\n")
            if line.startswith("; start of record"):
                record_num += 1
                entry_dict[record_num] = {}
                new_record = True
                continue
            elif line.startswith("----------------"):
                new_record = False
                continue
            elif new_record == True and line.startswith(";")==False:
                if re.match(r"^[A-Z][A-Z]:", line):
                    prev_line = line
                else:
                    prev_line += line
                key = prev_line.split(":")[0]
                value = prev_line.split(f"{key}: ")[-1]
                entry_dict[record_num][key] = value
            else:
                continue
    
    # write to json file
    json_data = json.dumps(entry_dict, indent=4)

    # Writing to sample.json
    out_file = '/home/karinamartinez/carbbank.json'
    with open(out_file, "w") as outfile:
        outfile.write(json_data)

    print (f"Saved {out_file}")

    # write to csv file
    headers = []
    for value in entry_dict.values():
        for header in value.keys():
            if header not in headers:
                headers.append(header)

    out_file = '/home/karinamartinez/carbbank.csv'
    with open(out_file, "w") as outfile:
        csv_writer = csv.writer(outfile,quoting=csv.QUOTE_ALL)
        count = 0
        for record in entry_dict.values():
            if count == 0:
                csv_writer.writerow(headers)
                count += 1

            for header in headers:
                if header not in record:
                    record[header] = ""

            sorted_dict = {i: record[i] for i in headers}
            csv_writer.writerow(sorted_dict.values())

    print (f"Saved {out_file}")
            
    

if __name__ == '__main__':
    main()