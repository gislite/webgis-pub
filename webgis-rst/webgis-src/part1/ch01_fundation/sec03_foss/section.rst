.. Author: Bu Kun .. Title: Introduction to major open source WebGIS

Introduction to major open source WebGIS
========================================

WebGIS is composed of four parts, and it can be seen from the name that
it includes at least Web and GIS, which involves technical complexity.
From the perspective of WebGIS, open source tools can be divided into
two categories: component products and full-stack products.

Free and open source software, open specification and open data
---------------------------------------------------------------

At present, the use and maintenance costs of commercial GIS software are
getting higher and higher. For example, a complete set of ESRI ArcGIS
software including client and server is priced at about 700,000 yuan.
And its sales strategy is that if you buy server-side software, you must
buy client-side software. The reason is that since users use their
server-side software to publish services, they must use their
client-side software to process data. This is far beyond the affordable
range for some relatively small WebGIS applications. And many commercial
software GIS data and operations are not completely able to convert and
share, resulting in some information islands.

But on the opposite side of commercial GIS software is open source GIS.
Founded in 1994, OGC is committed to researching and establishing open
geographic data interoperability standards, enabling users and
developers to interoperate. The International Geospatial Development
Foundation (Open Source Geospatial Foundation) was established in
February 2006. Its mission is to support the development of open source
geographic information software and remote sensing software and promote
their wider application, provide organizational, legal and financial
assistance for the projects it supports, and promote the development,
promotion and popularization of OSGeo Foundation’s standard software
based on geographic information and its Interoperability Technology.

Free and open source GIS software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Free and open source software is a type of computer software that can be
classified as both free software and open source software. That is,
anyone who is licensed is free to use, copy, research, and modify the
software in any way, and its source code is open and shared, so people
are encouraged to voluntarily improve the design of the software. Such
software is in contrast to commercial software, which is under strict
copyright restrictions and whose source code is generally not available
to users.

At present, there are many free and open source GIS software including
various levels. For example, large desktop GIS includes QGIS and grass
GIS. Currently the more popular server-side software includes GeoServer,
MapServer and QGIS server, as well as open source GIS database projects
such as PostGIS / PostgreSQL spatial database, In addition, there are
some open source projects such as data conversion tools (such as GDAL /
ogr) and map projection algorithm libraries (such as proj and geotrans).
Most of these software are supported by osgeo.

The role of open data
~~~~~~~~~~~~~~~~~~~~~

Open data is a type of data that can be freely used, reused, and
redistributed by anyone. Among its limitations, at best, requires
attribution and redistribution using a similar protocol. Data.gov
contains a lot of open data collected by the U.S. government. In
addition, OpenStreetMap (OSM for short) is also a widely used open data
source. The OSM project was founded by British Steve Coast. The concept
was inspired by the Wikipedia website. It is an online map collaboration
project for building free content, the goal is to create a free-content
map of the world that can be edited by anyone, with an easy-to-navigate
solution for cheap mobile devices.

Components of WebGIS
--------------------

Four components of WebGIS: WebGIS Application Development and GIS
Services

1. Client
2. Web Services and Application Services
3. GIS service
4. Data service

Client: The client is where the user interacts with spatial objects and
analysis functions in Web GIS. It is also where Internet GIS programs
present their output to the user.

Web Servers and Application Servers: Web servers respond to requests
from web browsers via HTTP. When the web server passes requests to other
programs, it requests services from the application server. The
application server acts as a translator or connector between the web
server and the GIS server.

GIS server: GIS server is a main component, which can complete spatial
query, perform spatial analysis, and generate and provide maps to
clients according to user’s request.

Data Servers: Data servers provide spatial and non-spatial data in
relational or non-relational database structures. In this website, we
pay special attention to GIS server as well as client application. Many
GIS servers are on the internet such as GeoServer, MapServer, Mapnik,
MapGuide, QGIS Server, etc. All of these servers are open source
servers, i.e. freely available. ArcGIS also provides a server, but it is
not freely available but has many additional features. All open source
servers are free to download from their respective websites.

