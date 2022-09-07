# -*- coding:utf-8 -*-

'''
发布 OSGeo 的文档。
pip install fabric
pip install patchwork
'''

import os
from fabric import Connection

from cfg import mach

def main_deploy():

    c = Connection("{}@{}".format(mach['u'], mach['h']), port=11022, connect_kwargs={"password": mach['p']})
    with c.cd('/home/bk/deploy/GISLite/static'):
        c.run('python3 clean_sphinx.py')

    with c.cd('/home/bk/deploy/GISLite'):
        c.run('git pull')
        # c.run('sh push_code.sh')
        c.run('~/vpy_gislite/bin/python helper.py -i init')
        c.run('source ~/vpy_gislite/bin/activate && sh run_import_tuto.sh')
        c.run('sudo supervisorctl restart gislite1')
        c.run('sudo supervisorctl restart gislite2')
        c.run('sudo service nginx restart')
        c.run('source ~/vpy_gislite/bin/activate && python helper.py -i sitemap')
        c.run('mv xx_sitemap.txt static/sitemap.txt')


if __name__ == '__main__':

    main_deploy()
