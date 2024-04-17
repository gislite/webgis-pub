<template>

  <div id="mapid" class="absolute"></div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';

  export default {
    name: "demo_8",
    setup() {

      var map = null;
      const initMap = () => {

        map = new maplibregl.Map({
          container: 'mapid',
          style: {
            "version": 8,
            "sources": {
              "raster-tiles": {
                "type": "raster",
                "tiles": ['https://iserver.supermap.io/iserver/services/map-china400/rest/maps/China/zxyTileImage.png?z={z}&x={x}&y={y}'],
                "tileSize": 256
              }
            },
            "layers": [{
              "id": "simple-tiles",
              "type": "raster",
              "source": "raster-tiles",
              "minzoom": 0,
              "maxzoom": 22
            }]
          },
          center: [120.143, 30.236], // 地图初始中心点
          zoom: 3 // 地图初始缩放级别
        });


        map.on('load', () => {
          //导航控件：
          console.log()
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