.. raw:: html

   <!--
   Client: The client is a place for users to interact with spatially object and analysis functions in web GIS. It is also a place for Internet GIS programs to present outputs to the users.
   Web server and application server: The web server responds to request from web browser via HTTP. When the web server passes the requests to other programs, it requests service from application servers. An application server acts as a translator or connector between the web server and the GIS server.
   GIS server: A GIS server is a major workhorse component that fulfills spatial queries, conducts spatial analysis, and generates and delivers maps to the client based on the user's request.
   Data server: A data server serves data, spatial and non-spatial, in a relational or non-relational database structure.
   In this post we are focusing particularly on GIS servers. There are many GIS servers available on the internet such as GeoServer, MapServer, Mapnik, MapGuide, QGIS server etc. All these servers are open source servers i.e. Freely available. ArcGIS also provides server but it is not available for free, but with many add on features. All the open source servers can be freely downloaded from their respective websites.
   -->

Component product
-----------------

The following products are typically used as components and combined
with other tools in various combinations to create custom applications.

MapServer
~~~~~~~~~

.. raw:: html

   <!--
   MapServer is an open source platform for publishing spatial data and creating interactive mapping applications to the web. It has been in existence since the mid 90s and is recognized as mature and stable, with ongoing active development. Its primary focus is producing maps from multiple layers including base imagery and spatial data sets. It also provides intelligent labeling with advanced typography and layout including collision-detection. It can read and serve spatial data in a variety of formats including Shapefiles, WMS, GDAL, PostGIS, and GeoTIFF. It is often used to produce map tiles along with its MapCache extensions. It has libraries that enable application development in a variety of languages including Python, Perl, Ruby, Java, and PHP.
   -->

MapServer is an open source platform for publishing spatial data and
creating interactive map applications to the Web. It has been around
since the mid-1990s and is considered mature and stable, with continued
active development. Its main focus is to generate maps from multiple
layers, including base imagery and spatial datasets. It also offers
smart labels, including advanced typography and layout, including
collision detection. It can read and serve spatial data in various
formats, including Shapefiles, WMS, GDAL, PostGIS, and GeoTIFF. It is
typically used to generate map tiles and its MapCache extension. It has
libraries that support application development in various languages,
including Python, Perl, Ruby, Java, and PHP.

http://www.mapserver.org

PostGIS
~~~~~~~

PostGIS is an extension to the PostgreSQL database that supports spatial
queries. PostgreSQL is both a relational and object database and is
widely regarded as the most advanced open source database, similar to
Oracle and MS-SQL. PostGIS supports various spatial queries including
proximity, radius, bounding box, collision/overlap detection, etc. It is
a very useful tool that is often used in Web GIS projects.

http://postgis.net/

OpenLayers
~~~~~~~~~~

.. raw:: html

   <!--
   OpenLayers is a front-end UI library for creating web-based spatial apps

   For example, map tiles can be pulled from GoogleMaps or from a custom tile source.
   The advantage this brings is that it enables developers to reuse elements
   Such as tile sources, and focus instead on the more unique aspects
   Of their application such as the "business logic".
   Default components such as tile sources can easily be swapped out at a later time.
   It supports bitmap and vector layers, including points, lines and polygons.
   One of its most widely used features is the ability to overlay data layers
   On top of base maps.
   -->

OpenLayers is a front-end UI library for creating web-based spatial
applications using javascript. It supports various layer sources and
backends. For example, map tiles can be extracted from GoogleMaps or a
custom tile source. The advantage this brings is that it enables
developers to reuse elements such as tile sources and instead focus on
more unique aspects of their application, such as “business logic”.
Default components such as tile sources can easily be swapped out later.
It supports bitmap and vector layers, including points, lines and
polygons. One of its most widely used features is the ability to overlay
data layers on top of the base map.

http://openlayers.org

GDAL (Geospatial Data Abstraction Library)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <!--
   GDAL is a translation library for geospatial data formats.
   It enables import and export of a very large variety of file and encoding types.
   It can be used to transform spatial data between different projection systems.
   Raster data formats are handled by GDAL, and vector data formats are handled by OGR
   Which is now included with GDAL.
   It can also be used to create mosaics from multiple image file sources.
   GDAL is a valuable tool for taking data from disparate sources
   And converting them to work together.
   -->

