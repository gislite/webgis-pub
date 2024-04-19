<template>

  <div id="mapid" class="absolute"></div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';


  export default {
    name: "demo_10",
    setup: function () {
      let hoveredStateId = null;
      let popup = new maplibregl.Popup(
        {
          closeOnClick: false
        });
      var map = null;
      const initMap = () => {

       const MAPTILER_KEY = 'hAA4PuTSrWhRcIgil5Fy';
        map = new maplibregl.Map({
          container: 'mapid',

        style: `https://api.maptiler.com/maps/basic-v2/style.json?key=${MAPTILER_KEY}`,
          center: [-116.231, 43.604], // starting position [lng, lat]
          zoom: 11 // starting zoom
        });


        map.on('load',  () => {
          map.addSource('off-leash-areas', {
            'type': 'geojson',
            'data':
              './data/boise.geojson'
          });

          map.addLayer({
            'id': 'off-leash-areas',
            'type': 'symbol',
            'source': 'off-leash-areas',
            'layout': {
              'text-field': [
                'format',
                ['upcase', ['get', 'FacilityName']],
                {'font-scale': 0.8},
                '\n',
                {},
                ['downcase', ['get', 'Comments']],
                {'font-scale': 0.6}
              ],
              // 'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
              'text-offset': [0, 0.6],
              'text-anchor': 'top'
            }
          });


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
    top: 0;
    right: 10px;
    height: 80vh;
    width: 100vw
  }
</style>
