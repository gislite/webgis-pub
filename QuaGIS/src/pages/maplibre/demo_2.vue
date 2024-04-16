<template>

  <div id="mapid" class="absolute"></div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";
import '@supermap/iclient-maplibregl';
import 'maplibre-gl/dist/maplibre-gl.css';
  export default {
    name: "demo_2",
    setup() {

      var map = null;
      const initMap = () => {
        var attribution = "<a href='https://maplibre.org/' target='_blank'>© MapLibre </a>" +
          " with <span>© <a href='https://iclient.supermap.io' target='_blank'>SuperMap iClient</a> | </span>" +
          " Map Data <span>© <a href='http://support.supermap.com.cn/product/iServer.aspx' target='_blank'>SuperMap iServer</a></span> ";

        map = new maplibregl.Map({
          container: 'mapid',
          style: {
            "version": 8,
            "sources": {
              "raster-tiles": {
                "attribution": attribution,
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

          map.addControl(new maplibregl.NavigationControl(), 'top-left');
          //比例尺控件：
          map.addControl(new maplibregl.ScaleControl({}));
          //定位：
          map.addControl(new maplibregl.GeolocateControl({}));
          //全屏：
          map.addControl(new maplibregl.FullscreenControl({}));
          //版权：
          map.addControl(new maplibregl.AttributionControl({}));
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
