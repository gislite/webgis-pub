.. Author: Bu Kun .. Title: Use LeafletJS for the first time

Introduction to Leaflet
=======================

Leaflet is an open source JavaScript library for mobile rendering of
interactive maps. Its design philosophy is efficient, lightweight and
practical. It is only about 38KB in size, but it has the map
manipulation capabilities that most developers need and can work on
common desktop and mobile platforms. Has an extensible plug-in system,
clear and readable code, and elegance documentation and easy-to-operate
API.

Brief introduction
------------------

Leaflet is a modern, open source JavaScript library developed to build
interactive maps for mobile devices. The code is only 33 KB, but it has
most of the functions of developing online maps. Leaflet design adheres
to the philosophy of simplicity, high performance and good usability. It
works efficiently on all major desktop and mobile platforms, taking
advantage of HTML5 and CSS3 in modern browsers, while also supporting
access to older browsers. Support for plug-in extensions, with a
friendly, easy-to-use API documentation and a simple, readable source
code. Leaflet’s powerful open source library plug-in involves all
aspects of map applications, including map services. There are more than
140 plug-ins for data provision, data format, geocoding, route and route
search, map controls and interactions. These controls enrich the
functions of leaflet, at the same time, it is very convenient to
implement custom controls with good expansibility.

Leaflet getting started Guid
----------------------------

This step-by-step guide gives you a quick understanding of the basics of
leaflet, including building leaflet maps, using tags, multilines and
pop-up windows, and handling events.

.. raw:: html

   <table>
   <tbody>
   <tr>
   <td style="text-align: center; border: none">
   <iframe src="http://webgis.pub/leaflet_quickstart/example.html" width="616" height="416">
   </iframe>
   </td>
   </tr>
   <tr>
   <td style="text-align: center; border: none">
   View this example
   </td>
   </tr>
   </tbody>
   </table>


Prepare the page
----------------

Before you write the map code, you need to do the following on the page:

On the page ``<head>`` Label vs. ``</head>`` Add the following code
between the tags:

::

   <link rel="stylesheet" href="/f2elib/leaflet-1.8.0/leaflet.css"
   integrity="sha512-puBpdR0798OZvTTbP4A8Ix/l+A4dHDD0DGqYW6RQ+9jxkRFclaxxQb/SJAWZfWAkuyeQUytO7+7N4QKrDh+drA=="
   crossorigin=""/>
   <!-- Make sure to place leaflet.js after leaflet.css . -->
   <script src="/f2elib/leaflet-1.8.0/leaflet.js"
   integrity="sha512-nMMmRyTVoLYqjP9hrbed9S+FzjZHW5gY1TWCHA5ckwXZBadntCNs8kEqAWdrb9O7rxbCaA4lKTIWjDXZxflOcA=="
   crossorigin=""></script>

Create a map where you want to create a map with a ``id`` Of ``div`` .

::

   <div id="mapid"></div>

Make sure the map has a clear height, such as defined in CSS:

::

   #mapid {{ height: 180px; }}

Now that the map has been initialized, you are ready to do something
with it.

Create a map
------------

.. raw:: html

   <table>
   <tbody>
   <tr>
   <td style="text-align: center; border: none">
   <iframe src="http://webgis.pub/leaflet_quickstart/example-basic.html" width="616" height="416">
   </iframe>
   </td>
   </tr>
   <tr>
   <td style="text-align: center; border: none">
   View this example
   </td>
   </tr>
   </tbody>
   </table>

1.Initialize the map and set its view to the geographic coordinates and
zoom level we selected：

::

   var mymap = L.map('mapid').setView([51.505, -0.09], 13);

By default (because we didn’t set any parameters when we created the map
instance), all mouse events and touch interactions on the map are turned
on, and it has zoom and property controls.

2. Show the map:

::

   L.tileLayer('https://api.tiles.mapbox.com/v4/{{id}}/{{z}}/{{x}}/{{y}}.png?access_token={{accessToken}}', {{
       attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
       maxZoom: 18,
       id: 'mapbox.streets',
       accessToken: 'your.mapbox.access.token'
   }}).addTo(mymap);

Make sure that all the code is used to display the map ``div`` And
``leaflet.js`` Called after containing.

Dot mark, circle mark, and polygon mark
---------------------------------------

.. raw:: html

   <table>
   <tbody>
   <tr>
   <td style="text-align: center; border: none">
   <iframe src="http://webgis.pub/leaflet_quickstart/example-overlays.html" width="616" height="416">
   </iframe>
   </td>
   </tr>
   <tr>
   <td style="text-align: center; border: none">
   View this example
   </td>
   </tr>
   </tbody>
   </table>

In addition to tiles, you can easily add other things to your map,
including markers, broken lines, polygons, circles and pop-ups. Let’s
add a tag:

::

   var marker = L.marker([51.5, -0.09]).addTo(mymap);

Add a circle tag:

::

   var circle = L.circle([51.508, -0.11], {{
       color: 'red',
       fillColor: '#f03',
       fillOpacity: 0.5,
       radius: 500
   }}).addTo(mymap);

Adding polygon tags is equally simple:

::

   var polygon = L.polygon([
       [51.509, -0.08],
       [51.503, -0.06],
       [51.51, -0.047]
   ]).addTo(mymap);

Use pop-up window
-----------------

.. raw:: html

   <table>
   <tbody>
   <tr>
   <td style="text-align: center; border: none">
   <iframe src="http://webgis.pub/leaflet_quickstart/example-popups.html" width="616" height="416">
   </iframe>
   </td>
   </tr>
   <tr>
   <td style="text-align: center; border: none">
   View this example
   </td>
   </tr>
   </tbody>
   </table>

Pop-up windows are usually used to attach some information to specific
objects on a map. Leaflet has a very simple way to do this:

::

   marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
   circle.bindPopup("I am a circle.");
   polygon.bindPopup("I am a polygon.");

Try to click on our object. The bindPopup method appends a pop-up window
with the specified HTML content to the tag, so when you click an object,
the pop-up window appears, and the openPopup method (for markup only)
immediately opens the attached pop-up window.

You can also set the pop-up window as a layer (when you need more
instead of attaching a pop-up window to an object):

::

   Var popup = L.popup ()
       .setLatLng([51.5, -0.09])
       .setContent("I am a standalone popup.")
       .openOn(mymap);

Here we use ``openOn`` Instead of ``addTo`` Because it handles the
automatic closure of previously opened pop-up windows when it opens a
new pop-up window, which enhances usability.

Deal with events
----------------

Every time something happens in Leaflet, such as when a user clicks a
marker or a map zoom change, the corresponding object sends an event
that you can handle through a function that allows you to react to user
interaction:

::

   function onMapClick(e) {{
       alert("You clicked the map at " + e.latlng);
   }}
   mymap.on('click', onMapClick);

Each object has its own set of events, and the first parameter of the
listener function is the event object, which contains useful information
about the events that occur. For example, the MAP click event object (e
in the example above) has the latlng property, and the latlng property
is where the click occurs.

Let’s improve our example by using pop-ups instead of alert:

::

   var popup = L.popup();
   function onMapClick(e) {{
       popup
           .setLatLng(e.latlng)
           .setContent("You clicked the map at " + e.latlng.toString())
           .openOn(mymap);
   }}
   mymap.on('click', onMapClick);

Try clicking on the map and you will see the coordinates in the pop-up
window. Check out the complete example:

Show the example
