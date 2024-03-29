
=====================================
Open Source WebGIS online Tutorial
=====================================

Making geospatial education and opportunities accessible to all.
Use Open Source GIS “Geo for All” is the Open Source Geospatial Foundation’s Committee
for Educational outreach and works in close collaboration with ICA,
ISPRS, UN-GIS, AGILE, UCGIS ,
IGU and other partners worldwide in our mission for making geospatial education
and opportunities accessible to all.


.. attention:: This website is open-source. Hosted on github: https://github.com/gislite/webgis-pub . Stars are welcome.


This website is based on https://demo.mapserver.org/tutorial/ and has undergone significant improvements.

.. note:: Many thanks to `JET BRAINS <https://www.jetbrains.com/>`_  for the free license for the repo of this tutorial. 
   Lots of technologies are involved in WebGIS, the  `PyCharm IDE <https://www.jetbrains.com/pycharm/>`_ is essential and suitable for the project.

Logs:

- August, 2023: Recieved the free license form JET BRAINS for IDE.
- July, 2023: The OS has been upgraded to Debian 12 (Used to be Debian 10). The MapServer has been upgraded to 8.0. Since 2023/7/7 .
- 2022: The source codes of this tutorial are published on Github .


Went through a series of refactoring.

1. Rebuild with PHP, using templates.
2. Integrated into TorCMS to serve as dynamic website.
3. Using Python to write the SSG for Mapfile processing, and using Jinja2 for webpage management.
4. Finally using Sphinx for the management of the pages. And keep the scripts for Mapfiles.

Based on MapServer, and would supply WebGIS relevant technologies.

There are a large number of historical legacy issues that need
to be addressed during the conversion process.
All the pull requests arc welcome.



Introduction
===================================

The Open Source WebGIS Tutorial Website was created by the two authors
based on their practical work experience in the process of cooperation.
Open-source WebGIS has many meanings and skills for GIS technology and data sharing.
As an online tutorial of open source GIS, the design of this website uses examples
that can be accessed and operated online to facilitate users
to understand the principles and technologies of WebGIS.
In addition, it also explains some principles and background of WebGIS,
which can be used as a general WebGIS tutorial.




MapServer
---------------------------------------------------------------------

.. image:: logo_mapserver.png

MapServer was originally an open source WebGIS software developed
by the University of Minnesota and the US Space Agency (NASA).
MapServer itself is a program written in C language, providing two development modes,
one based on CGI and the other in MapScript mode;
You can use any module on the server-side to write a WebGIS program.
MapServer as a WebGIS solution is object-based, and the basic configuration files The API organization of the MapFile and MapScript modules is object-based.
MapServer supports OGC's WMS/WFS service specification by implementing several standards of OGC, supporting distributed access and interoperability.
MapServer is a WebGIS platform developed based on the fat server/thin client mode to read geographic data.
The GD library is used to render the JPeg/PNG/GIF format image and then sent back to the client browser.
MapServer supports multiple platforms such as Windows, UNIX, and Linux.
Languages supported by MapScript include Python, PHP, Perl, Java, Tcl, C#, and more.

MapProxy
---------------------------------------------


.. image:: logo_mapproxy.png


The MapProxy example is a basic WMS slice client. It shows the various layers of the configuration.
It doesn't have the complex features of changing projections, but it's enough to verify that the service is working.


LeafletJS
--------------------


.. image:: logo_leaflet.png

Leaflet is a modern, open-source JavaScript library developed for building mobile-friendly interactive maps.
It was developed by Vladimir Agafonkin, a team of professional contributors, with a small amount of code, but it has most of the features developers develop online maps.
The Leaflet design adheres to the idea of simplicity, high performance and usability, and operates efficiently on all major desktop and mobile platforms.
The advantages of HTML5 and CSS3 are exploited in modern browsers, while old browser access is also supported.
Support for plugin extensions, a friendly, easy to use API documentation and a simple, readable source code.

OpenLayers
------------------------------


