#!/bin/bash  

# define resource
resource=mcw_oglcnac

# add the time stamped folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%Y_%m_%d)
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget -b -q --no-check-certificate "https://www.oglcnac.mcw.edu/download/?oglcnac_format=csv&download_oglcnac=download_oglcnac&oglcnac_organisms=Homo+sapiens" -O human_o_glcnacome_mcw.csv
wget -b -q --no-check-certificate "https://www.oglcnac.mcw.edu/download/?oglcnac_format=csv&download_oglcnac=download_oglcnac&oglcnac_organisms=Mus+musculus" -O mouse_o_glcnacome_mcw.csv &&
wget -b -q --no-check-certificate "https://www.oglcnac.mcw.edu/download/?oglcnac_format=csv&download_oglcnac=download_oglcnac&oglcnac_organisms=Rattus+norvegicus" -O rat_o_glcnacome_mcw.csv &&
wget -b -q --no-check-certificate "https://www.oglcnac.mcw.edu/download/?oglcnac_format=csv&download_oglcnac=download_oglcnac&oglcnac_organisms=Drosophila+melanogaster" -O fruitfly_o_glcnacome_mcw.csv &&
wget -b -q --no-check-certificate "https://www.oglcnac.mcw.edu/download/?oglcnac_format=csv&download_oglcnac=download_oglcnac&oglcnac_organisms=Saccharomyces+cerevisiae" -O yeast_o_glcnacome_mcw.csv &&

sleep 10 &&
echo "MSG 1: Download completed."

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/ &&

# create symbolic links to the files according to species

cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current

sleep 5
echo "MSG 2: Download is ready, process completed."



