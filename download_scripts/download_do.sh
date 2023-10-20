#!/bin/bash  

# define resource
resource=do

# add the glyconnect time_stamped_folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%Y_%m_%d)/
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget -q https://github.com/DiseaseOntology/HumanDiseaseOntology/raw/main/src/ontology/releases/doid.owl

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current

sleep 15 &&
echo "Download Complete"