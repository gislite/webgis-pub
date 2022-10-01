# -*- coding: utf-8 -*-

'''
Running with python3, with markdown module.
'''

import os

import subprocess

from pathlib import Path

if os.path.exists('./owg/ms_tmp'):
    pass
else:
    os.makedirs('./owg/ms_tmp')

############################################################

pwd = os.path.abspath(os.path.split(__file__)[0])

src_ws = Path(os.path.join(pwd, 'templates'))

def run_it():
    for wfile in src_ws.rglob('*'):
        if wfile.name == 'script_mapfile_pub.sh':
            os.chdir(wfile.parent)
            subprocess.run('sh script_mapfile_pub.sh', shell=True)
    for wfile in src_ws.rglob('*'):
        if wfile.name == 'script_gen_diff.py':
            os.chdir(wfile.parent)
            subprocess.run('python3 script_gen_diff.py', shell=True)



if __name__ == '__main__':
    run_it()
