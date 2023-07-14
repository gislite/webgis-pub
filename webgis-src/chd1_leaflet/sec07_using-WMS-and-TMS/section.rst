.. Author: Bu Kun .. Title: Use WMS with TMS services

Use WMS with TMS services
=========================

WMS is an abbreviation for **web map service** , a popular way for
professional GIS software to publish maps (rarely used by non-GIS
personnel).

TMS stands for **tiled map service** ( **tile map service** ).

WMS in Leaflet
--------------

When someone publishes a WMS service, the most likely link is to the
``GetCapabilities`` document. In this tutorial, we will use the demo map
service from GeoServer at https://demo.boundlessgeo.com/geoserver/web/.
We will use GeoServer’s demo map service at
https://demo.boundlessgeo.com/geoserver/web/. As you can see on this
page, “WMS” links to the following URL:

::

   https://demo.boundlessgeo.com/geoserver/ows?service=wms&version=1.3.0&request=GetCapabilities

Leaflet cannot parse WMS’s ``GetCapabilities`` document. So you have to
create a ``L.TileLayer.WMS`` layer, which is used to provide a basic WMS
link and specify any WMS options you need.

The basic WMS link is just a ``GetCapabilities`` link with no
parameters, for example:

::

   https://demo.boundlessgeo.com/geoserver/ows?


The way to use this in Leaflet’s map is simple:



::

   var map = L.map(mapDiv, mapOptions);
   var wmsLayer = L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', wmsOptions).addTo(map);

An instance of ``L.TileLayer.WMS`` requires at least one option:
``layers``. Note that the “layer” concept in Leaflet is not the same as
the “layer” concept in WMS!

The WMS server will define **a set of layers** in the
``GetCapabilities`` XML document, but the document is mostly lengthy and
difficult to understand, so it is usually used like QGIS. Software to
view information about available layers in the WMS server:

We can see that OpenGeo demonstrates WMS with a WMS layer named
``ne:ne`` with a base map. Let’s see what it looks like:

::

   var wmsLayer = L.tileLayer.wms('http://webgis.osgeo.cn/cgi-bin/mapserv?map=/owg/mfb3.map&', {{
       layers: 'states',
       format: 'image/png',
       transparent: true,
   }}).addTo(map);

Note that the Mapfile used above needs to define the output projection
as ``EPSG:3857``.

It is also important to note that if the Mapfile is not properly
configured, it is possible that the MapServer map (the full map by
default) will be used as a slice to form an overlay.

.. raw:: html

    <table>
    <tbody>
    <tr> <td style="text-align: center; border: none">
    <iframe src="./wms-example1.html" width="616" height="416"></iframe>
    </td> </tr>
    <tr> <td style="text-align: center; border: none">
    <small><a href="./wms-example1.html">Show the example</a> </small>
    </td> </tr>
    </tbody>
    </table>

Or we can try the WMS layer of ``nasa:bluemarble``:

::

   var wmsLayer = L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', {{
   layers: 'nasa:bluemarble'
   }}).addTo(map);

.. raw:: html

    <table>
    <tbody>
    <tr>
    <td style="text-align: center; border: none">
    <iframe src="./leaflet_using_wms_tms/wms-example2.html"
    width="616" height="416"></iframe>
    </td>
    </tr>
    <tr>
    <td style="text-align: center; border: none">
    <small><a
    href="./leaflet_using_wms_tms/wms-example2.html">Show the example</a>
    </small>
    </td>
    </tr>
    </tbody>
    </table>

The ``layers`` option is a comma-separated list of layers. If the WMS
service defines multiple layers, the map can introduce multiple layers
to create images at the same time.

For example, on the WMS server we are using, there is a
``ne:ne_10m_admin_0_countries`` layer displays the country’s terrestrial
and country names. There is also a
``ne:ne_10m_admin_0_boundary_lines_land`` layer shows country borders.
If we request two layers at the same time, the WMS server will combine
the two layers into one image and separate them with a comma:

::

   var countriesAndBoundaries = L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', {{
   layers: 'ne:ne_10m_admin_0_countries,ne:ne_10m_admin_0_boundary_lines_land'
   }}).addTo(map);

Note that this will request an image from the WMS server that is
different from the ``L.TileLayer.WMS`` created for the country and
country boundaries, which will both Add to the map. In the first case,
an image request is made and then the WMS server decides how to combine
the images. In the second case, two image requests are made, and then
the Leaflet code running in the web browser determines how the images
are combined.

If we combine these with layer controls, we can create a simple map to
see the differences:

::

   var basemaps = {{
   Countries: L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', {{
       layers: 'ne:ne_10m_admin_0_countries'
   }}),

   Boundaries: L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', {{
       layers: 'ne:ne_10m_admin_0_boundary_lines_land'
   }}),

   'Countries, then boundaries': L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', {{
       layers: 'ne:ne_10m_admin_0_countries,ne:ne_10m_admin_0_boundary_lines_land'
   }}),

   'Boundaries, then countries': L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', {{
       layers: 'ne:ne_10m_admin_0_boundary_lines_land,ne:ne_10m_admin_0_countries'
   }})
   }};

   L.control.layers(basemaps).addTo(map);
   basemaps.Countries.addTo(map);

