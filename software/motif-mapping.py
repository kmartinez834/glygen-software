#!/usr/bin/python

'''
This file will generate a mapping file with motif name and ids for Glycan Highlight widget

Example:
[
    {
        "id" : "GGM.000001",
        "name": "Type 2 LN"
    },
    {
        "id" : "GGM.000005",
        "name": "Type 1 LN"
    },
]'''


import os
import glob
import csv
import json

def main():

    mapping_list = []

    motif_file = "/data/projects/glygen/downloads/glytoucan/current/export/allmotifs.tsv"

    with open(motif_file, "r") as in_file:
        infile = csv.reader(in_file, delimiter="\t")

        for row in infile:
            motif_id,prop,motif_name = row[0],row[1],row[2]
            if prop == 'PreferredName':
                mapping_list.append(dict(id=motif_id,name=motif_name))
        
    json_data = json.dumps(mapping_list, indent=4)

    # Writing to sample.json
    out_file = '/data/projects/glygen/downloads/export_files/for_uga/motif_mapping.json'
    with open(out_file, "w") as outfile:
        outfile.write(json_data)

    print (f"Saved {out_file}")

if __name__ == '__main__':
    main()