.. image:: logo_openlayers.png

OpenLayers is a JavaScript package for developing WebGIS clients.
Sources supported by OpenLayers include Google Maps, Yahoo, Map, Microsoft Virtual Earth, etc.
Users can also use a simple image map as a background image to overlay other layers in OpenLayers.
In this regard OpenLayers offers a lot of options.

In addition, OpenLayers' approach to accessing geospatial data is in line with industry standards.
OpenLayers supports WMS (Web Mapping Service) and WFS (Web Feature) developed by the Open GIS Association
Service service and other network service specifications, which can be done by remote service.
Map data published as OGC services is loaded into the browser-based OpenLayers client for display.
OpenLayers is developed in an object-oriented way and uses some components from Prototype.js and Rico.

Cesium
------------------

.. image:: logo_cesium.png

WebGL-based front-end 3D JavaScript class library.
Cesium launched the 3D Tiles data specification around March 2016, providing LOD capabilities on a glTF basis.
Positioning is massive 3D model data in the Web environment.
Although the current 3D Tiles is still in the Beta stage, there are quite a few flaws.
However, the 3D Tiles data specification began the OGC standardization process on September 30, 2016, and the active component is still very large.

About the website
===========================================


Author: gislite

Northeast Institute of Geography and Agroecology, Chinese Academy of Sciences. Ph.D, Senior Engineer

Wang Juanle

Institute of Geographic Sciences and Natural Resources Research, Chinese Academy of Sciences. Ph.D, Research Professorship

Director of World Data System (WDS) for Renewable Resources and Environment


.. image:: authors.jpg

- The development of this new website is to promote the use of open source WebGIS;
- The Chinese version of this tutorial is maintained by OSGeo China Center - Open Geospatial Laboratory;
- The first part of the tutorial is the Chinese translation of the MapServer tutorial;
- The original MapServer tutorial runs in a PHP environment and is currently completely rewritten using Python to generate static websites;
- The development of the tutorial uses some English tutorials and official website cases;
- A separate MapServer server is configured to provide map services;
- Please send any questions and suggestions to bukun (at) osgeo.cn and correct them in time.


Technical Environment
---------------------------------------------------------

- Operating system：Debian Linux 12 (bookworm), 64bit
- Apache 2.4.57-2
- cgi-mapserver 8.0.0-3+b8
- MapProxy 1.15.1-2

Building Environment
------------------------------------------

Build under Python 3.11.2 , using the flollowing modules：


- beautifulsoup4==4.11.1
- Jinja2==3.1.2
- lxml==4.8.0
- mappyfile==0.9.7
- Markdown==3.3.7
- PyYAML==6.0


Catalog
====================================

.. toctree::
   :maxdepth: 2
   :numbered: 3
   :caption: Part Ⅰ  Fundation

   cha1_fundation/chapter
   cha2_ogc-opengis/chapter


.. toctree::
   :maxdepth: 2
   :numbered: 3
   :caption: Part Ⅱ  MapServer

   chb1_mapserver-setup/chapter
   chb2_using-mapserver/chapter
   chb3_mapserver-cgi/chapter
   chb4_using-cgi/chapter
   chb5_mapserver-wms/chapter
   chb6_mapserver-wfs/chapter
   chb7_mapserver-wcs/chapter
   chb8_ref-addon/chapter


.. toctree::
   :maxdepth: 2
   :numbered: 3
   :caption: Part  Ⅲ GeoServer

   chc1_geoserver-introduction/chapter
   chc2_geoserver-management/chapter


.. toctree::
   :maxdepth: 2
   :numbered: 3
   :caption: Part Ⅳ Front End(Client)

   chd1_leaflet/chapter
   chd2_openlayers/chapter
   chd3_cesium/chapter


.. toctree::
   :maxdepth: 2
   :numbered: 3
   :caption: Part Ⅴ  Tiles and Tools

   che1_tools/chapter
   che2_tiles/chapter
   che3_gislite/chapter
