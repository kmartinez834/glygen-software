#!/bin/bash  

# define resource
resource=mgi

# add the time stamped folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%Y_%m_%d)
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir
wget -O -q mgi_homologs.tsv --user-agent="Mozilla" "http://www.informatics.jax.org/downloads/reports/HOM_AllOrganism.rpt"

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current

sleep 15
echo "Download Complete"
