# site_gislite

此套 WebGIS 程序，部署于 aliyun6 ， 用于 IKCEST DRRKS.
在GISLite中也有应用，但暂时不再更新。

文档内容，用于 GISLite . 

## 代码位置 

    https://git.dev.tencent.com/osgeo/site_gislite.git

    sudo ln -s /home/bk/coding/site_gislite/wwwpub/owg/  /owg


##  子模块组成

添加：

    git submodule add https://git.dev.tencent.com/osgeo/book_pygis.git
    git submodule add https://git.dev.tencent.com/osgeo/book_wulun.git
    git submodule add https://git.dev.tencent.com/osgeo/gislite_blog.git
    git submodule add https://git.dev.tencent.com/osgeo/book_webgis4gislite.git
    git submodule add https://git.dev.tencent.com/osgeo/book_python.git



初始化与pull，在根目录下：

    git submodule init && git submodule update
    git submodule foreach git checkout master
    git submodule foreach git pull

## 翻译工具

    sphinx-build -b gettext . _build/locale    

生成要翻译成英文

    sphinx-intl update -p _build/locale  -l en