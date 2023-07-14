.. Author: Bu Kun .. Title: Browse and zoom control

MapServer interaction: browse and zoom control
==============================================

This section introduces how to realize the control of map browsing and
zooming through CGI in MapServer.

How to browse and zoom
----------------------

As in the previous map, we pass our mapfile path and other parameters (
``map=/ms4w/apps/tutorial/htdocs/example2-1.map&amp;mode=browse`` )
Initialize our application MapServ ( ``/cgi-bin/mapserv`` ). Here is a
link:

`Open sample map
1 <http://webgis.pub/cgi-bin/mapserv?map=/owg/mdca.map&mode=browse&root=/owg&program=/cgi-bin/mapserv&layer=topo&zoom=0&map_web=template+example2-1.html>`__

In Mapfile, you need to add: ``TEMPLATEPATTERN '.'`` ，otherwise, it may
appear:

::

   loadWeb(): General error message. URL-based TEMPLATE configuration failed pattern validation.

For clarity, use the Python code to list the parameters as follows:

::

   >>> paras = [
   ... ['map', '/owg/mdca.map'],
   ... ['mode', 'browse'],
   ... ['root', '/owg'],
   ... ['program', '/cgi-bin/mapserv'],
   ... ['layer', 'modis'],
   ... ['zoom', '0'],
   ... ['map_web', 'template+example2-1.html']
   ... ]
   >>> url_para = '&'.join(x for x in ['='.join(x ) for x in paras])
   >>> url_para
   'map=/owg/mdca.map&mode=browse&root=/owg&program=/cgi-bin/mapserv&layer=topo&zoom=0&map_web=template+example2-1.html'

`Open sample Map
2 <http://webgis.pub/cgi-bin/mapserv?map=/owg/mdca.map&mode=browse&root=/owg&program=/cgi-bin/mapserv&layer=topo&layer=states_line&zoom=0&map_web=template+example2-1.html>`__

If you want to use multiple layers, use the ``layer`` parameter multiple
times. But the same template file can be used.

::

   >>> paras = [
   ... ['map', '/owg/mdca.map'],
   ... ['mode', 'browse'],
   ... ['root', '/owg'],
   ... ['program', '/cgi-bin/mapserv'],
   ... ['layer', 'modis'],
   ... ['layer', 'states_line'],
   ... ['zoom', '0'],
   ... ['map_web', 'template+example2-1.html']
   ... ]
   >>> url_para = '&'.join(x for x in ['='.join(x ) for x in paras])
   >>> url_para
   'map=/owg/mdca.map&mode=browse&root=/owg&program=/cgi-bin/mapserv&layer=topo&layer=states_line&zoom=0&map_web=template+example2-1.html'

This example seems to have no new knowledge points.

`Open the sample
map <http://webgis.pub/cgi-bin/mapserv?map=/owg/mfc2.map&mode=browse&root=/owg&program=/cgi-bin/mapserv&layer=states&zoom=0&map_web=template+example2-1.html>`__

This time we use ``browse`` mode instead of ``map`` mode. The ``browse``
mode tells MapServer to create a map (image) on the ``/tmp/`` directory.
The path and name of the image are referenced by MapServer under the
name ``img`` . When MapServer parses the HTML template, it replaces the
``[img]`` tag with the correct path to the image: ``img``.

There are a few things you can do with this map. First, click on any
part of the image and the map will refresh and center the clicked point.
This is panning. If you click the ``Map Control`` drop-down box, you can
choose a ``zoom in`` or ``zoom out`` value. If you set it to
``Zoom In 2x`` and then click on any part of the map, the map will be
refreshed, zoomed in, and the clicked point will be centered. If you
zoom out, the opposite happens. When you select a “Zoom In” or “Zoom
Out” value and click the “Refresh” button, the map zooms in or out from
the center of the previous map. You can refresh the map at any time
using the refresh button.

The zoom/pan controls use internal MapServer CGI variables. This example
shows how to use the “scale” variable. The value of zoom determines how
far to zoom in or out. If the value is ‘0’, MapServer will reposition
the image based on the user’s mouse click. If the value is greater than
“0”, the CGI program zooms in (the current scale of the map multiplied
by the zoom value). If it is negative, the CGI program zooms out
(divides the current scale by the zoom value). Other variables that can
be used to control zoom and pan are “zoomdir” and “zoomsize”. These two
variables are almost the same as “zoom” - “zoomdir” controls the zoom
direction, and “zoomsize” controls how far to zoom in or out. Check out
the OSGeo Gallery or other examples in the MapServer wiki for other
zoom/pan control options.

Try changing the “map mode” from ``browse`` to ``map``. What happens
after hitting refresh? Remember, when we use ``mode=map``, MapServer
returns a static map…it ignores the HTML template and just streams the
map image directly to the browser.

Although more data layers have been added, it is still similar to
Mapfile in part 1.

Now, look at the HTML template file. You’ll notice that it’s essentially
an HTML form that calls a MapServer CGI program. Because it’s a form,
you can implement your interface with radio buttons and checkboxes and
dropdown boxes. Don’t be limited by this example - creativity is fine.
;) For more information, check out the HTML Template Reference page.

Pan and zoom map in WebGIS map: POST form submission
----------------------------------------------------

The following shows the use of a form for submission, with various
parameters through the ``input`` To pass on. The effect is the same as
above:

.. raw:: html

	<form method="get" action="http://webgis.pub/cgi-bin/mapserv" role="form">
    	<!-- The following two variables are user defined variables.
         	MapServer will pass its value to the HTML template if the
         	proper tags are found, in square brackets "[]"  -->
    	<input type="hidden" name="root" value="/owg">
    	<input type="hidden" name="program" value="/cgi-bin/mapserv">
    	<!-- The map and layer variables are internal MapServer variables.
         	They are required by the mapping application. -->
    	<input type="hidden" name="map" value="/owg/mdca.map">
    	<input type="hidden" name="layer" value="modis">
    	<input type="hidden" name="layer" value="states_line">
    	<input type="hidden" name="zoom" value="0">
    	<div class="col-sm-12">
        	<div class="col-sm-4">
            	<!-- The map_web_template variable will replace the TEMPLATE
                 	parameter in the WEB object of the MAP file... -->
            	<select name="map_web" class="form-control">
                	<option value="template example2-1.html"> 1: Browse and zoom control</option>
            	</select>
        	</div>
        	<div class="col-sm-2">
            	<input type="submit" name="submit" value="Start the tutorial!" class="btn btn-primary">
        	</div>
    	</div>
	</form>

View Mapfile
------------

Take a look at Mapfile here:


.. literalinclude:: ./mdca.map
   :lineno-start: 1

