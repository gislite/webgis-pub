.. Author: gislite .. Title: Introduction to MapServer

Introduction to MapServer
=========================

MapServer is a real-time map publishing system based on the fat
server/thin client mode. When the client sends a data request, the
server processes the spatial data in real time and sends the generated
data to the client. The core part of MapServer is the map operation
module written in C language, and the implementation of many functions
of MapServer itself depends on some open source or free libraries.

The core part of MapServer is the map manipulation module written in C
language, and many of its functions rely on some open source or free
libraries. Using the support of GEOS and OGR/GDAL for a variety of
vector and raster data, the projection transformation is carried out in
real time through the Proj.4 shared library. MapServer follows OGC
series specifications and can integrate PostGIS and open source database
PostgreSQL, and store and SQL query the geospatial data. Based on a
series of client-side JavaScript APIs such as ka-map, MapLab, Cartoweb
and Chameleon to support the transmission and expression of geospatial
data, and comply with a series of WMS, WFS, WCS, WMC, SLD, GML and
Filter Encoding formulated by OGC specification.

Development history of MapServer
--------------------------------

MapServer is an open source geospatial data rendering engine written in
C language. It originated from the University of Minnesota (UMN), NASA
and the Minnesota Department of Natural Resources (MNDNR) in the
mid-1990s. A collaborative project - ForNet, and later the TerrSIP
project. Government support played a big role in the early development
of MapServer.

This is an open source software released under the MIT-style License for
publishing spatial data and interactive map applications on the Web,
supporting all major operating systems, including Windows, Linux, Mac OS
X, etc. Its positioning is not to implement a full-featured GIS, but to
provide most of the core GIS functions for Web applications.

In 1994, Steve Lime, the father of MapServer, and his MapServer were
familiar to more people. MapServer is not isolated in its development
and growth, but has been supported by many open source communities and
open source enthusiasts. In November 2005, the MapServer Foundation was
established with the aim of “promoting a professional open source
network mapping development environment and community. Even though it
initially focused on network mapping projects, it hopes to provide
funding to other open source geographic information projects”, not only
promotes the professional development of MapServer, but also promotes
the development of the entire open source network mapping technology.

With the further development of open source geographic information
system software and the further optimization of open source network
mapping environment, in February 2006, the MapServer Foundation was
officially renamed the Open Source Geospatial Foundation (OSGeo), and
Autodesk added MapGuide as an open source code to the foundation. It
will further promote the development of MapServer.

Characteristics of MapServer
----------------------------

MapServer is a popular open source project for displaying dynamic
spatial maps on the Internet. It has the following characteristics:

-  Support for displaying and querying hundreds of grid, vector and
   database formats. Supported vector formats: ESRI shapefiles, PostGIS,
   ArcSDE of ESRI, etc. (implemented by OGR library). Supported grid
   formats: TIFF/GeoTIFF, EPPL7, etc. (implemented through the GDAL
   library). For shapefile files, you can build a quad tree spatial
   index.
-  Ability to run on many different systems (Windows, Linux, Mac OS X,
   etc.)
