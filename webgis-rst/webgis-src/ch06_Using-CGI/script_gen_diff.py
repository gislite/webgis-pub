# -*- coding: utf-8 -*-

'''
用来检查 Mapfile 的差异
'''
import os
import datetime

from difflib import HtmlDiff

tmpl = '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title></title>
    <style type="text/css">
        table.diff {font-family:Courier; border:medium;}
        .diff_header {background-color:#e0e0e0}
        td.diff_header {text-align:right}
        .diff_next {background-color:#c0c0c0}
        .diff_add {background-color:#aaffaa}
        .diff_chg {background-color:#ffff77}
        .diff_sub {background-color:#ffaaaa}
    </style></head><body>'''


def diff_table(rawinfo, newinfo):
    '''
    Generate the difference as the table format.
    :param rawinfo:
    :param newinfo:
    :return:
    '''
    return HtmlDiff.make_table(HtmlDiff(), rawinfo.split('\n'), newinfo.split('\n'),
                               context=True,
                               numlines=1)


def get_diff_recent(hou, qian):
    '''
    Generate the difference of posts. recently.
    '''
    diff_str = ''

    infobox = diff_table(hou, qian)

    # diff_str = diff_str + '<h3>CONTENT:{0}</h3>'.format(
    #     'aa'
    # ) + infobox + '</hr>'

    return infobox


def diff_it(infile1, infile2):
    sig1 = os.path.splitext(infile1)[0].split('_')[-1]
    sig2 = os.path.splitext(infile2)[0].split('_')[-1]
    outname = 'xx_diff_{}_{}.htmp'.format(sig1, sig2)
    aa = get_diff_recent(open(infile2).read(), open(infile1).read())
    with open(outname, 'w') as fo:
        # fo.write(tmpl)
        fo.write(aa)
        # fo.write('''</body></html>''')


if __name__ == '__main__':
    diff_it( 'mfd3.map', 'mfd2.map')
    diff_it( 'mfd2.map', 'mfd1.map')

    diff_it( 'mfp2.map', 'mfp1.map')
    diff_it( 'mfp3.map', 'mfp2.map')
    diff_it( 'mfp4.map', 'mfp3.map')

