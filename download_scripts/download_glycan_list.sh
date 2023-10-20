#!/bin/bash  

# define resource and version
resource=glycan_list

# add the time_stamped_folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%m_%d_%Y)
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget https://raw.githubusercontent.com/glygen-glycan-data/PyGly/GlyGen-GlycanData-Export-Current/smw/glycandata/data/glytoucan_allacc.txt &&
wget https://raw.githubusercontent.com/glygen-glycan-data/PyGly/GlyGen-GlycanData-Export-Current/smw/glycandata/data/glytoucan_archived.txt && 
wget https://raw.githubusercontent.com/glygen-glycan-data/PyGly/GlyGen-GlycanData-Export-Current/smw/glycandata/data/glytoucan_replaced.txt && 

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current