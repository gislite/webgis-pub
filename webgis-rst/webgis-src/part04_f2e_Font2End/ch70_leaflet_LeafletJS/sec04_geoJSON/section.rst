; Author: Bu Kun ; Title: Use GeoJSON

Use GeoJSON and Leaflet
=======================

GeoJSON is very simple, lightweight, and straightforward. It is becoming
a very popular data format for many GIS technologies and services.
Leaflet is very good at dealing with GeoJSON. In this case, you’ll learn
how to create and interact with a map vector in a GeoJSON object.

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align: center; border: none">

.. raw:: html

   <iframe src="./leaflet_with_geojson/example.html" width="616" height="416">

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

Introduction of GeoJSON
-----------------------

According to the GeJJSON specification (RFC 7946): GeoJSON is a format
for encoding various geographic data structures. GeoJSON objects can
represent geometry, features, or feature sets. GeoJSON supports the
following geometry types: point, line, polygon, multipoint, multiline,
polygon, and geometry. Features in GeoJSON contain a geometric object
and other properties, and a feature set represents a series of features.

Leaflet supports all of the above GeoJSON types, but features and
feature sets perform best because they allow you to describe features
with a set of attributes. We can even use these properties to design our
Leaflet vector. Here’s an example of a simple GeoJSON feature:

::

   var geojsonFeature = {{
       "type": "Feature",
       "properties": {{
           "name": "Coors Field",
           "amenity": "Baseball Stadium",
           "popupContent": "This is where the Rockies play!"
       }},
       "geometry": {{
           "type": "Point",
           "coordinates": [-104.99404, 39.75621]
       }}
   }};

GeoJSON Layer
-------------

GeoJSON objects are added to the map via the GeoJSON layer. To create it
and add it to the map, we can use the following code:

::

   L.geoJSON(geojsonFeature).addTo(map);

GeoJSON objects can also be passed as arrays of valid GeoJSON objects.

::

   var myLines = [{{
       "type": "LineString",
       "coordinates": [[-100, 40], [-105, 45], [-110, 55]]
   }}, {{
       "type": "LineString",
       "coordinates": [[-105, 40], [-110, 45], [-115, 55]]
   }}];

Alternatively, we can create an empty GeoJSON layer and assign it to a
variable so that we can add more features later.

::

   var myLayer = L.geoJSON().addTo(map);
   myLayer.addData(geojsonFeature);

``style`` options
-----------------

The ``style`` option can be used to style in two different ways. First,
we can set the style of all paths (polylines and polygons) in the same
way through a simple object:

::

   var myLines = [{{
       "type": "LineString",
       "coordinates": [[-100, 40], [-105, 45], [-110, 55]]
   }}, {{
       "type": "LineString",
       "coordinates": [[-105, 40], [-110, 45], [-115, 55]]
   }}];

   var myStyle = {{
       "color": "#ff7800",
       "weight": 5,
       "opacity": 0.65
   }};

   L.geoJSON(myLines, {{
       style: myStyle
   }}).addTo(map);

Or, we can use functions to set the style of their various properties.
In the following example, we check the “party” attribute and set our
polygon style accordingly:

::

   var states = [{{
   "type": "Feature",
   "properties": {{"party": "Republican"}},
   "geometry": {{
       "type": "Polygon",
       "coordinates": [[
           [-104.05, 48.99],
           [-97.22,  48.98],
           [-96.58,  45.94],
           [-104.03, 45.94],
           [-104.05, 48.99]
       ]]
   }}
   }}, {{
       "type": "Feature",
       "properties": {{"party": "Democrat"}},
       "geometry": {{
           "type": "Polygon",
           "coordinates": [[
               [-109.05, 41.00],
               [-102.06, 40.99],
               [-102.03, 36.99],
               [-109.04, 36.99],
               [-109.05, 41.00]
           ]]
       }}
   }}];

   L.geoJSON(states, {{
       style: function(feature) {{
           switch (feature.properties.party) {{
               case 'Republican': return {{color: "#ff0000"}};
               case 'Democrat':   return {{color: "#0000ff"}};
           }}
       }}
   }}).addTo(map);

Point Layer（ ``pointToLayer``\ ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Points are treated differently than polylines and polygons. By default,
simple tags are drawn for GeoJSON points. When creating a GeoJSON
coating, we can change this by passing a function in the GeoJSON option
object with ``pointToLayer``. This function passes a ``LatLng`` and
returns an instance of ``ILayer``, which in this case might be
``Marker`` or ``CircleMarker``.

We can also create a circular tag using the ``pointToLayer`` option:

::

   var geojsonMarkerOptions = {{
       radius: 8,
       fillColor: "#ff7800",
       color: "#000",
       weight: 1,
       opacity: 1,
       fillOpacity: 0.8
   }};

   L.geoJSON(someGeojsonFeature, {{
       pointToLayer: function (feature, latlng) {{
           return L.circleMarker(latlng, geojsonMarkerOptions);
       }}
   }}).addTo(map);

We can also set the ``style`` of the property in this example - If you
create a circle-like vector layer inside the pointToLayer function, the
Leaflet is smart enough to apply the style to the GeoJSON point (
``pointToLayer`` ).

onEachFeature
~~~~~~~~~~~~~

The ``onEachFeature`` option is a feature that is called before each
feature is added to the GeoJSON layer. This option is usually used to
attach pop-ups when clicking on a feature.

::

   function onEachFeature(feature, layer) {{
       // does this feature have a property named popupContent?
       if (feature.properties && feature.properties.popupContent) {{
           layer.bindPopup(feature.properties.popupContent);
       }}
   }}

   var geojsonFeature = {{
       "type": "Feature",
       "properties": {{
           "name": "Coors Field",
           "amenity": "Baseball Stadium",
           "popupContent": "This is where the Rockies play!"
       }},
       "geometry": {{
           "type": "Point",
           "coordinates": [-104.99404, 39.75621]
       }}
   }};

   L.geoJSON(geojsonFeature, {{
       onEachFeature: onEachFeature
   }}).addTo(map);

Filter（ ``filter``\ ）
~~~~~~~~~~~~~~~~~~~~~~~

This filter option can be used to control the visibility of GeoJSON
functionality. To do this, we set the filter option through a function.
This function is called by each element in the GeoJSON layer and passes
the feature and layer. You can then use the value in this property to
control the visibility false by returning true or.

In the example below, “Busch Field” will not be displayed on the map.

::

   var someFeatures = [{{
   "type": "Feature",
   "properties": {{
       "name": "Coors Field",
       "show_on_map": true
   }},
   "geometry": {{
       "type": "Point",
       "coordinates": [-104.99404, 39.75621]
   }}
   }}, {{
       "type": "Feature",
       "properties": {{
           "name": "Busch Field",
           "show_on_map": false
       }},
       "geometry": {{
           "type": "Point",
           "coordinates": [-104.98404, 39.74621]
       }}
   }}];

   L.geoJSON(someFeatures, {{
       filter: function(feature, layer) {{
           return feature.properties.show_on_map;
       }}
   }}).addTo(map);
