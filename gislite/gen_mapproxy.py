# -*- coding:utf-8 -*-

'''
生成MapProxy的YAML配置文件
'''

import os
import yaml

from config import GIS_BASE
import gislite.helper as helper
from gislite.helper import TPL_MAPPROXY

raw_yaml = ''
if os.path.exists('/home/bk/wcs_maplet/mapproxy.yaml'):
    raw_yaml = '/home/bk/wcs_maplet/mapproxy.yaml'
else:
    pass


def chuli_serial_file(png, mapserver_ip, uu, wroot):
    print(png)
    rrxlsx_file = os.path.join(wroot, png)

    map_mata = helper.xlsx2dict(rrxlsx_file)

    data_apth = ''
    for x in map_mata:
        for key in x:

            if key == 'data':
                data_apth = x[key]
    if '[' in data_apth:
        print('-' * 40)

        print(data_apth)
        qq = data_apth.index('[')
        hh = data_apth.index(']')
        sig_q = data_apth[:qq]
        sig_h = data_apth[hh + 1:]
        print(sig_q)
        print(sig_h)
        for wwfile in os.listdir(wroot):
            if wwfile.startswith(sig_q) and wwfile.endswith(sig_h):
                print(wwfile)

                the_sig = wwfile[qq: hh - 1]
                print(the_sig)
                shp = os.path.join(wroot, wwfile)
                npng = png.replace('[sig]', the_sig)
                print(npng)
                gen_imagery4d(npng, mapserver_ip, uu, wroot)


def do_for_raster(mapserver_ip, out_yaml_file):
    uu = yaml.load(TPL_MAPPROXY)
    rst_ws = GIS_BASE
    for wroot, wdirs, wfiles in os.walk(rst_ws):
        for png in wfiles:

            if png.startswith('meta_') and png.endswith('.xlsx'):
                if '_mul' in png:
                    gen_mul_lyr(png, mapserver_ip, uu, wroot)
                elif '_grp' in png:
                    pass
                elif '[' in png:
                    chuli_serial_file(png, mapserver_ip, uu, wroot)
                else:
                    gen_imagery4d(png, mapserver_ip, uu, wroot)

            else:
                continue

    with  open(out_yaml_file, 'w') as fo:
        yaml.dump(uu, fo, encoding='utf-8', allow_unicode=True)


def gen_mul_lyr(png, mapserver_ip, uu, wroot):
    lqian, lhou = os.path.splitext(png)
    xxuu = lqian.split('_')
    if len(xxuu) > 2:
        lidx, lslug, lname = xxuu
    else:
        lidx, lslug = xxuu
        lname = xxuu[-1]

    mqian, mhou = os.path.split(wroot)
    midx, mslug, mname = mhou.split('_')

    the_file = os.path.join(wroot, png)
    lyr_list = helper.lyr_list(mslug, the_file)
    (lyr_name, lyr_ext) = os.path.splitext(png)
    lyr_name_arr = lyr_name.split('_')
    the_name = '_'.join(lyr_name_arr[1:])
    # sig = 'maplet_' + the_name

    sig = 'maplet_{}_{}'.format(mslug, lslug)

    uu['caches'][sig] = {}
    uu['caches'][sig]['grids'] = ['webmercator']
    uu['caches'][sig]['grids'] = ['webmercator']
    uu['caches'][sig]['sources'] = lyr_list
    new_dic = {'name': sig, 'title': sig, 'sources': [sig]}
    uu['layers'].append(new_dic)


def gen_imagery4d(png, mapserver_ip, uu, wroot):
    lqian, lhou = os.path.splitext(png)
    xxuu = lqian.split('_')
    if len(xxuu) > 2:
        lidx, lslug, lname = xxuu
    else:
        lidx, lslug = xxuu
        lname = xxuu[-1]

    mqian, mhou = os.path.split(wroot)
    midx, mslug, mname = mhou.split('_')
    fc_map_file = os.path.join(mqian, 'mfile_{}.map'.format(mslug))

    (lyr_name, lyr_ext) = os.path.splitext(png)
    lyr_name_arr = lyr_name.split('_')
    the_name = '_'.join(lyr_name_arr[1:])

    sig = 'maplet_{}_{}'.format(mslug, lslug)
    # fo.write(tmpl.format('maplet_' + sig))
    uu['sources'][sig] = {}
    uu['sources'][sig]['type'] = 'wms'
    uu['sources'][sig]['image'] = {'transparent_color_tolerance': 0, 'transparent_color': '#ffffff'}
    uu['sources'][sig]['req'] = {}
    uu['sources'][sig]['req']['url'] = 'http://{0}/cgi-bin/mapserv?map={1}'.format(
        mapserver_ip, fc_map_file)
    uu['sources'][sig]['req']['layers'] = 'lyr_{}'.format(lslug)
    uu['caches'][sig] = {}
    uu['caches'][sig]['grids'] = ['webmercator']
    uu['caches'][sig]['grids'] = ['webmercator']
    uu['caches'][sig]['sources'] = [sig]
    new_dic = {'name': sig, 'title': sig, 'sources': [sig]}
    uu['layers'].append(new_dic)


def gen_by_ip(mapserver_ip, out_yaml_file):
    do_for_raster(mapserver_ip, out_yaml_file)


if __name__ == '__main__':
    mapserver_ip = '127.0.0.1'

    # mapserver_ip = '159.226.123.26'
    out_yaml_file = 'out_mapproxy.yaml'
    # mapfile_ws = '/opt/mapdisk/mapws'
    gen_by_ip(mapserver_ip, out_yaml_file)
