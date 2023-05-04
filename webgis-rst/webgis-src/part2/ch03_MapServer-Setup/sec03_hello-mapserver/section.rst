.. Author: Bu Kun .. Title: start using Mapfile

Start using Mapfile
===============================

The core program of MapServer is used to generate maps based on
geospatial data. Configure the function of using CGI and give it the
function of WebGIS. MapServer uses a configuration file to declare the
size and format of the generated map, all paths, names, formats of the
data used, and various more complex control options.
This configuration file is called Mapfile. Mapfile is multi-layered, and each map file
defines a large number of other objects. These objects include scale
bars, legends, map colors, map names, map layers, and so on. There are
more objects that need to be defined and will be discussed in more
detail in the following sections. In addition, there is a comprehensive
reference for special MapServer keywords.

The first application uses a simple Mapfile and does not actually
generate a map， it generates a rectangular picture showing the word
“Hello World”. This application is very simple, so configuration
problems or errors can be easily found.

Each object is explained when it is used. The program does not use any
resources, such as spatial data, symbols, fonts and so on. However, it
needs space to store images. You will see how to specify the directory
of images in MapServer and make sure that Apache can find this
directory.

Grammar
-------

-  MapFile files ignore letter case
-  Non-alphabetic strings or strings containing MapServer keywords must
   be enclosed in quotation marks. It is recommended that all strings be
   enclosed in double quotation marks.
-  File paths in MapFile can use absolute paths or relative paths, where
   relative paths are relative to ``SHAPEPATH``.
-  MapFile has a specific hierarchy, Map Object is the “root” of
   MapFile, and other objects are under it.
-  The comment in the MapFile file starts with ``#``, and the part from
   ``#`` to the end of the line is the commented part, and the content
   of this part will be ignored when the program is executed. Writing
   notes is a good habit and recommended.

Add appropriate comments to your MapFile to make it easier for others to
understand your file. Such as:

::

   # ================================================================
   # MapFile for World Map
   # Created by Bu Kun 
   # Created 2019-4-20
   # ----------------------------------------------------------------
   # Revision History    
   # ----------------------------------------------------------------

-  The syntax used for attribute names is ``[ATTRIBUTENAME]`` . Note:
   Property names are enclosed in square brackets and are
   case-sensitive. All attribute names in ESRI ShapeFiles (.dbf) are in
   uppercase, while in PostGIS all attribute names are in lowercase.

The use of regular expressions in MapServer depends on the C language
library used by the operating system you are using. For more details,
please refer to the reference documentation provided by the C library.
Under Linux this library is GlibC, under this system you can use
``man 7 regex`` . These regular expressions are POSIX compliant, so
under Windows users can search the Internet for “man 7 regex”.

INCLUDE
~~~~~~~

As of MapServer 5.0, multiple MapFiles can be created using the
``INCLUDE`` command, the files form a logically single file.

Example: Include mylayer.map mymap.map in the mymap.map file as follows

::

   # ===========================
   #mymap.map
   # Create By YanMing
   #============================ MAP
    „„
       INCLUDE “mylayer.map”
    „„
   END

The content of mylayer.map is as follows

::

   # ===========================
   # mylayer.map
   # Create By YanMing
   #============================
   LAYER
                    NAME mylayer
                    DATA mylayer
    TYPE POLYGON  STATUS ON
   END

In this case, mymap.map is logically equivalent to:

::

   # ===========================
   #mymap.map
   # Create By YanMing
   #============================
   MAP
       LAYER
           NAME mylayer
           DATA mylayer
           TYPE POLYGON   STATUS ON
           „„
       END
   END

CGI variable
~~~~~~~~~~~~

Variables are parameters that can be substituted in a MapFile file (same
as variable types in programming languages, assignable values in a
program, etc.). In this case, cookies and CGI parameter values are
supported, which allows MapServer MapFiles to obtain user cookies (which
enable secure authentication), or non-MapServer request parameters.

Syntax: ``%`` + ``variable name`` + ``%``

Example 1: secure connection to spatial database

You need access to a PostGIS database. The username and password were
saved in cookies, ``uid`` and ``passwd`` in previous operations. Then in
MapFile you can write:

::

   CONNECTION "user=%uid% password=%passwd% dbname=postgis"

Example 2: dealing with temporary files

A program needs to generate the corresponding shapefile and store the
produced data in the directory corresponding to the server user.
``username`` can be obtained from a cookie, and ``filename`` can be
obtained from the request parameter number.

::

   DATA "/home/%username%/tempshp/%filename%"

Such parameters can only be used in the CGI version of MapServer, if you
use MapScript, you need to come up with the corresponding logic to
achieve this function.

“Maps” that do not use data
---------------------------

Let’s take a look at the basic usage of MapServer without using any GIS
data. The following figure shows the effect:


The picture is shown above, and the code is:

::

   <img border="1" src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfa0.map&mode=map"/>

The above code is the basic usage of declaring images in HTML, but the
parameters of ``src`` are not common image formats such as Jpeg, PNG,
GIF, but the MapServer CGI program and some parameters. All you need to
know here is that the MapServer CGI program will return an image based
on these parameters, so the HTML image declaration above is actually
nothing special; the mechanism will be explained later.

The basic usage of Mapfile
--------------------------

A Mapfile defines a collection of cartographic objects, which together
determine the appearance and behavior of the map displayed on the page.
It functions similarly to Apache’s ``httpd.conf`` configuration file.
Based on the same geographic data, mapping applications can use
different Mapfiles to present maps with different characteristics,
corresponding to different user behaviors.

