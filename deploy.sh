# python3 r1_gen_mapfile.py
# python3 r2_place_inc.py
sudo python3 r0_copy_files.py
python3 r3_pub_rst.py
cd _pub
. /xpy/bin/activate && make html
sudo rsync -avp _build/html/ /owg/
sudo chown -R www-data.www-data /owg/
