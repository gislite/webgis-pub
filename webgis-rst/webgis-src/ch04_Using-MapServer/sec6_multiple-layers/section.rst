.. Author: Bu Kun .. Title: Build a map with multiple layers

Build a map with multiple layers
================================

MapServer builds maps by stacking layers together. On every render, it
is placed at the top of the stack. Each layer displays features selected
from a single dataset. Features to display can be selected using Unix
regular expressions, string comparisons and logical expressions. You can
think of layers as topics due to the similarity of data and the
similarity of style parameters such as scale, color, and labels. The
display of layers is under interactive control, allowing the user to
select which layers to render. While it is not possible to generate
layers dynamically, it is possible to populate empty layers with dynamic
data and manipulate them via URL.

View examples
-------------

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

To make the map richer, continue adding new data (river data) using a
new ``LAYER`` object. The definitions of each layer are relatively
independent and have nothing to do with each other.

Here is the map file（mfml2.map）：


.. literalinclude:: ./mfml2.map
   :lineno-start: 1


The roads layer map ( ``wroads`` ) is also defined in the Mapfile above
and this layer is further added to the map below.

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

Order of layers
---------------

Pay attention to the order of the layers. In this map, the river layer
is above the road, which is inconsistent with the usual mapping
principles. Usually, the road layer is placed above the river layer.

Swap the position when passing parameters, the effect is as follows, you
can see that it is the same as the map above. The order of the layers
defined in the Mapfile cannot be changed by passing parameters to the
URL.

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

If you want to modify the order of layers, you can only modify it in the
Mapfile:


.. literalinclude:: ./mfml.map
   :lineno-start: 1


You can see that although it is not obvious, the river layer is below
the road layer.

.. raw:: html

   <p align="center">

.. raw:: html

   </p>
