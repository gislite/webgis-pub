==========================================
Control Color
==========================================

The raster source allows arbitrary manipulation of pixel values.
In this example, the RGB values on the input tile source are adjusted
in pixel mode before being rendered using the second raster source.
The raster operation converts the pixels in the RGB space into HCL color spaces,
adjusts the values according to the above controls,
and then converts them back into RGB space for rendering.

.. raw:: html

   <iframe src="./xx-ol-color.html" width="100%" height="450" style="border:1px solid">
   </iframe>


`View the example <xx-ol-color.html>`_