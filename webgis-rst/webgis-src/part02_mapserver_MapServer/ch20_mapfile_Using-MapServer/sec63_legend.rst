; Author: Bu Kun ; Title: Add legend

Add Legend
==========

The map legend of MapServer can be added to or separated from the map.

Effect
------

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

Key code
--------

::

   LEGEND
   STATUS embed
   IMAGECOLOR 230 230 230
   LABEL
   TYPE truetype
   FONT "arial"
   COLOR 0 0 0
   SIZE 10
   ANTIALIAS true
   END
   END

Where ``STATUS`` is set to ``embed`` , which can be directly mosaicked
into the generated map.
