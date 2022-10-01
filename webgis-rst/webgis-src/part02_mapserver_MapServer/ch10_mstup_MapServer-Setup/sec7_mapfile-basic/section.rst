.. Author: Bu Kun .. Title: Basic usage of MapServer

Usage process of MapServer
==========================

MapServer as a WebGIS solution. It is object-oriented, and the API
organization of the basic profile MapFile and MapScript modules is
object-based. MapServer supports distribution and interoperability by
supporting several standards of the OGC Association. No matter using
MapServer CGI module or server scripting language + MapScript, the
dynamic interaction between server and client browser can be realized.
The syntax for configuring MapFile files is simple and easy to learn,
especially if you have experience of using desktop GIS software such as
ArcMap to make thematic maps. Compared with commercial software,
MapServer is open source, you can use it for free, and you can modify
the source code as needed. It should be pointed out that MapServer, as
an open source project, which is in continuous development; but in
recent years, the function has been relatively perfect and the update is
relatively small. The content of this website is based on Mapserver
version 7. 0 and later.

Once the MapFile file is configured, you can use the MapServer CGI
module or the MapScript module to develop WebGIS programs. The
difference between them:

1. The work that needs to be done to use the MapServer CGI module:
   prepare the resources required by MapFile, configure MapFile, and
   design the user interface (ie html file, you can use scripting
   languages such as JavaScript to enhance interactivity). Server-side
   design is not possible because MapServer CGI itself is a customized
   server-side program. Of course, it is possible to make Map Server CGI
   have the desired features by modifying the source code.

2. Using the MapScript module requires other server-side solutions
   (referring to scripting languages), such as PHP (installed on the Web
   Server as a CGI module). The MapScript module, as a PHP extension
   module, is placed in the extensions directory of the PHP installation
   path. The MapScript module preserves the hierarchical object
   structure of the MapFile file and provides PHP with an API for the
   object structure. Then, the programmer can use PHP on the server side
   to flexibly choose to modify the MapFile file by calling the
   MapScript API; instead of being rigid like the MapServer CGI module.
   At the same time, combined with PHP’s support for many databases -
   non-spatial databases, such as Oracle, Sybase, MySQL, etc., it
   becomes easy to integrate spatial data and non-spatial data in
   WebGIS.

Languages supported by MapScript include PHP, Perl, Python, Java, Tcl,
C#, etc.

Basic requirements of Mapfile
-----------------------------

As you can see, the syntax of Mapfile is relatively simple. In general,
the keywords and values of MapServer are not case-sensitive. In this
book, however, the keywords are always uppercase and values are
lowercase. This is for the sake of clarity and is not necessary. It is a
good idea to assume that they are case-sensitive. However, you should be
aware that in this case, it may be important that when you interact with
a spatial dataset, the attribute values are still case-sensitive. For
example, attribute names in the underlying database may be
case-sensitive, so references to attributes that the expression contains
will also be case-sensitive.

