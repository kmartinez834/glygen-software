#!/bin/bash  

# define resource
resource=sandbox

# add the time_stamped_folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%m_%d_%Y)
mkdir $new_dir

# create accessionlist.csv and glycotree_annotated_glycans.csv
cd /software/glygen/
python3 sandbox-xref-download.py -d accessionlist
python3 sandbox-xref-download.py -d glycotree_annotated_glycans

# move files to new folder
mv /tmp/accessionlist.csv /data/projects/glygen/downloads/$resource/$new_dir
mv /tmp/glycotree_annotated_glycans.csv /data/projects/glygen/downloads/$resource/$new_dir

# download allPaths.json to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget https://raw.githubusercontent.com/glygen-glycan-data/glycoTree/master/portal/api/paths/allPaths.json

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current