-  Available in two ways: CGI (for CGI, Ajax, Flex developers) and
   MapScript (For Php, Java, C # developers), native CGI is the most
   efficient
-  Support for popular scripting languages and development environments
   (PHP, Python, Perl, Ruby, Java, .NET)
-  On-the-fly projection
-  High quality rendering model
-  The output of custom template is fully supported.
-  Many off-the-shelf open source application environments
-  MapFile is the core of MapServer. It organizes various map elements
   into a hierarchical object system, and define the data source, the
   data format used, user interaction and support for the OGC protocol.
-  Support the font standard TrueType jointly developed by Microsoft and
   Apple.
-  Block (tiled) vector and raster data are supported.
-  Automatic control of map elements (such as scale, legend, reference,
   etc.).
-  The image scale is adjusted automatically.
-  Generate thematic maps using logical or regular expressions.
-  Feature annotations (including dimension conflict resolution).
-  MapServer can be configured dynamically through URLs.
-  Dynamic projection transformation is supported.
-  Support for several Open Geospatial Consortium network
   specifications: WMS (client/server), non-transactional WFS
   (client/server), WCS (server only), WMC, SLD,GML and Filter Encoding.

In its most basic form, MapServer is an inactive CGI program on a Web
server. When a request is sent to MapServer, it uses the information and
Mapfile passed in the requested URL. Creates an image of the requested
map, the request can return the legend, ruler, reference map and
variable values passed by CGI.

Compared with the many WebGIS solutions provided by commercial
enterprises, MapServer is an open source project. This means that you
can use MapServer for free and have the right to modify, copy and
redistribute it yourself, MapServer has many advantages as well:

MapServer is an open source real-time map publishing system based on fat
server / thin client mode. When the client sends data requests, the
server processes the spatial data in real time and sends the generated
data to the client. The core part of MapServer is the map operation
module written in C language, and many of its functions depend on some
open source or free libraries.

Using GEOS, OGR/GDAL to support a variety of vector and raster data,
real-time projection transformation through the Proj.4 shared library.
At the same time, it also integrates PostGIS and the open source
database PostgreSQL to store and query geospatial data, and supports the
transmission and expression of geospatial data based on a series of
client-side JavaScript APIs such as ka-map, MapLab, Cartoweb, and
Chameleon. A series of specifications such as WMS, WFS, WCS, WMC, SLD,
GML and Filter Encoding formulated by OGC.

MapServer creates a map image based on spatial information stored in a
digital format. It can handle vector and raster data. MapServer can
render more than 20 different vector data formats, including
shapefile,PostGIS and ArcSDE geometric features OPeNDAP,Arc/Info
coverage and Census TIGER files.

Not all information displayed on the map must be in vector format. For
example, aerial or satellite photos of an area can be displayed behind
the rendered vector data to understand more clearly how these vector
elements relate to the characteristics of the real world. MapServer
reads two grid formats natively: GeoTIFF and EPPL7. However, you can
read more than 20 formats (including Windows bitmaps, GIF, and JPEG)
through the GDAL package, although MapServer understands and can render
these grid types, it cannot mark images with spatial information.



Components of MapServer
-----------------------

One of the realization methods of WebGIS is to use Common Gateway
Interface (CGI) technology. On the server side, the WebServer and the
GIS spatial database are connected through the CGI application program,
and the client side can query and analyze the spatial data only by using
the browser [2]. The University of Minnesota in the United States
provides a WebGIS solution: MapServer, which uses CGI technology.

MapServer is an open source WebGIS project developed in C language. It
is a real-time map publishing system based on fat server / thin client
mode. When the client sends data requests, the server processes the
spatial data in real time and sends the generated data to the client.

MapServer supports a three-tier architecture:

-  Application layer: client browser
-  Middle tier: MapServer CGI module / scripting language + MapScript,
   Web server
-  Storage tier: GIS spatial database

A simple MapServer consists of the following parts, as shown in the
figure:

.. figure:: mapserver_general.png
   :alt: Schematic of MapServer principle

   Schematic of MapServer principle

MapFile

   Structured text configuration files for MapServer applications. It
   defines the field of the map and is used to tell MapServer where the
   data is and where to output the image. It also defines the map layer.
   Including their data source, projection and notation. It must have a
   .map extension, otherwise MapServer will not recognize it. MapFile
   files organize various map elements into a system of objects with
   hierarchical relationships. Data sources, data formats used, user
   interaction and support for the OGC protocol are also defined in
   MapFile. Objects included in MapFile and their hierarchical
   relationships:

Geographic Data

   MapServer can take advantage of many types of geographic information
   data sources. The default is the ESRI data format, and other formats
   of data are also supported.

HTMLPages

   It is the interface between the user and MapServer, usually located
   at the web root. In its simplest form, MapServer can be called to
   place a static map image on an HTML page. To make the map
   interactive, the image is placed on an HTML form on the page.

MapServer CGI

   Binary executables. It can receive requests to return images, data,
   etc., located in the cgi-bin or scripts directory of the web server.
   The user of the WEB server must have execute permissions on these
   directories. For security reasons, they cannot be in the root
   directory of the web. By default, this program is called mapserv.

WEB/HTTP Server

   The HTML page is provided when the user’s browser is hit. You need a
   working Web (HTTP) server. For example, Apache or Microsoft’s IIS,
   they are on the same machine where you installed MapServer.

Two modes of MapServer
----------------------

MapServer can be regarded as the general name of two independent
modules: MapServer CGI module and MapScript module. On the server side,
any module can be used to write WebGIS programs. However, they use the
same configuration file MapFile.

MapServer can run in two different modes: CGI and MapScript. In CGI
mode, MapServer runs as a CGI script in the Web server environment. This
is easy to set up and produce fast, direct applications. In MapScript
mode, you can access MapServer API from Perl,Python or PHP. The
MapScript interface allows flexible, feature-rich applications that can
still take advantage of MapServer’s template tools.

Comparison between MapServer and GeoServer
------------------------------------------

MapServer and GeoServer are both widely used open source WebGIS tools.
Both publish maps through the Internet and are often compared. MAPSERVER
is also OGC-compliant WMS and non-transactional WFS, based on CGI and
written in C++; GEOSERVER is written in Java (you need to install Java
SDK (not JRE) to run it), based on servlet and using the struts
framework.

-  Functionally: MapServer is weaker than GeoServer, QGIS and stronger
   than UDIG.
-  Efficiency: Mapserver’s support for WMS (Web Map service) is more
   efficient, while Geoserver is better at attribute queries combined
   with WFS (Web Feature service) specifications.

In addition to functional comparison, special attention should be paid
to the technical selection during development. MapServer focuses on map
service functions and can be used as project components (or even core
components), but other functions need to be implemented by developers
most of the time; GeoServer is a relatively complete suite, which can
basically be used as a product after deployment and installation.

MapServer is not a full-featured GIS, it does not provide integrated
DBMS (Database Management System) tools, it has limited analytical
capabilities, and there are no georeferencing tools.

Which is better? It’s hard to tell, depending on how you want to publish
your data and what language you’re better at using. Both are excellent
and have excellent documentation and user base. GEOSERVER enables you to
edit spatial data online and generate thematic maps. Maps are published
in XML files. MAPSERVER is good at generating thematic maps and is more
mature than ever. Maps are published through text configuration files.

Which one is more appropriate? I advocate using MapServer if you just
publish the map and don’t allow modification, it’s easier to maintain.
GeoServer was chosen because of wanting better features such as online
editing and database support like PostgreSQL or Oracle spatial database,
another advantage of GeoServer is that there is a free client software
UDIG.

.. _characteristics-of-mapserver-1:

Characteristics of MapServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides two ways of working, the CGI way (for CGI, AJAX, FLEX
developers) and the MapScript way (for Php, Java, C#, Python
developers). The native CGI method is the most efficient, and with
TileCache, large-scale map tile data can be quickly generated. Compared
with commercial or open source platforms based on .Net and J2EE,
MapServer is more suitable for high-load large-scale Internet map
applications. MapServer is a map service software written based on C,
which is faster than GeoServer written in JAVA. Moreover, the history of
MapServer is longer than that of GeoServer, and even the performance of
MapServer is comparable to that of commercial ArcIMS.

Characteristics of GeoServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GeoServer（http://geoserver.org/ ）is a J2EE compliant and implements
the WCS, WMS and WFS specifications , supports TransactionWFS (WFS-T),
and its technical core is the integration of the well-known
Java-developed GIS tools GeoTools.

For spatial information storage, it supports ESRI Shapefile and spatial
databases such as PostGIS, Oracle, and ArcSDE, and the output GML files
meet the requirements of GML2.1.

Because it is pure Java, it is more suitable for complex environmental
requirements, and because of its open source, development organizations
can flexibly implement specific target requirements based on GeoServer,
which are lacking in commercial GIS components.

As a pure Java implementation, GeoServer is deployed in application
servers, such as Tomcat; its WMS and WFS components respond to requests
from browsers or uDig to access configured spatial databases, such as
PostGIS, OracleSpatial, etc., and generate Maps and GML documents are
transferred to the client.

GeoServer has the following advantages:

1. Written in Java language, standard J2EE framework, based on servlet
   and STRUTS framework, supporting efficient Spring framework
   development;
2. Compatible with WMS and WFS features, support WFS-T specification;
3. Efficient database supports PostGIS, ShapeFile, ArcSDE,Oracle, MySQL,
   etc.
4. Support hundreds of projections;
5. Ability to output network maps to formats such as jpeg, gif, png;