GDAL is a translation library for geospatial data formats. It can import
and export a wide variety of file and encoding types. It can be used to
convert spatial data between different projection systems. Raster data
formats are handled by GDAL, and vector data formats are handled by OGR,
now included in GDAL. It can also be used to create mosaics from
multiple image file sources. GDAL is a valuable tool for taking data
from disparate sources and transforming it into collaborative work.

http://www.gdal.org

TileMill
~~~~~~~~

.. raw:: html

   <!--
   TileMill is a desktop application that is used to generate map tile images
   Which are then hosted as static files for use as base layers.
   TileMill can be used to create base layers which are visually stunning.
   It has a strong emphasis on aesthetics including many well-thought-out presets
   Which enable people without a background in design
   To produce very attractive and professional map layers.
   TileMill's development is lead by a company called MapBox.
   They offer several attractive paid services including tile hosting
   And an excellent collection of curated and highly-tuned base layers.
   -->

TileMill is a desktop application for generating map tile images, which
are then hosted as static files to be used as base layers. TileMill can
be used to create visually stunning base layers. It has a strong focus
on aesthetics and includes many well thought out presets that enable
people without a design background to make very attractive and
professional map layers. The development of TileMill is led by a company
called MapBox. They offer several attractive paid services, including
tile hosting and curated and fine-tuned base layers.

http://www.mapbox.com/tilemill/

Leaflet
~~~~~~~

Leaflet is a Javascript library with an emphasis on front-end UI. It
supports a combination of multiple base layers and geometry types. It
covers somewhat similar areas to OpenLayers, but with slightly reduced
functionality. Its strengths over OpenLayers are its excellent support
for mobile devices, great product value, clean minimalist design, and a
strong focus on performance.

http://leafletjs.com/

Stack Products
--------------

.. raw:: html

   <!--
   The following products are distributed as "stacks" or "bundles".
   They are pre-configured combinations of modular products.
   Some can be used as-is (after adding configuration and base layers)
   And all of them can be further extended to create custom applications.
   -->

The following products are distributed as “stacks” or “bundles”. They
are preconfigured combinations of modular products. Some can be used as
is (after adding configuration and base layers), and all of them can be
extended further to create custom applications.

GeoServer
~~~~~~~~~

.. raw:: html

   <!--
   GeoServer is primarily based on the Java language.
   It provides basic functionality for creating and editing geospatial data
   And making maps available in a service-oriented architecture.
   It uses the OpenLayers module and provides and implementation
   Of the Web Map Service (WMS) standard.
   It also makes use of the GeoTools framework
   Which covers a slightly smaller subset of MapServer's functionality.
   Like GeoServer itself, is written in Java.
   It will appeal largely to developers already working
   With Java- based tools and platforms.
   -->

GeoServer is mainly based on the Java language. It provides basic
functionality for creating and editing geospatial data and providing
maps in a service-oriented architecture. It uses the OpenLayers module
and provides and implements the Web Map Service (WMS) standard. It also
uses the GeoTools framework, which covers a small subset of MapServer’s
functionality. Like GeoServer itself, it is written in Java. It will
primarily appeal to developers already using Java-based tools and
platforms.

http://geoserver.org/display/GEOS/Welcome

MapGuide
~~~~~~~~

.. raw:: html

   <!--
   MapGuide is a full-featured web-based GIS application
   Primarily written in PHP and Javascript.
   It includes an AJAX-based application UI for viewing and creating mapsand data layers.
   It supports an impressive range of layer formats including ESRI SHP
   SDF, ESRI ArcSDE, PostGIS, SQL Server Spatial, Raster file formats (via GDA)
   OGC, WMS and WFS.
   It also makes use of the OpenLayers toolkit
   And supports custom application development in PHP and Java.
   It will appeal primarily based on its support for various input formats
   Out-of-the-box editing tools, as well as to developers already working with PHP.
   -->

