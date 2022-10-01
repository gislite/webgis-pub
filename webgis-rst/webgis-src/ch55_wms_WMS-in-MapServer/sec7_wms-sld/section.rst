.. Author: Bu Kun .. Title: WMS layers use SLD

WMS layers use SLD
==================

By using SLD, the style of the map can be modified dynamically.

This page describes the process of leveraging Styled Layer Descriptor
(SLD) support in WMS ``Getmap`` requests using Mapserver. SLD supports
both server-side (ability to read SLD and apply it with ``getmap``
requests) and client-side (including sending SLD requests to the server
and dynamically generating SLD files from the map server’s Mapfile). SLD
support was added to MapServer in version 4.2.

Definition and effect of SLD
----------------------------

SDL is defined using the XML format. Let’s take a look at the example:


.. literalinclude:: ./sld_world_lyr.xml
   :lineno-start: 1


Effect:

.. figure:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=&SLD=http://webgis.pub/sld_world_lyr.xml
   :alt: Use GetMap operation with SLD

   Use GetMap operation with SLD

Get a partial map with GetMap

The URL is parsed as follows:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map
   1 SERVICE=WMS
   2 VERSION=1.3.0
   3 REQUEST=GetMAP
   4 LAYERS=states
   5 BBOX=73,3,136,54
   6 CRS=CRS:84
   7 INFO_FORMAT=text/html
   8 format=image/png
   9 width=200
   10 height=150
   11 styles=
   12 SLD=http://webgis.pub/sld_world_lyr.xml

Definition and effect of SLD 1.1.0
----------------------------------

The definition of SLD version 1.1.0 is not quite the same as the latest
version.


.. literalinclude:: ./sld_world_lyr110.xml
   :lineno-start: 1


Effect:

.. figure:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=&SLD=http://webgis.pub/sld_world_lyr110.xml
   :alt: The effect of SLD 1.0.0

   The effect of SLD 1.0.0

Get a partial map with GetMap

The URL is parsed as follows:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map
   1 SERVICE=WMS
   2 VERSION=1.3.0
   3 REQUEST=GetMAP
   4 LAYERS=states
   5 BBOX=73,3,136,54
   6 CRS=CRS:84
   7 INFO_FORMAT=text/html
   8 format=image/png
   9 width=200
   10 height=150
   11 styles=
   12 SLD=http://webgis.pub/sld_world_lyr110.xml
