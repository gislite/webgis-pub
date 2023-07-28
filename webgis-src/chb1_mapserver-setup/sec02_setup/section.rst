.. Author: gislite .. Title: Install and configure MapServer

Install and configure MapServer
===============================

Setting up the initial runtime environment when starting a job can be
tedious, especially when following the step-by-step steps, but the basic
“Hello World” still doesn’t appear, and it can be maddening. Building a
running environment requires comprehensive technology, some experience,
and a bit of luck. Don’t underestimate the ability to configure the
runtime environment. Many programmers cannot build a development
environment by themselves, let alone a real production environment.

Basic requirements for installing and configuring MapServer
-----------------------------------------------------------

MapServer is an open source software written in C language, which itself
relies on some open source or free libraries, such as Shapelib,
FreeType, Proj.4, GDAL/OGR, GD Library, Regex. MapServer is written in
C, and the sub-projects it depends on have corresponding C language
implementation versions. When running MapServer, the relevant class
libraries must be installed, and sometimes they also depend on specific
versions of certain class libraries. When compiling and installing
MapServer, you need to have a certain understanding of these libraries.

-  Shapelib provides the ability to read, write and update data in the
   “ESRI Shapefile” format, and to modify the corresponding property
   file (.dbf);
-  FreeType is a font rendering library, capable of rendering most
   vector and bitmap font formats, designed to be small, efficient,
   highly customizable, and as lightweight as possible without
   sacrificing performance and functionality;
-  Proj.4 is a geographic projection library that provides a variety of
   projection definitions and interfaces;
-  GDAL/OGR, GDAL (Geospatial Data Abstraction Library) is an open
   source raster spatial data conversion library under the X/MIT
   license. It utilizes an abstract data model to express the various
   file formats it supports. It also has a range of command line tools
   for data transformation and processing. OGR is a branch of the GDAL
   project, similar in function to GDAL, except that it provides support
   for vector data. There are many well-known GIS products that use the
   GDAL/OGR library, including ESRI’s ArcGIS 9.3, Google Earth and the
   cross-platform GRASS GIS system.
-  GD Library, generate images dynamically, supports most formats: JPEG,
   GIF, WEBP, XPM, BMP. Usually used to dynamically generate charts,
   pictures, thumbnails, etc., often used in the web environment;
-  Regex, provides regular expression support for MapServer.

By understanding these libraries, you can simplify the installation
process by reducing the number of features to install. Even though you
only install a basic version of MapServer, it still has the ability to
create a powerful application. After you become familiar with MapServer,
you can add other features you want.

MapServer is a program that generates maps, but provides a CGI
interface (the operation of MapServer CGI depends on PHP), and related
functions can be called through Web access. So many times in order to
run MapServer, you need to install a web server (such as Apache 2), and
a tool (such as FastCGI) to let the application (MapServer) communicate
with the web server (Apache). Apache 2 does not have CGI enabled by
default.

.. figure:: zz_fig_gis_libs1.png
   :alt: Libraries that MapServer depends on

   Libraries that MapServer depends on



Detailed introduction of MapServer related class libraries
----------------------------------------------------------

GD
    GD is an image library. Since Mapserver uses GD for image rendering, it
    must be installed. GD has its own dependent class library, including
    zlib, libpng, FreeType2.x and libJPEG. These types enable GD to perform
    image compression (for supported data), to render PNG images, to use
    TrueType fonts, and to render JPEG images. Since the license on GIF has
    expired, it is now available as well.

    GD support has been removed in MapServer 7. 0.

FreeType
    FreeType is a font rendering engine. It is not referenced directly by
    Mapserver, but is used by GD to render fonts. Since TrueType is more
    attractive than the bitmap fonts provided by Mapserver, it is worth
    including this class library.

LibPNG
    LibPNG enables Mapserver to render JPEG images. A new version has been
    released since 2001. Generally speaking, this library should already be
    installed on the machine. If not, you can install it yourself. Libpng
    uses MapServer to render PNG images. It is not directly used by
    MapServer, but by GD. Libpng requires the library zlib.

Zlib
    Zlib is a data compression library used by GD.

GDAL
    GDAL is a conversion class library for raster data. It provides import
    and projection of raster images with geographic projections. You won’t
    use those features in this book, but this library is necessary to
    install basic Mapserver.

OGR
    The OGR library provides the ability to read and write some vector
    formats. In this book you will use some of the features provided by OGR.

Proj.4
    Proj.4 is a program for cartographic projection. It can be called by
    Mapserver, or it can be projected on the entire database alone.

Shapelib
    Shapelib is a C program to generate and process Shape files. You can use
    the useful tools provided by this class library without having to write
    any C code yourself. It has the contents of generating shape files
    (including DBF files) and destroying shape files and DBF files, and
    change the projection of the shape file. Some of these features are
    based on Proj.4.

Libcurl
    libcurl is a client library that supports FTP, FTPS, HTTP, HTTPS,
    GOPHER, TELNET, DICT, FILE and LDAP URL conversion. This library is
    required if you want to provide WMS support. The WMS protocol is used to
    transmit map images and file data over the network. To keep the
    Mapserver environment simple, you don’t have to install it.

