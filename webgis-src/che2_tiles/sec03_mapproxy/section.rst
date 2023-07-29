.. Author: gislite .. Title: Installation and use of MapProxy

Installation and use of MapProxy
================================

MapProxy is the Swiss Army knife of WMS web map service and slicing
service provider. It caches, accelerates and transforms existing data
services and serves any desktop and web client that supports the OGC
standard.

MapProxy installation
---------------------

At present, MapProxy is already in the official source of Debian/Ubuntu,
and you can use the ``apt`` Command to install.

To use a newer version, you can establish a Python virtual environment,
and then use the ``pip`` Command to install.

MapProxy1.11.0 installation: refer to official help

Create a virtual environment for Python

Administrator privileges are required to install dependencies.

::

   sudo apt install python-imaging python-yaml libproj9
   sudo apt install libgeos-dev python-lxml libgdal-dev python-shapely

With regard to dependent class libraries, libproj, Proj4 is a coordinate
transformation library; Pillow,Pillow (PIL) is an image processing
library.

Installation

::

   pip install PyYAML

Shapely and GEOS (optional)

If you want to use the coverage feature of MapProxy, you need to install
Shapely. Shapely provides Python bindings for the GEOS library. To
install and use, you need ``libgeos-dev`` Vs. ``python-shapely`` . If a
newer version (1.2.0 or later) of Shapely is not available on the
system, you can use the ``pip`` Command is installed as a third-party
package for Python.

GDAL (optional)

The coverage feature allows users to read geometry from OGR databases
(Shapefiles, PostGIS, etc.). This package is optional and only support
for OGR data sources (BBOX,WKT and GeoJSON overrides are natively
supported) is required. OGR is GDAL ( ``libgdal-dev`` ) part of the
package.

Lxml (optional)

Lxml is used to support more advanced WMS feature information
operations, such as XSL transactions, or to connect multiple XML/HTML
documents. The name of this package is ``python-lxml`` .

Install MapProxy

::

   pip install MapProxy

To check whether the installation is successful, use the following
command

::

   mapproxy-util --version

Create a profile for MapProxy:

::

   mapproxy-util create -t base-config mymapproxy

This command creates a folder called mymapproxy that contains a minimum
sample configuration ( ``mapproxy.yaml`` And ``seed.yaml`` ), and two
completed sample configuration files ``full_example.yaml`` 和
``full_seed_example.yaml`` ).

Start the test service

::

   cd mymapproxy
   mapproxy-util serve-develop mapproxy.yaml

Start the service on the specified port

::

   mapproxy-util serve-develop ~/mapproxy/mapproxy.yaml -b 0.0.0.0:8011

MapProxy comes with a demo service that lists all configured WMS and TMS
layers. You can access that service by visiting
http://localhost:8080/demo/.

Use
---

Then configure the mapproxy.yaml file according to the tutorial. The
following is an introduction to the components of the configuration
file. During testing, only the mapproxy.yaml configuration was used.

mapproxy.yaml and seed.yaml

Mapproxy.yaml: the main configuration file that configures all parts of
the service, such as which services need to be started, where the data
comes from, and those that need to be cached

Mapproxy-seed mapproxy creates all the required images, and to speed up
requests, this tool can cache one or more polygonal areas.

The configuration file uses the YAML format ``mapproxy.yaml`` It mainly
includes the following parts:

``globals`` : Set default values, global variables that can be used in
other configuration sections.

``services`` : Services provided by MapProxy, such as jWMS or TMS.

``sources`` : Defines where MapProxy can fetch new datasets.

``caches`` : configure internal caches

``layers`` : Configure the layers provided by MapProxy, each layer can
contain multiple data sources and caches.

``grids`` : defines the grid that MapProxy uses to arrange cached images

Note that to maintain formatting, you cannot use the tab key, but only
the spacebar.

The contents of the configuration file are posted as follows, and the
code looks like this:

::

   services:
      tms:
        use_grid_names: true
   layers:
      - name: my_layer
        title: WMS layer from tiles HiFleet
        sources: [mycache]
   caches:
      mycache:
        grids: [webmercator]
        sources: [my_tile_source]
   sources:
      my_tile_source:
        type: tile
        url: url.png
   grids:
    webmercator:
      base: GLOBAL_WEBMERCATOR
      srs: 'EPSG:3857'

For this example, you can use LeafLetJS or OpenLayers for access
testing.

The code for posting OpenLayers is as follows:

::

   var raster = new ol.layer.Tile({
           source: new ol.source.XYZ({
   url:'http://localhost:8080/tms/1.0.0/my_layer/webmercator/.png'
           }),
   opacity: 1,
   visible:false
       });
