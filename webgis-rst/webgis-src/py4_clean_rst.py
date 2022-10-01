# -*- coding: utf-8 -*-


import os
import shutil



def do_for_chapter(secws):
    sec_list = os.listdir(secws)
    sec_list.sort()

    index = 1
    rst_new_list = []
    for sec_dir in sec_list:

        if sec_dir.startswith('sec')  :
            tt = sec_dir.split('_')
            feaname = '_'.join(tt[1:])

            outname = 'sec{0}_{1}'.format(index, feaname)
            index = index + 1
            rst_new_list.append(outname)
            inpath = os.path.join(secws, sec_dir)
            outpath = os.path.join(secws, outname)

            shutil.move(inpath, outpath)

    if os.path.exists(os.path.join(secws, 'chapter.rst')):
        pass
    else:
        return False
    sec_cnt = open(os.path.join(secws, 'chapter.rst')).readlines()

    with open(os.path.join(secws, 'chapter.rst'), 'w') as fo:
        for uu in sec_cnt:
            if '.. toctree::' in uu:
                break
            else:
                fo.write(uu)
        fo.write('''\n.. toctree::\n   :maxdepth: 2\n\n''')
        for x in rst_new_list:
            fo.write('   {0}/section\n'.format(x))


def do_for_book(secws):
    sec_list = os.listdir(secws)
    sec_list.sort()

    index = 1
    rst_new_list = []
    for sec_dir in sec_list:
        if sec_dir.startswith('ch'):
            tt = sec_dir.split('-')
            feaname = '-'.join(tt[1:])

            outname = 'ch{0}-{1}'.format(str(index).zfill(2), feaname)

            inpath = os.path.join(secws, sec_dir)
            outpath = os.path.join(secws, outname)

            shutil.move(inpath, outpath)

            rst_new_list.append(outname)

            index = index + 1
    if os.path.exists(os.path.join(secws, 'index.rst')):
        pass
    else:
        return False
    sec_cnt = open(os.path.join(secws, 'index.rst')).readlines()

    with open(os.path.join(secws, 'index.rst'), 'w') as fo:
        for uu in sec_cnt:
            if '.. toctree::' in uu:
                break
            else:
                fo.write(uu)
        fo.write('''.. toctree::
   :maxdepth: 2
   :numbered: 2

''')
        for x in rst_new_list:
            fo.write('   {0}/chapter\n'.format(x))

#         fo.write('''
# Indices and tables
# ==================
#
# * :ref:`genindex`
# * :ref:`modindex`
# * :ref:`search`
#         ''')


def clean_section():
    for wroot, wdirs, wfiles in os.walk('./'):
        for wdir in wdirs:
            if wdir.startswith('sec'):
                inws = os.path.join(wroot, wdir)
                # do_for_section(inws)
            elif wdir.startswith('ch'):
                inws = os.path.join(wroot, wdir)
                do_for_chapter(inws)
    do_for_book(os.getcwd())


if __name__ == '__main__':
    clean_section()
