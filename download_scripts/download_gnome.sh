#!/bin/bash  

# define resource
resource=gnome

# add the time_stamped_folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%m_%d_%Y)
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget https://raw.githubusercontent.com/glygen-glycan-data/GNOme/master/restrictions/GlyGen.valid-accessions.txt &&
wget https://raw.githubusercontent.com/glygen-glycan-data/GNOme/master/restrictions/GlyGen_NGlycans.valid-accessions.txt &&
wget https://raw.githubusercontent.com/glygen-glycan-data/GNOme/master/restrictions/GlyGen_OGlycans.valid-accessions.txt &&
wget https://raw.githubusercontent.com/glygen-glycan-data/GNOme/master/restrictions/GlycoTree_NGlycans.valid-accessions.txt &&
wget https://raw.githubusercontent.com/glygen-glycan-data/GNOme/master/restrictions/GlycoTree_OGlycans.valid-accessions.txt &&

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current