.. WebGISPub documentation master file, created by
   sphinx-quickstart on Sat Oct  1 13:10:29 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====================================
Open Source WebGIS online Tutorial
=====================================

Making geospatial education and opportunities accessible to all.
Use Open Source GIS “Geo for All” is the Open Source Geospatial Foundation’s Committee
for Educational outreach and works in close collaboration with ICA, ISPRS, UN-GIS, AGILE, UCGIS ,
IGU and other partners worldwide in our mission for making geospatial education and opportunities accessible to all.


Introduction
===================================

The Open Source WebGIS Tutorial Website was created by the two authors based on their practical work experience in the process of cooperation. Open-source WebGIS has many meanings and skills for GIS technology and data sharing.
As an online tutorial of open source GIS, the design of this website uses examples that can be accessed and operated online to facilitate users to understand the principles and technologies of WebGIS. In addition, it also explains some principles and background of WebGIS, which can be used as a general WebGIS tutorial.



MapServer
---------------------------------------------------------------------

.. <img src="/images/logo_mapserver.png" style="float: right; width:100px; margin:10px;"/>
.. {# MapServer可以看作是两个独立模块的统称：MapServer CGI模块和MapScript模块。  #}

MapServer was originally an open source WebGIS software developed by the University of Minnesota and the US Space Agency (NASA).
MapServer itself is a program written in C language, providing two development modes, one based on CGI and the other in MapScript mode;
You can use any module on the server-side to write a WebGIS program.
MapServer as a WebGIS solution is object-based, and the basic configuration files The API organization of the MapFile and MapScript modules is object-based.
MapServer supports OGC's WMS/WFS service specification by implementing several standards of OGC, supporting distributed access and interoperability.
MapServer is a WebGIS platform developed based on the fat server/thin client mode to read geographic data.
The GD library is used to render the JPeg/PNG/GIF format image and then sent back to the client browser.
MapServer supports multiple platforms such as Windows, UNIX, and Linux.
Languages ​​supported by MapScript include Python, PHP, Perl, Java, Tcl, C#, and more.

MapProxy
---------------------------------------------

.. <img src="/images/logo_mapproxy.png" style="float: right; width:200px; margin:10px;"/>

MapProxy is the Swiss Army Knife for WMS web map services and slice service providers. It caches, accelerates, and converts data services for existing services to any OGC-compliant desktop and web client. MapProxy is flexible to develop and easy to integrate with the Apache environment. MapProxy can also be used as a standalone service. This is the easiest way for new users.
The MapProxy example is a basic WMS slice client. It shows the various layers of the configuration. It doesn't have the complex features of changing projections, but it's enough to verify that the service is working.


LeafletJS
--------------------


.. <img src="/images/logo_leaflet.png" style="float: right; width:200px;margin:10px;"/>

Leaflet is a modern, open-source JavaScript library developed for building mobile-friendly interactive maps. It was developed by Vladimir Agafonkin, a team of professional contributors, with a small amount of code, but it has most of the features developers develop online maps. The Leaflet design adheres to the idea of simplicity, high performance and usability, and operates efficiently on all major desktop and mobile platforms.
The advantages of HTML5 and CSS3 are exploited in modern browsers, while old browser access is also supported.
Support for plugin extensions, a friendly, easy to use API documentation and a simple, readable source code.

OpenLayers
------------------------------



.. <img src="/images/logo_openlayers.png" style="float: right;width:200px;margin:10px;"/>

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

.. <img src="/images/logo_cesium.png" style="float: right;width:200px;margin:10px;"/>



WebGL-based front-end 3D JavaScript class library. Cesium launched the 3D Tiles data specification around March 2016, providing LOD capabilities on a glTF basis. Positioning is massive 3D model data in the Web environment.
Although the current 3D Tiles is still in the Beta stage, there are quite a few flaws.
However, the 3D Tiles data specification began the OGC standardization process on September 30, 2016, and the active component is still very large.

About the website
===========================================


Author: Bu Kun

Northeast Institute of Geography and Agroecology, Chinese Academy of Sciences. Ph.D, Senior Engineer

Wang Juanle

Institute of Geographic Sciences and Natural Resources Research, Chinese Academy of Sciences. Ph.D, Research Professorship

Director of World Data System (WDS) for Renewable Resources and Environment

- The development of this new website is to promote the use of open source WebGIS;
- The Chinese version of this tutorial is maintained by OSGeo China Center - Open Geospatial Laboratory;
- The first part of the tutorial is the Chinese translation of the MapServer tutorial;
- The original MapServer tutorial runs in a PHP environment and is currently completely rewritten using Python to generate static websites;
- The development of the tutorial uses some English tutorials and official website cases;
- A separate MapServer server is configured to provide map services;
- Please send any questions and suggestions to bukun (at) osgeo.cn and correct them in time.


Technical Environment
---------------------------------------------------------

- Operating system：Debian Linux 10 (buster), 64bit
- Apache 2.4.38-3+deb10u8
- CGI MapServer 7.2.2-1
- MapProxy 1.11.0-3+deb10u1

Building Environment
------------------------------------------

Build under Python 3.7.3 , using the flollowing modules：


- beautifulsoup4==4.11.1
- Jinja2==3.1.2
- lxml==4.8.0
- mappyfile==0.9.7
- Markdown==3.3.7
- PyYAML==6.0

.. toctree::
   :maxdepth: 2
   :numbered: 2

   ch01_fundation/chapter
   ch02_OGC-OpenGIS/chapter
   ch03_MapServer-Setup/chapter
   ch04_Using-MapServer/chapter
   ch05_MapServer-CGI/chapter
   ch06_Using-CGI/chapter
   ch07_MapServer-WMS/chapter
   ch08_MapServer-WFS/chapter
   ch09_MapServer-WCS/chapter
   ch10_ref-Addon/chapter
   ch11_GeoServer-Introduction/chapter
   ch12_GeoServer-Management/chapter
   ch13_leaflet/chapter
   ch14_openlayers/chapter
   ch15_cesium/chapter
   ch16_tools/chapter
   ch17_tiles/chapter
   ch18_gislite/chapter
