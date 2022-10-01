; Author: Bu Kun ; Title: MapSever interaction using CGI

MapSever interaction using CGI
==============================

To map through the Mapfile configuration file, you have understood the
basic ideas of maps, layers and classes, and know how the various parts
of a Mapfile are combined. Now move on to an app that will offer full
pan and zoom functionality, as well as the ability to toggle layers on
and off.

So far, the map can only be viewed when the map is created. Creating a
web mapping application usually means creating maps that can be changed
by the user (of the application). That is, a user can change the content
(or information) of the map. To do this interactively, we use the
MapServer HTML template.

MapServer CGI is template based. When first executed in response to a
web request, it reads a configuration file (Mapfile) that describes the
map’s layers and other components. Then it draws and saves the map.
Next, it reads one or more HTML template files identified in the
Mapfile. Each template consists of traditional HTML markup tags and
special MapServer replacement strings. For example, these strings are
used to specify paths to map images created by MapServer, identify
layers to render, and specify zoom levels and orientations. MapServer
replaces the current values of these strings and sends the data stream
to the web server, which then forwards it to the browser. When the
requester changes any form element on the page (for example, by changing
the zoom direction or zoom value) and clicks the submit button,
MapServer will receive requests with these new values from the web
server. Then the cycle starts again.

Technical note on network access of MapServer
---------------------------------------------

Your original purpose is to generate maps in a CGI environment where
users connect to the Apache web server through a web browser. In this
environment, Apache calls MapServer, which can pass various forms of
variables from the browser.

Using this information, MapServer generates maps and web pages, which
Apache returns to the browser. Of course, it is not enough for MapServer
to generate a map only from the browser’s information.

In fact, CGI MapServer network applications have four components: Map
files, HTML initialization forms, one or more template files, and
spatial data (libraries).

Note: Web applications can provide fixed content for static pages, as
well as dynamic content through scripts in response to web forms, as
well as database queries and other functions.

The standard that determines the interaction between these scripts and
the Web server is called the universal gateway interface, which is
usually abbreviated to CGI.

These four components are discussed in this chapter. The premise is that
the user’s web browser has already displayed the initialized file.

MapServer, like all web applications, is based on a stateless protocol -
that is, on each call, it only knows what information the browser
communicates to it. Stateless protocols preclude using programs to
answer anything other than the last question. However, some clever code
can provide a stateful environment that enables web applications to do
more complex work. For example, state can be maintained between calls by
storing state information in a variable in a hidden form, such as in a
URL or a cookie. But some methods need to bootstrap the program, so it
contains the information needed for the first call.

In MapServer, this is done by initializing the file. In CGI MapServer
applications, initialization files are traditional HTML forms that have
initialization information that converts hard-coding into form
variables. Almost all values used by MapServer can be set in the
initialization file.

When Apache first calls MapServer using HTML’s initialization form, the
form variable is used to specify the name of the map file (the extension
is usually ``.map`` ).

It then finds the fonts, symbols, templates, and spatial data of the
file. The map file also specifies the size and geographical range of the
final map, and whether the map is in GIF,JPEG or PNG format. After
reading the map file, MapServer renders one or more images: the map
itself, legends and scale bars, and possibly a reference map. It stores
these images in a specified location in the map file.

In order to show the results, MapServer needs to design the map format
and organize the relevant elements to make it a web page. The program
itself does not generate HTML; instead, it scans the HTML template to
replace the string. String substitution can refer to files, details of
map geometry, layer specifications, or scaling factors. They can also be
constants of CGI variables, such as image size, name of the map file,
map range, and so on.

MapServer replaces the string with the appropriate value and returns the
modified HTML to the browser that requested the information.

In this chapter, you will build a map application to illustrate the
simplicity of using MpaServer and how the components work together.

The following chapters will introduce the features of MapServer
(projection, tile retrieval, notation, query, etc.), which will make the
capabilities of MapServer more obvious.

MapServer application development through CGI
---------------------------------------------

MapServer provides two development interfaces: CGI and MapScript. CGI is
the most basic method for MapServer application development. In CGI
mode, MapServer uses the GD library to convert spatial data into
geographic graphics and transmit them back to the user’s browser. Users
do not need to install any specific browsing program to operate on it
through the browser.

The user can send a request directly to the MapServer server through a
URL similar to the following, and MapServer creates the appropriate map
image according to the requested parameters, and returns the result to
the user’s browser:

::

   http://hostname/cgi-bin/mapserv?map=/ms4w/apps/txitorial/htdocs/example1-1.map&layer=states&mode=map 

where ``/cgi-bin/mapserv`` is the MapServer CGI program. ``?`` is
followed by a query string consisting of MapServer CGI parameters such
as ``map`` , ``layer`` , and ``mode`` . The ``map`` parameter specifies
the map file to be processed by MapServer, the ``layer`` parameter tells
``mapserv`` to display the layer, and the ``mode`` parameter tells
``mapserv`` to generate a static map image.

