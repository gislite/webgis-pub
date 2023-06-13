========================================
MapServer query mechanism
========================================

- Update: 2022-10-7

In addition to its rendering capabilities, MapServer also provides powerful query functions,
and supports spatial query (location based selection) and attribute query
(attribute value based selection).
To do this without programming support,
MapServer uses templates extensively to build queries and present results.
This leads to some complex interactions among MapFile, template and MapServer programs.
There are also a lot of different query methods and different ways to use templates.
For these reasons, MapServer's query tools are probably the most confusing aspect.

MapServer has powerful and complex query functions, but under CGI mode,
it lacks the analysis tools that allow real GIS to provide.
This overview describes some query functions of MapServer.


Spatial retrieval concept
========================================


Spatial query is a special kind of query supported by geodatabases and spatial databases.
Spatial query queries
differ from non-spatial SQL queries in many important ways.
The two most important differences are: the use of
geometric type data such as points, lines, polygons,
and queries involving spatial relationships between geometric types.

The two-dimensional or three-dimensional spatial data is used as the basis of the query,
and the query results are represented graphically;
the spatial query statement is composed of one or more spatial operation operators,
including predicates expressing spatial relationships.

Spatial query and analysis are at the core of GIS,
and most of the daily tasks in GIS projects are related to queries.
GIS query types can be divided into the following three types: simple attribute query, query related to spatial location, and joint query related to spatial location and attribute.


Basic requirements for implementing spatial retrieval in MapServer


The query template is an HTML fragment that is a suitable HTML interface when placed together by the MapServer CGI program.


The following two variables are user-defined variables. 
If the tag defined by ``[]`` in square brackets is found,
MapServer will pass its value to the HTML template.


The ``map`` and ``layer`` variables are interactive MapServer variables that
are required by the map application.


The variable passed by ``map_web`` will replace the ``TEMPLATE`` parameter in the WEB object of the Mapfile.
This variable is different from a user-defined variable.
  

