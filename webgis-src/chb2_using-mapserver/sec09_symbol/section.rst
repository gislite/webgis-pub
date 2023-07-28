.. Author: gislite .. Title: Use custom styles in Mapfile

Use custom styles in Mapfile
============================

Vector data can be divided into three types: point, line and surface.
The simplicity of the data type structure gives the diversity of
expression. In MapServer, you can set styles in various dimensions such
as color, size (thickness), and transparency for points, lines, and
surfaces.

Point
-----

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfy3.map&layer=world-country&layer=world-city&mode=map

The Mapfile used is:


.. literalinclude:: ./mfy3.map
   :lineno-start: 1


Line fill example
-----------------

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfu1.map&layer=world-country&mode=map


The Mapfile used is:


.. literalinclude:: ./mfu1.map
   :lineno-start: 1


Circular fill exampl
--------------------

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfu2.map&layer=world-country&mode=map

The Mapfile used is:


.. literalinclude:: ./mfu2.map
   :lineno-start: 1


River style
-----------

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfmr.map&layer=wroads&mode=map


The Mapfile used is:


.. literalinclude:: ./mfmr.map
   :lineno-start: 1


``GepMap`` can be further used to get the effect of the magnification:

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfmr.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=wroads&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=500&height=300&styles=