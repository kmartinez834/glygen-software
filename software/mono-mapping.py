#!/usr/bin/python

'''
This file will generate a residue mapping file with hierarchy to use in Glycan Highlight widget

Example:
[
        {
            "id": "Hex",
            "name": "Hexose",
            "children" : [
                {
                    "id": "Gal",
                    "name": "Gal"
                }
            ]
        }'''


import os
import glob
import csv
import json

def main():

    subsumption = {}
    mapping_list = []

    iupac_syms = "/data/projects/glygen/downloads/glytoucan/current/export/iupac_syms.tsv"
    res_names = "/data/projects/glygen/generated/misc/monosaccharide_residue_name.csv"

    with open(iupac_syms, "r") as in_file:
        infile = csv.reader(in_file, delimiter="\t")

        header = True
        for row in infile:
            if header == True:
                header = False
                continue
            id = row[-1]
            child = row[0]
            if id not in subsumption and id != '-':
                subsumption[id]=[child]
            elif id != '-':
                subsumption[id].append(child)
            elif child not in subsumption:
                subsumption[child]=[]

    residue_names = {}

    with open(res_names, "r") as in_file:
        infile = csv.reader(in_file, delimiter=",")

        header = True
        for row in infile:
            if header == True:
                header = False
                continue
            residue_names[row[0]]=row[1]

    for key,value in subsumption.items():
        key_dict = dict(id=key,name=residue_names[key],children=[])
        for child in value:
            child_dict = dict(id=child,name=residue_names[child])
            key_dict['children'].append(child_dict)
        mapping_list.append(key_dict)
    
    json_data = json.dumps(mapping_list, indent=4)

    # Writing to sample.json
    out_file = '/data/projects/glygen/downloads/export_files/for_uga/mono_mapping.json'
    with open(out_file, "w") as outfile:
        outfile.write(json_data)

    print (f"Saved {out_file}")

if __name__ == '__main__':
    main()