# -*- coding: utf-8 -*-
'''
对 XLSX 进行遍历，生成 Mapfile.
'''
import os
import mappyfile
import gislite.helper as helper
from config import GIS_BASE
from gislite.helper import TPL_MAP, TPL_LAYER, TPL_CLASS

MTS = helper.get_mts()


def map_map(map_dir):
    '''
    生成总的 Mapfile.
    '''

    mqian, mhou = os.path.split(map_dir)

    midx, mslug, mname = mhou.split('_')

    fc_inc = ''
    for wroot, wdirs, wfiles in os.walk(map_dir):
        for wfile in wfiles:
            if wfile.endswith('.xlsx'):
                if '_mul' in wfile:
                    continue
                elif '_grp' in wfile:
                    continue
                else:
                    pass
            else:
                continue

            for lyr_name in get_lyr_mapfile(map_dir, wfile, wroot):
                # lyr_name =
                fc_inc = fc_inc + 'include "{}"\n'.format(lyr_name)

    # fc_map_file = os.path.join(map_dir, 'mapfile.map')
    fc_map_file = os.path.join(mqian, 'mfile_{}.map'.format(mslug))

    with open(fc_map_file, 'w') as fo2:
        tmp_str = TPL_MAP.format(
            basedir=map_dir,
            fc_name='map_dir_sig', fc_includes=fc_inc,
            fc_extent='{x_min} {y_min} {x_max} {y_max}'.format(
                x_min=-180,
                x_max=180,
                y_min=-90,
                y_max=90)
        )
        fo2.write(tmp_str)


def get_lyr_mapfile(map_dir, wfile, wroot):
    '''
    生成图层的 Mapfile
    '''

    rrxlsx_file = os.path.join(wroot, wfile)
    print(rrxlsx_file)

    t_mts = helper.get_mts(rrxlsx_file)

    map_mata = helper.xlsx2dict(rrxlsx_file)

    data_apth = ''
    for x in map_mata:
        for key in x:
            if key == 'data':
                data_apth = x[key]
    lyrs_file = []
    if '[' in data_apth:
        # print('-' * 40)

        print(data_apth)
        qq = data_apth.index('[')
        hh = data_apth.index(']')
        sig_q = data_apth[:qq]
        sig_h = data_apth[hh + 1:]
        # print(sig_q)
        # print(sig_h)
        for wwfile in os.listdir(wroot):
            if wwfile.startswith(sig_q) and wwfile.endswith(sig_h):
                print(wwfile)

                the_sig = wwfile[qq: hh - 1]
                shp = os.path.join(wroot, wwfile)

                lyr_file = generate_lyr_mapfile(map_dir, map_mata, shp, wfile, t_mts, sig=the_sig)
                lyrs_file.append(lyr_file)

    else:
        shp = os.path.join(wroot, data_apth)
        lyr_file = generate_lyr_mapfile(map_dir, map_mata, shp, wfile, t_mts)
        lyrs_file.append(lyr_file)

    # pprint(new_layer)

    # print(yaml.dump(new_layer))
    return lyrs_file


def generate_lyr_mapfile(map_dir, map_mata, shp, wfile, t_mts, sig=None):
    '''
    生成图层的 Mapfile.
    '''
    mqian, mhou = os.path.splitext(wfile)
    xxuu = mqian.split('_')
    if len(xxuu) > 2:
        midx, mslug, mname = xxuu
    else:
        midx, mslug = xxuu
        mname = xxuu[-1]
    new_layer = mappyfile.loads(TPL_LAYER)
    shp_info = helper.get_epsg_code(shp)
    # print(shp)
    qian, hou = os.path.split(shp)
    shpfile_name, shpfile_ext = os.path.splitext(hou)
    # lyr_name = 'lyr_' + shpfile_name + '.map'
    if sig:
        lyr_name = 'lyr_' + mslug.replace('[sig]', sig) + '.map'
    else:
        lyr_name = 'lyr_' + mslug + '.map'
    lyr_file = os.path.join(map_dir, lyr_name)
    if t_mts > MTS:

        if shp_info['geom_type'].lower() in ['linestring', 'multilinestring']:
            lyr_type = 'line'
        elif shp_info['geom_type'].lower() in ['multipolygon']:
            lyr_type = 'polygon'
        else:
            lyr_type = shp_info['geom_type']
        new_layer['type'] = lyr_type
        new_layer['data'] = shp
        # new_layer['name'] = os.path.splitext(wfile)[0]
        if sig:
            new_layer['name'] = 'lyr_{}'.format(mslug.replace('[sig]', sig))
        else:
            new_layer['name'] = 'lyr_{}'.format(mslug)
        new_layer['metadata']['ows_title'] = os.path.splitext(wfile)[0]
        new_layer['metadata']['wms_title'] = os.path.splitext(wfile)[0]
        new_layer['PROJECTION'] = "{}".format(shp_info['proj4_code'])

        new_layer['processing'] = []
        for idx, cl in enumerate(map_mata):

            cls = mappyfile.loads(TPL_CLASS)
            for key in cl:
                if key.lower() == 'classitem':
                    new_layer['classitem'] = cl[key]
                elif key.lower() == 'labelitem':
                    new_layer['labelitem'] = cl[key]
                elif key.lower() == 'data':
                    new_layer['data'] = shp
                elif key.lower() == 'labelminscaledenom':
                    new_layer['labelminscaledenom'] = cl[key]
                elif key.lower() == 'labelmaxscaledenom':
                    new_layer['labelmaxscaledenom'] = cl[key]
                elif key.lower() == 'encoding':
                    new_layer['encoding'] = cl[key]
                elif key.lower() == 'processing':
                    #  对于影像的单独处理
                    new_layer['processing'].append(cl[key])
                elif key.lower() == 'class':
                    pass
                elif key.lower() == 'expression' and type(cl[key]) == type(1):
                    '''
                    注意，即使是使用数值作为条件，也需要添加引号。故需转换为字符串。
                    '''
                    cls[key] = str(cl[key])
                elif key.lower() == 'style':
                    for subkey in cl[key]:
                        cls['styles'][0][subkey] = cl[key][subkey]

                elif key.lower() == 'label':
                    for subkey in cl[key]:
                        cls['labels'][0][subkey] = cl[key][subkey]
                else:
                    cls[key] = cl[key]

            new_layer["classes"].insert(0, cls)
        # 去掉原来的。
        new_layer['classes'].pop()
        new_layer['classes'].pop()
        # print(help(new_layer['classes']))
        with open(lyr_file, 'w') as fo:
            fo.write(mappyfile.dumps(new_layer, indent=1, spacer="    "))
    return lyr_file


def run_it():
    for wroot, wdirs, wfile in os.walk(GIS_BASE):
        for wdir in wdirs:
            if wdir.startswith('maplet'):
                # if 'maplet80' in wdir:
                map_map(os.path.join(wroot, wdir))


if __name__ == '__main__':
    run_it()
