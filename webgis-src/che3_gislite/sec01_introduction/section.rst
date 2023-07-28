.. Author: gislite .. Title: Introduction to GISLite

Introduction to GISLite
=======================

Brief introduction
------------------

GISLite is an application that publishes GIS data in the form of static
websites based on open source GIS technologies (including MapServer,
MapProxy, Leafet). The purpose is to solve the problem of data update,
style modification, and the application of different style combinations
when publishing a large number of maps. Try to make the data source
unique and use XLSX files to define styles. It mainly realizes the
publishing of GIS data layers, but also realizes the function of
publishing multi-source data to a single map slice and multiple layers
to layer grouping.

In addition to re-establishing the original MapServer tutorial using
Python, another important reason for the development of this website is
to explain some technologies used in the development of GISLite. From
another perspective, it can also be said that GISLite is a comprehensive
application of the main open source GIS technologies described on this
website. Apart from the introduction, this part is published based on
the GISLite program and integrated into this website as a demo.

At present, GISLite has been registered and released in PYPI, and can be
installed by the following command:

::

   pip install gislite

-  Based on MapServer, MapProxy
-  Define styles using the open spreadsheet format XLSX
-  It can be used for rapid release and management of team geographic
   information data.
-  Open source code, released on Github.

Related website
---------------

-  Project official website:https://www.osgeo.cn/gislite/
-  Project GitHub address:https://github.com/bukun/GISLite
-  Project PyPi address:https://pypi.org/project/gislite/

Technical background website
----------------------------

Technically, the development of GISLite mainly uses Python and open
source GIS technology to read data. Integrate with the open source
WebGIS introduced on this website.

-  https://www.osgeo.cn/pygis/

“Python and Open Source GIS”, a tool for reading and processing GIS data
using Python.

-  http://webgis.pub/

A basic introduction to MapServer, MapProxy and Leaflet.