SDE client library
    The SDE client library is part of ESRI’s spatial data warehouse.
    If you want Mapserver to access it, you need to compile the library.

PostgreSQL client library
~~~~~~~~~~~~~~~~~~~~~~~~~

The PostgreSQL client library provides the ability to access PostGIS
data using Mapserver. They provide similar functionality to ESRI
products, but they are not open source.

Oracle Spatial client library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Oracle Spatial client library enables users to access the Oracle
Spatial Data Warehouse using MapServer. They provide similar
functionality to ESRI products.

Ming
~~~~

Ming enables MapServer to create SWF videos. It can provide some
interesting functions.

PDFLib
~~~~~~

It is also useful for PDFLib to be able to output in PDF format using
MapServer.

Installation under Debian / Ubuntu system
-----------------------------------------

Debian / Ubuntu is my most commonly used Linux release, and its
well-designed package management tool is really enjoyable. To install
MapServer, simply run the following installation command (administrator
privileges are required):

In Debian 12:

::

   apt install -y apache2 php8.2 libapache2-mod-fcgid cgi-mapserver \
       mapserver-bin libapache2-mod-php
   a2enmod authnz_fcgi
   a2enmod cgi
   service apache2 restart



In Debian 9:

::

   apt install -y apache2 php7.0 libapache2-mod-fcgid cgi-mapserver \
       mapserver-bin libapache2-mod-php
   a2enmod authnz_fcgi
   a2enmod cgi
   service apache2 restart

In Ubuntu 22.04:

::

   apt install -y apache2 php8.1 libapache2-mod-fcgid cgi-mapserver \
       mapserver-bin libapache2-mod-php
   a2enmod authnz_fcgi
   a2enmod cgi
   service apache2 restart

In Ubuntu 18.04:

::

   apt install -y apache2 php7.2 libapache2-mod-fcgid cgi-mapserver \
       mapserver-bin libapache2-mod-php
   a2enmod authnz_fcgi
   a2enmod cgi
   service apache2 restart

Almost no difference except the different versions of PHP Debian/Ubuntu. 
When installing these packages, if the corresponding dependencies are missing, 
they will be installed automatically.

After the installation is complete, you can enter the following command on the terminal to view the results:

::

   $ mapserv -v
   MapServer version 7.0.4 OUTPUT=PNG OUTPUT=JPEG OUTPUT=KML SUPPORTS=PROJ
       SUPPORTS=AGG SUPPORTS=FREETYPE SUPPORTS=CAIRO SUPPORTS=SVG_SYMBOLS 
       SUPPORTS=RSVG SUPPORTS=ICONV SUPPORTS=FRIBIDI SUPPORTS=WMS_SERVER 
       SUPPORTS=WMS_CLIENT SUPPORTS=WFS_SERVER SUPPORTS=WFS_CLIENT 
       SUPPORTS=WCS_SERVER SUPPORTS=SOS_SERVER SUPPORTS=FASTCGI 
       SUPPORTS=THREADS SUPPORTS=GEOS INPUT=JPEG INPUT=POSTGIS 
       INPUT=OGR INPUT=GDAL INPUT=SHAPEFILE


And some configureations are needed for the service of MapServer.
The config files could be founds under the `etc` directory of the soruce codes.
May be you just need Apache. 
Howerver, //webgis.pub uses Nginx for reverse proxy  to Apache.

Notes about FastCGI.

CGI (Common Gateway Interface) defines the method of interaction between
web server and external content generation program, which usually refers
to CGI program or CGI script. It is the simplest and commonly used
method to realize dynamic pages on the website, making the interaction
between external program and web server possible. But early CGI programs
ran in separate processes and created a process for each web request.
This method is very easy to implement, but inefficient and difficult to
scale. In the face of a large number of requests, a large number of
processes are created and killed, which greatly reduces the performance
of the operating system. In addition, because the address space cannot
be shared, resource reuse is also limited.

FastCGI uses persistent (daemon) processes to handle a chain of
requests, these processes are managed by the FastCGI server, not the web
server. When a request comes in, the web server passes the environment
variables and the page request to the FastCGI process through a socket,
such as the FastCGI process and the web server (both locally), or a TCP
connection (FastCGI process on the remote server farm) is passed to the
FastCGI process.

Configure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then, edit the file of Apache2 configure. Sush as ``more /etc/apache2/sites-enabled/webgis_pub_apache.conf`` .

::

    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
    <Directory "/usr/lib/cgi-bin">
    AllowOverride None
    Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
    Require all granted
    </Directory>


Installation under Windows system
---------------------------------

To install MapServer under Windows, you also need to install Apache2,
CGI, and MapServer programs, which also have binary packages under
Windows, but such a step-by-step installation is more troublesome and
prone to problems. It is recommended to use ``MS4W`` (MapServer 4
Windows), the link is: https://www.ms4w.com/ .