Alternatively, dynamic, interactive maps can be generated by specifying
the value of the ``mode`` parameter to the browser. At this time, when
the user clicks on the map, MapServer will generate a zoom-in, zoom-out
or repositioning map centered on the user’s clicked location.

Generating a dynamic map requires an HTML template with a form to
interact with the user.

A simple form is as follows:

::

   <!-START OF MAPSERVER FORM->
   <form name=”mapserv” method=”GET" action="/cgi-bin/mapserv.exe">
   <!-HIDDENMAPSERVERCGIVARIABLES->
   <input type=Mhidden"name="map"value=n[map]">
   <input type="hidden"name="imgext"value="[mapext]n>
   <input type="hidden"name="imgxy"value="199.5149.5">
   <input type="hidden"name="zoom"value=,T'>
   <input type="hidden"name="mode"value="browse">
   <div align="center">
   <table border='T'cellpadding="0"cellspacing=”0">
   <tr>
   <td>
   <!-THE INTERACTIVE,DYNAMICALLY CREATEDMAP->
   <input type="image"name="img"src="[img]"
   width=”400”height=”300”>
   </td>
   </tr>
   </table>
   </div>
   </form>

A MapServer HTML template is an HTML-formatted file with MapServer tags.
MapServer tags are MapServer CGI variables enclosed in square brackets
(``[]``), such as ``[map]``, ``[img]``, and ``[mapext]``, etc., which
represent Map file, map image URL, and extent of the map. Through HTML
templates, MapServer CGI programming can be greatly simplified.

When the MapServer CGI program receives the request from the MapServer
HTML template, The parameters are first parsed, the request is processed
and the necessary output is generated, then some of these outputs are
replaced with the corresponding MapServer tags (variables) in the HTML
template, and finally the HTML (template) file with the output results
is returned to the client browser. Since the map in the template is
returned as a form element, the user can interact with it.

MapServer provides many CGI variables for Web mapping. Almost all
keywords in MapServer’s map files can be defined as a variable, but
there are not many CGI variables in the core of mapping. In addition,
users can also customize variables, such as users can define a variable
named ``root``, which is used to represent the root directory of the
application.

MMap browsing can only rely on MapServer to provide the basic functions
of Web mapping services. In addition, MapServer also provides powerful
spatial and attribute query functions. In CGI mode, HTML templates are
used extensively to construct queries and organize the information
returned by queries, which often involves complex interactions with map
files, templates, and MapServer CGI programs.

MapServer has many modes ( ``mode``, and browse ( ``browse`` ) mode is
the default mode of MapServer. There are 18 modes related to queries. By
using these query modes, MapServer can implement points such as:
querying points based on mouse position, querying points based on input
coordinate values, querying attributes by inputting an expression, and
querying based on the serial number of elements.

MapServer creates legends and scales (configurable in mapfile) and
generates reference maps. The reference map displays the context of the
currently displayed map. Zooming and panning are controlled by the user.

MapServer HTML template
-----------------------

With the MapServer HTML template, you need to add the MapServers
template declaration to each HTML template file. Otherwise, when using
GetFeatureInfo (with an info_format collection) as the text/html
request, you will get the following error message:

::

   Content-type: text/xml isValidTemplate(): Web application error.
   Missing magic string, template-file doesn't look like a MapServer template.

You need to add at the beginning of each template:

::

   <!-- MapServer Template -->

Example the exemplar template query footer.html is:

::

   <!-- MapServer Template -->

A MapServer HTML template is actually a MapServer-specific HTML file –
these table tags are MapServer CGI variables enclosed in ``[]``. When a
MapServer CGI program processes an application, it first parses the
``query_string`` and map file, and produces the necessary output. These
outputs need to be written in an HTML template file, which must be
defined in the Mapfile by using the web template keyword (or in a
separate HTML initialization file). The CGI program will replace all
variables in the HTML template with appropriate values before sending it
to the web browser. If you view the contents of the HTML template
directly on a web browser, there will be no maps available, but empty
images and other characters of unknown meaning.

MapServer’s network mapping provides some variables – ``img`` variables,
which have been examples before, where several commonly used CGI
variables are designed as part of the initialization of the map
interface, but actually all MapFile parameters can be defined as
variables.

An explicit reference to CGI variables is at:
http://www.mapserver.org/cgi/index.html

The CGI variables used by MapServer can also be defined by the developer
and MapServer will pass it to the application. For example, we could
create a variable called ``root`` to represent our root directory for
this tutorial – the value of ``root`` will be read by ``/tutorial`` .
When the MapServer CGI value processes our HTML template, it will
replace every instance of the ``[root]`` tag and ``/tutorial``. You’ll
see this in action in each of the following examples.
