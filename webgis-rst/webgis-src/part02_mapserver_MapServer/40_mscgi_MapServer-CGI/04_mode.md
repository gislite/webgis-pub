; Author: Bu Kun
; Title: Interactive map and Browse mode

# Interactive Map and Browse Model


## View examples


<p align="center">
<img border= "1"
     src="{SITE_URL}/cgi-bin/mapserv?map=/owg/mdc1.map&layer=states_line&layer=topo&mode=map"/>
</p>


The map above is in ``map`` Generated in mode. It is a static map (nothing changes when you click).

But open the map below and you can use mouse clicks to interoperate.

<a target="blank" href="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfd1.map&layer=states_line&layer=topo&mode=browse">
{SITE_URL} / cgi-bin/mapserv?map=/owg/mdc1.map&layer=states_line&layer=topo&mode=browse
</a>


## Submit CGI variables using Post form

Previously, you put all the parameters needed by MapServer in URL, which is the way to use parameters explicitly, but it can cause the URL to become very long.


### Instruction

Another way is to use a form to submit parameters. Here is a form:

<form method=POST action="/cgi-bin/mapserv" role="form"  class="form-horizontal" style="border: 1px solid saddlebrown;">
<input type="hidden" name="map" value="/owg/mfc1.map">
<input type="hidden" name="layer" value="modis">
<input type="hidden" name="layer" value="states_line">

<div class="form-group">
<label for="subit"  class="col-sm-2 control-label"> </label>
<div class="col-sm-3">
<input id='subit' class="form-control btn btn-primary" type="submit" value="Generate map using POST">
</div>
</div>


<!--<input type="hidden" name="map_web_imagepath" -->
<!--value="/var/www/ms_tmp/">-->
<!--<input type="hidden" name="map_web"-->
<!--value="imagepath+/var/www/ms_tmp/+imageurl+/ms_tmp/">-->
</form>


### POST form

This part of the code is as follows


    <form method=POST action="/cgi-bin/mapserv">
    <input type="submit" value="Use forms to generate maps">
    <input type="hidden" name="map" value="/owg/mfc1.map">
    <input type="hidden" name="layer" value="modis">
    <input type="hidden" name="layer" value="states_line">
    </form>
    <IMG SRC="[img]" width=400 height=300 border=0>


With POST submission, the parameters need to be placed in the form.

<!--
<p>
There were changes in MapServer 5.0 in the way CGI variables are
Passed...so you might try to replace that "map_web_imagepath" line in
Your hello.html with something like:


    value="imagepath /ms4w/tmp/ ms_tmp/ imageurl /ms_tmp/"

But you can't use it either. You can just delete it.
-->


## Mapfile and template file description


### Mapfile description

Now, take a look at Mapfile:

->-> mfc1.map



Compared to static maps, only the following line is actually added to Mapfile:

    TEMPLATE 'example1-9.html'


This tells MapServer to use the page ``example1-9.html`` as the template file.
MapServer will process this file and replace the tags it encounters before sending it to the web browser. This is the mechanism by which MapServer implements dynamic pages.

