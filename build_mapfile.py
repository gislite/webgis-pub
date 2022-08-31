# -*- coding: utf-8 -*-

'''
Running with python3, with markdown module.
'''


import os

import subprocess


if os.path.exists('./owg/ms_tmp'):
    pass
else:
    os.makedirs('./owg/ms_tmp')



############################################################

pwd = os.path.abspath(os.path.split(__file__)[0])

src_ws = os.path.join(pwd, 'templates')


def gen_ms_files(src_ws):
    # src_ws = os.path.abspath(src_ws)
    print(src_ws)
    src_ws = os.path.abspath(src_ws)
    the_dirs = os.listdir(src_ws)
    the_dirs = [x for x in the_dirs]
    for the_dir in the_dirs:
        print('=' * 40)

        inws = os.path.join(src_ws, the_dir)
        print(inws)
        if os.path.isdir(inws):
            print('-' * 40)
            print(inws)
            os.chdir(inws)
            if os.path.exists(os.path.join(inws, 'script_mapfile_pub.sh')):
                print('a' * 40)
                subprocess.run('sh script_mapfile_pub.sh', shell=True)

            if os.path.exists(os.path.join(inws, 'script_gen_diff.py')):
                print('a' * 40)
                subprocess.run('python3 script_gen_diff.py', shell=True)
            os.chdir(src_ws)


def run_it():
    gen_ms_files(src_ws)


if __name__ == '__main__':
    run_it()
