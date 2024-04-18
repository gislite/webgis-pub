<template>

  <div id="mapid" class="absolute"></div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';

  export default {
    name: "demo_7",
    setup() {

      var map = null;
      const initMap = () => {

        map = new maplibregl.Map({
          container: 'mapid',

          style: './data/style.json',
          center: [ 126.82767,43.289783], // 地图初始中心点
          zoom: 5 // 地图初始缩放级别
        });


        map.on('load', () => {
         map.addSource('wms-test-source', {
            'type': 'raster',
            // use the tiles option to specify a WMS tile source URL
            // https://maplibre.org/maplibre-style-spec/sources/
            'tiles': [
              'http://tile.igadc.cn/service?&SERVICE=WMS&REQUEST=GetMap&LAYERS=qn1964&STYLES=&FORMAT=image%2Fpng&TRANSPARENT=true&VERSION=1.3.0&WIDTH=256&HEIGHT=256&CRS=EPSG%3A3857&BBOX={bbox-epsg-3857}'
          ],
            'tileSize': 256
        });
        map.addLayer(
            {
                'id': 'wms-test-layer',
                'type': 'raster',
                'source': 'wms-test-source',
                'paint': {}
            }
        );
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
