.. Author: Bu Kun .. Title: Annotations in a map

Annotations in a map
====================

When you generate a map, MapServer automatically performs multiple
tasks. It annotates features and prevents conflicts between adjacent
dimensions. It provides the use of bitmapped and TrueType fonts.

View examples
-------------

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfa4.map&layer=states_poly&layer=states_line&mode=map


MapServer has a very flexible annotation engine. It supports local
bitmaps and TrueType fonts. Font scaling uses TrueType support. The
angle and placement of the dimensions can be customized.

.. raw:: html

   <!-- If you take the time to learn the many parameters involved in creating good annotations, you will be rewarded with knowledgeable and beautiful maps. -->

Here is the map file（mfa4.map）：


.. literalinclude:: ./mfa4.map
   :lineno-start: 1


Annotated Mapfile

The file contains the font alias font location determined by the
``FONTSET`` Keyword assignment.

In order to label each city district with an attribute in the shapefile,
determine the name as the value of the ``LABELITEM`` keyword. When
rendering a country feature, the value of the feature’s ``NAME``
attribute will be used to create the label.

If you want to look at Shapefiles, there are several ways. You can open
the associated DBF file in Excel or other spreadsheet program that can
read DBF files, and you can see the feature attribute values. If you
just want to find out the name of the attribute, you can use the utility
dbfinfo, part of the shapelib library. In addition, the application
``ogrinfo`` provides geographic information, as well as feature values.

Each district will be labelled with the labelling parameters specified
in 027 to 030. Label objects start with the keyword Label and end with
the keyword END (line 030). Layer object with LABELITEM value set to
‘name’. Select the attribute NAME as the source of the label text. Each
label will be drawn black and its size will be small. Besides small, you
can choose small, medium, large, or huge.

The MapFile structure, by object, looks like this:

.. raw:: html

   <pre>
                                     MAP
         (states_poly) LAYER----------|---------LAYER (states_line)
        (land) CLASS-----|-CLASS (water)        |-CLASS
           STYLE-|-LABEL   |-STYLE                |-STYLE
   </pre>

The changes in the documents are as follows:

`Open the file:diff_mfa4_mfa3.html <./diff_mfa4_mfa3.html>`_

.. ./xx_diff_mfa4_mfa3.htmp



Annotation parameter description
--------------------------------

Here, we introduce several parameters and dimension objects:

::

   FONTSET "../fonts/fonts.list"

Here, we specify the file for the list of TrueType fonts (or the full
path set of fonts). This file lists each available font. See the file
itself and the MapFile reference for more information. The MAP object of
FONTSET is a parameter.

The contents of this file are as follows:


.. literalinclude:: ./fonts.list
   :lineno-start: 1


``LABELITEM``

In the ``"STATE"`` case, the specified data attribute is used for the
annotation. ``LABELITEM`` is a parameter of the layer object.

``LABEL`` Marks the beginning of the definition ``LABEL`` Object.
Dimension objects can be used for other objects (that is, scale bar
objects)

   -  ``COLOR`` objects within the callout, color specifies the color of
      the callout text.
   -  ``SHADOWCOLOR`` specifies the shadow color for dimension text.
   -  ``SHADOWSIZE`` specifies the size of the shadow. This value
      corresponds to the transition of pixels at ``X`` and ``Y``.
      Therefore, ``2`` means two pixels wide by two pixels high.
   -  ``TYPE`` in the LABEL object, the type specifies what type of font
      to use. We have a choice of TrueType or Bitmap (built-in fonts).
      We choose ``TRUETYPE`` .
   -  ``FONT`` If specified as TrueType, you need to specify what font
      to use. The value mentioned here is “alias”; the “alias” in the
      font list file.
   -  ``SIZE`` If using a TrueType font, the value in pixels is the size
      of the dimension. If it’s a bitmap, say something like “small” or
      “big”.
   -  ``ANTIALIAS`` This turns truetype antialiasing on or off. Remember
      that the value is not ``OPEN`` or ``CLOSE`` , but ``TRUE`` or
      ``FALSE`` .
   -  ``POSITION`` locates the label point of the label text. The value
      is a combined vertical and horizontal position. You have the
      following options: ``C`` for center vertical alignment, ``U`` for
      upper, and ``L`` for lower. For horizontal alignment you have the
      following options: ``C`` for center, ``L`` for left, and ``R`` for
      right. Therefore, to call the center of the callout ID for the
      text alignment, use the value ``CC`` (center - center). Or, if you
      wanted it to be the ID at the bottom left, you would use ``LL`` .
      Another approach is to let MapServer decide the best location for
      the label. For this, you can use the ``AUTO`` value.
   -  ``PARTIALS`` tells MapServer whether to generate incomplete label
      text. The default here is to not generate fragments of the label
      text. The value is ``TRUE`` or ``FALSE`` .
   -  ``MINDISTANCE`` is the minimum distance, in pixels, between
      duplicate annotations. See what happens if you increase or
      decrease the value.
   -  ``BUFFER`` Padding (pixels) of the callout. This is used to
      improve readability. A buffer of 4 pixels means that no labels
      will be drawn over the four pixels of each other. Again, change
      and see how it works.

You can also create dimensions to separate a polygon layer. You do it
with the data type of the annotation. Take a look at the MapFile of the
following example to see how you implement this tagging. You will find
that the “annotation” layer within the class object has color parameter
values. ``-1 -1 -1`` . Negative numbers tell MapServer to give this
class a transparent color (the callout logo is not displayed). Again,
modify these values and view the results to see how it affects the map.

Automatic optimization of annotations
-------------------------------------

To prevent the map from looking cluttered, MapServer optimizes the
labeling according to the scale of the data.

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfs2.map&layer=states_poly&layer=states_line&mode=map

Annotation processing
---------------------

Since version 6.2, MapServer has been able to draw label lines for
functions that are problematic in the label space (usually when the
label text is larger than the marked polygon). This feature is done
through the addition of MS RFC 81: offset labels with leaders. This
feature is for polygon annotations only.

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfs8.map&layer=states_poly&layer=states_line&mode=map

`Open the file:diff_mfs8_mfs2.html <./diff_mfs8_mfs2.html>`_

.. ./xx_diff_mfs8_mfs2.htmp


