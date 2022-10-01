.. Author: Bu Kun .. Title: Draw maps with style layer

Draw maps with style layer
==========================

More advanced WMSs use “style layers” to describe a map. A style layer
can be thought of as a transparent layer composed of symbolic elements.
A map is composed of these style layers in a certain order, which is
usually called Z-value order. Users can define complex or simple maps by
adding or removing style layers. A style layer is actually a combination
of a layer and a style. Conceptually, the layer defines a stream of
features, and the style defines how those features are symbolized. In a
WMS process, the drawing style of a map is specified according to the
LAYERS and STYLES request parameters.

Support for named styles
------------------------

Named styles support are introduced in MapServer 5.2. The support is
base on MS RFC 39: Support of WMS/SLD Named Styles.

MapServer 5.2 introduces the possibility to assign a group to a series
of classes defined on a layer object using two new non-mandatory
keywords CLASSGROUP (at the layer level) and GROUP at the class level:

::

   LAYER
       ...
       CLASSGROUP "group1"
       ...
       CLASS
           NAME "name1"
           GROUP "group1"
           ...
       END
       CLASS
           NAME "name2"
           GROUP "group2"
           ...
       END
       CLASS
           NAME "name3"
           GROUP "group1"
           ...
       END
       ...

At rendering time, if the CLASSGROUP is defined, only classes that have
the same group name would be used. Based on this concept, WMS/SLD
support uses the class groups as named styles. Each group of classes is
considered equivalent to a named style:

::

   The GetCapbilities request will output all the styles that are available
   The GetMap request can use the STYLES parameter to specify a named style
   The GetLegendGraphic can use the STYLES parameter to specify a named style

Example
-------

Here is an example:

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb5.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=group1

Mapfile is as follows:

->-> mfb5.map

Use ``GetCapabilities`` to return:

::

   <Style>
     <Name>group1</Name>
     <Title>group1</Title>
     <LegendURL width="72" height="20">
        <Format>image/png</Format>
        <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" ...
     </LegendURL>
   </Style>

Consider the following sample WMS request snippet:

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb5.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states,states&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=group3,group2

There are three style layers:

-  States: group1
-  States: group2
-  States: group3

They are stacked in a certain order. A layer can be drawn multiple times
with different styles to achieve the desired effect. The following
example draws the road layer using the ``casing`` and ``centerline``
styles:

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb5.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states,states&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=group1,group2

A WMS itself may not know how to make a meaningful combination of style
layers, it’s all up to the client. WMS uses names to identify styles and
layers, and other documents refer to such named layers and styles. This
is currently the only way for WMS to define style layers.
