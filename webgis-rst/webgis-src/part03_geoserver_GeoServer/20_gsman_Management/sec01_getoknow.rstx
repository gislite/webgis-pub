=============
了解界面
=============

您在上一章中使用了web界面来更改管理员用户的密码。
再次登录GeoServer；我们现在将注意力集中在布局上。

正如您在下面的屏幕截图中看到的，GeoServer web界面有三个主要区域。

中心区域是显示信息的地方；其中的元素根据您执行的操作而变化。登录后，
它会向您显示配置数据的简要信息，以及应更正的警告或错误。版本号显示在末尾，
并且有一个指向管理员邮箱的链接；

在右侧，有一个列表显示GeoServer的功能。列出的首字母缩略词是指标准的OGC协议；
我们将详细讨论其中的一些协议，每个协议至少支持一个版本。这些数字是指向XML文档的链接，
这些文档准确地描述了每个协议支持哪些数据和操作。对于愿意使用您的服务的客户来说，
它们是非常宝贵的资源。

在左侧，有一个列出配置区域的目录。每个区域都包含指向管理操作的链接。
单击其中一个选项时，中心区域将显示上下文选项。我们将在下一段中探讨每个领域。

.. figure:: ./geoserver_index_x7w.png
   :alt: geoserver_index

   geoserver_index

关于状态
=============================

此区域提供有关运行时变量的信息，以及如何向连接GeoServer的客户端描述GeoServer。

.. figure:: ./image42_x70.jpg
   :alt: image42

   image42

服务器状态
-------------------

服务器状态可让您很好地了解主要配置参数 以及有关GeoServer当前状态的信息。
该信息以表格视图的形式组织。
除了提供信息外，该视图使您可以执行一些维护操作。
我们将描述以下屏幕截图中列出的主要项目：

.. figure:: ./server_stutas_xn8.png
   :alt: server_stutas

   server_stutas

1. 锁

使用事务性Web功能服务（WFS-T），客户端可以编辑配置的功能类型。
为避免数据损坏，GeoServer锁定需要进行交易的数据，直到交易结束。
如果显示的数字大于1，则说明您的数据正在进行一些事务。
Free Locks按钮可让您重置挂起的编辑会话，删除所有孤立进程以释放可能已被放弃的锁。

2. 连接

这将显示矢量数据存储连接的数量。
矢量数据存储库是为特征的持久性而配置的存储库。

3. 内存使用

这显示了GeoServer正在使用多少内存。
您可以通过单击“可用内存”按钮来手动运行垃圾收集器。这将破坏标记为删除的Java对象。

4. JVM版本和字体

这是GeoServer使用的Java虚拟机（JVM）的版本。
您是在第2章GeoServer入门中配置的， 在安装过程中。
您还将看到JVM和GeoServer看到的字体列表。
字体对于渲染空间特征标签很有用。
我们将在第6章，设置图层样式中对此进行探讨。

5. JAI使用和配置

Java Advanced Imaging（JAI）库用于图像渲染
并在GeoServer处理栅格数据时获得更好的性能， 与Web Coverage
Service（WCS）和Web Map Service（WMS）请求一样。
我们将在第11章“在生产环境中调整GeoServer”中安装本机JAI支持。

6. 更新序列

这将显示服务器配置更新了多少次。截至本文撰写之时，信息量还没有那么大。
开发人员似乎计划使用它来让您知道您的配置文件已从应用程序外部更新。可能是休息电话。

7. 资源缓存

GeoServer还缓存到存储、要素类型定义、外部图形、字体定义和CRS定义的连接。
你可以按 清除
按钮以强制这些地理服务器重新打开存储并重新读取图像和字体信息。

8. 配置和目录

此选项对于更新配置而不必重新启动服务非常有用。GeoServer将配置数据保存在内存中。
如果有外部进程更新包含配置参数的文件，则可以强制GeoServer从磁盘重新加载数据。

GeoServer日志
-------------------

从这里可以预览当前日志文件，也可以从底部的链接下载完整内容。
当您无法访问存储实际日志文件的文件系统时，它可能很有用。

.. figure:: ./image44_x2b.png
   :alt: image44

   image44

每次的执行记录也会在日志中进行保存，保存位置的配置位置在全球中。

.. figure:: ./log_xyu.png
   :alt: log

   log

联系方式
-------------------

在此面板中，应插入有关管理服务的组织和人员的信息。
默认配置向古代制图师克劳迪斯·托勒密致敬( http://en.wikipedia.org/wiki/Ptolemy ).
此信息包含在WMS功能中，是用户的参考信息。

关于
^^^^

正如它所说的，这只是构建信息以及在哪里可以找到GeoServer文档、
bug跟踪器和wiki的全部内容。

.. figure:: ./image45_xq9.png
   :alt: image45

   image45

手动重新加载配置
================================================

现在，我们将对GeoServer的配置执行一个简单的更改，
以演示重新加载配置功能。

1.打开 global.xml 首选编辑器中的文件：

::

   ~ $ sudo vi /opt/apache-tomcat-7.0.27/webapps/geoserver/data/global.xml

2.找到 ``contact`` 部分并插入您的详细信息：

::

   <contact>
       <addressCity>Rome</addressCity>
       <addressCountry>Italy</addressCountry>
       <addressType>Work</addressType>
       <contactEmail>Stefano.iacovella@myworkemail</contactEmail>
       <contactOrganization>Packt Publishing</contactOrganization>
       <contactPerson>Stefano Iacovella</contactPerson>
       <contactPosition>Chief geographer</contactPosition>
   </contact>

3.现在保存文件并关闭它。然后转到 WEB 界面；在 **关于和状态** 面板，单击 **服务器状态** 菜单链接显示地理服务器状态，向下滚动， 然后单击 ``reload`` 按钮。

4.现在，转到“信息”面板。 它显示您的更新信息。


我们探索了一个使用reload配置函数的简单案例。
如果必须使用自动过程更新远程服务器或配置更多共享同一配置的GeoServer实例，
则这非常有用。我们将在 第十一章 ， 在生产环境中调整GeoServer 。

错误跟踪
---------------

GeoServer的错误跟踪器是一个很好的监视资源。
错误跟踪器的链接位于“关于GeoServer”页面的末尾。
活动流的RSS提要为您提供了GeoServer开发的窗口。
将 **feed：//jira.codehaus.org/plugins/servlet/streams？key=GEOS** 放入您的Feed聚合器，并保持循环状态。
