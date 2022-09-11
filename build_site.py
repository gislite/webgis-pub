# -*- coding: utf-8 -*-

'''
Running with python3, with markdown module.
'''

import logging

from pprint import pprint
import os
import shutil
import markdown
from bs4 import BeautifulSoup
import htmlmin
from docutils.core import publish_string
from config import SITE_URL

if os.path.exists('./owg/ms_tmp'):
    pass
else:
    os.makedirs('./owg/ms_tmp')

# import render_jinja
import helper

logger = logging.getLogger('fib')
logger.setLevel(logging.DEBUG)
hdr = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
hdr.setFormatter(formatter)
logger.addHandler(hdr)

############################################################

pwd = os.path.split(__file__)[0]

src_ws = os.path.join('templates')
tpl_ws = os.path.join(pwd, 'static')
dst_ws = os.path.join(pwd, 'owg')

if os.path.exists(dst_ws):
    pass
else:
    os.makedirs(dst_ws)


def rst2html(rst_text):
    html = publish_string(rst_text, writer_name='html').decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    logger.debug(html)

    html = str(soup.find_all('div')[0])
    # pprint.pprint(html)

    intag = ['<h3', '</h3>', '<h2', '</h2>', '<h1', '</h1>', ]
    outtag = ['<h4', '</h4>', '<h3', '</h3>', '<h2', '</h2>', ]
    # for xx, yy in zip(intag, outtag):
    #     html = html.replace(xx, yy)

    return htmlmin.minify(html)


def markdown2html(markdown_text, format='md'):
    '''
    Convert markdown text to HTML. with extensions.
    :param markdown_text:   The markdown text.
    :return:  The HTML text.
    '''
    if format == 'md':
        html = markdown.markdown(
            markdown_text,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.toc',
                'markdown.extensions.codehilite',
                'markdown.extensions.meta'
            ]
        )
    else:
        html = rst2html(markdown_text)

    han_biaodians = ['。', '，', '；', '、', '！', '？']
    for han_biaodian in han_biaodians:
        html = html.replace(han_biaodian + '\n', han_biaodian)
    return htmlmin.minify(html)


'''
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-bs-toggle="dropdown">
        Dropdown link
      </a>
      <div class="dropdown-menu">
        <a class="dropdown-item" href="#">Link 1</a>
        <a class="dropdown-item" href="#">Link 2</a>
        <a class="dropdown-item" href="#">Link 3</a>
      </div>
    </li>
'''


def format_nav(list_main, chapter_slug='', sec_slug=''):
    '''
    format navigate bar.
    '''
    a_nav = '''<li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle {active}" href="#" id="navbardrop" data-bs-toggle="dropdown">
         {nav_title} 
         </a>
        <div class="dropdown-menu">
        {nav_arr}</div>
        </li>
        '''
    a_md = '<a class="dropdown-item {active}" href="{router}/{slug}-index.html">{title}</a>'

    out_str = ''

    sig_ch = False

    for idx_list, the_list in enumerate(list_main):
        sub_str = ''
        sig_it = False

        for idx_link, the_link in enumerate(the_list['list_md']):
            if the_link['slug'] == sec_slug:
                sig_it = True

            a_md_f = a_md.format(
                router=SITE_URL,
                slug=the_link['slug'],
                title=the_link['title'],
                active='active' if the_link['slug'] == sec_slug else '',
            )

            sub_str = sub_str + a_md_f

        if the_list:
            pass
        else:
            continue

        if the_list['slug'] == chapter_slug:
            sig_ch = True
        # print(the_list['list_md'][0]['slug'])
        a_nav_f = a_nav.format(
            router='',
            nav_arr=sub_str,
            # nav_slug=the_list['list_md'][0]['slug'],
            nav_title=the_list['title'],
            active='active' if (sig_it or sig_ch) else '',
        )

        sig_ch = False
        out_str = out_str + a_nav_f
    return htmlmin.minify(out_str)


