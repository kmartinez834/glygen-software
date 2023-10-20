#!/bin/bash  

# define resource
resource=oma

# add the time stamped folder
cd /data/projects/glygen/downloads/$resource/

new_dir=$(date +%Y_%m_%d)
mkdir $new_dir

# download files to new folder
cd /data/projects/glygen/downloads/$resource/$new_dir

wget -O human_rat_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=HUMAN&p2=RATNO&p3=UniProt"
wget -O human_mouse_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=HUMAN&p2=MOUSE&p3=UniProt"
wget -O human_fruitfly_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=HUMAN&p2=DROME&p3=UniProt"
wget -O human_yeast_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=HUMAN&p2=YEAST&p3=UniProt"
wget -O human_dicty_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=HUMAN&p2=DICDI&p3=UniProt"


sleep 7 && 
echo "Human orthologs successfully downloaded..."

wget -O rat_human_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=RATNO&p2=HUMAN&p3=UniProt"
wget -O rat_mouse_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=RATNO&p2=MOUSE&p3=UniProt"
wget -O rat_fruitfly_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=RATNO&p2=DROME&p3=UniProt"
wget -O rat_yeast_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=RATNO&p2=YEAST&p3=UniProt"
wget -O rat_dicty_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=RATNO&p2=DICDI&p3=UniProt"


sleep 7 && 
echo "Rat orthologs successfully downloaded..."

wget -O mouse_human_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=MOUSE&p2=HUMAN&p3=UniProt"
wget -O mouse_rat_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=MOUSE&p2=RATNO&p3=UniProt"
wget -O mouse_fruitfly_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=MOUSE&p2=DROME&p3=UniProt"
wget -O mouse_yeast_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=MOUSE&p2=YEAST&p3=UniProt"
wget -O mouse_dicty_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=MOUSE&p2=DICDI&p3=UniProt"


sleep 7 && 
echo "Mouse orthologs successfully downloaded..."

wget -O fruitfly_human_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DROME&p2=HUMAN&p3=UniProt"
wget -O fruitfly_rat_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DROME&p2=RATNO&p3=UniProt"
wget -O fruitfly_mouse_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DROME&p2=MOUSE&p3=UniProt"
wget -O fruitfly_yeast_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DROME&p2=YEAST&p3=UniProt"
wget -O fruitfly_dicty_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DROME&p2=DICDI&p3=UniProt"

sleep 7 && 
echo "Fruitfly orthologs successfully downloaded..."

wget -O yeast_human_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=YEAST&p2=HUMAN&p3=UniProt"
wget -O yeast_rat_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=YEAST&p2=RATNO&p3=UniProt"
wget -O yeast_mouse_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=YEAST&p2=MOUSE&p3=UniProt"
wget -O yeast_fruitfly_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=YEAST&p2=DROME&p3=UniProt"
wget -O yeast_dicty_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=YEAST&p2=DICDI&p3=UniProt"

sleep 7 && 
echo "Yeast orthologs successfully downloaded..."

wget -O dicty_human_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DICDI&p2=HUMAN&p3=UniProt"
wget -O dicty_rat_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DICDI&p2=RATNO&p3=UniProt"
wget -O dicty_mouse_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DICDI&p2=MOUSE&p3=UniProt"
wget -O dicty_fruitfly_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DICDI&p2=DROME&p3=UniProt"
wget -O dicty_yeast_oma_orthologs.txt --user-agent="Mozilla" "https://omabrowser.org/cgi-bin/gateway.pl?f=PairwiseOrthologs&p1=DICDI&p2=YEAST&p3=UniProt"

sleep 7 && 
echo "Dicty orthologs successfully downloaded..."

# update new folder permissions
chmod -R 775 /data/shared/glygen/downloads/$resource/$new_dir/

# create symbolic link
cd /data/projects/glygen/downloads/$resource/
rm current
ln -s $new_dir current

sleep 7 &&
echo "Download Complete"
