Intruduction for OpenLayers 2
======================================================

Intruduction for OpenLayers.

Technical overview
OpenLayers is a JavaScript package for developing WebGIS clients.
Sources supported by OpenLayers include Google Maps, Yahoo, Map, Microsoft Virtual Earth, etc. Users can also use a simple image map as a background image to overlay other layers in OpenLayers. In this regard, OpenLayers provides a lot of s Choice.

The code implements the function of loading a tile map (ie OpenStreetMap map) and can pan and zoom the map.
When initializing a map, you need at least one view, one or more layers, and a target HTML tag for the map to load.



The Second.

.. raw:: html

    <link rel="stylesheet" href="https://www.osgeo.cn/static/f2elib/ol-7.4.x/ol.css" type="text/css">
    <!--导入最新版本ol的js文件。-->
	<script src="https://www.osgeo.cn/static/f2elib/ol-7.4.x/dist/ol.js"></script>
    <div id="olmap" class="olmap" style="height: 400px; width: 100%"></div>
    <script>
    //layers、target、view是地图最基本的部分，是必需的
    //初始换Map对象，显示地图。
    var olmap = new ol.Map({
        //在地图容器中加载地图
        layers: [
            new ol.layer.Tile({				// 加载瓦片图层数据
                source: new ol.source.OSM()		// 图层对应的数据源，此处加载OpenStreetMap在线瓦片服务数据
            })
        ],
        target: 'olmap',						// 地图容器div层的id值
        controls: ol.control.defaults({		 // 设置地图控件，collapsible控件不显示。
            attributionOptions: {
                collapsible: false
            }
        }),
        //表示显示简单的2D视图地图。
        view: new ol.View({
            center: [0, 0],	//地图初始中心点
            zoom: 2			//地图初始显示级别为2
        })
    });
    var lonLat = new OpenLayers.LonLat( -0.1279688 ,51.5077286 )
     .transform(
       new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
       map.getProjectionObject() // to Spherical Mercator Projection
     );

    var zoom=16;

    var markers = new OpenLayers.Layer.Markers( "Markers" );
    map.addLayer(markers);

    markers.addMarker(new OpenLayers.Marker(lonLat));

    olmap.setCenter (lonLat, zoom);
    </script>