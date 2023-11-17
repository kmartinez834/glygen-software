#!/usr/bin/python

'''
This file generates a summary for all files used in the previous release.
The summary is intended to show which files have been updated.
Checks include the previous and current file paths, size changes, creation date, 
file name, and current permissions.
'''

import os
import glob
import csv
import subprocess
import json
import datetime

# Get input files from previous release bco io domain
def get_inputs (path):
    bco_list = glob.glob(path)
    downloads = []
    for file in bco_list:
        with open(file, "r") as in_file:
            data = json.load(in_file)
            for i in data["io_domain"]["input_subdomain"]:
                if "downloads" in i["uri"]["uri"]:
                    downloads.append(i["uri"]["uri"])
    output = set(downloads)
    return output

# Get file size, creation time and permissions
def get_stats (file):
            output = os.stat(file)
            size = output.st_size
            creation_time = output.st_ctime
            permissions = oct(output.st_mode)[-3:]
            return size, creation_time, permissions


#######################################
def main():

    downloads = []
    bco_path = "/data/shared/glygen/releases/data/current/jsondb/bcodb/*.json"
    output = get_inputs(bco_path)
    user = os.getlogin()
    
    resource_dict = {}
    path = "/data/projects/glygen/downloads/"

    # Create dictionary with file names as keys
    for file in output:
        filepath = file.split("/downloads/")[1].split("/")
        resource_name, subfolders, file_name = filepath[0], filepath[1:-1], filepath[-1]
        previous_folder = path + file.split("/downloads/")[1].split(file_name)[0]

        resource_dict[file_name] = {"file_name":"",
                                    "previous_folder":previous_folder, 
                                    "current_folder":"", 
                                    "previous_ctime":"",
                                    "current_ctime":"",
                                    "ctime_flag":"",
                                    "previous_size":"", 
                                    "current_size":"",
                                    "size_flag":"", 
                                    "permissions_flag":"", 
                                    "folder_status":"", 
                                    "error_flag":""}

        # Check folder path for "current" symbolic link
        for i in range(len(subfolders)):
            new_subs = subfolders.copy()
            new_subs[i] = "current"
            sub_path = ""
            for x in new_subs:
                sub_path += x + "/"
                test_path = path + resource_name + "/" + sub_path
            if os.path.exists(test_path) == True:
                symlink = test_path.split("current")[0] + "current"
                current_folder = os.readlink(symlink)
                current_path = test_path.replace("current", current_folder).replace("//","/")
                resource_dict[file_name]["current_folder"] = current_path

    new_list = []
    row = 0
    for key, value in resource_dict.items():
        if row == 0: new_list.append([keys for keys in value.keys()])
        row += 1

        # check to make sure symbolic links are relative and not absolute
        if len(value["current_folder"]) == 0:
            value["folder_status"], value["current_folder"] = "Same folder", value["previous_folder"]
        elif len(value["previous_folder"]) != len(value["current_folder"]):
            value["folder_status"] = f"Check current folder path length: {value['current_folder']}"
        elif value["previous_folder"] == value["current_folder"]:
            value["folder_status"] = "same"
        else:
            value["folder_status"] = "different"

        # make sure current path exists
        if os.path.exists(value["current_folder"] + key) == True:
            # check if file is the same as previous
            value["previous_size"], value["previous_ctime"], permissions = get_stats(value["previous_folder"] + key)
            value["current_size"], value["current_ctime"], value["permissions_flag"] = get_stats(value["current_folder"] + key)
            if value["permissions_flag"] == "775":
                value["permissions_flag"] = "" 

            # Compare file size
            if value["previous_size"] > value["current_size"]:
                value["size_flag"] = "decrease"
            elif value["previous_size"] < value["current_size"]:
                value["size_flag"] = "increase"

            # Compare creation time
            if value["previous_ctime"] == value["current_ctime"]:  
                value["ctime_flag"] = "same"
            else:
                value["ctime_flag"] = "different"

            value["previous_ctime"] = datetime.datetime.fromtimestamp(value["previous_ctime"]).strftime("%m/%d/%Y, %H:%M:%S")
            value["current_ctime"] = datetime.datetime.fromtimestamp(value["current_ctime"]).strftime("%m/%d/%Y, %H:%M:%S")

        else:
            value["error_flag"] = f"ERROR: Path not valid, check folder and file name: {value['current_folder']}{key}"

        value["file_name"] = key
        new_list.append([value[i] for i in value])

    with open(f'/data/projects/glygen/generated/misc/{user}_download_summary.csv', 'w') as out_file:
        writer = csv.writer(out_file, delimiter = ',', quoting=csv.QUOTE_ALL)
        writer.writerows(new_list)

    
    cmd = f'chmod 775 /data/projects/glygen/generated/misc/download_summary_{user}.csv'
    os.system(cmd)

    print (f'{user}_download_summary.csv saved at /data/projects/glygen/generated/misc/')

if __name__ == '__main__':
    main()
    