The above code snippet defines the parameters of the Web object, starting with the keyword ``WEB`` and ending with the keyword ``END``. The ``WEB`` object tells the map server the name of the HTML template file (in this case, only one, named ``example1-9.html`` ), the paths to the images to create, and the URLs to point to those images.
As before, IMAGEPATH specifies the path to images created by MapServer.
In this case you use absolute paths, but you can also use relative paths from the location of the mapfile. Note that you cannot remove the leading or final slash ``/`` from the IMAGEURL.
The string defined by IMAGEURL is appended to the base URL (ie, http://localhost ) to generate the URL for the image rendered on the page.

Note that if you're not sure about the importance of ``/``, or what Apache's ``DocumentRoot`` is, you can look it up at http://httpd.apache.org/docs/mod/core.html#documentroot.


### HTML file

In the template file, in addition to the HTML text content, the key is the form code block within this page (right-click on your browser page and select "View Source" or something similar):

Now, let's build an interactive interface for our application.

The following shows the use of a form for submission, with various parameters passed through the input control.

    <!-- START OF MAPSERVER FORM -->
    <form name="mapserv" method="GET" action="/cgi-bin/mapserv">
        <input type="hidden" name="root" value="/owg">

Each time the user clicks the map, this block executes the MapServer CGI program ( ``/cgi-bin/mapserv`` ).
The program here can be defined using the following:

        
    <input type="hidden" name="program" value="/cgi-bin/mapserv">


    
The following two variables are user-defined variables. If it finds the correct tag within square brackets ``[]``, MapServer will pass its value to the HTML template.

``map`` And ``layer`` Variables are MapServer internal variables. They are required for MapServer mapping applications.

    
      <!-- HIDDEN MAPSERVER CGI VARIABLES -->
      <input type="hidden" name="map" value="[map]">
      <input type="hidden" name="imgext" value="[mapext]">
      <input type="hidden" name="imgxy" value="199.5 149.5">
      <input type="hidden" name="zoom" value="1">
      <input type="hidden" name="mode" value="browse">
    
      <div align="center">
      <table border="1" cellpadding="0" cellspacing="0">
      <tr>
            <td>
              <!-- THE INTERACTIVE, DYNAMICALLY CREATED MAP --
              <input type="image" name="img" src="[img]"
                width="400" height="300">
            </td>
          </tr>
        </table>
      </div>
    </form>


The ``map_web_template`` variable will replace the TEMPLATE parameter in the WEB object in the Mapfile.
       

The map is actually in another form. ``input`` Using the following code to represent:

    <input type="image" name="img" src="[img]" width="400" height="300">
    
The items in square brackets (``[map]`` , ``[mapext]`` , and ``[img]`` ) are so-called MapServer tags - these are MapServer CGI variables, which are MapServer CGI program for assignment.
The label ``[map]`` is a placeholder for the Mapfile path, so when MapServer runs, it will be replaced with ``"/owg/mfc1.map"`` .
The label ``[mapext]`` will be replaced with the current map extent, which will change as you click on the map;
The ``[img]`` tag will be replaced with the path to the image created by the MapServer CGI program, and the name will be passed to the client after MapServer renders the image on the server side.
On the server, the path ``IMAGEPATH`` ( ``/owg/ms_tmp/`` ) must exist and have appropriate permissions.
You can check to see if the image exists (on the server) under the ``IMAGEPATH`` ( ``/owg/ms_tmp/`` ) path in MapServer.

Note that the above call also has a hidden variable ``"mode"`` with the value ``"browse""``, which tells MapServer to create and store images in the ``tmp`` directory. Then, this Images are referenced as ``[img]``, which is what you see in the browser.

## Requirements for MapServer template files


The MapServer template file must contain the specific string ``mapserver template`` on the first line, usually given in the form of HTML, JavasSript or XML comments. This line is not passed to the client. This particular string is not case sensitive.

MapServer's template file name suffix is limited. The available suffixes are:
``.gml`` , ``.html`` , ``.htm`` , ``.js`` , ``.kml`` , ``.svg`` , ``.tmpl`` , ``.wml`` , ``.xml`` .

### CGI variable

All CGI parameters can replace references, MapServer specific parameters, and user-defined parameters in the template.
In principle, parameters are passed directly by MapServer without any processing. This feature is critical to implementing MapServer applications.

The following reference lists only the template placeholder-specific strings needed to obtain information about MapServer modifications, such as new scale bars, query results, and so on.

The placeholder string for the template is case-sensitive.

The property item substitution must be the same as the item name in the dbase file.

ArcView and ArcInfo usually generate dbase files with project names all in uppercase.
When the template is URL, apply the appropriate URL encoding (that is, ``' '`` To ``'+'`` ).

Some placeholder strings can also be provided in escaped form, such as URL encoding.

### Special character

A template is simply an HTML file or URL string that contains special characters replaced by mapserv each time the template is processed.
Simple substitution allows information such as the active layer or space range to be passed from the user to mapserv and back again.
In most cases, the new value is dumped into the form variable that will be passed again. Here is a list of special characters and form variables.
HTML templates can contain anything, including JavaScript and Java calls.

In HTML files, attribute values can be enclosed in quotation marks (``""``). Writing property values within quotes allows you to set special characters that the value does not normally use (such as: ``]``, ``=``, ``"``, and spaces. To write single quotes within the property value, only Use two quotation marks (``""``).

