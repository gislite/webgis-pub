.. Author: Bu Kun .. Title: WCS service foundation

WCS Map Service
===============

WCS - Web Coverage Service, WCS is a specification for sharing
geospatial data in the form of “Coverage” on the Web as defined by the
OGC. The so-called “Coverage” refers to data that can return the value
of any specified point in its space-time domain, and its form is easy to
input into the model for use. The WCS service realizes the sharing of
raster image datasets in the form of “Coverage”.

Mapfile definition
------------------

As in WMS and WFS support, WCS publishing is enabled by adding certain
metadata key/value pairs to the ``.map`` file.

.. figure:: fig-wcs2.jpg

    WMS

MapServer targets only layers that meet the following conditions and
includes them in its WCS function:

-  the data source is a raster and can be processed using GDAL (eg
   GeoTIFF, Erdas Imaging, …);
-  the layer name must be set;
-  the layer type is set to ``RASTER`` ;
-  Web metadata or layer metadata ``wcs_enable_request`` must be set;
-  Web metadata ``wcs_label`` must be set;
-  must set layer metadata ``wcs_label`` , ``wcs_rangeset_name`` ,
   ``wcs-rangeset-label`` ;
-  Layers can be served via WCS (see MS RFC 67);
-  The layer projection must be set, even if the projection is set at
   the map level.

Take a look at the Mapfile used in this section:


.. literalinclude:: ./mfw8.map
   :lineno-start: 1


GetCapabilities request
-----------------------

As in WMS and WFS, you can also use ``GetCapabilities`` to view the
capabilities of WCS:

`http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCapabilities <%7BSITE_URL%7D/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCapabilities>`__

Parse the parameters using Python:

::

   >>> [print(x) for x  in url.split('&')]
   http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map
   SERVICE=WCS
   VERSION=2.0.1
   REQUEST=GetCapabilities

View the output results in XML format. Only the parts related to version
are shown here:

::

   <ows:ServiceType codeSpace="OGC">OGC WCS</ows:ServiceType>
   <ows:ServiceTypeVersion>2.0.1</ows:ServiceTypeVersion>
   <ows:ServiceTypeVersion>1.1.1</ows:ServiceTypeVersion>
   <ows:ServiceTypeVersion>1.0.0</ows:ServiceTypeVersion>
   <ows:Profile>http://www.opengis.net/spec/WCS/2.0/conf/core</ows:Profile>
       

You can see that the versions of WCS are:

-  2.0.1
-  1.1.1
-  1.0.0

DescribeCoverage request
------------------------

The ``DescribeCoverage`` request lists more information about a specific
coverage product.

`http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=world-img <%7BSITE_URL%7D/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=world-img>`__

The parameters are described as follows:

::

   >>> [print(x) for x  in url.split('&')]
   http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map
   SERVICE=WCS
   VERSION=2.0.1
   REQUEST=DescribeCoverage
   COVERAGEID=world-img

The parameters vary greatly between different versions, and the returned
results are also different. You can open the link to have a look at it:

WFS 1.0.0:

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=1.0.0&REQUEST=DescribeCoverage&COVERAGE=world-img

Parse the URL:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map
   1 SERVICE=WCS
   2 VERSION=1.0.0
   3 REQUEST=DescribeCoverage
   4 COVERAGE=world-img

WFS 1.1.1:

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=1.1.1&REQUEST=DescribeCoverage&IDENTIFIERS=world-img

Parse the URL:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map
   1 SERVICE=WCS
   2 VERSION=1.1.1
   3 REQUEST=DescribeCoverage
   4 IDENTIFIERS=world-img

Usage of GetCoverage
--------------------

``GetCoverage`` returns data, which is raster data. Since the request
cannot specify the name and suffix of the file at this time, the file
can be downloaded and saved, and modified into a file with ``.tif`` as
the suffix. This file has geospatial information.

`http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=1.1.0&REQUEST=GetCoverage&IDENTIFIER=world-img&FORMAT=image/tiff&BOUNDINGBOX=43,33,44,34,urn:ogc:def:crs:EPSG::4326 <%7BSITE_URL%7D/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=1.1.0&REQUEST=GetCoverage&IDENTIFIER=world-img&FORMAT=image/tiff&BOUNDINGBOX=43,33,44,34,urn:ogc:def:crs:EPSG::4326>`__

The parameters are decomposed as follows:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map
   1 SERVICE=WCS
   2 VERSION=1.1.0
   3 REQUEST=GetCoverage
   4 IDENTIFIER=world-img
   5 FORMAT=image/tiff
   6 BOUNDINGBOX=43,33,44,34,urn:ogc:def:crs:EPSG::4326

GetCoverage return image
~~~~~~~~~~~~~~~~~~~~~~~~

``GetCoverage`` can also directly return the image, just modify
``format=image/png`` . However, it should be noted that the returned
image must be returned by a separate request in the web, and cannot be
used in the web page as an ``<image>`` object.

The following is an example, the picture in the web page, which cannot
be displayed here. But by “right click” -> “view image”, you can see
that it is a picture.


http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=1.1.0&REQUEST=GetCoverage&IDENTIFIER=world-img&FORMAT=image/tiff&BOUNDINGBOX=33,70,54,135,urn:ogc:def:crs:EPSG::4326&format=image/png


.. figure:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw8.map&SERVICE=WCS&VERSION=1.1.0&REQUEST=GetCoverage&IDENTIFIER=world-img&FORMAT=image/tiff&BOUNDINGBOX=33,70,54,135,urn:ogc:def:crs:EPSG::4326&format=image/png

    Result of WCS
