#!/bin/bash  

# define resource
resource=glyconnect

# add the time stamped folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%Y_%m_%d)
mkdir $new_dir

# download files to new folder & create symbolic links
cd /data/projects/glygen/downloads/$resource/$new_dir

wget -O glyconnect_human.json https://glyconnect.expasy.org/api/glycosylations?taxonomy=Homo%20sapiens &&
wget -O glyconnect_rat.json https://glyconnect.expasy.org/api/glycosylations?taxonomy=Rattus%20norvegicus &&
wget -O glyconnect_mouse.json https://glyconnect.expasy.org/api/glycosylations?taxonomy=Mus%20musculus &&
wget -O glyconnect_sarscov2.json 'https://glyconnect.expasy.org/api/glycosylations?taxonomy=Severe%20acute%20respiratory%20syndrome%20coronavirus%202%20(2019-nCoV)' && 
wget -O glyconnect_fruitfly.json https://glyconnect.expasy.org/api/glycosylations?taxonomy=Drosophila%20melanogaster &&
wget -O glyconnect_yeast.json https://glyconnect.expasy.org/api/glycosylations?taxonomy=Saccharomyces%20cerevisiae && 
wget -O glyconnect_dictyostelium.json https://glyconnect.expasy.org/api/glycosylations?taxonomy=Dictyostelium%20discoideum &&

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current
