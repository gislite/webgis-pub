.. Author: Bu Kun .. Title: Define projection and extent

Define projection and extent
============================

View examples
-------------

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

This map is clearly a region from the one shown earlier, but it doesn’t
look the same. This map uses another map projection.

In the projection definition part of the Mapfile, the projection is
processed by the Proj.4 library through parameters. For more information
about the PROJ.4 library, visit https://proj4.org/ .

.. raw:: html

   <!-- http://trac.osgeo.org/proj/ -->

The following is the Mapfile source file ``mfa6.map`` used in this
example:

->-> mfa6.map

The changes in the documents are as follows:

->-> xx_diff_mfa6_mfa5.htmp

The first thing you will notice is that the MapFile is the original
``EXTENT`` replaced by the new range value, which doesn’t look like
longitude and latitude. In addition, a projection object ``PROJECTION``
was added, and a ``PROJECTION`` definition was added to ``LAYER``.

Take a look at the parameters of the new spatial extent:

::

   EXTENT 201621.496941 -294488.285333 1425518.020722 498254.511514

.. raw:: html

   <!--
   To the extent that we provide MapServer, we need to project the same units in the output.
   Since the units in Lambert azimuth and other areas are meters, we have a new degree of rice.
   -->

Writing way of Mapfile
----------------------

Projection can be defined in MAP objects, as well as in LAYER objects.
Projections can be defined in MAP objects (only once, but multiple can
be defined) This defined projection is the output projection of the map,
and MapServer will use this projection to render the map result. The
projection defined in the ``LAYER`` object is the input projection, that
is, the projection of the data corresponding to the layer object. The
definition of the projection in the layer object can be different from
that in the map object, and MapServer will do the projection
transformation and reproject to the output projection. If there is no
projection information in the ``LAYER`` object, MapServer will assume
that the input and output projections are the same.

In a Mapfile, the ``PROJECTION`` object is not required. But if you want
to support the OGC interoperability specification (WMS/WFS/WCS), it
still needs to be clearly defined in the Mapfile.

Defined only once in the map object, this definition becomes your output
projection - MapServer will render your map in this projection. You can
also define input projections using projection object layer objects. It
is possible to project on different layers - MapServer reprojects them
to your output projection. If no objects within the projection layer are
defined, MapServer assumes that the input projection is the same as the
output projection. This is not the desired object unless you create a
map file that supports an OGC Interoperable Web Services Specification
(WMS/WFS/WCS).

MapServer’s projections are defined in two ways. The traditional way is
to define it through the Proj.4 parameter, such as the Lambert Azimuthal
Equal-Area projection of the continental United States defined below.

This is the output projection definition:

::

   PROJECTION
       "proj=laea"
       "ellps=clrk66"
       "lat_0=45"
       "lon_0=-100"
   END

Another way is to use EPSG codes. These codes are standard projection
codes (or spatial reference identifiers) as defined by the European
Petroleum Survey Group (EPSG). Defined by the following EPSG code in
MapServer, the following ``EPSG:2163`` also means (Lambert Azimuthal
Equal-Area), the effect is the same:

::

   PROJECTION
       "init=epsg:2163"
   END

If you want to learn more about EPSG code, take a look at
``/usr/ROJ/PSG`` or ``C:/PROJ/NAD/EPSG`` (``/ms4w/proj/nad`` MS4W).
Also, check out the EPSG website http://www.epsg.org .

Calculation of projection coordinates by cs2cs
----------------------------------------------

The projected coordinates can be calculated using QGIS or some other GIS
package, or you can use PROJ.4’s cs2cs tool. The following commands are
raw range values that can be used to reproject:

::

   cs2cs +proj=latlong +datum=WGS84 +to +proj=laea +ellps=clrk66 +lat_0=45 +lon_0=-100

After typing the command, enter the southwest coordinate pair (lower
left coordinate), separated by a space: ``-97.54 1.619778``

The result returned by the ``cs2cs`` utility is:

::

   208398.01       -372335.44  0.000

Next, type the northeast coordinate pair (upper-right coordinate), also
separated by a space: ``-82.122902 49.38562``, returns the following
values:

::

   1285308.08      632638.93   0.000

``cs2cs`` returns a ternary value. The third value, 0.000, can be
ignored and is meant to represent altitude (which we don’t use).

Now, the extent of the map under this projection can be defined in the
Mapfile:

::

   EXTENT 208398.01 -372335.44 1285308.08 632638.93

Note that the definition here is not the same as what is actually used
in Mapfile. When re-projecting, the map defined using the range of the
data may not be what you expected. By considering “buffering” the range,
the range can be extended a few kilometers up and down, left and right
(this varies according to the projection and the specific application).
How much expansion is needed can be assisted by desktop GIS software
such as QGIS, which may be more convenient.

Map projection online document
------------------------------

If you need to know more about map projection, take a look at some of
the links below:

-  
   http://www.colorado.edu/geography/gcraft/notes/mapproj/mapproj_f.html
-   http://www.geography.hunter.cuny.edu/mp/
-   http://www.nationalatlas.gov/articles/mapping/a_projections.html
-   http://en.wikipedia.org/wiki/Map_projection
-   http://erg.usgs.gov/isb/pubs/MapProjections/projections.html
