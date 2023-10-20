#!/bin/bash  

# define resource
resource=glytoucan

# add the time_stamped_folder
cd /data/projects/glygen/downloads/$resource/

new_dir=gtc_$(date +%m_%d_%Y)
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir
wget https://github.com/glygen-glycan-data/PyGly/archive/refs/tags/GlyGen-GlycanData-Export-Current.zip &&

# unzip export folder
unzip GlyGen-GlycanData-Export-Current.zip

# move export folder to downloads, delete unused PyGly directory
mv PyGly-GlyGen-GlycanData-Export-Current/smw/glycandata/export/ /data/shared/glygen/downloads/$resource/$new_dir/
rm -rf PyGly-GlyGen-GlycanData-Export-Current/
rm -rf GlyGen-GlycanData-Export-Current.zip

# run unzip.sh program in new export folder
cd /data/shared/glygen/downloads/$resource/$new_dir/export/ && bash /software/glygen/legacy/unzip.sh 

# run glycan_images.sh program in new export folder
cd /data/shared/glygen/downloads/$resource/$new_dir/export/ && bash /software/glygen/legacy/glycan_images.sh

# prepare glycoctxml files
cd /data/shared/glygen/downloads/$resource/$new_dir/export/
mkdir glycoctxml
cat glycoctxml.zip.* > glycoctxml/glycoctxml_all.zip
cd glycoctxml
unzip glycoctxml_all.zip

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current
