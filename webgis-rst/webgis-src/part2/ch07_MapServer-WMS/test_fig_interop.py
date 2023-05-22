
import pygraphviz as pyg

# from helper.textool import get_tmp_file



g=pyg.AGraph()  #建立图
g.add_node('文件格式转换')  #建立点
g.add_edge('文件格式转换','插件读取')  #建立边
g.add_edge('插件读取','Web服务')  #建立边


g.layout(prog='dot')  #绘图类型
# g.layout(prog='circo')  #绘图类型
# g.layout(prog='fdp')  #绘图类型
# g.layout(prog='sfdp')  #绘图类型
g.draw('mapfile_obj_rel.png')   #绘制

