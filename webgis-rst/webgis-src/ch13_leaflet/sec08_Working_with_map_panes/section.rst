.. Author: Bu Kun .. Title: Use the map panes

Use the map panes
=================

In Leaflet, map panes can automatically group layers, but developers are
not aware that this allows browsers to process multiple layers more
efficiently, rather than processing one layer at a time.

Map panes uses z-index CSS property Properties to control some layers to
appear on top of other layers. The default order is as follows:

-  ``TileLayer``\ s and ``GridLayer``\ s
-  ``Path``\ s, like lines, polylines, circles, or ``GeoJSON`` layers.
-  ``Marker`` shadows
-  ``Marker`` icons
-  ``Popup``\ s

That’s why in the Leaflet map, popups are displayed on top of other
layers, markers are always displayed on the slice layer, and so on.

Leaflet 1.0.0 has added a new feature (0.7.X not available) to customize
the map panes to adjust the default order.

Default value is not always appropriate
---------------------------------------

In some special cases, the default layer sorting is not always
appropriate. We use the following basemap and an example of a label
layer to explain:

.. raw:: html

   <style>
       .tiles img {{
           border: 1px solid #ccc;
           border-radius: 5px;
       }}
   </style>

.. container:: col-sm-12

   ::

      <div class="col-sm-4">
          <img src="./leaflet_with_map_panes/5_002.png" class="bordered-img"><br>
          Basemap without annotation
      </div>
      <div class="col-sm-4">
          <img src="./leaflet_with_map_panes/5.png" class="bordered-img"><br>
          Transparent label layer
      </div>
      <div class="col-sm-4">
          <img src="./leaflet_with_map_panes/5_002.png" class="bordered-img">
          <img src="./leaflet_with_map_panes/5.png" style="position:absolute; left:0; top:0;"><br>
          Label the layer above the basemap
      </div>

If we add the above basemap and annotation layer to the Leaflet map, any
polygons or markers will appear above the two layers, but it might be
better to have the annotation layer appear on top. How should we achieve
this?

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align: center; border: none">

.. raw:: html

   <iframe src="./leaflet_with_map_panes/example.html" width="616" height="416">

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

Custom panes
------------

For basemaps and overlay layers like GeoJSON, we can use their default
settings, but for annotation layers we need to customize a pane so that
it appears on top of the GeoJSON layer.

Custom map panes are created on top of the original map, so we should
first create a map instance of ``L.Map`` and the panes it needs:

::

   var map = L.map('map');
   map.createPane('labels');

The next step is to set the value of the pane’s z-index. To view the
default values for the pane, set the new pane’s z-index value to 650 to
have the label layer appear below the popups layer above the markers
layer. Use the ``getPane()`` method to get the Html element of the pane
and then modify its z-index value.

::

   map.getPane('labels').style.zIndex = 650;

One of the problems with having the image layer on top of other layers
is that the slice captures events such as clicks or touches. If the user
clicks on an area of the map, the browser will think that the user is
clicking on the image layer instead of the GeoJSON layer or the markup
layer. We can use CSS’s pointer-events property to solve this problem:

::

   map.getPane('labels').style.pointerEvents = 'none';

The new pane has been created, we can add the layer, pay attention to
the ``pane`` option on the label layer:

::

   var positron = L.tileLayer('http://{{s}}.basemaps.cartocdn.com/light_nolabels/{{z}}/{{x}}/{{y}}.png', {{
       attribution: '©OpenStreetMap, ©CartoDB'
   }}).addTo(map);

   var positronLabels = L.tileLayer('http://{{s}}.basemaps.cartocdn.com/light_only_labels/{{z}}/{{x}}/{{y}}.png', {{
       attribution: '©OpenStreetMap, ©CartoDB',
       pane: 'labels'
   }}).addTo(map);

   var geojson = L.geoJson(GeoJsonData, geoJsonOptions).addTo(map);

Finally, add some interactive features to the GeoJSON layer:

::

   geojson.eachLayer(function (layer) {{
   layer.bindPopup(layer.feature.properties.name);
   }});
   map.fitBounds(geojson.getBounds());

This way the example map is complete!
