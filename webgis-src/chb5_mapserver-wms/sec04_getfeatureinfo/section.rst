.. Author: gislite .. Title: WMS GetFeatureInfo access

WMS GetFeatureInfo access
=========================

The ``GetFeatureInfo`` operation (optional) returns information about
features near the specified point on the map. Allows users to click on a
pixel to query a feature’s schema and metadata.

``GetFeatureInfo`` is an optional operation. This operation is only
supported for layers with the attribute ``queryable="1"`` (true). If a
WMS client makes a request to a layer that does not support this
operation, a formatted service exception will be returned.

TA WMS may provide the optional ``GetFeatureInfo`` operation, and a WMS
that provides this operation calls its map “queryable”. The client can
add a position parameter (such as (X, Y) value, that is, the offset from
the upper left corner of the picture) or the number of elements that
need to query information near the point, to the URL of the requested
map, information about the corresponding feature on the map can now be
requested.

Since WMS is stateless, the ``GetFeatureInfo`` request should also
include all the parameters in the original ``GetMap`` request (except
Version and Request). Based on the spatial context information (BBOX,
SRS, Width and Height) in the ``GetMap`` request and the ``(X, Y)``
location selected by the user, the WMS returns more information about
that location.

Also included in the ``GetFeatureInfo`` request parameter is the
``Query_Layers`` parameter, which specifies the layers from which
feature information is obtained. The layers in this parameter list must
be those contained in the WMS ``Capabilities`` XML document.

The optional ``Info_Format`` parameter in the ``GetFeatureInfo`` request
specifies the format in which the feature’s information is returned. The
format is defined as a MIME type in the WMS ``Capabilities`` XML
document. Such as ``Info_Format=application/vnd.ogc.gml`` table does not
return results described in GML.

The optional ``Feature_Count`` parameter in the ``GetFeatureInfo``
request indicates the maximum number of features to return feature
information. The default value is ``1`` . The ``X,Y`` parameters
represent the pixel coordinates of the point of interest on the map. The
``X,Y`` values are within the ``Width`` and ``Height`` parameter values,
respectively. The origin of the coordinates is in the upper left corner
of the picture.

If ``GetFeatureInfo`` request is valid, WMS will respond according to
``Info_Format``. The nature of the response will be at the discretion of
the WMS server, but generally corresponds to the closest element to the
point ``(X,Y)``.

``GetFeatureInfo`` request using WMS service in MapServer
---------------------------------------------------------

This describes the ``GetFeatureInfo`` access to the published MapServer
WMS service.

The first is Mapfile:


.. literalinclude:: ./mfb2.map
   :lineno-start: 1


Compared to the previous ``mfb1.map``:


`diff_mfb2_mfb1.html <diff_mfb2_mfb1.html>`_

This Mapfile is configured with the WMS service. View function:

`Open a link <http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities>`_





View the map
------------


.. figure:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&layer=states&mode=map





Access using GetFeatureInfo
---------------------------

Use GetFeatureInfo


`Use GetFeatureInfo <http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&QUERY_LAYERS=states&LAYERS=states&BBOX=-96,45,-95,46&CRS=CRS:84&INFO_FORMAT=text/html&j=43&i=-95&WIDTH=256&HEIGHT=256&styles=&format=image/png>`_


The above results are output using a template.

Note
~~~~

WMS, Web Mapping Server, is a specification published by OGC.

``GetFeatureInfo`` is an access method supported by WMS.
