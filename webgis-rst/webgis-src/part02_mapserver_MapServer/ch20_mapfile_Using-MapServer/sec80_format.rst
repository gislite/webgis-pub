; Author: Bu Kun ; Title: Change the output format of the map

Change the output format of the map
===================================

View examples
~~~~~~~~~~~~~

Depending on the format you choose, the image may not be displayed in
your browser. If the link doesn’t appear in your browser, right-click on
the image above to see what format is specified in MapFile for saving.

.. figure:: %7BSITE_URL%7D/cgi-bin/mapserv?map=/owg/mfa8.map&layers=land-shallow-topo+wcountry-line&map.imagetype=AGG&mode=map
   :alt: Different output results

   Different output results

Mapfile example
---------------

The following is the Mapfile used in this example ``mfa8.map`` ):

->-> mfa8.map

Files are changed as follows:
-----------------------------

->-> xx_diff_mfa8_mfa6.htmp

Now our MapFile contains a new object ``OUTPUTFORMAT`` . Within the
``MAP`` object defined by this object, and when used with the keyword
``IMAGETYPE``.

Depending on the compiled library of MapServer, you can have a variety
of output formats to choose from - the GD library provides ``PNG``
(8-bit and 24-bit), ``GIF``, ``JPEG``, ``WBMP`` , the GDAL library,
which sources many of MapServer’s input formats, and can also provide
output in ``PNG``, ``JPEG``, ``TIFF/GeoTIFF``, and other raster formats;
the pdflib library provides PDF output.

.. raw:: html

   <!-- Mingku provides flash output -->

Have a look at your MAPFILE object by changing the keyword ``IMAGETYPE``
and experiment with ``OUTPUTFORMAT`` . It should be used as
``IMAGETYPE`` value (eg: ``IMAGETYPE png`` or ``PNG24 IMAGETYPE`` ), the
name of the output format.

Please consult the ``OUTPUTFORMAT`` object reference:

//www.mapserver.org/mapfile/outputformat.html#outputformat
