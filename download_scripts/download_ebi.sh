#!/bin/bash  

# define resource
resource=ebi

# add the time stamped folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%Y_%m_%d)/
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget -b -q ftp://ftp.ebi.ac.uk/pub/contrib/glygen/current_release/* &&
sleep 180 &&

echo "MSG 1: Download completed, unzipping files."

# unzip the downloaded folder

cd /data/projects/glygen/downloads/$resource/$new_dir
gunzip /data/projects/glygen/downloads/$resource/$new_dir/*.gz &&

echo "MSG 2: unzipping completed, changing folder permissions and creating softlinks."


# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/ &&


# create symbolic links to the files according to species

cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current

sleep 5
echo "MSG 3: Download is ready, process completed."