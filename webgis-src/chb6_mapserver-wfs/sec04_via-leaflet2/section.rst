======================================
Leaflet render WFS with custom styles
======================================

Example
======================================

WMS completes the task of map rendering by server.
If you want to customize the map style, you can use SLD to transfer the definition file of style to the server.
The server returns the result of the map. The data returned by WFS can be adjusted and rendered by client.



In this case, there is no need to make any changes to the server, the server can only provide data.

On the client side, you can define the implementation style of anonymous functions.

::

    style:function(feature){
        return {
            stroke:true,
            color:'#333333',
            opacity: 1,
            fillOpacity: 0.1,
            fillColor: '#333333',
            weight:1
        }
    },


Example
======================================

.. raw:: html

   <iframe src="./xx-leaflet-wfs2.html" width="100%" height="450" style="border:1px solid">
   </iframe>


`Open the example </xx-leaflet-wfs2.html>`_