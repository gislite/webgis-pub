# python3 r1_gen_mapfile.py
# python3 r2_place_inc.py
#
#
# 构建完英文版本后运行
# set -e

cd _pub
# 换域名
python3  /home/bk/bkcase/webgis_cn/helper_replace_pub_cn.py xx_rst/

make gettext
sphinx-intl update -p _build/gettext  -d xx_rst/locales -l zh
# 更新 po files
python3  /home/bk/bkcase/webgis_cn/helper_chuli_locales.py

# 构建后部署
make -e SPHINXOPTS="-Dlanguage='zh'" html
sudo rsync -avp _build/html/ /owg/
sudo chown -R www-data:www-data /owg/
#
# cd /owg  && sudo python3 /home/bk/bkcase/webgis_cn/add_ad.py  1 2 3 4 5
#

