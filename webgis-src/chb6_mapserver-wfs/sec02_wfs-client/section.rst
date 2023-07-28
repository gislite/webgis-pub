.. Author: gislite .. Title: Use MapServer as a WFS client

Use MapServer as the WFS client
===============================

WFS can be added as a layer in MapServer. In this way, it is used as a
WFS client.

Since WFS needs to transfer data over the network, it is best to use
smaller amounts of data. The selection here is to use point feature
data.

Writting way of MapFile
-----------------------


.. literalinclude:: ./mft6.map
   :lineno-start: 1


Example effect
--------------

The effect is:

.. image:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mft6.map&layers=states%20wcity_wfs&mode=map

Note that the above graph is a traditional MapServer generated map.
Defined by the WFS point layer in front, so it’s mostly occluded by
polygons.


