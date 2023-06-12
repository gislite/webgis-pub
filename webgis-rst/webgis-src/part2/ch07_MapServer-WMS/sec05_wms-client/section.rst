.. Author: Bu Kun .. Title: Use MapServer as a WMS client

Use MapServer as a WMS client
=============================

View examples
-------------

  
.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb4.map&layers=topo_wms+states&mode=map

Another exciting feature of MapServer is its ability to use layers
provided by other map servers as its data source. In this case, the
MapServer application becomes a WMS (WFS) client. MapServer can also
share (or serve) layers in MapFile to other map servers. This makes the
application a WMS (WFS) server. What is WMS or WFS? These are the
Web-based Interoperability Services specification, released by the Open
Geospatial Alliance (OGC). WMS stands for Web map service, and WFS
stands for Web feature service.

The difference between the two specifications, in simple terms, is that
WMS uses web raster formats (PNG, GIF, JPEG) to share layers, while WFS
uses the Geographic Markup Language GML. The third commonly used OGC
interoperability specification is the Web Coverage Service Specification
(WCS), which MapServer provides server-side support only. If you need
more information about WMS, WFS and WCS, you can find OGC Implementation
Specifications or OGC Abstract Specifications on the OGC official
website. MapServer’s website also has some pages related to these
specifications.

This example shows you how to add a WMS layer to your MapFile.

The following is the Mapfile used in this example ``mfb4.map`` ):


.. literalinclude:: ./mfb4.map
   :lineno-start: 1


In the above resource, WMS needs to start with ``http://``, not ``//`` .

In addition, as a client, there is no need to configure WEB in the
Mapfile; it is required on the server.

Add WMS layer to Mapfile

The file changes are as follows:

Definition of MapServer
-----------------------

Let’s look at the WMS layer:

``LAYER``, marking the beginning of the WMS layer object.
``NAME modis_jpl``, the layer identifier. ``TYPE RASTER``, since this
WMS layer is an image, use the raster layer type. ``OFFSITE 0 0 0`` ,
ignore black background color ``STATUS OFF``, this layer is turned off
by default. ``CONNECTIONTYPE WMS`` Input layer connection use. Defaults
to local .

If we had to be explicit, we would add all other vector and raster
layers locally in our MapFile CONNECTIONTYPE. Instead, we only define
connection types that are external. WMS is an external data layer from
other map servers.

``CONNECTION "http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map"``,
the connection string that allows us to “get” data from another server.
In the case of a WMS connection, this is a URL. If we were using a
PostGIS database, this would be an SQL statement. Note that the string
in your MapFile is on a single line.

``METADATA``, marks the metadata object of our WMS layer. MapServer uses
the parameters defined by this object, along with the above connection
parameters, to form valid WMS requests to the WMS server.

``"wms_srs" "epsg:4326"`` , WMS projection. Sometimes WMS servers
support multiple projections. If that’s the case, you’ll probably want
to ask for your output projection (``EPSG:2163``) map. Unfortunately,
external WMS servers do not support this kind of projection.

``"wms_name" "modis"`` , the name of the WMS layer to add. It’s like
adding the parameter ``"layers=modis"`` ,
``"wms_server_version" "1.1.1"`` , the version of the server for the WMS
version. More supported versions can be viewed.
``"wms_format" "image/jpeg"`` , the image format we expect to receive
from the WMS server. You can try ``image/png`` or other allowed values.

Additional information
----------------------

To learn more about adding WMS layers to your application, visit the WMS
client how to record.

In addition to adding WMS layer objects, there is also the next new
object for the map. This is the Web object. There are two parameters in
the Web object:

``IMAGEPATH '/data/tmp/'`` , the local absolute path to the temporary
directory for web access. The user running the web server process should
be able to write to this directory. Make sure the path contains the last
slash ( ``/`` ). (Your IMAGEPATH might look like this:
\`\ ``/home/apache/htdocs/tmp/`` or ``C:/Inetpub/wwwroot/tmp/``.)

``IMAGEURL '/tmp/'`` , which is how IMAGEPATH appears relative to the
web server’s root directory. If we had to enter the full URL, it would
be “http://terrasip.gis.umn.edu/tmp/” . Make sure the path contains the
last slash ( ``/`` ).

Finally, a new parameter has been added to the ``MAP`` object: ``NAME``
. This is the identifier of the map object. MapServer creates and dumps
a ``tmp`` directory for all images using this prefix. It’s not really
needed in this example, but it won’t have any bad effects either.

If you want to share your data layer to other map servers, you need to
add ``METADATA`` object to your ``MAP`` object, and add ``METADATA``
object to each layer object you want to share with everyone. All WMS
layers added from another server are automatically cascaded and made
available to others (contagious). For details on how to make your
MapServer application a WMS server, please read the WMS server
documentation carefully. In addition, in addition to the WMS service,
MapServer also supports the WFS service, you can check the documentation
to learn how to configure MapServer to implement a WFS server, or a WFS
client.
