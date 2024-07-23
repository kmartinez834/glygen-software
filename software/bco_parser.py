import glob
import os
import sys
import json    
from optparse import OptionParser

BCO_DICT = {}

def get_string(new_key,id):
    if new_key not in BCO_DICT:
        BCO_DICT[new_key] = id

def get_list(new_key,value,id):
    for item in value:
        if type(item) == dict and len(item) != 0:
            get_keys(new_key,item,id)

        elif type(item) == str and item != "":
            get_string(new_key,id)

        elif type(item) == list and len(item) != 0:
            get_list(new_key,value,id)

def get_keys(parent_key, val, id): #json has to be a dict
    for key,value in val.items():
        new_key = f"{parent_key}{key}" if parent_key == "" else f"{parent_key}.{key}"
        if type(value) == str and value != "":
            get_string(new_key,id)

        elif type(value) == dict and len(value) != 0:
            get_keys(new_key,value,id)

        elif type(value) == list and len(value) != 0:
            get_list(new_key,value,id)

def main():

    usage = "\n%prog  [options]"
    parser = OptionParser(usage,version="%prog version___")
    parser.add_option("-p","--page",action="store",dest="page",help="Page type [glycan, protein, site, publication, etc.]")
    (options,args) = parser.parse_args()
    for key in ([options.page]):
        if not (key):
            parser.print_help()
            sys.exit(0)
    user_id = os.getlogin()
    page = options.page

    file_list = glob.glob(f"/data/shared/glygen/releases/data/current/jsondb/{page}db/*.json")
    for bco_file in file_list:
        bco_id = bco_file.split("/")[-1].split(".json")[0]
        doc = json.loads(open(bco_file, "r").read())
        get_keys("",doc, bco_id)

    print (BCO_DICT)
    json_data = json.dumps(BCO_DICT, indent=4)
    out_file = f'logs/{user_id}_{page}_bco_fields.json'
    with open(out_file, "w") as outfile:
        outfile.write(json_data)

    print (f"Saved {out_file}")

if __name__ == '__main__':
    main()