def format_leftnav(the_nav, slug):
    '''
    format left navigate panel.
    '''
    a_nav = '''<div class="panel mbclass">
    <a href="{router}/{slug}.html">
    <div class="panel-heading {cls}" id="{navid}">
<h4 class="panel-title" style="text-align:left;">{title}</h4></div></a></div>
'''
    out_str = ''
    for the_idx, linav in enumerate(the_nav):
        the_nav = a_nav.format(
            slug=linav['slug'],
            title=str(the_idx + 1) + '. ' + linav['title'],
            cls='active' if linav['slug'] == slug else '',
            navid='leftnavli' if linav['slug'] == slug else '',
            router=SITE_URL
        )

        out_str = out_str + the_nav
    return htmlmin.minify(out_str)


def format_cntnav(cnt_arr):
    '''
    format contents panel.
    '''
    try:
        tpl = '''<li {sig}><a href="#{index}">{title}</a></li>'''
        out_str = ''
        for idx, title in enumerate(cnt_arr):
            the_str = tpl.format(
                index=title['key'],
                title=title['val'],
                sig=''
            )

            out_str = out_str + the_str
    except:
        out_str = '<div></div>'
    return out_str  # htmlmin.minify(out_str)


def gen_part_html_pages():
    the_dirs = [x for x in os.listdir(src_ws) if x.startswith('part')]

    # list_main = []
    the_dirs.sort()
    for the_dir in the_dirs:
        gen_html_pages(os.path.join(src_ws, the_dir))

        # if the_dir.startswith('part'):
        #     pass
        # else:
        #     continue
        # idx, slug, title = the_dir.split('_')


def gen_chapter_index(the_dir, md_index='', idx_dir=0, list_main='', src_ws=src_ws):
    print('=' * 40)
    print(the_dir)
    pprint(list_main)
    ch_slug = os.path.split(src_ws)[-1].split('_')[1]

    bbcc = the_dir.split('_')
    if len(bbcc) == 3:
        dir_idx, dir_slug, dir_title = bbcc
    else:
        dir_idx, dir_slug = bbcc
        dir_title = bbcc[-1]

    out_html_file = os.path.join(dst_ws, '{}-index.html'.format(dir_slug))
    tpl_file = 'content.jinja2'

    if md_index:
        the_html = markdown2html(open(md_index).read(), format='md')
        cnt_title_arr = get_h2_nav(the_html)
    else:
        the_html = ''
        cnt_title_arr = ' '

    helper.render_html(
        tpl_file, out_html_file,
        cnt=the_html,
        nav=format_nav(fetch_part(), chapter_slug=ch_slug),
        dir_slug=list_main[idx_dir]['list_md'][0]['slug'],
        dir_title=dir_title,
        slug=dir_slug,
        title='',
        leftnav=format_leftnav(list_main[idx_dir]['list_md'], ''),
        cntnav=format_cntnav(cnt_title_arr),  # ToDo: 添加
        first_nav=str(src_ws).split('_')[2]
    )


