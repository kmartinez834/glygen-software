#!/bin/bash  

echo "X X X X X X The process takes around 45mins to complete X X X X X X"
# define resource
resource=ncbi/refseq

# add the time stamped folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%Y_%m_%d)/
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/human.*.protein.gpff.gz
sleep 120 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/human.*.protein.faa.gz &&
sleep 120 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/M_musculus/mRNA_Prot/mouse.*.protein.gpff.gz &&
sleep 120 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/M_musculus/mRNA_Prot/mouse.*.protein.faa.gz &&
sleep 120 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/R_norvegicus/mRNA_Prot/rat.*.protein.gpff.gz &&
sleep 120 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/R_norvegicus/mRNA_Prot/rat.*.protein.faa.gz &&
sleep 120 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/*protein.gpff.gz &&
sleep 120 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/*protein.faa.gz &&
sleep 120 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/release/invertebrate/invertebrate.*.protein.gpff.gz &&
sleep 180 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/release/invertebrate/invertebrate.*.protein.faa.gz &&
sleep 180 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/release/fungi/fungi.*.protein.gpff.gz &&
sleep 180 &&
wget -b -q  ftp://ftp.ncbi.nlm.nih.gov/refseq/release/fungi/fungi.*.protein.faa.gz &&
sleep 180 &&
wget -b -q https://ftp.ncbi.nlm.nih.gov/refseq/release/protozoa/*.protein.gpff.gz &&
sleep 180 &&
wget -b -q https://ftp.ncbi.nlm.nih.gov/refseq/release/protozoa/*.protein.faa.gz &&
sleep 180 &&
echo "MSG 1: Download completed, unzipping files."


# unzip the downloaded folder

cd /data/projects/glygen/downloads/$resource/$new_dir
gunzip /data/projects/glygen/downloads/$resource/$new_dir/*.gz &&

sleep 80 &&
echo "MSG 2: unzipping completed, renaming files."

# renaming files
cd /data/projects/glygen/downloads/$resource/$new_dir
cat human.*.protein.gpff > refseq_protein_all_9606.gpff
cat human.*.protein.faa > refseq_protein_all_9606.faa
cat mouse.*.protein.gpff > refseq_protein_all_10090.gpff
cat mouse.*.protein.faa > refseq_protein_all_10090.faa
cat rat.*.protein.gpff > refseq_protein_all_10116.gpff
cat rat.*.protein.faa > refseq_protein_all_10116.faa
cat viral.*.protein.gpff > refseq_protein_all_viral.gpff
cat viral.*.protein.faa > refseq_protein_all_viral.faa
cat invertebrate.*.protein.gpff > refseq_protein_all_7227.gpff &&
cat invertebrate.*.protein.faa > refseq_protein_all_7227.faa &&
cat fungi.*.protein.gpff > refseq_protein_all_559292.gpff &&
cat fungi.*.protein.faa > refseq_protein_all_559292.faa &&
cat protozoa.*.protein.gpff > refseq_protein_all_44689.gpff &&
cat protozoa.*.protein.faa > refseq_protein_all_44689.faa &&

sleep 60 &&
echo "MSG 3: Files renamed, changing folder permissions and creating softlinks."

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/ &&

sleep 15

# create symbolic links to the files according to species

cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current

sleep 5
echo "MSG 4: Download is ready, process completed."
