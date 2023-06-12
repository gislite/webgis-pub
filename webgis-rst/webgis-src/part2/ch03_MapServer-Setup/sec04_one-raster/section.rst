.. Author: Bu Kun .. Title: Release remote sensing images

Release remote sensing images
=============================

Let’s take a look at how to publish a three-band remote sensing image.

Conceptual differences between image, icon and picture
------------------------------------------------------

Visualizations acquired by satellites or other sensor equipment are
generally referred to as “image” rather than “icon.” The concept of
“icon” has a broader connotation, and “image” is a kind of “icon”. Image
and fihure together constitute the icon world. “Image” mainly refers to
the replica image world formed by photography, television, film, digital
imaging, computer painting, and network image, and of course, it also
includes remote sensing means.

“Picture” refers to the flat media composed of graphics, images, etc.
Note the definition here that “icon” is not a kind of “picture”. First
of all, the picture is a medium (or medium) that actually exists (can be
electronic); in addition, it is flat. “picture” is a form of expression
of “icon”.

Add remote sensing image
------------------------

Similar to the Mapfile structure used earlier, but you need to define a
remote sensing image data source:


.. literalinclude:: ./mf3t.map
   :lineno-start: 1


``../geodata`` specified as MapServer will look for the base directory
of the spatial dataset. The initial map range is determined by the
coordinates of the specified southwest and northeast corners.

Here is the effect:


.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mf3t.map&layer=topo&mode=map