.. raw:: html

   <!--
   Note that version 4.4.1 of MapServer appears case-insensitive for shapefile attribute names, although this statement is the opposite of the file (http://mapserver.gis.umn.edu/doc44/mapfile-reference.html) of "MAPFILE reference MapServer 4.4".
   -->

Strings that contain embedded spaces must be in quotation marks. Single
or double quotation marks are acceptable, but they must be used in
pairs. You can’t let a string use two different quotation mark
characters.

Analysis of MapServer Map File format
-------------------------------------

MapServer configures the map to publish through a map file (mapfile).
Mapfile is the core of MapServer, which organizes all kinds of map
elements into a hierarchical object system. The mapfile defines the
elements that make up the map and the relationships between them, and
tells MapServer where to load the data and how to represent the data. In
a Mapfile, a layer is a combination of data and styles; the data in it
is a combination of spatial data and attribute data; styles are
implemented through Class and Style objects.

Map files use ``#`` as line comment characters. The map files all use
the keyword MAP as the beginning of the map object, and the keyword END
as the end mark of the map object definition. The entire map file
represents a map object. Between the MAP and END keys are key/value
pairs describing the properties of the map object.

Map objects have many properties, such as map image format (IMAGETYPE),
map size (SIZE), path to map data (SHAPEPATH), The extent of the map
(EXTENT) and the symbol set (SYMBOLSET) and font set (FONTSET) used by
the map.

Every map file must have at least one layer object. Users can define as
many layers as they want, but MapServer has a default maximum layer
limit of 100 layers. This parameter can be modified by modifying the
``map.h`` file, However, after the modification is completed, MapServer
needs to be recompiled before it can be used.

MapServer supports not only vector layers, but also raster image layers,
such as GeoTIFF, JPEG, PNG and GIF. What is more noteworthy is that
MapServer also supports WMS layers, that is, a layer that obtains map
images from other WMS servers to form map objects.

Each layer also has some commonly used attributes such as layer name
(NAME), dataset (DATA), type (TYPE) and whether to display (STATUS) and
so on.

Each layer has one or more Class objects, which are used to classify the
features in the layer. Usually, there is a keyword CLASSITEM in the
layer object, which is used to specify a property field, so that layers
can be divided into categories (Class) or themes (Theme) based on the
value of this field. If the keyword CLASSITEM is specified in the layer
object, a keyword EXPRESSION is required in each Class object to
indicate the attribute value represented by the category. Class objects
usually have a Name property.

Each Class object uses one or more Style objects to define the display
style of this type of feature, such as the type of symbol (SYMBOL), the
color of the fill (COLOR or OUTLINECOLOR), the size of the symbol
(SIZE), and so on.

Structure of Mapfile
--------------------

Mapfile consists of objects in a hierarchical structure. At the top of
the hierarchy is the map object (that is, the Mapfile itself). Map
objects contain both simple and structured projects. A simple project
consists of key value pairs, and a structured project contains other
projects, each of which can be simple or structural. You have seen
examples of the structure of these two types of mapfile For example,
first.map, discussed in Chapter 2, contains the following lines:

::

   NAME "First"
   EXTENT -125.00 20.00 -65.00 50.00

Each of these lines contains some simple mapfile objects. You will also
notice that these keywords specify a value that makes the map as a whole
meaningful. For example, the keyword name first sets the name of the
map. This keyword is used at the map level to specify a string that
identifies all the maps produced in the mapfile’s process of generating
the output file MapServer. Note, however, that a keyword can use the
same name at other levels, and its function depends on where it’s used.
Likewise, the scope of the keyword sets the scope of the entire map, so
it must also be defined at the map hierarchy level. Like NAME, it can
also be used at lower levels.

Note that if you are new to MapServer and user, using the same keywords
(like name, template or color) at different levels in the mapfile can be
confusing. When you’re familiar with the concept of mapfiles, this
shouldn’t be a problem, in fact, you’ll appreciate that developers
choose to define the same keywords at different levels with relatively
similar concepts.

first.map including the following lines:

::

   WEB
      TEMPLATE '/var/www/htdocs/first.html'
      IMAGEPATH '/var/www/htdocs/tmp'
      IMAGEURL '/tmp/'
   END

This is an example of a structured object. The Web object determines
which HTML template MapServer will use, and where the template is
located. The Web object is typically used to determine how MapServer
responds to Web requests and can contain more keywords than those shown
here. Due to the Web object definition is used to display the entire
map, it makes sense to specify the map. However, the same keyword
template can be used at a lower level, and its function is very
different. A lot of MapServer objects can define maps, but now I’m going
to introduce you to a layer object.

Using MapServer CGI module to develop WebGIS
--------------------------------------------

CGI is a set of rules that define the communication between a Web server
and other software on the same machine. Other software that follows CGI
communication rules is called CGI programs or CGI scripts. Web server
can use CGI program to realize dynamic interaction function
(Server-side). Usually, the CGI program runs on the server-side Mini
Program and is called by the Web server. Process the data obtained from
the web server (such as form data processing, query the database, etc.),
and return the processing results to the web server:

Web servers-CGI programs-other software (such as databases).

CGI programs can be written in any language, as long as they follow the
CGI communication rules. Such as compilation languages: C, C++, etc.;
scripting languages: Perl, Python, Bourne shell,Java, etc.

MapServer CGI module is a CGI program written in C language, which is
very small. The core mapserv.exe of the MapServer CGI module is only
36KB.

When the browser informs the Web Server to call the MapServer CGI module
through the URL, the Web Server creates a process for the CGI module;
the CGI module runs and loads the MapFile file specified by the URL, and
reads the TEMPLATE file (HTML file) in the MapFile file. Replace the
template substitutions of the CGI variables in the TEMPLATE file with
specific values; after processing the TEMPLATE file, the CGI module
returns the TEMPLATE file processing result (HTML file) to the Web
Server, and the Web Server outputs the HTML file to on the user’s
browser. At this time, the TEMPLATE file (HTML file) is used as the
user’s interactive interface.

Basic steps to design WebGIS using MapServer CGI program:

1. Configure MapFile: Generally, the user interface used is specified in
   the TEMPLATE property of the Web Object. The user can also specify
   the user interface to use via the URL.

2. Design the initialization interface: Considering that the URL for
   accessing the CGI program (mapserv.exe) is very long, moreover,
   ordinary users do not know the URL format for accessing the CGI
   program (mapserv.exe); therefore, a link (URL) to the CGI program
   (mapserv.exe) is embedded in the initial interactive interface.

3. Design user interaction and interactive interface: Here we need to
   introduce the key concepts of MapServer CGI module: CGI variables and
   templates. MapServer CGI variable can be regarded as CGI module
   mapserv Exe interface. Calling CGI variables in URL or HTML forms can
   complete most dynamic interactions, such as layer selection, zooming
   in and out, etc.

Templates are HTML files or URLs. Templates contain CGI variables and
its substitution variables, where the substitution variables (template
substitutions) correspond to CGI variables one-to-one. Design user
interactions and interactive interfaces, that is, use CGI variables and
substitution variables in URLs or HTML files. So, since template
substitutions correspond one-to-one with CGI variables, why introduce
the concept of template substitutions? It’s a bit conceptually overkill
indeed. However, the use of substitution variables can be used to
indicate that a CGI variable has an empty value.

Examples of developing WebGIS using the MapServer CGI module will be
provided in Appendix 2.

Developing WebGIS with MapScript Module
---------------------------------------

CGI module programming is to use CGI variables and its substitution
variables, and CGI modules are compiled programs (mapserv.exe); it is
difficult to use CGI modules to achieve more complex dynamic
interactions. Using other server-side scripting languages and MapScript
can more easily implement complex WebGIS functions.

Here we will take the popular server-side scripting language PHP as an
example to introduce the usage of MapScript modules. PHP is installed in
the Web Server as a CGI program, the MapScript module is placed under
the extensions in the PHP installation path, and the ``php.int`` file is
configured to support the use of the MapScript module, and the
PHP/Mapscript installation is completed. MapScript modules can be loaded
using the function ``dl`` (“MapScript Module Name”) in a ``*.php`` file
or ``*.phtml`` file. The API provided by the MapScript module is
object-based, which organizes objects in MapFile into object interfaces.
Object properties and methods can be called in ``*.php`` files or
``*.phtml`` files.

The source code of the program written by the author using PHP/MapScript
will be provided in Appendix 3.

MapServer data processing flow
------------------------------

The client sends the parameters and the required cgi program to
MapServer. After MapServer receives the parameters sent by the client,
it reads the mapfile file according to the mapfile path specified in the
parameters. Read the relevant data according to the data path specified
in the mapfile. Convert the read data to text data. This work is done by
calling FreeType Font Engine with GD Graphics Library. After the graph
is created, save it to the directory specified in the client parameters.
According to the information defined in the mapfile, MapServer reads the
specified template (template file), configures the html and screen
display and related data, and creates and embeds graphics (such as scale
size, sample image, reference text), Dynamically generated spatial
infographics are embedded in templates to generate files that can be
used by clients. Return to the client when done.

MapFile file
------------

Some tools for Mapfile, including VIM highlight tool, Sublime highlight
tool.

MapFile files organize various map elements into object systems with
hierarchical relationships. Data sources, data formats used, user
interaction and support for the OGC protocol are also defined in
MapFile.

-  MapObject
-  Querymap
-  Symbol
-  Projection
-  WebObject
-  Reference Map
-  Outputformat
-  Scalebar
-  Lengend
-  Layer Object
-  Label Object
-  Label Object
-  Feature
-  Projection
-  Class Object
-  Join Object
-  Label Object
-  Style Object
-  Grid Object

.. figure:: zz_fig_obj_rel1.png
   :alt: Objects and their hierarchical relationships in MapFile; note
   that some objects are omitted Object for drawing convenience

   Objects and their hierarchical relationships in MapFile; note that
   some objects are omitted Object for drawing convenience

Objects and their hierarchical relationships in MapFile; note that some
objects are omitted Object for drawing convenience

The syntax of MapFile is simple. The keywords for MapFile include the
object name (all the objects in figure 2), the object keyword, and the
object closing tag “END”. Object names and object closing tag “END” are
case-insensitive; attribute names are case-sensitive Shapfile files that
configure ESRI should be uppercase, while PostGIS files are always
lowercase. In MapFile files, the symbol ``#`` is used for single-line
comments. MapFile files have a ``.map`` extension and can be written
using various text editors.

Here is an example of MapFile:

Configuring a complete MapFile file requires: GIS data source, font
file, symbol file. GIS data sources can be distributed on different
computers: The font file is used to define the type of font used in the
output map. The point, line and face symbols used in the map can be
defined in the Symbol object in the MapFile file; However, in order to
achieve symbol reuse - without having to define the same symbols in
different MapFile files, a separate symbol file is usually defined
outside the MapFile.

Most of the objects in MapFile files either correspond to map elements,
or are commonly used in GIS. Such as Lengend,Scalebar,Layer, etc. The
function of these objects is obvious and easy to understand. The meaning
of the objects and attributes in the MapFile file will be explained in
detail in Appendix 1. Explain the meaning of four special objects here:
Web Object,Outputformat Object,Query Object,Reference Map Object.

-  Web Object defines how to handle the web interface. Such as: the
   attribute IMAGEPATH defines the path to store temporary files and
   images, and TEMPLATE defines the interactive interface file used.
-  Outputformate Object defines the format of the output image.
   MapServer converts GIS data format files (such as shapefiles) into
   image formats supported by the MIME (Multipurpose Internet Mail
   Extensions) protocol, such as gif, png, jpeg, etc.
-  QueryMap Object defines the generation mechanism of query results.
   For example: the attribute STYLE (not an object) sets how the
   selected feature is displayed.
-  Reference Map Object defines how the reference map is created.
   MapServer supports three reference map types. The most common use of
   a reference map is as a map viewing window.

The query results can be observed using the reference map. When a point
query occurs, a dot symbol is generated in the output Reference Map to
indicate the location being queried. The area query generates a box in
the Reference Map to indicate the query area. Feature queries display
the features of the query in the Reference Map. In short, the Reference
Map can be regarded as the observation window of the query [5].

After planning the WebGIS website, configure the MapFile file steps:

1. Prepare the resources required by the MapFile file, including GIS
   data, font files, and symbol files.
2. According to the requirements of the WebGIS website, following the
   syntax of MapFile, use text editing software or special MapFile
   writing software such as MapLab to write MapFile.
3. Use debugging software (such as MapLab) to test to see if the MapFile
   configuration is correct and appropriate.