Change to "Countries, then The boundaries option, so you can see the
borders of the land, and the WMS server is smart enough to display the
building tags on the map. When multiple layers are requested, how to
combine the layers depends on the WMS server.

.. raw:: html

    <table>
    <tbody>
    <tr> <td style="text-align: center; border: none">
    <iframe src="./leaflet_using_wms_tms/wms-example3.html" width="616" height="416"></iframe>
    </td> </tr>
    <tr> <td style="text-align: center; border: none">
    <small><a href="./leaflet_using_wms_tms/wms-example3.html">Show the example</a>
    </small>
    </td> </tr>
    </tbody>
    </table>

Information for GIS users of WMS services
-----------------------------------------

From a GIS perspective, Leaflet’s WMS processing is very basic. It does
not support ``GetCapabilities``, does not support legend, and does not
support ``GetFeatureInfo``.

We can do this in the Leaflet’s API Found in the documentation
documentation Additional options for ``L.TileLayer.WMS``. Any option can
be passed to the WMS server via a link to ``getImage``.

Also note that Leaflet supports very few coordinate systems:
``CRS:3857``, ``CRS:3395`` And ``CRS:4326`` (see the ``L.CRS``
documentation). If your WMS service is unable to provide images in these
coordinate systems, you may need to create additional coordinate systems
in Leaflet using Proj4Leaflet . In addition, to use the correct CRS when
initializing your map, add it to any WMS layer:

::

   var map = L.map('map', {{
       crs: L.CRS.EPSG4326
   }});

   var wmsLayer = L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', {{
       layers: 'nasa:bluemarble'
   }}).addTo(map);

.. raw:: html

    <table>
    <tbody>
    <tr>
    <td style="text-align: center; border: none">
    <iframe src="./leaflet_using_wms_tms/wms-example-crs.html" width="616" height="416"></iframe>
    </td>
    </tr>
    <tr>
    <td style="text-align: center; border: none">
    <small> <a href="./leaflet_using_wms_tms/wms-example-crs.html">Show the example</a> </small>
    </td>
    </tr>
    </tbody>
    </table>

TMS in Leaflet
--------------

Although Leaflet does not explicitly support the TMS service, the naming
rules for tiles are very similar to the naming rules for
``L.TileLayer``, so the TMS service will not be described here.

Using the same OpenGeo WMS/TMS server demo, we can see a TMS endpoint:

::

   https://demo.boundlessgeo.com/geoserver/gwc/service/tms/1.0.0

Check MapCache help about TMS And TMS specification , You can see the
links to the map tiles in TMS as follows:

::

   http://base_url/tms/1.0.0/{{tileset}}/{{z}}/{{x}}/{{y}}.png

Using OpenGeo’s TMS service as ``L.TileLayer``, we can check the
function documentation to see which ``tileset`` is available and builds
our basic link:

::

   https://demo.boundlessgeo.com/geoserver/gwc/service/tms/1.0.0/ne:ne@EPSG:900913@png/{{z}}/{{x}}/{{y}}.png
   https://demo.boundlessgeo.com/geoserver/gwc/service/tms/1.0.0/nasa:bluemarble@EPSG:900913@jpg/{{z}}/{{x}}/{{y}}.jpg

Use the ``tms:true`` option when instantiating a layer as follows:

::

   var tms_ne = L.tileLayer('https://demo.boundlessgeo.com/geoserver/gwc/service/tms/1.0.0/ne:ne@EPSG:900913@png/{{z}}/{{x}}/{{y}}.png', {{
       tms: true
   }}).addTo(map);

   var tms_bluemarble = L.tileLayer('https://demo.boundlessgeo.com/geoserver/gwc/service/tms/1.0.0/nasa:bluemarble@EPSG:900913@jpg/{{z}}/{{x}}/{{y}}.jpg', {{
       tms: true
   }});

.. raw:: html

    <table> <tbody>
    <tr> <td style="text-align: center; border: none">
    <iframe src="./leaflet_using_wms_tms/wms-example4.html" width="616" height="416"></iframe>
    </td> </tr>
    <tr> <td style="text-align: center; border: none">
    <small><a href="./leaflet_using_wms_tms/wms-example4.html">Show the example</a> </small>
    </td> </tr>
    </tbody> </table>

A new feature of **Leaflet 1.0** is the ability to use ``{{-y}}``
instead of ``tms: true`` options, for example:

::

   var layer = L.tileLayer('http://base_url/tms/1.0.0/tileset/{{z}}/{{x}}/{{-y}}.png');

``tms: true`` option (Leaflet 0.7) or ``{{-y}}`` (Leaflet 1.0) is
necessary because the origin of the coordinates of ``L.TileLayer`` is
usually in the upper left corner, so the Y coordinate is lowered. In
TMS, the coordinate origin is in the lower left corner, so the Y
coordinate **rises**.

In addition to the differences in ``y`` coordinates and the discovery of
tiles, the TMS service also provides accurate services in the form of
``L.TileLayer``.
