.. Author: Bu Kun .. Title: Use custom styles in Mapfile

Use custom styles in Mapfile
============================

Vector data can be divided into three types: point, line and surface.
The simplicity of the data type structure gives the diversity of
expression. In MapServer, you can set styles in various dimensions such
as color, size (thickness), and transparency for points, lines, and
surfaces.

Point
-----

.. container::

The Mapfile used is:


.. literalinclude:: ./mfy3.map
   :lineno-start: 1


Line fill example
-----------------

.. container::

The Mapfile used is:


.. literalinclude:: ./mfu1.map
   :lineno-start: 1


Circular fill exampl
--------------------

.. container::

The Mapfile used is:


.. literalinclude:: ./mfu2.map
   :lineno-start: 1


River style
-----------

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

The Mapfile used is:


.. literalinclude:: ./mfmr.map
   :lineno-start: 1


``GepMap`` can be further used to get the effect of the magnification:

.. raw:: html

   <p align="center">

.. raw:: html

   </p>
