======================================
Access WFS using LeafletJS
======================================

The WFS service returns data(or features), not maps.

Returning data means more information. Users can parse information to accomplish more complex tasks.
But it also means that the task of drawing is left to the client, which requires more coding work.

Config WFS in MapServer
======================================

Leaflet can be drawn using GeoJSON data. To display the data returned by the WFS service,
using JSON as the data type returned, you need to open it in MapServer.

::

    OUTPUTFORMAT
        NAME "geojson"
        DRIVER "OGR/GEOJSON"
        MIMETYPE "application/json; subtype=geojson"
        FORMATOPTION "STORAGE=stream"
        FORMATOPTION "FORM=SIMPLE"
    END

In METADATA, it is stated that:

::

    "wfs_getfeature_formatlist" "geojson"

You can view the information about the service by following links.

<a href="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw2.map&SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities">http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw2.map&SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities</a>

Example
======================================

The following is an example of using Leaflet.
Note that due to the size of data, the filter is used to get the data of China.
But maybe you will still have to wait for a while for the data loaded.

.. raw:: html

   <iframe src="./xx-leaflet-wfs1.html" width="100%" height="450" style="border:1px solid">
   </iframe>

`Open the example </xx-leaflet-wfs1.html>`_