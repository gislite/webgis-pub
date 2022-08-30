Introduction
=============================================

用于生成简单的静态网站的程序。

源代码在 `templates` 中，资源文件在`static`中。

源代码分为 MarkDown、Restructured 与 Jinja2 两类文件。

MarkDows 文件是常用的普通文档，
使用二级标题作为网页的标题，
里面的内容使用三级标题进行小节的划分。

Jinja2 是用处理比较复杂的页面，无法统一成MarkDown格式的。
在 Jinja2中，页面都是单独来写，可以用作产品展示页，
效果展示页，案例展示等。

## 源代码文件结构说明

文件夹使用下划线分隔三部分，形如 `03_projman_项目管理`。
`03`为顺序编码，`projman`为 slug ， 用于HTML路由，
`项目管理`为说明文字。

文件使用下划线分隔两部分，形如 `02_proj2.md`，
`02`为顺序编码，`proj2`为slug，用于HTML路由。
页面的 `Title` 从页面中获取，根据 MarkDown 与 Jinja2 而不同。

注意
================================

在对文件夹进行改名时，注意在部署服务器中进行删除。

安装与配置
==============================

安装

::

    sudo apt install -y apache2 php7.3 libapache2-mod-fcgid cgi-mapserver \
		mapserver-bin libapache2-mod-php
    # aptitude install -y qgis-mapserver
    sudo a2enmod authnz_fcgi
    sudo a2enmod cgi
    sudo service apache2 restart

获取前端类库

::

    git clone https://github.com/bukun/torcms_f2elib.git ./static/f2elib

配置

::

    # Alias /owg/ "/wegis/"
    <Directory "/owg/">
      AllowOverride None
      Options Indexes FollowSymLinks Multiviews
      Require all granted
    </Directory>

    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
    <Directory "/usr/lib/cgi-bin">
        AllowOverride None
        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
        Require all granted
    </Directory>

将开发路径链接成发布路径：

::

    sudo ln -s `pwd`/owg /owg

新的配置路径：

::
    mkdir /owg/ms_tmp/
    chown -R www-data.www-data /var/www/ms_tmp/

SubModule
================================================

::

    git submodule add https://git.dev.tencent.com/osgeo/book_webgis.git


在根目录下：

::

    git submodule init && git submodule update
    git submodule foreach git checkout master

    git submodule foreach git pull


部署说明
===================================================

部署于阿里云3

因为运行于 Apache2 ， 生成后，要运行：

::

    cd /home/bk/coding/book_webgis/webgis_cases
    python3 build_site.py
    chown -R www-data.www-data owg/
