<template>

  <div id="mapid" class="absolute"></div>
  <q-btn @click="jumpTo(120.143, 30.236,3)" icon="gps_fixed" label="Jump To"/>
  <q-btn @click="zoomIn" icon="add" label="Zoom In"/>
  <q-btn @click="zoomOut" icon="remove" label="Zoom Out"/>
  <q-card class="q-ma-lg bg-blue-1" style="width: 40vw;margin-top: 6vh">
    <q-card-section>
      <div>
        鼠标位置：{{reac_list.mousePosition}}
      </div>
      <div>
        中心点坐标：{{reac_list.mapCenter}}
      </div>
      <div>
        缩放级别：{{reac_list.mapZoom}}
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted, reactive, ref} from "vue";
  import '@supermap/iclient-maplibregl';
  import 'maplibre-gl/dist/maplibre-gl.css';

  export default {
    name: "demo_3",
    setup() {

      var map = null;
      let reac_list = reactive({
        mousePosition: ref([120.143, 30.236]),
        mapCenter: ref([120.143, 30.236]),
        mapZoom: ref(3)
      });
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
          map.on('mousemove', mouseMove)
          map.on('zoom', zoomchange)

        })

      };

      function zoomIn() {
        map.zoomIn()
      }

      function zoomOut() {
        map.zoomOut()
      }

      function jumpTo(lat, lng, zoom) {
        map.jumpTo({
          center: [lat, lng],
          zoom: zoom
        })
      }

      function mouseMove(e) {
        reac_list.mousePosition = e.lngLat
        reac_list.mapZoom = map.getZoom()
        reac_list.mapCenter = map.getCenter()

      }
      function zoomchange(e) {
        reac_list.mapZoom = map.getZoom()
        reac_list.mapCenter = map.getCenter()

      }

      onMounted(() => {
        initMap()

      })


      return {
        zoomIn,
        zoomOut,
        jumpTo,
        reac_list,
      }
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
