#!/usr/bin/python
import os,sys
import glob
import csv
import json
from optparse import OptionParser


def main():

    usage = "\n%prog  [options]"
    parser = OptionParser(usage,version="%prog version___")
    parser.add_option("-v","--ver",action="store",dest="ver",help="Data version [e.g: 1.11.2]")
    (options,args) = parser.parse_args()
    for key in ([options.ver]):
        if not (key):
            parser.print_help()
            sys.exit(0)

    rel = options.ver

    data_dir = (f"/data/shared/glygen/releases/data/v-{rel}/reviewed/")
    file_list = glob.glob(data_dir+'*proteoform_glycosylation_site*')

    known_sites = {}
    pmids = []

    for in_file in file_list:

        if in_file.split(".")[-2] == "stat": continue
        with open(in_file, "r") as infile:

            FR = csv.reader(infile, delimiter=",")
            row_ct = 0

            for row in FR:
                if row_ct ==0 and any(field.find("uniprotkb_canonical_ac") for field in row) == True:
                    row_ct += 1
                    uniprotkb_ac, position, xref_key, xref_id = row.index("uniprotkb_canonical_ac"), row.index("glycosylation_site_uniprotkb"), row.index("xref_key"), row.index("xref_id")
                    continue

                protein, site = row[uniprotkb_ac].split("-")[0], row[position]
                if site == "":
                    site = "x"
                
                if row[xref_key] == "protein_xref_pubmed":
                    pmids.append(row[xref_id])
   
                if protein not in known_sites:
                    known_sites[protein] = [site]
                    
                elif site not in known_sites[protein]:
                    known_sites[protein].append(site)

    
    lit_mining_file = "/data/projects/glygen/downloads/lit_min/udel_pipeline_output/summary/set_30k.csv"
    #lit_mining_file = "/data/projects/glygen/downloads/lit_min/current/proteoform_glycosylation_sites_literature_mining.csv"
    seen = []

    new_sites_list = [["pmid","uniprotkb_ac","amino_acid","position","species","qc_flag","protein_flag","site_flag","pmid_flag"]]
    #new_sites_list = [["uniprotkb_ac","amino_acid","glycosylation_site","evidence","protein_flag","site_flag","pmid_flag"]]
    with open(lit_mining_file, "r") as infile:
        FR = csv.reader(infile, delimiter=",")

        row_ct = 0
        for row in FR:
            if row_ct ==0:
                row_ct += 1
                continue
            
            pmid_new, protein_new, site_new = row[0], row[1], row[3]
            #pmid_new, protein_new, site_new = row[3], row[0], row[2]

            seen.append(protein_new)

            if protein_new not in known_sites:
                row.append("new_protein")
                if site_new == "x":
                    row.append("no_site")
                else:
                    row.append("new_site")
            else:
                row.append("old_protein")
                if site_new == "x":
                    row.append("no_site")
                elif site_new not in known_sites[protein_new]:
                    row.append("new_site")
                else:
                    row.append("old_site")
            
            if pmid_new not in pmids:
                row.append("new_pmid")
            else:
                row.append("old_pmid") 

            new_sites_list.append(row)
            

    outfile = "/data/projects/glygen/generated/misc/lit_mining_new_sites.csv"
    with open(outfile, "w") as out_file:
        writer = csv.writer(out_file, delimiter = ',', quoting=csv.QUOTE_ALL)
        writer.writerows(new_sites_list)

    '''lit_mining_file = "/data/projects/glygen/downloads/lit_min/udel_pipeline_output/summary/set_30k.csv"
    same_protein = 0
    seen2 = []
    with open(lit_mining_file, "r") as infile:
        FR = csv.reader(infile, delimiter=",")

        for row in FR:
            pmid_new, protein_new, site_new = row[0], row[1], row[3]

            if protein_new not in seen2:
                seen2.append(protein_new)
                if protein_new in seen:
                    same_protein += 1

                
    print (same_protein)'''

if __name__ == '__main__':
    main()