def gen_html_pages(src_ws):
    '''
    convert from markdown to html.
    '''

    chapter_slug = os.path.split(src_ws)[-1].split('_')[1]

    list_main = fetch_structure(src_ws)

    the_dirs = os.listdir(src_ws)

    the_dirs.sort()

    # find directories.
    tt_dirs = []
    for the_dir in the_dirs:
        wroot = os.path.join(src_ws, the_dir)
        if os.path.isdir(wroot):
            tt_dirs.append(the_dir)
        else:
            continue
    the_dirs = tt_dirs
    the_dirs.sort()

    # walk through directory.
    for idx_dir, the_dir in enumerate(the_dirs):

        wroot = os.path.join(src_ws, the_dir)
        if os.path.isdir(wroot):
            pass
        else:
            continue

        bbcc = the_dir.split('_')
        if len(bbcc) == 3:
            dir_idx, dir_slug, dir_title = bbcc
        else:
            dir_idx, dir_slug = bbcc
            dir_title = bbcc[-1]

        md_index = os.path.join(src_ws, '{}_{}.md'.format(dir_idx, dir_slug))
        if os.path.exists(md_index):
            pass
        else:
            md_index = ''

        gen_chapter_index(
            the_dir,
            md_index,
            idx_dir=idx_dir,
            # nav_formated=format_nav(fetch_part(), chapter_slug=chapter_slug),
            list_main=list_main,
            src_ws=src_ws
        )

        md_files = [x for x in os.listdir(wroot) if os.path.splitext(x)[-1] in ['.md', '.rst']]

        for idx_file, md_file in enumerate(md_files):

            # print(md_file)

            # dir_idx, dir_slug, dir_title = the_dir.split('_')

            the_file = os.path.join(wroot, md_file)

            md_dic = {}
            cnt_arr = []
            with open(the_file) as fin:
                # markdown pre.
                for cnt in fin.readlines():
                    if cnt.strip().startswith(';'):
                        tkey, tval = cnt.strip().strip(';').split(':')

                        md_dic[tkey.strip().lower()] = tval.strip()
                    elif cnt.strip().startswith('->->'):
                        map_name = cnt.strip().split()[-1]
                        map_file_path = os.path.join(wroot, map_name)
                        mcnts = open(map_file_path).readlines()
                        idx = 1
                        for mcnt in mcnts:

                            if map_name.endswith('.htmp'):
                                cnt_arr.append(mcnt.strip())
                            elif map_name.endswith('.map'):
                                cnt_arr.append('    ' + str(idx).zfill(2) + ' ' + mcnt)
                            else:
                                cnt_arr.append('    ' + str(idx).zfill(2) + ' ' + mcnt)
                            idx = idx + 1

                    else:
                        cnt_arr.append(cnt)

            format = 'rst' if md_file.endswith('.rst') else 'md'
            the_html = markdown2html(''.join(cnt_arr).format(SITE_URL=SITE_URL), format=format)

            # h3_count = len(soup.find_all('h3'))

            cnt_title_arr = get_h2_nav(the_html)

            tpl_sig = the_dir.split('_')[0]
            if tpl_sig:
                tpl_file = os.path.join(
                    tpl_ws,
                    'base{sig}.jinja2'.format(sig=tpl_sig)
                )
                if os.path.exists(tpl_file):
                    pass
                else:
                    tpl_file = 'content.jinja2'
            else:
                tpl_file = 'content.jinja2'

            file_slug = os.path.splitext(md_file)[0].split('_')[-1]

            if md_dic:
                pass
            else:
                continue
            file_title = md_dic['title']
            slug = dir_slug + '-' + file_slug
            file_name = slug + '.html'
            out_html_file = os.path.join(dst_ws, file_name)

            helper.render_html(
                tpl_file, out_html_file,
                cnt=the_html,
                nav=format_nav(fetch_part(), chapter_slug=chapter_slug, sec_slug=dir_slug),
                dir_slug=list_main[idx_dir]['list_md'][0]['slug'],
                dir_title=dir_title,
                slug=slug,
                title=file_title,
                leftnav=format_leftnav(list_main[idx_dir]['list_md'], slug),
                cntnav=format_cntnav(cnt_title_arr),
                first_nav=str(src_ws).split('_')[2]
            )

        # dealing with jinja2 files.
        md_files = [x for x in os.listdir(wroot) if x.endswith('.jinja2') and not x.startswith('xx_')]
        for idx_file, md_file in enumerate(md_files):

            # dir_idx, dir_slug, dir_title = the_dir.split('_')

            file_slug = os.path.splitext(md_file)[0].split('_')[-1]
            # file_title = md_dic['title']
            if md_file[0] in ['0', '1', '2', '3', '4', '5', '6',
                              '7', '8', '9']:
                file_name = dir_slug + '-' + file_slug + '.html'

            else:
                file_name = os.path.splitext(md_file)[
                                0] + '.html'

            out_html_file = os.path.join(dst_ws, file_name)

            jinja2_file = os.path.join(wroot, md_file)
            x_jinja2_file = os.path.join(wroot, 'xx_' + md_file)

            jinja2_file2 = '/'.join(x_jinja2_file.split('/')[1:])
            # x_jinja2_file2 = '/'.join(x_jinja2_file.split('/')[1:])
            slug = dir_slug + '-' + file_slug
            ja2_cnts = open(jinja2_file).readlines()

            # print(jinja2_file)
            cnt_title_arr = get_h2_nav(open(jinja2_file).read())

            with open(x_jinja2_file, 'w') as fo_ja2:
                for cnt in ja2_cnts:

                    if cnt.strip().startswith('->->'):
                        map_name = cnt.strip().split()[-1]
                        map_file_path = os.path.join(wroot, map_name)
                        mcnts = open(map_file_path).readlines()
                        idx = 1

                        if map_name.endswith('.htmp'):
                            for mcnt in mcnts:
                                fo_ja2.write(mcnt)
                        elif map_name.endswith('.map'):
                            fo_ja2.write('<pre><code>')
                            for mcnt in mcnts:
                                fo_ja2.write(str(idx).zfill(2) + ' ' + mcnt)
                                idx = idx + 1
                            fo_ja2.write('</code></pre>')
                        else:
                            pass

                        # for mcnt in mcnts:
                        #     if map_name.endswith('.htmp'):
                        #         fo_ja2.write(mcnt)
                        #     elif map_name.endswith('.map'):
                        #         fo_ja2.write(str(idx).zfill(2) + ' ' + mcnt)
                        #     else:
                        #         pass


                    else:
                        fo_ja2.write(cnt)

            helper.render_html(
                jinja2_file2, out_html_file,
                dir_title=dir_title,
                title=get_html_title(jinja2_file),
                leftnav=format_leftnav(list_main[idx_dir]['list_md'], slug),
                nav=format_nav(fetch_part(), chapter_slug=chapter_slug, sec_slug=dir_slug),
                cntnav=format_cntnav(cnt_title_arr),
                SITE_URL=SITE_URL,
                first_nav=str(src_ws).split('_')[2]
            )

            # shutil.copy(, out_html_file)


