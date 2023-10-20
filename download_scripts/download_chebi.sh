#!/bin/bash  

# define resource
resource=chebi

# add the glyconnect time_stamped_folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%Y_%m_%d)
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget ftp://ftp.ebi.ac.uk/pub/databases/chebi/Flat_file_tab_delimited/database_accession.tsv
wget ftp://ftp.ebi.ac.uk/pub/databases/chebi/Flat_file_tab_delimited/chebiId_inchi.tsv
wget ftp://ftp.ebi.ac.uk/pub/databases/chebi/Flat_file_tab_delimited/reference.tsv.gz
gunzip reference.tsv.gz

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current