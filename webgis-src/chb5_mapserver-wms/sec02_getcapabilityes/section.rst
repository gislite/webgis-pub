.. Author: gislite .. Title: WMS GetCapabilities access

WMS service with ``GetCapabilities`` access
============================================

Web Map Service (Web Map Service,WMS) generates “maps” about geospatial
data, which belongs to the specification published by OGC. A map is a
visual description of geographic data, not geographic data itself. Web
map service provides unified access to the interface supported by the
map server through the Web client on the Internet.

Instruction
-----------

The basic web map service provides 4 interfaces ``GetCapabilities``,
``GetMap``, ``GetFeaturelnfo`` and ``DescribeLayer`` to support the
creation and display of registered and layered, map-like view
information , these views come from multiple service sources, both
remote and heterogeneous.

When requesting a map, the client can specify the information displayed
on the map, layer styles, bounds, projection or spatial reference
system, as well as output format, image size, background transparency
and color, etc. When generating maps with the same BBox (bounding
rectangle), SRS (spatial reference system) and dimensions, these maps
can be overlaid to further generate a composite map. WMS supports the
creation of a network of distributed map services so that clients can
generate custom maps.

The basic Web mapping service mainly provides the following functions:

1. Other programs can provide information about map services: what it
   can do and what can be further queried.
2. A map can be dynamically constructed in the form of pictures, graphic
   element sets or geographic element data sets.
3. Answer basic queries about map content.
4. The advanced web map server supports the combination with cascading
   map servers and style layer descriptors.

The stacked map server aggregates the contents of multiple independent
map servers into one server, and provides other servers with functions
such as output format conversion, coordinate conversion and so on.

The style layer descriptor (Styled-Layer Descriptor,SLD) allows you to
define symbols for feature data, rather than the established named
layers and their styles. SLD is an extension of WMS. WMS services that
support SLD get elements from WFS. The map is then drawn using the style
information provided by the user. The style layer descriptor adds
operations that are not supported by basic WMS: ``DescribeLayer`` 、
``GetLegendGraphic`` 、 ``GetStyles`` And ``PutStyles`` .

It is explained here that the WMS service is published using MapServer.
As explained in the previous section, a Mapfile corresponds to a map.
Through WMS access, you can access layer information in Mapfile more
flexibly. The map design function of Mapfile is enhanced to a service
function.

Access the WMS service
----------------------

Since each WMS is independent, a description of the respective functions
must be provided. This “service metadata” enables each client to
formulate legitimate requests and to construct a queryable directory to
guide clients to specific WMSes. ``GetCapabilities`` allows a client (or
client agent) to request a WMS to reveal its mapping content and
processing capabilities. The returned result is an XML document that
describes the content of the service information and the parameters that
can be requested; in the case of a specific WMS, general information
about the service itself and specific information about the available
maps are returned.

This Mapfile is configured with the WMS service. The contents of Mapfile
``mfb1.map`` is:


.. literalinclude:: ./mfb1.map
   :lineno-start: 1


With the front ``mfa1.map`` Compared to:


`diff_mfb1_mfa1.html <diff_mfb1_mfa1.html>`_


Note the version ``1.3.0`` here. OGC’s WMS has two major versions,
``1.1.1`` and ``1.3.0``. If you use ``1.1.1``, you may be prompted to
save the file after accessing, and you will find that it is an XML
format file after saving. With ``1.3.0`` , it will be opened directly in
the browser.

``GetCapabilities`` access
--------------------------

Open a link

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb1.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities

View the map
------------

MapServer supports returning maps from the beginning, and you can use
the ``mode=map`` Parameters.

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb1.map&layer=states&mode=map



