Cartographic Application of MapServer
=====================================

This part focuses on the techniques of cartography in MapServer.
Including the use of layers and style settings, text annotations.

MapServer configures the map to publish through a map file (Mapfile).
Mapfile is the core of using MapServer. It organizes various map
elements into a hierarchical object system, declaring the size and
format of the generated map, all the paths, names and formats of the
data used, as well as a variety of more complex control options. The
syntax for configuring Mapfile files is simple and easy to learn,
especially if you have experience of using desktop GIS software such as
ArcMap to make thematic maps. Mapfile is multi-layered, and each map
file defines a large number of other objects. These objects include
scale bars, legends, map colors, map names, map layers, and so on.

Configuring a complete Mapfile file requires GIS data sources, font
files, and symbol files. GIS data sources can be distributed on
different computers; font files are used to define the font types used
in the output map. The point, line and surface symbols used in the map
can be defined in the Symbol object of the Mapfile file; however, in
order to achieve symbol reuse, independent symbol files are usually
defined outside the Mapfile, and there is no need to define the same
symbols in different Mapfile files.

After planning the WebGIS website, configure the Mapfile file steps:

1. Prepare the resources required for Mapfile files, including GIS data,
   font files, and symbol files.
2. According to the requirements of WebGIS website, follow the syntax of
   Mapfile, use text editing software or special Mapfile writing
   software such as MapLab to write Mapfile.
3. Use debugging software (such as MapLab) to test and see if the
   Mapfile configuration is correct and appropriate.

The core program of MapServer is used to generate maps according to
geospatial data, configure the function of using CGI, and give it the
function of WebGIS. MapServer supports distribution and interoperability
by supporting several standards from the OGC Consortium. Whether using
the MapServer CGI module or the server-side scripting language
MapScript, the dynamic interaction between the server and the client
browser can be realized.







.. toctree::
   :maxdepth: 2

   sec1_raster/section
   sec2_grid/section
   sec3_format/section
   sec4_one-layer/section
   sec5_two-layers/section
   sec6_multiple-layers/section
   sec7_classes/section
   sec8_labels/section
   sec9_symbol/section
   sec10_projection/section
   sec11_scalebar/section
   sec12_legend/section
