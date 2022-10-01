.. Author: Bu Kun .. Title: WFS service foundation

Geographic Web Services
=======================

MapServer publishing services are configured through Mapfile, and WFS
services are no exception. Similar to configuring WMS, to publish WFS,
add key-value pairs about WFS in the METADATA section of the Mapfile
configuration file. MapServer will only include WFS functionality if the
layer meets the following conditions:

-  The data source is vector data: shapefile, OGR, Postgis, sde
   (ArcSDE);
-  Layer name must be set;
-  The layer data space type must be one of ``point`` , ``line`` ,
   ``polygon``;
-  ``wfs_onlineresource`` and ``wfs_enable_request`` must be set.

MapServer itself can be configured to support WFS, and you can also use
TinyOWS. Using TinyOWS can support WFS-T and realize the function of
online editing and saving.

Configure an instance
---------------------

Based on the Mapfile configuration of the published WMS, add the WFS
configuration. The following is a Mapfile instance with WMS and WFS
configured.

Mapfile is as follows:

->-> mfw1.map

Compared with the Mapfile that only configures WMS, the main change lies
in the METADATA sub-object of the MAP object and the METADATA sub-object
of the LAYER object. In the METADATA of the MAP object, the added
key-value pairs include:

-  ``wfs_title`` , required, returned in the ``GetCapabilities`` request
   as the ``title`` element of the XML document in the service response;
-  ``wfs_onlineresource``, required, provide the server address of
   ``wfs``;
-  ``wfs_srs``, the spatial reference system of the data (Spatial
   Reference System);
-  ``wfs_abstract`` , returned by the ``Abstract`` element of the XML
   document in the ``GetCapabilities`` request as the service response;
-  ``wfs_enable_request``, which means to configure MapServer map to
   support all operations of ``wfs`` globally.

The key-value pair added to the METADATA of the LAYER object is as
follows (Note: There are many repetitions of the METADATA of the
configuration and the MAP object. If it is not set, the METADATA
configuration of the MAP object will be inherited. If it is set, the
configuration of the LAYER will be used, which is in a MAP Useful when
the object contains multiple layers):

-  ``wfs_title`` , returned by the ``title`` element of the XML document
   in the ``GetCapabilities`` request as the service’s response;
-  ``wfs_srs``, the Spatial Reference System of the data;
-  ``gml_featureid`` , the attribute name of the feature ID
   corresponding to the layer;
-  ``wfs_enable_request`` , configures the layer to support all wfs
   operations.

Access
------

We can call the MapServer WFS service through the URL. By default, WFS
will return the result in GML format, and the call result can be viewed
in the browser. WFS contains many operations, you can see the WFS
operations supported by Mapfile from the ``GetCapabilities`` response:

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities

The following are those that use cities around the world:

`http://webgis.pub/cgi-bin/mapserv?map=/owg/mft2.map&SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities <http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities>`__

The URL is parsed as follows:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map
   1 SERVICE=WFS
   2 VERSION=2.0.0
   3 REQUEST=GetCapabilities

DescribeFeatureType
-------------------

When operating the database, we sometimes need to reflect the structure
of the database, and we also have the same problem when using WFS.
Sometimes we need to know what attributes a FeatureType has and what
type they are, then we need the ``DescribeFeatureType`` method. A
typical ``DescribeFeatureType`` call looks like this:

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=DescribeFeatureType&TypeName=world-country

The following are those that use cities around the world:

`http://webgis.pub/cgi-bin/mapserv?map=/owg/mf21.map&service=WFS&VERSION=2.0.0&request=DescribeFeatureType&TypeName=world-country <http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=DescribeFeatureType&TypeName=world-country>`__

Pay attention to when configuring

：：

::

   "gml_include_items" "all" #  Note that this keyword has no attributes by default if it is not configured.

The URL is parsed as follows:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map
   1 service=WFS
   2 VERSION=2.0.0
   3 request=DescribeFeatureType
   4 TypeName=world-country

GetFeature
----------

Finally arrived at this method, this method can be said to be the basis
of WFS, its purpose is clear at a glance, get Feature. If you type this
call: The link below returns all the elements.

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country

The following are those that use cities around the world:

`http://webgis.pub/cgi-bin/mapserv?map=/owg/mft2.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country <http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country>`__

The URL is parsed as follows:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map
   1 service=WFS
   2 VERSION=2.0.0
   3 request=GetFeature
   4 TypeName=world-country

This call means that all the data is returned, usually resulting in a
large XML/GML document.

A limited number of features can be returned
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By using parameters ``count=2`` You can limit the number of features
returned

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country&count=2

The following are those that use cities around the world:

`http://webgis.pub/cgi-bin/mapserv?map=/owg/mft2.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country&count=2 <http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country&count=2>`__

The resolution of URL is as follows:

::

   >>> [print(idx, x) for idx, x in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map
   1 service=WFS
   2 VERSION=2.0.0
   3 request=GetFeature
   4 TypeName=world-country
   5 count=2

Return features according to the index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can return features based on the index, and to do this, you need to
configure:

::

   "gml_include_items" "all" ## Optional (serves all attributes for layer)
   "gml_featureid"     "OBJECTID" ## REQUIRED

Here ``OBJECTID`` Is a field in Shapefile.

The following link returns the ID number as ``227`` Elements of:

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country&FeatureId=world-country.227

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map
   1 service=WFS
   2 VERSION=2.0.0
   3 request=GetFeature
   4 TypeName=world-country
   5 FeatureId=world-country.227

Use Filter
~~~~~~~~~~

According to the selector, such as:

::

   http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country&Filter=<Filter><PropertyIsEqualTo><PropertyName>OBJECTID</PropertyName><Literal>227</Literal></PropertyIsEqualTo></Filter>

The URL is resolved as follows:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map
   1 service=WFS
   2 VERSION=2.0.0
   3 request=GetFeature
   4 TypeName=world-country
   5 Filter=<Filter><PropertyIsEqualTo><PropertyName>OBJECTID</PropertyName><Literal>227</Literal></PropertyIsEqualTo></Filter>

More meaningfully, choose according to the name. Note the selection
here, and the comparison of attributes is case-sensitive.

::

   http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map&service=WFS&VERSION=2.0.0&request=GetFeature&TypeName=world-country&Filter=<Filter><PropertyIsEqualTo><PropertyName>NAME</PropertyName><Literal>CHINA</Literal></PropertyIsEqualTo></Filter>

The resolution of URL is as follows:

::

   >>> [print(idx, x) for idx, x  in enumerate(url.split('&'))]
   0 http://webgis.pub/cgi-bin/mapserv?map=/owg/mfw1.map
   1 service=WFS
   2 VERSION=2.0.0
   3 request=GetFeature
   4 TypeName=world-country
   5 Filter=<Filter><PropertyIsEqualTo><PropertyName>NAME</PropertyName><Literal>CHINA</Literal></PropertyIsEqualTo></Filter>
