.. Author: Bu Kun .. Title: Add a graticule

Add a graticule
===============

In order to accurately indicate the location of each place on the earth,
people assume a coordinate system for the earth’s surface, which is the
latitude and longitude coordinate system.

On maps and globes, we can see thin lines, some horizontal and some
vertical, which are the longitude and latitude. The warp and weft are
intertwined, much like the squares on a chessboard, forming a warp and
weft network.

According to these longitude and latitude lines, the position and
direction of any place on the ground can be accurately determined. Using
the longitude and latitude marked on it, various locations, regions and
various geographic locations on the earth’s surface can be determined.
It is useful in military, aviation, navigation, etc. For example, a ship
is sailing on the vast sea, and an airplane is flying in the vast sky.
No matter where you go, people can use instruments to accurately measure
its latitude and longitude to determine its position.

View examples
-------------

In MapServer, latitude and longitude lines can be drawn on the map
according to its cartographic capabilities. This feature is a latecomer,
originally developed by John Novak in 2003. The drawing of graticules is
almost necessary for desktop mapping to facilitate location
determination when reading maps; however, it is not necessary for
WebGIS. WebGIS enhances the user’s operations on the map, and the
latitude and longitude coordinates can be quickly obtained through the
spatial query function.

The image below is an example, drawn on a map with latitude and
longitude lines, with the longitude and latitude of the longitude lines
drawn to the ends of the line.

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

Here is its Mapfile :


.. literalinclude:: ./mfd8.map
   :lineno-start: 1


Code modification
-----------------

Compared with the previously released image map, the code changes are as
follows:


.. literalinclude:: ./xx_diff_mfd8_mfa5.htmp
   :lineno-start: 1

