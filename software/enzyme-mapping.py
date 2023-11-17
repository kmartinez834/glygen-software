#!/usr/bin/python

'''
This file will generate a mapping file with enzyme name, ids and organism for Glycan Highlight widget

Example:
[
    {
        "id" : "P42867",
        "name": "Dpagt1",
         "tax_common_name": "Mouse",
         "tax_name": "Mus musculus"
    },
    {
        "id" : "P27808",
        "name": "Mgat1",
         "tax_common_name": "Mouse",
         "tax_name": "Mus musculus"
    },
]'''


import os
import glob
import csv
import json

def main():

    species_dict = {}
    seen = []
    mapping_list = []

    enzyme_file = "/data/projects/glygen/downloads/sandbox/current/glycotree_annotated_glycans.tsv"
    species_file = "/data/projects/glygen/generated/misc/species_info.csv"

    with open(species_file, "r") as in_file:
        infile = csv.reader(in_file, delimiter=",")

        header = True
        for row in infile:
            if header == True:
                header = False
                continue
            long_name, common_name = row[2],row[3]
            species_dict[long_name] = common_name
            

    with open(enzyme_file, "r") as in_file:
        infile = csv.reader(in_file, delimiter="\t")

        header = True
        for row in infile:
            if header == True:
                header = False
                continue
            if len(row) < 9:
                continue

            uniprot,gene_name,tax_common_name,species = row[3],row[4],species_dict[row[-1]],row[-1]
            if 0 in [i.find(uniprot) for i in seen]:
                continue
            else:
                seen.append(uniprot)   
                mapping_list.append(dict(id=uniprot,name=gene_name,tax_common_name=tax_common_name,tax_name=species))
        
    
    json_data = json.dumps(mapping_list, indent=4)

    # Writing to sample.json
    out_file = '/data/projects/glygen/generated/misc/enzyme_mapping.json'
    with open(out_file, "w") as outfile:
        outfile.write(json_data)

    print (f"Saved {out_file}")

if __name__ == '__main__':
    main()