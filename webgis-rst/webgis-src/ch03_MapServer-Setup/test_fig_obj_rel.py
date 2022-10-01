import pygraphviz as pyg

from helper.textool import get_tmp_file



g=pyg.AGraph()  #建立图
g.add_node('MapObject')  #建立点
g.add_edge('MapObject','WebObject')  #建立边
g.add_edge('MapObject','Symbol')  #建立边
g.add_edge('MapObject','MapProjection')  #建立边
g.add_edge('MapObject','Outputformat')  #建立边
g.add_edge('MapObject','LayerObject')  #建立边
g.add_edge('MapObject','Scalebar')  #建立边
g.add_edge('MapObject','ReferenceMap')  #建立边
g.add_edge('MapObject','Lengend')  #建立边
g.add_edge('MapObject','QueryMap')  #建立边

g.add_edge('Scalebar', 'Label(Scalebar)')  #建立边
g.add_edge('Lengend', 'Label(Legend)')  #建立边

g.add_edge('LayerObject', 'Feature')  #建立边
g.add_edge('LayerObject', 'LayerProjection')  #建立边
g.add_edge('LayerObject', 'ClassObject')  #建立边
g.add_edge('LayerObject', 'GridObject')  #建立边
g.add_edge('LayerObject', 'JoinObject')  #建立边

g.add_edge( 'ClassObject', 'LabelObject',)  #建立边
g.add_edge( 'ClassObject', 'StyleObject',)  #建立边



g.layout(prog='dot')  #绘图类型
# g.layout(prog='circo')  #绘图类型
# g.layout(prog='fdp')  #绘图类型
# g.layout(prog='sfdp')  #绘图类型
g.draw('mapfile_obj_rel.png')   #绘制

g.draw(get_tmp_file(__file__, '1', file_ext='pdf'))
g.draw(get_tmp_file(__file__, '1', file_ext='png'))
