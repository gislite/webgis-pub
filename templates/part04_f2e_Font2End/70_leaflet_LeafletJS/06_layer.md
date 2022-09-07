; Author: Bu Kun
; Title: Layer group and layer control

# Layer group and layer control

This tutorial shows you how to combine multiple layers into a set of layers
and how to use layer controls to allow users to easily switch between different layers on the map.

<table>
    <tbody>
    <tr> <td style="text-align: center; border: none">
            <iframe src="./leaflet_layer_control/example.html" width="616" height="416"></iframe>
    </td> </tr>
    <tr> <td style="text-align: center; border: none">
            <small><a href="./leaflet_layer_control/example.html">Show the example</a></small>
     </td> </tr>
    </tbody>
</table>

## Layer group

Suppose you have a bunch of layers, and you want to combine them in your code to handle them:

```
var littleton = L.marker([39.61, -105.02]).bindPopup('This is Littleton, CO.'),
denver    = L.marker([39.74, -104.99]).bindPopup('This is Denver, CO.'),
aurora    = L.marker([39.73, -104.8]).bindPopup('This is Aurora, CO.'),
golden    = L.marker([39.77, -105.23]).bindPopup('This is Golden, CO.');
```


Instead of adding them directly to the map, you can use the LayerGroup class to do the following:

```
var cities = L.layerGroup([littleton, denver, aurora, golden]);
```


Easy enough! Now you have a `cities` layer that merges your city logos into one layer 
so you can add or remove them from the map right away.


## Layer control

Leaflet is a nice little control that allows users to control the layers they see on the map. 
In addition to showing you how to use it, we'll show you another convenient use of layer groups.


There are two types of layers:

(1) mutually exclusive base layers (only one can be seen at a time on the map), for example, tile layers, and 

(2) overlay layers, which are all placed on the base layer.

Other content. 
In this example, we want to have two base layers (grayscale and color base maps) to switch, 
and an overlay layer (the city markers we created earlier) to switch and close.

Now let's create the base layer and add the default layer to the map:

```
var grayscale = L.tileLayer(mapboxUrl, {{id: 'MapID', attribution: mapboxAttribution}}),
streets   = L.tileLayer(mapboxUrl, {{id: 'MapID', attribution: mapboxAttribution}});

var map = L.map('map', {{
center: [39.73, -104.99],
zoom: 10,
layers: [grayscale, cities]
}});
```


Next, we create two objects. 
One contains our base layer and one contains our overlay layer.
These are just simple objects with key/value pairs. 
The key sets the text of the layer in the control (for example "Streets"), 
and the corresponding value is the opposite layer (for example, `streets` ).

```
var baseMaps = {{
"Grayscale": grayscale,
"Streets": streets
}};

var overlayMaps = {{
"Cities": cities
}};
```

Now, just create a layer control and add it to the map. 
The first parameter passed when the layer control is created is the base layer object, 
and the second parameter is the overlay object. 
Both of these parameters are optional: when the second argument is omitted, you can only pass the base layer object, 
or pass null as the first argument if you only want to pass the overlay object. 
In either case, the omitted layer type will not appear for the user to select.

```
L.control.layers(baseMaps, overlayMaps).addTo(map);
```

Notice that we added the `grayscale` layer and `cities` layer, but no `streets`. 
Layer control is smart enough to detect which layers we have added and set the corresponding radio buttons and checkboxes.

Also note that when using multiple base layers, you only need to add one of them to the map when instantiating,
but all of these base layer objects should exist when you create a layer control.

Finally, when you define an object for a layer, you can define a style for the object's keys.
For example, this code will make the grayscale map's labels gray:

```
var baseMaps = {{
"<span style='color: gray'>Grayscale</span>": grayscale,
"Streets": streets
}};
```

Now let's take a separate page <a href="./leaflet_layer_control/example.html">View results→</a>

