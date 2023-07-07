# -*- coding: utf-8 -*-

'''
Running with python3, with markdown module.
'''

import os

import subprocess

from pathlib import Path

# if os.path.exists('./owg/ms_tmp'):
#     pass
# else:
#     os.makedirs('./owg/ms_tmp')

############################################################

def run_it(src_ws):
    for wfile in src_ws.rglob('*'):
        if wfile.name == 'script_mapfile_pub.sh':
            print(wfile)
            # os.chdir(wfile.parent)
            subprocess.run('sh script_mapfile_pub.sh', shell=True, cwd = wfile.parent)
    for wfile in src_ws.rglob('*'):
        if wfile.name == 'script_gen_diff.py':
            print(wfile)
            # os.chdir(wfile.parent)
            subprocess.run('python3 script_gen_diff.py', shell=True, cwd = wfile.parent)



if __name__ == '__main__':
    # pwd = os.path.abspath(os.path.split(__file__)[0])

    # src_ws = Path(os.path.join(pwd, 'templates'))
    # run_it(src_ws)
    src_ws = Path( 'webgis-src')
    if src_ws.exists():
        run_it(src_ws)
    else:
        print('The directory not exists.')

