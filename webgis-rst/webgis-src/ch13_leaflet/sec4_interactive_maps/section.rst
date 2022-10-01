.. Author: Bu Kun .. Title: Interactive Choropleth Map

Interactive Choropleth Map
==========================

This is a case study that, with the help of GeoJSON and some custom
controls, creates a color interactive US state population density map.

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align: center; border: none">

.. raw:: html

   <iframe src="./leaflet_choropleth/example.html" width="816" height="516">

.. raw:: html

   </iframe>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align: center; border: none">

Show the example

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Data source
-----------

We visualize data on US population density. Since the amount of data is
not very large, the easiest way to store and display data is GeoJSON.

Each feature of our GeoJSON data will look like this:

::

   {{
   "type": "Feature",
   "properties": {{
       "name": "Alabama",
       "density": 94.65
   }},
   "geometry": ...
   ...
   }}

Basic states diagram
--------------------

Let’s display our states data on the map in a custom Mapbox style.

::

   var mapboxAccessToken = {{your access token here}};
   var map = L.map('map').setView([37.8, -96], 4);
   L.tileLayer('https://api.tiles.mapbox.com/v4/{{id}}/{{z}}/{{x}}/{{y}}.png?access_token=' + mapboxAccessToken, {{
   id: 'mapbox.light',
   attribution: ...
   }}).addTo(map);
   L.geoJson(statesData).addTo(map);

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align: center; border: none">

.. raw:: html

   <iframe src="./leaflet_choropleth/example-basic.html" width="616" height="416">

.. raw:: html

   </iframe>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align: center; border: none">

Show the example

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Adding colors
-------------

Now we need to color the states based on population density. Choosing
good colors for your map may require a bit of skill, but there is a
great tool to help us – ColorBrewer. We create a function that returns
the population based density based on the values obtained from
ColorBrewer:

::

   function getColor(d) {{
   return d > 1000 ? '#800026' :
          d > 500  ? '#BD0026' :
          d > 200  ? '#E31A1C' :
          d > 100  ? '#FC4E2A' :
          d > 50   ? '#FD8D3C' :
          d > 20   ? '#FEB24C' :
          d > 10   ? '#FED976' :
                     '#FFEDA0';
   }}

Next, we define the style function of the GeoJSON layer so that its
``fill color`` depends on ``feature.properties.density`` . At the same
time, we also adjusted the appearance and added beautiful strokes.

::

   function style(feature) {{
   return {{
       fillColor: getColor(feature.properties.density),
       weight: 2,
       opacity: 1,
       color: 'white',
       dashArray: '3',
       fillOpacity: 0.7
   }};
   }}    
   L.geoJson(statesData, {{style: style}}).addTo(map);

It looks much better now!

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align: center; border: none">

.. raw:: html

   <iframe src="./leaflet_choropleth/example-color.html" width="616" height="416">

.. raw:: html

   </iframe>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align: center; border: none">

View this example

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Adding Interaction
------------------

Now let’s make the color block highlight when we pass the mouse over the
color patches on the map that represent the states of the United States.
First, we’ll define an event listener for the layer’s mouse events:

::

   function highlightFeature(e) {{
   var layer = e.target;

   layer.setStyle({{
       weight: 5,
       color: '#666',
       dashArray: '',
       fillOpacity: 0.7
   }});    
   if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {{
       layer.bringToFront();
   }}
   }}

Here we pass ``e.target`` Get the mouseover layer and set a wide gray
border on this layer as our highlight, while placing the layer on the
top layer, This way the border will not conflict with the nearby state
(instead of IE, Opera or Edge).

Next, we’ll define what happens to ``mouseout``:

::

   function resetHighlight(e) {{
       geojson.resetStyle(e.target);
   }}

The convenient geojson.resetStyle method will reset the layer’s style to
the default state (defined by our ``style`` function). To do this, make
sure our GeoJSON layer can be defined by the previous listener
``geojson`` variable access, then assign this GeoJSON layer to
``geojson`` variable:

::

   var geojson;
   // ... our listeners
   geojson = L.geoJson(...);

Let’s define a click listener to zoom in on the state:

::

   function zoomToFeature(e) {{
       map.fitBounds(e.target.getBounds());
   }}

Now we will use the ``onEachFeature`` option to add listeners to the
layers in which the states are located:

::

   function onEachFeature(feature, layer) {{
   layer.on({{
       mouseover: highlightFeature,
       mouseout: resetHighlight,
       click: zoomToFeature
   }});
   }}    
   geojson = L.geoJson(statesData, {{
   style: style,
   onEachFeature: onEachFeature
   }}).addTo(map);

This makes the state on the map stand out when the mouse passes, and
gives us the ability to add other interactive features to the listener.

Custom information control
--------------------------

Usually we use pop-ups to display information, but we now use a
different method - displaying information in a custom control when
hovering over it.

Here is our control code:

::

   var info = L.control();    
   info.onAdd = function (map) {{
   this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
   this.update();
   return this._div;
   }};

   // method that we will use to update the control based on feature properties passed
   info.update = function (props) {{
   this._div.innerHTML = '<h4>US Population Density</h4>' +  (props ?
       '<b>' + props.name + '</b><br />' + props.density + ' people / mi<sup>2</sup>'
       : 'Hover over a state');
   }};    
   info.addTo(map);

When the user mouses over a certain state, we need to update the
controls, so we modify the listener as follows:

::

   function highlightFeature(e) {{
   ...
   info.update(layer.feature.properties);
   }}

   function resetHighlight(e) {{
   ...
   info.update();
   }}

The control needs some CSS style to make it look good:

::

   .info {{
   padding: 6px 8px;
   font: 14px/16px Arial, Helvetica, sans-serif;
   background: white;
   background: rgba(255,255,255,0.8);
   box-shadow: 0 0 15px rgba(0,0,0,0.2);
   border-radius: 5px;
   }}
   .info h4 {{
   margin: 0 0 5px;
   color: #777;
   }}

Custom legend control
---------------------

It’s easier to create a control with a legend because it’s static and
won’t change when the state is hovered. JavaScript code:

::

   var legend = L.control({{position: 'bottomright'}});

   legend.onAdd = function (map) {{

   var div = L.DomUtil.create('div', 'info legend'),
       grades = [0, 10, 20, 50, 100, 200, 500, 1000],
       labels = [];

   // loop through our density intervals and generate a label with a colored square for each interval
   for (var i = 0; i < grades.length; i++) {{
       div.innerHTML +=
           '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
           grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
   }}

   return div;
   }};

   legend.addTo(map);

The CSS style of the control (we also reuse the previously defined
``info`` class):

::

   .legend {{
   line-height: 18px;
   color: #555;
   }}
   .legend i {{
   width: 18px;
   height: 18px;
   float: left;
   margin-right: 8px;
   opacity: 0.7;
   }}

Enjoy results at the top of this page, or on a separate page.