It may seem like a static configuration file would have limited
functionality, but MapServer is designed so that using Mapfiles can
produce very powerful applications.

The definition of a map file consists of key-value pairs. Some of the
listed values are separated by spaces and must be enclosed in
parentheses. Both single and double parentheses are fine.

Keyword values with embedded spaces must be enclosed, which is good
practice for all strings.

At the same time, it should be noted that MapServer keywords are not
case-sensitive, but some database retrieval methods are case-sensitive.

In MapServer, to generate the above picture, the Mapfile code is:


.. literalinclude:: ./mfa0.map
   :lineno-start: 1


First Mapfile

The code is as follows, lines ``01`` to ``06`` establish the basic map
image parameters. The keyword ``NAME`` defines the base name of any
images created. Each time MapServer is called, it creates a unique
identifier by concatenating the system time (i.e. the number of seconds
since 1/1/1970 00:00:00) and the process ID. This unique identifier is
appended to the basename to form the filename. Two or three character
expansion (depending on file type), then append. In some cases, another
string is inserted after the base name of the map server to distinguish
the reference map image or legend image from the map image itself.

Keyword ``SIZE`` specifies the pixel size (width × height) of the map
image.

``IMAGECOLOR`` sets the background color of the image to white (recall
that the color is chosen on the map server by specifying three integer
RGB component values between 0 and 255, and white is 255, 255, 255).

Image type is set to ``PNG`` . It can also be used in Mapfile ``JPEG`` ,
or ``GIF`` Image.

Layer objects are defined under the map object. Before displaying a map,
you need to define at least one layer in your map file. You can define
as many layers as you want in MapServer. In older versions of MapServer,
the upper limit of the number of layers is defined in the source code.
``map.h`` Medium, limited to 100; You can remove this restriction by
modifying the source code. However, this restriction is no longer
available in commonly used Linux distributions.

Draw content
------------

MapServer now knows what kind of map to produce, including the size and
background color, and how to display the map on a web page. But it’s not
clear what to draw and how to draw-the work is done by the LAYER object.

The layer applies a single dataset and contains a series of elements,
use specific projections (which will be included later in this book) to
depict them on a specific scale. Layer with keyword ``LAYER`` Generate,
with keyword ``END`` End.

Keyword ``STATUS`` Determines whether the layer is rendered. Default
value ``Default`` It means it’s always rendered.

Each layer has a geometric type. In this example, the feature is a point
feature (a pair of coordinate values), and the point feature is selected
to simplify the example.

The value of the keyword TYPE is selected as ``POINT`` Layer types are
described in more detail in the next chapter.

In order to generate maps, MapServer must have spatial data. Instead of
using complex real-world data to describe a messy “Hello World” map, it
is built with artificial coordinate points (0. 0,0. 0).

Add the following to hello.map.

-  The keyword ``FEATURE`` specifies the associated geographic feature.
   Rather than reading records from a spatial database, FEATURE allows
   for the rapid creation of “features”.
-  The keyword ``FEATURE`` can only be used inside a LAYER object and
   must end with the keyword ``END``. Then specify the feature by the
   coordinate point.
-  The keyword ``POINTS`` describes the listed coordinate point pairs.
   Values are separated by spaces. Obviously, the number of values must
   be even. The listed values represent a single point (if there is only
   one coordinate pair), and can represent a line (if there are more
   than one pair).
-  If the first pair of coordinates is the same as the last pair, then
   the value listed is the polygon (equal to the first and last point
   closing the figure). The keyword ``END`` ends.
-  The keyword ``TEXT`` specifies the text string used to label the
   feature. Again, if there are spaces, they must be enclosed in quotes.

Add the following to hello.map.

-  In each layer, one or more classes ( ``CLASS`` ) need to be defined.
   The default category without a specific selection will delineate all
   elements in the dataset. If selection criteria are specified, only
   content that meets the selection criteria will be depicted.
-  Labels, line shapes, annotation types, and colors for depicting
   features are all defined at the class level.
-  ``STYLE`` objects define the properties of symbols used in classes to
   draw features. For simplicity, the value defines the color in this
   case. ``STYLE`` objects are terminated by the keyword ``END``.
-  The keyword ``COLOR`` determines the color of the feature, by setting
   the ``RGB`` component to determine the color. The value is between
   ``0-255``. Here, features are set as red dots with a default size of
   1 pixel.
-  ``CLASS`` also includes ``LABEL`` objects. The LABEL object is
   described within the class and specifies the font type, size and
   color of the label. Tags are far more complex than this, and are
   discussed in greater detail later in this book. Labels start with the
   keyword ``LABEL`` and end with ``END``.
-  The keyword ``TYPE`` determines the type of label font. There are two
   types: the ``bitmapped`` standard and the ``TrueType`` standard.
   Bitmapped fonts are generated internally without external references.
   TrueType must be installed and must also be determined by an alias in
   the file defined by the keyword FONTSET. For simplicity, the examples
   use bitmapped fonts.

Note that the default color for labels is black - of course it could be
a different color, but for now the default is used to simplify the
example.

The structure of the map file just shown is very simple, and the map it
generates cannot be called a map at all. But it should paint a tagged
image and display it on the web page.

View the result
---------------

With MapFile, you can render it as a picture using the following
command.

::

   shp2img  -m hello.map  -o out.png