def get_h2_nav(html_info):
    # print('=' * 40)
    # print(html_info)
    soup = BeautifulSoup(html_info, 'lxml')
    cnt_title_arr = []
    if '</h1>' in html_info:
        for child in soup.find_all('h2'):
            try:
                cnt_title_arr.append({'key': child.attrs['id'],
                                      'val': child.text})
            except:
                pass
    else:
        for child in soup.find_all('h3'):
            cnt_title_arr.append({'key': child.attrs['id'],
                                  'val': child.text})
    return cnt_title_arr


def get_html_title(the_file):
    soup = BeautifulSoup(open(the_file).read(), 'lxml')
    logger.debug('=' * 100)
    logger.debug(soup.title)
    logger.debug('=' * 100)
    return soup.title.text


def gen_html_index():
    '''
    Generate ``index.html`` for the website.
    '''
    list_main = fetch_part()

    pprint(list_main)

    nav_formated = format_nav(list_main)

    index_in = 'index.jinja2'
    index_out = os.path.join(dst_ws, 'index.html')

    helper.render_html(index_in, index_out, nav=nav_formated, active_index='active')


def fetch_part():
    '''
    Fetch the list form `part` in template directory.
    '''
    the_dirs = [x for x in os.listdir(src_ws) if x.startswith('part')]

    list_main = []
    the_dirs.sort()
    for the_dir in the_dirs:
        # if the_dir.startswith():
        #     pass
        # else:
        #     continue
        uu = fetch_structure(os.path.join(src_ws, the_dir))

        bbcc = the_dir.split('_')

        dir_idx, dir_slug, dir_title = bbcc

        list_main.append(
            {
                'slug': dir_slug,
                'title': dir_title,
                'list_md': uu
            }
        )
    return list_main


