#!/usr/bin/python
import os,sys
import glob
import csv
import json
from optparse import OptionParser
import tarfile

# Get file molecule and file type 
def get_mol_sep(in_file):
    mol = in_file.split("_")[0].lower()   
    file_ext = in_file.split(".")
    if file_ext[-1] in ["csv", "tsv"]:
        sep = "\t" if file_ext[-1] == "tsv" else ","
    elif file_ext[-2] == "tar" and file_ext[-1] == "gz":
        sep = "r:gz"
    else:
        sep = None
        print (f"File type not accepted: {in_file}")
    
    return mol, sep

# Print alert if glycan/protein file has no accessions 
def find_accession(file_tax_ids,mol,in_file):
    if len(file_tax_ids) == 0 and mol == "glycan":
        print (f"No GlyTouCan accession found: {in_file}")
    if len(file_tax_ids) == 0 and mol == "protein":
        print (f"No UniProtKB accession found: {in_file}")


#######################################
def main():

    usage = "\n%prog  [options]"
    parser = OptionParser(usage,version="%prog version___")
    parser.add_option("-v","--ver",action="store",dest="ver",help="BCO Dataversion [e.g: 1.11.2]")
    (options,args) = parser.parse_args()
    for key in ([options.ver]):
        if not (key):
            parser.print_help()
            sys.exit(0)
    user_id = os.getlogin()

    data_dir = "/data/projects/glygen/generated/datasets/unreviewed/"
    misc_dir = "/data/projects/glygen/generated/misc/"
    test_dir = "/home/" + user_id + "/"

    rel = options.ver

    in_file = misc_dir + "species_info.csv"
    tax_to_long_name = {}
    short_name_to_tax = {}
    with open(in_file, "r") as infile:
        FR = csv.reader(infile, delimiter=",")
        for row in FR:
            if "tax_id" in row:
                continue
            tax_to_long_name[row[0]] = row[2]
            short_name_to_tax[row[1]] = row[0]

    in_file = data_dir + "glycan_species.csv"
    glycan_dict = {}
    with open(in_file, "r") as infile:
        FR = csv.reader(infile, delimiter=",")
        for row in FR:
            glytoucan_ac,taxid = row[0],row[1]
            if "glytoucan_ac" in row:
                continue
            elif glytoucan_ac not in glycan_dict:
                glycan_dict[glytoucan_ac] = [taxid]
            elif taxid not in glycan_dict[glytoucan_ac]:
                glycan_dict[glytoucan_ac].append(taxid)

    
    file_list = glob.glob(data_dir + "*_protein_xref_uniprotkb.csv")
    protein_dict = {}
    for in_file in file_list:
        with open(in_file, "r") as infile:
            FR = csv.reader(infile, delimiter=",")
            species = in_file.split("/")[-1].split("_")[0]
            for row in FR:
                uniprotkb_ac = row[2]
                if "uniprotkb_canonical_ac" in row:
                    continue
                protein_dict[uniprotkb_ac] = species


    file_list = glob.glob(data_dir + "*")
    new_list = []
    for in_file in file_list:
        ds_name = in_file.split("/")[-1]
        if ds_name.split("_")[0] not in short_name_to_tax:
            new_list.append(ds_name)


    new_file = [["bco_id","file_name","tax_id","tax_name"]]
    for in_file in new_list:
        file_tax_ids = {}
        mol, sep = get_mol_sep(in_file)

        if mol == "glycan" and sep == "r:gz":
            tarf = tarfile.open(data_dir + in_file, sep)
            tar_names = tarf.getnames()
            for name in tar_names:
                glytoucan_ac = name.split("/")[-1].split(".")[0]
                if glytoucan_ac in glycan_dict:
                    for tax_id in glycan_dict[glytoucan_ac]:
                        file_tax_ids[tax_id] = "Seen"
            for key in file_tax_ids.keys():
                new_file.append(["",in_file,key,""])
            find_accession(file_tax_ids,mol,in_file)
            
        elif mol == "glycan" and sep != None:
            with open(data_dir + in_file, "r") as infile:
                FR = csv.reader(infile, delimiter=sep)
                glytoucan_index = 0
                for row in FR:
                    if "glytoucan_ac" in row: 
                        glytoucan_index = row.index("glytoucan_ac")
                    elif "glytoucan_ac_current" in row: 
                        glytoucan_index = row.index("glytoucan_ac_current")
                    elif "glytoucan_ac_list" in row: 
                        glytoucan_index = row.index("glytoucan_ac_list")
                    elif "id" in row: 
                        glytoucan_index = row.index("id")
                    else:
                        glytoucan_ac = row[glytoucan_index]
                        if glytoucan_ac in glycan_dict:
                            for tax_id in glycan_dict[glytoucan_ac]:
                                file_tax_ids[tax_id] = "Seen"
            for key in file_tax_ids.keys():
                new_file.append(["",in_file,key,""])
            find_accession(file_tax_ids,mol,in_file)

        elif mol == "protein" and sep != None:
            with open(data_dir + in_file, "r") as infile:
                FR = csv.reader(infile, delimiter=sep)
                protein_index = 0
                for row in FR:
                    if "uniprotkb_ac_current" in row: 
                        protein_index = row.index("uniprotkb_ac_current")
                    elif "uniprotkb_primary_accession" in row: 
                        protein_index = row.index("uniprotkb_primary_accession")
                    elif "uniprotkb_canonical_ac" in row: 
                        protein_index = row.index("uniprotkb_canonical_ac")
                    elif "uniprotkb_ac" in row: 
                        protein_index = row.index("uniprotkb_ac")
                    else:
                        protein_ac = row[protein_index]
                        if protein_ac in protein_dict:
                            tax_name = protein_dict[protein_ac]
                            file_tax_ids[tax_name] = "Seen"
            for key in file_tax_ids.keys():
                new_file.append(["",in_file,"",key])
            find_accession(file_tax_ids,mol,in_file)
        
        else:
            print (f"File not parsed: {in_file}")
         

    file_list = glob.glob(f"/data/shared/glygen/releases/data/v-{rel}/jsondb/bcodb/*.json")
    filename2bcoid = {}
    for bco_file in file_list:
        bco_id = bco_file.split("/")[-1].split(".")[0]
        doc = json.loads(open(bco_file, "r").read())
        if "io_domain" not in doc:
            continue
        if doc["io_domain"]["output_subdomain"] == []:
            continue
        file_name = doc["io_domain"]["output_subdomain"][0]["uri"]["filename"]
        file_name = file_name.strip()
        filename2bcoid[file_name] = bco_id


    for row in new_file[1:]:
        try:
            row[0] = filename2bcoid[row[1]]
        except:
            row[0] = "ERROR:NO_BCO"
            
        if row[2] != "":
            row[3] = tax_to_long_name[row[2]]
        else:
            row[2] = short_name_to_tax[row[3]]
            row[3] = tax_to_long_name[row[2]]


    outfile = misc_dir + "dataset2species.csv"
    with open(outfile, "w") as out_file:
        writer = csv.writer(out_file, delimiter = ',', quoting=csv.QUOTE_ALL)
        writer.writerows(new_file)

    cmd = "chmod 775 " + outfile
    os.system(cmd)
    print (f"Created file: {outfile}")

if __name__ == '__main__':
    main()

