<template>

  <div id="mapid" class="absolute"></div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';

  export default {
    name: "demo_15",
    setup() {

      var map = null;
      const initMap = () => {

        const MAPTILER_KEY = 'hAA4PuTSrWhRcIgil5Fy';
        map = new maplibregl.Map({
          container: 'mapid',

          style:
            `https://api.maptiler.com/maps/streets/style.json?key=${MAPTILER_KEY}`,
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
