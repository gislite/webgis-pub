<template>

  <div id="mapid" class="absolute"></div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';
  import jilingeo from "../../../public/data/jilingeo";


  export default {
    name: "demo_9",
    setup: function () {
      let hoveredStateId = null;
      let popup = new maplibregl.Popup(
        {
          closeOnClick: false
        });
      var map = null;
      const initMap = () => {

        map = new maplibregl.Map({
          container: 'mapid',

          style: './data/style.json',
          center: [126.629423, 43.430018], // 地图初始中心点
          zoom: 5 // 地图初始缩放级别
        });


        map.on('load', () => {
          map.addSource('jilingeo', {
            'type': 'geojson',
            'data': jilingeo
          });


          map.addLayer({
            'id': 'jilin-fill',
            'type': 'fill',
            'source': 'jilingeo',
            'paint': {
              'fill-color': '#888888',
              'fill-opacity': [
                'case',
                ['boolean', ['feature-state', 'hover'], false],
                1,
                0.5
              ]
            }
          });

          map.addLayer({
            'id': 'jilin-borders',
            'type': 'line',
            'source': 'jilingeo',
            'layout': {},
            'paint': {
              'line-color': '#627BC1',
              'line-width': 2
            }
          });


          // When the user moves their mouse over the state-fill layer, we'll update the
          // feature state for the feature under the mouse.
          map.on('mousemove', 'jilin-fill', (e) => {
            if (e.features.length > 0) {
              if (hoveredStateId) {
                map.setFeatureState(
                  {source: 'jilingeo', id: hoveredStateId},
                  {hover: false}
                );
              }
              hoveredStateId = e.features[0].id;
              map.setFeatureState(
                {source: 'jilingeo', id: hoveredStateId},
                {hover: true}
              );
            }
          });

          // When the mouse leaves the state-fill layer, update the feature state of the
          // previously hovered feature.
          map.on('mouseleave', 'jilin-fill', () => {
            if (hoveredStateId) {
              map.setFeatureState(
                {source: 'jilingeo', id: hoveredStateId},
                {hover: false}
              );
            }
            hoveredStateId = null;
          });

          map.on('click', 'jilin-fill', (e) => {
            if (hoveredStateId) {
              if (e.features[0].properties.cityName) {
                popup.setLngLat(e.lngLat)
                  .setHTML(`${e.features[0].properties.cityName} ${e.features[0].properties.Name}`)
                  .addTo(map);
              } else {

                popup.setLngLat(e.lngLat)
                  .setHTML(`${e.features[0].properties.Name}`)
                  .addTo(map);
              }

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
    top: 10vh;
    right: 10px;
    height: 70vh;
    width: 60vw
  }
</style>
