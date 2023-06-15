# -*- coding: utf-8 -*-

'''
Running with python3, with markdown module.
'''

from pathlib import Path
import logging

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

#
env = Environment(loader=FileSystemLoader('.'))


def get_html_title(html_file):
    uu = BeautifulSoup(open(html_file), 'lxml')
    return uu.title.text


def render_html(tmpl, outfile, **kwargs):
    '''
    注意一点: 其中path需要为当前python文件所在目录的完整路径，
    get_template内部的参数为html模板相对于该python文件所在目录的路径(相对路径)。
    '''

    template = env.get_template(tmpl)
    output_from_parsed_template = template.render(kwargs)

    # to save the results
    with open(outfile, "w") as fh:
        fh.write(output_from_parsed_template)


import os

logger = logging.getLogger('fib')

# 设置logger的level为DEBUG
logger.setLevel(logging.DEBUG)

# 创建一个输出日志到控制台的StreamHandler
hdr = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
hdr.setFormatter(formatter)

# 给logger添加上handler
logger.addHandler(hdr)


def gen_html_pages(src_ws):
    '''
    根据输入的 MarkDown 文件，生成 HTML 结果。
    '''

    for wfile in src_ws.rglob('*.jinja2'):
        out_html_file = Path('/tmp') / (wfile.stem + '.html')
        print(wfile)
        render_html(
            str(wfile), str(out_html_file),
            # dir_title=dir_title,
            # title=get_html_title(jinja2_file),
            # leftnav=format_leftnav(list_main[idx_dir]['list_md'], slug),
            # nav=nav_formated,
            # cntnav=format_cntnav(cnt_title_arr),
            # SITE_URL = SITE_URL,
            # first_nav=str(src_ws).split('_')[2]
        )


def run_it():
    gen_html_pages(Path('./webgis-src'))


if __name__ == '__main__':
    run_it()
