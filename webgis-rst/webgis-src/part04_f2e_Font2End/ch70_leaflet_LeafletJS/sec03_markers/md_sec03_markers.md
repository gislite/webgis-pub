; Author: Bu Kun
; Title: Custom callout icon

# Custom callout icon

In this tutorial, you'll learn how to easily tag a map with a custom icon.

<table>
    <tbody>
    <tr>
        <td style="text-align: center; border: none">
            <iframe src="./leaflet_custom_icons/example.html" width="616" height="416"></iframe>
        </td>
    </tr>
    <tr>
        <td style="text-align: center; border: none">
            <small><a href="./leaflet_custom_icons/example.html">Show the example</a></small>
        </td>
    </tr>
    </tbody>
</table>

## Preparing images

In order to make a custom icon, we usually need two images - the actual icon image and its shadow image.
For this tutorial, we used the Leaflet logo and created 4 images -
3 different color blade images and a common shadow image for them:


<img style="border: 1px solid #ccc" src="./leaflet_custom_icons/leaf-green.png">
<img style="border: 1px solid #ccc" src="./leaflet_custom_icons/leaf-red.png">
<img style="border: 1px solid #ccc" src="./leaflet_custom_icons/leaf-orange.png">
<img style="border: 1px solid #ccc" src="./leaflet_custom_icons/leaf-shadow.png">

Note that the white areas in the image are actually transparent. 

## Create icon

The marker icon in the Leaflet is defined by the `L.Icon` object and is used as a parameter option when creating the marker. Let's create a green leaf icon: 

    var greenIcon = L.icon({{
        iconUrl: 'leaf-green.png',
        shadowUrl: 'leaf-shadow.png',

        iconSize:     [38, 95], // size of the icon
        shadowSize:   [50, 64], // size of the shadow
        iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
        shadowAnchor: [4, 62],  // the same for the shadow
        popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
    }});


Now it's easy to put an icon on the map:

    L.marker([51.5, -0.09], {{icon: greenIcon}}).addTo(map);


<table>
    <tbody>
    <tr>
        <td style="text-align: center; border: none">
            <iframe src="./leaflet_custom_icons/example-one-icon.html" width="616" height="416"></iframe>
        </td>
    </tr>
    <tr>
        <td style="text-align: center; border: none">
            <small><a href="./leaflet_custom_icons/example-one-icon.html">View this example</a></small>
        </td>
    </tr>
    </tbody>
</table>

## Define icon class

What if we need to create some icons that have a lot in common? 
Let's define our own icon class, which includes        sharing options. 
It's really easy to inherit Leaflet from the L icon (　`L.Icon`　):
    

    var LeafIcon = L.Icon.extend({{
        options: {{
            shadowUrl: 'leaf-shadow.png',
            iconSize:     [38, 95],
            shadowSize:   [50, 64],
            iconAnchor:   [22, 94],
            shadowAnchor: [4, 62],
            popupAnchor:  [-3, -76]
        }}
    }});

Now we can create these three leaf icons in this class and use them:

    var greenIcon = new LeafIcon({{iconUrl: 'leaf-green.png'}}),
    redIcon = new LeafIcon({{iconUrl: 'leaf-red.png'}}),
    orangeIcon = new LeafIcon({{iconUrl: 'leaf-orange.png'}});

As you may have noticed, we created a leaf icon instance using the keyword `new`. 
So why aren't all Leaflet classes created with it? The answer is
simple: the real Leaflet classes are named with uppercase letters (such as L.Icon), and they also need to use `new` is created, but it is also named with a lowercase letter name
(L.icon), which is created for convenience, such as:

    L.icon = function (options) {{
        return new L.Icon(options);
    }};

You can also do the same thing in class. Ok, let's put the markers for these icons on the map:

    L.marker([51.5, -0.09], {{icon: greenIcon}}).addTo(map).bindPopup("I am a green leaf.");
    L.marker([51.495, -0.083], {{icon: redIcon}}).addTo(map).bindPopup("I am a red leaf.");
    L.marker([51.49, -0.1], {{icon: orangeIcon}}).addTo(map).bindPopup("I am an orange leaf.");

Now open <a href="./leaflet_custom_icons/makericons.html"> the full example </a>.

