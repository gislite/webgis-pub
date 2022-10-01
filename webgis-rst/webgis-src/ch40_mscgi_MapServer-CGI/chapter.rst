CGI interaction of MapServer
============================

So far, you can only view maps before creating maps. The general meaning
of creating a Web mapping application is to create a map that can be
changed by the user (the application). In other words, a user can change
the content (or information) of the map. To do this, you need to use the
MapServer HTML template.

The application will be interactive and allow users to zoom and roam the
map image. You will see how to generate scale bars and legends, and how
to embed valid information in the output HTML (similar to the size of
the map and the coordinates of the mouse click). In other words, you
will generate a “real” map application for the first time.

Also, in addition to being dynamic, scaleable maps also exhibit more
ways of presenting detail in different ways.

This section explains more about the interoperation of CGI. Query
function is also an important function of MapServer. But the design of
MapServer is old, and the query function is clumsy to use. Only a simple
description, more query functions, described in the later section of the
map service.

.. toctree::
   :maxdepth: 2

   sec1_mapserver-cgi-intro/section
   sec2_mode/section
   sec3_zoom/section
