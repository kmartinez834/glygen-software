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

def main():

    entry_dict = {}

    src_file = "/data/projects/glygen/downloads/carbbank/current/carbbank.txt"
    headers = ("AG:","AM:","AN:","AU:","BA:","BS:","CC:","CT:","DA:","DB:","FC:","MT:","NC:","NT:","PA:","PM:","SB:","SC:","SD:","SI:","ST:","structure:","TI:","TN:","VR:")

    with open(src_file, "r", encoding = 'latin-1') as in_file:
        infile = in_file.readlines()
        
        record_num = 0
        prev_line = ""
        for line in infile:
            line = line.strip("\n")
            if line.startswith("; start of record"):
                record_num += 1
                entry_dict[record_num] = {}
                continue
            elif line.startswith(("; ", "----------------","================end of record")):
                continue
            elif line.startswith(headers):
                prev_line = line
            else:
                prev_line += line

            key = prev_line.split(":")[0]
            if key in [i.split(":")[0] for i in headers]:
                value = prev_line.split(f"{key}: ")[-1]
                entry_dict[record_num][key] = value
                       
    for key,value in entry_dict.items():
        if "structure" in value:
            value.pop("structure")

    json_data = json.dumps(entry_dict, indent=4)

    # Writing to sample.json
    out_file = '/home/karinamartinez/carbbank.json'
    with open(out_file, "w") as outfile:
        outfile.write(json_data)

    print (f"Saved {out_file}")

if __name__ == '__main__':
    main()