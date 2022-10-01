; Author: Bu Kun ; Title: Add a scale bar

Add a scale bar
===============

The map scale of MapServer can be added to the map or separated from the
map.

Effect
------

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

Key code
--------

::

   SCALEBAR
   LABEL
   COLOR 0 0 0
   ANTIALIAS true
   SIZE small
   END
   POSITION lr
   INTERVALS 5
   STATUS embed
   SIZE 188 5
   STYLE 0
   UNITS miles
   BACKGROUNDCOLOR 255 0 0
   IMAGECOLOR 255 255 255
   COLOR 128 128 128
   OUTLINECOLOR 0 0 255
   TRANSPARENT off
   END

Where ``STATUS`` is set to ``embed`` , which can be directly mosaicked
into the generated map.