def fetch_structure(src_ws):
    '''
    fetch the structure of the site.
    '''
    the_dirs = os.listdir(src_ws)

    list_main = []
    the_dirs.sort()
    for the_dir in the_dirs:
        xx_dir = os.path.join(src_ws, the_dir)
        if os.path.isdir(xx_dir):
            pass
        else:
            continue

        wroot = os.path.join(src_ws, the_dir)
        # the_files = [x  for x in os.listdir(wroot) ]
        # the_files = filter(lambda x: x.endswith('.md'), os.listdir(wroot))

        the_files = os.listdir(wroot)
        the_files = [x for x in the_files if os.path.splitext(x)[-1] in ['.md', '.jinja2', '.rst']]
        the_files = [x for x in the_files if x[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 's']]
        the_files.sort()

        bbcc = the_dir.split('_')
        if len(bbcc) == 3:
            dir_idx, dir_slug, dir_title = bbcc
        else:
            dir_idx, dir_slug = bbcc
            dir_title = bbcc[-1]

        # dir_idx, dir_slug, dir_title = the_dir.split('_')

        list_md = []
        for wfile in the_files:
            the_file = os.path.join(wroot, wfile)

            # print(the_file)

            md_dic = {}
            with open(the_file) as fin:
                cnt_arr = []
                for cnt in fin.readlines():
                    if cnt.strip().startswith(';'):
                        tkey, tval = cnt.strip().strip(';').split(':')
                        md_dic[tkey.strip().lower()] = tval.strip()
                    else:
                        cnt_arr.append(cnt)

            if wfile.endswith('jinja2'):
                the_title = helper.get_html_title(the_file)
                md_dic['title'] = the_title
            file_name = dir_slug + '-' + os.path.splitext(wfile)[0].split('_')[-1] + '.html'

            list_md.append(
                {'slug': os.path.splitext(file_name)[0],
                 'file_name': os.path.splitext(wfile)[0].split('_')[-1],
                 'title': md_dic['title'] if 'title' in md_dic else os.path.splitext(wfile)[0].split('_')[-1]
                 }
            )

        list_main.append(
            {
                'slug': dir_slug,
                'title': dir_title,
                'list_md': list_md
            }
        )

    return list_main


def copy_static_files():
    for part_dir in os.listdir(src_ws):
        uu_ws = os.path.join(src_ws, part_dir)
        if part_dir.startswith('part'):
            for the_dir in os.listdir(uu_ws):
                inpath = os.path.join(uu_ws, the_dir)
                # print('\033[33m')
                # print(inpath)
                # print('\033[0m')
                if os.path.isdir(inpath):
                    pass
                else:
                    continue
                copy_the_dir(inpath)
        # else:
        #     copy_the_dir(uu_ws)

    for ww in os.listdir(tpl_ws):

        inbb = os.path.join(tpl_ws, ww)

        outbb = os.path.join(dst_ws, ww)

        if os.path.isdir(inbb):
            if os.path.exists(outbb):
                shutil.rmtree(outbb)
            shutil.copytree(inbb, outbb)
        else:
            shutil.copy(inbb, outbb)


def copy_the_dir(inpath):
    for xx in os.listdir(inpath):
        the_x = os.path.join(inpath, xx)

        outbb = os.path.join(dst_ws, xx)
        # print('\033[33m')
        # print(outbb)
        # print('\033[0m')

        if os.path.isdir(the_x):
            if os.path.exists(outbb):
                shutil.rmtree(outbb)
            shutil.copytree(the_x, outbb)
        else:
            _, houzhui = os.path.splitext(xx)
            if houzhui.lower() in ['.jpg', '.png', '.jpeg',
                                   '.gif', '.dbf', '.map',
                                   '.html', '.js', '.xml',
                                   '.ico', '.txt', '.yaml']:
                shutil.copy(the_x, outbb)


def run_it():
    gen_html_index()

    gen_part_html_pages()
    # gen_html_pages()

    copy_static_files()


if __name__ == '__main__':
    run_it()
