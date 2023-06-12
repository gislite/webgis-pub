.. Author: Bu Kun .. Title: Add a grid layer

Add a grid layer
================

View examples
-------------

.. raw:: html

   <img src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfa5.map&layer=states&layer=states_line&layer=states_label&layer=topo&mode=map"/>


In addition to supporting vector data (points, lines, polygons and
labels), MapServer can also display raster data. Through the use of the
GDAL library, MapServer can import and export a variety of raster
formats. MapServer now supports RGB and multispectral images
(multilayers). In versions prior to 4.0, raster input was limited to
single-layer, grayscale or color image indices. This example shows how
to use multispectral data to choose what layers to display. With RGB and
multispectral images, there may be a significant performance penalty.

Since MapServer 5.x uses the GD 2.0.x library to generate image output,
it supports RGB (24-bit true color) output as well. Therefore, it is now
possible to use both ``PNG24`` (truecolor) output and 8-bit (indexed
color or grayscale) PNGs. This example uses PNG24 IMAGETYPE. Just like
RGB input, rendering results are significantly improved when using
PNG24.

MapServer can actually use GDAL to generate output images, but that’s
another topic. If you want to know more about it, see the specific usage
of the ``OUTPUTFORMAT`` object in MapFile.

The following is the Mapfile (mfa5.map) used in this example:

The file changes are as follows:


.. literalinclude:: ./mfa5.map
   :lineno-start: 1


Annotated Mapfile

The structure of mapfile, through objects, looks like this:

::

                                                  MAP
                  LAYER #1-------------LAYER #2----|----LAYER #3--------LAYER #4
               (states_poly)           (modis)       (states_line)   (states_label)
                  |                                     |               |
     (land) CLASS- |-CLASS (water) |-CLASS |-CLASS
                |   |                                     |                 |
          STYLE-|   |-STYLE                               |-STYLE     STYLE-|-LABEL



The modifications are as follows:

`Open the file:diff_mfa5_mfa4.html <./diff_mfa5_mfa4.html>`_

.. aa literalinclude:: ./xx_diff_mfa5_mfa4.htmp



When you are in MapFile , you will see that the new layer ``"modis"`` is
added after the polygon layer ``"states"``. MapServer displays layers in
reverse order - last in first out (LIFO), with the first layer drawn in
the MapFile defined at the bottom of the map.

So the country polygon layer, will be drawn at the bottom of the result.
Since the raster layer is drawn on top of it, it won’t be seen. That’s
why the first layer gets the status value ``STATUS OFF`` off. The line
layer is defined below the raster layer, so it will be drawn on top of
the result (you can see it). That’s why we started to separate the line
layer from the polygon layer. Finally, labels are drawn on top of
everything.

MapServer can automatically turn on or off the l layer according to the
status of other layers (the polygon layer will be turned off when the
raster layer is turned on). This is done with the ``REQUIRES``
parameter. You should use this feature once you start creating your own
MapServer applications.

Parameter description
---------------------

Let’s take a look at the new parameters introduced in MapFile:

``IMAGETYPE`` , which is not new, but the value is ``PNG24`` . PNG24 is
a 24-bit true color version of the PNG format. Instead of output images
being limited to 256 color combinations, map servers now have millions.
By the way, try changing this value back to PNG. Note the formats that
can be used, the time it takes to generate the image. Choose between
true color and indexed color, taking into account the time it takes to
generate the image.

``SYMBOLSET``, the path to the file defined by the symbols in the sub.
Symbols in this file are referenced through the SYMBOL object in the
class object. It’s not really needed at this point, but I thought I’d
throw this out here for now. See the MapFile reference and for more
information on MapServer Construction with Cartographic Symbols.

``DATA "raster/mod09a12003161_ugl_ll_8bit.tif"``, in the newly added
layer object, the data parameter points to a GeoTIFF image. Like
MapServer’s vector datasets, it supports multiple raster file formats.
This support is through the use of the GDAL library. For more
information on the different raster formats supported by MapServer and a
general discussion of using raster map servers, please read how raster
data works at http://www.mapserver.org/input/raster.html

``TYPE RASTER``, when using raster data (images), the value is
``RASTER``, not ``POLYGON``, ``LINE``, ``POINT``, or others.

``PROCESSING "BANDS=1,2,3"``, this layer object parameter is new in
MapServer 4.x. The processing keyword has many values, but in this case,
it is used to select the bands displayed in the multispectral image. The
value string here will be passed to the GDAL library. Documentation for
this is currently minimal, but see MAPFILE for more examples of using
the processing keyword.

``OFFSITE``, this parameter tells MapServer which pixel values to render
as the background (or ignore). You can get pixel value manipulation of
images or image manipulation programs (eg GIMP, Photoshop).

RGB and Index Image
-------------------

To compare the speed of creating a map using a RGB image with an indexed
color image, replace the following line in MapFile:

::

   DATA "raster/mod09a12003161_ugl_ll_8bit.tif"
   STATUS DEFAULT
   TYPE RASTER
   PROCESSING "BANDS=1,2,3"
   OFFSITE 71 74 65

Use the following code:

::

   DATA "raster/mod09a12003161_ugl_ll_idxa.tif"
   STATUS DEFAULT
   TYPE RASTER
   OFFSITE 70 74 66

In addition, try changing ``IMAGETYPE`` from ``PNG24`` to ``PNG`` .

Use preprocessing
-----------------

Raster data, such as remote sensing images, is not just a picture. In a
computer, an image is usually represented by three RGB channels. In
remote sensing images, channels are generally called bands. Moreover,
the band of the remote sensing image is different from the RGB channel
of the image. It does not necessarily correspond to the tricolor of RGB,
and the number of bands is not necessarily three.

In MapServer, in addition to rendering images by default, you can also
define how to handle them, such as which three bands are used in false
color, if the color is stretched, and so on.

For example, for remote sensing images, use the following statement to
reverse the order of bands:

::

   PROCESSING   "BANDS=3,2,1"

The results are as follows:

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfr1.map&layer=topo&mode=map