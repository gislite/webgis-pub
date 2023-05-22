# -*- coding: utf-8 -*-

'''
用来检查 Mapfile 的差异
'''
import os
import datetime
import difflib
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

def _read_file( file):
    """
    读取文件内容，以列表形式返回
    :param file: 文件路径
    :return:
    """
    try:
        with open(file, "rb") as fp:
            # 二进制方式读取文件内容，并转换为str类型
            lines = fp.read().decode('utf-8')
            # 按行进行分割
            text = lines.splitlines()
            # print text
            return text
    except Exception as e:
        print("ERROR: %s" % str(e))


def compare_file( file1, file2):
    """
    比较文件，生成html格式
    :param file1: 第1个文件路径
    :param file2: 第2个文件路径
    :param out_file: 比较结果文件路径
    :return:
    """

    sig1 = os.path.splitext(file1)[0].split('_')[-1]
    sig2 = os.path.splitext(file2)[0].split('_')[-1]
    out_file = 'yy_diff_{}_{}.html'.format(sig1, sig2)
 
    file1_content = _read_file(file1)
    file2_content = _read_file(file2)

    compare = difflib.HtmlDiff()
    compare_result = compare.make_file(file1_content, file2_content)
    with open(out_file, 'w') as fp:
        fp.writelines(compare_result)

if __name__ == '__main__':
    diff_it('mfa2.map', 'mfa1.map')
    compare_file('mfa2.map', 'mfa1.map')


    diff_it('mfa3.map', 'mfa2.map')
    diff_it('mfa4.map', 'mfa3.map')
    diff_it('mfa5.map', 'mfa4.map')
    diff_it('mfa6.map', 'mfa5.map')
    diff_it('mfa8.map', 'mfa6.map')
    diff_it('mfd8.map', 'mfa5.map')
    diff_it('mfs8.map', 'mfs2.map')
