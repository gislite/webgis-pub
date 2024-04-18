<template>

  <div id="mapid" class="absolute"></div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';

  export default {
    name: "demo_2",
    setup() {

      var map = null;
      const initMap = () => {

        map = new maplibregl.Map({
          container: 'mapid',

          style: './data/style.json',
          // center: [120.143, 30.236], // 地图初始中心点
          // zoom: 3 // 地图初始缩放级别

        zoom: 12,
        center: [11.39085, 47.27574],
          pitch: 52,
        });


        map.on('load', () => {
          //导航控件：

          map.addControl(new maplibregl.NavigationControl(), 'top-left');
          //比例尺控件：
          map.addControl(new maplibregl.ScaleControl({}));
          //定位：
          map.addControl(new maplibregl.GeolocateControl({}));
          //全屏：
          map.addControl(new maplibregl.FullscreenControl({}));
          //版权：
          map.addControl(new maplibregl.AttributionControl({}));
          //添加水印
          map.addControl(new maplibregl.LogoControl({compact: false}));


          map.addSource('terrainSource', {
            'type': 'raster-dem',
            'url': 'https://demotiles.maplibre.org/terrain-tiles/tiles.json',
            'tileSize': 256
          });
          map.addSource('hillshadeSource', {
            'type': 'raster-dem',
            'url': 'https://demotiles.maplibre.org/terrain-tiles/tiles.json',
            'tileSize': 256
          });
          map.addLayer({
            'id': 'hills',
            'type': 'hillshade',
            'source': 'hillshadeSource',
            'layout': {'visibility': 'visible'},
            'paint': {'hillshade-shadow-color': '#473B24'}
          });
          map.addControl(
            new maplibregl.TerrainControl({
              source: 'terrainSource',
              exaggeration: 1
            }))

        })

      }

      onMounted(() => {
        initMap()

      })


      return {}
    }
  }
</script>

<style scoped>
  #mapid {
    top: 10vh;
    right: 10px;
    height: 70vh;
    width: 60vw
  }
</style>