MapGuide is a full-featured web-based GIS application written primarily
in PHP and Javascript. It includes an AJAX-based application UI for
viewing and creating maps and data layers. It supports an impressive
range of layer formats including ESRI SHP, SDF, ESRI ArcSDE, PostGIS,
SQL Server Spatial, raster file formats (via GDA), OGC, WMS and WFS. It
also uses the OpenLayers toolkit and supports custom application
development in PHP and Java. It is primarily based on support for
various input formats, out-of-the-box editing tools, and developers
already using PHP.

http://mapguide.osgeo.org

GeoMoose
~~~~~~~~

.. raw:: html

   <!--
   GeoMoose combines several popular open source libraries to create a powerful
   And flexible mapping platform
   With emphasis on Javascript/AJAX on the front-end.
   It uses MapServer as a back-end and OpenLayers and Dojo (both Javascript-based)
   For its user interface.
   It provides a robust set of tools for viewing, editing
   And querying data from the browser.
   Its development community seems to be very active and have a good forward trajectory.
   Its appeal comes from its feature set and its modern, approachable UI.
   Its well-documented Javascript APIs will make it approachable
   For both Javascript developers and other web builders
   As most web developers have at least some exposure to Javascript.
   -->

GeoMoose combines several popular open source libraries to create a
powerful and flexible mapping platform with an emphasis on
Javascript/AJAX on the front end. It uses MapServer as the backend and
OpenLayers and Dojo (both Javascript based) for its user interface. It
provides a powerful set of tools for viewing, editing and querying data
in the browser. Its development community seems to be very active and
has a good trajectory going forward. Its appeal comes from its feature
set and modern, approachable user interface. Its well-documented
Javascript API will make it accessible to Javascript developers and
other web builders, since most web developers have at least some
exposure to Javascript.

http://www.geomoose.org

GeoDjango
~~~~~~~~~

.. raw:: html

   <!--
   GeoDjango is a set of spatial extensions for the Django application framework.
   Django is written primarily in Python and is one
   Of the most popular general-purpose frameworks
   For building web apps with Python. Unlike GeoMoose or MapGuide
   It does not provide an application out of the box
   And is rather a set of very nicely crafted building blocks
   For building custom applications.
   Unlike some of the other stack products described above
   It makes less assumptions about which other geospatial tools will be used in the stack
   And provides integration points through a series of clearly-designed
   Well-documented APIs.
   It will likely appeal to developers who want more choice
   And control in the building of their applications
   As well as those who prefer the Python language.
   -->

GeoDjango is a set of spatial extensions to the Django application
framework. Written primarily in Python, Django is one of the most
popular general-purpose frameworks for building web applications using
Python. Unlike GeoMoose or MapGuide, it does not provide out-of-the-box
applications, but a set of carefully designed building blocks for
building custom applications. Unlike some of the other stack products
described above, it makes fewer assumptions about which other geospatial
tools will be used in the stack and provides integration points through
a series of clearly designed, well-documented APIs. It may appeal to
developers who want more choice and control when building applications
and those who prefer the Python language.

http://geodjango.org

MapFish
~~~~~~~

.. raw:: html

   <!--
   MapFish is another stack product from the Python community.
   It is based on the (Python-based) Pylons framework
   As well as (Javascript-based) OpenLayers and ExtJs frameworks.
   Unlike GeoDjango, it provides a simple application out-of-the-box
   Which can be customized and extended.
   It also supports development in Rails and PHP via plugins.
   Its appeal is based on the fact that it provides a clean
   Compact starting point, that can be easily extended in a variety of languages.
   Its trade-off relative to GeoDjango is that it makes more choices for the developer
   So makes getting started a bit faster.
   It will likely appeal to developers who have Python or Javascript experience
   As well as Rails/PHP developers who value its clean, compact design.
   -->

MapFish is another stack product from the Python community. It is based
on the (Python-based) Pylons framework, as well as the
(Javascript-based) OpenLayers and ExtJs frameworks. Unlike GeoDjango, it
provides a simple application out of the box that can be customized and
extended. It also supports development in Rails and PHP via plugins. Its
appeal is that it provides a clean, compact starting point that can be
easily extended in various languages. Compared to GeoDjango, it has the
advantage that it gives developers more options so they can get started
faster. It will likely appeal to developers with Python or Javascript
experience, as well as Rails/PHP developers who value its clean, compact
design.

http://mapfish.org
