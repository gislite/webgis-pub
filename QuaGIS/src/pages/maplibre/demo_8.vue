<template>

  <div id="mapid" class="absolute"></div>
  <div class="calculation-box">
    <p>Draw a polygon using the draw tools.</p>
    <div id="calculated-area"></div>
  </div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';

  import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css'
  import MapboxDraw from '@mapbox/mapbox-gl-draw';

  import turf from 'turf';

  export default {
    name: "demo_8",
    setup() {

      var map = null;
      const draw = new MapboxDraw({
        displayControlsDefault: false,
        controls: {
          polygon: true,
          trash: true
        }
      });
      MapboxDraw.constants.classes.CONTROL_BASE = 'maplibregl-ctrl';
      MapboxDraw.constants.classes.CONTROL_PREFIX = 'maplibregl-ctrl-';
      MapboxDraw.constants.classes.CONTROL_GROUP = 'maplibregl-ctrl-group';
      const initMap = () => {

        map = new maplibregl.Map({
          container: 'mapid',

          style: './data/style.json',
          center: [120.143, 30.236], // 地图初始中心点
          zoom: 3 // 地图初始缩放级别
        });


        map.on('load', () => {
          //导航控件：
          console.log()

          map.addControl(draw);

          map.on('draw.create', updateArea);
          map.on('draw.delete', updateArea);
          map.on('draw.update', updateArea);

          function updateArea(e) {
            const data = draw.getAll();
            const answer = document.getElementById('calculated-area');
            if (data.features.length > 0) {
              console.log(data)
              const area = turf.area(data);
              // restrict to area to 2 decimal points
              const roundedArea = Math.round(area * 100) / 100;
              answer.innerHTML =
                `<p><strong>${
                  roundedArea
                }</strong></p><p>square meters</p>`;
            } else {
              answer.innerHTML = '';
              if (e.type !== 'draw.delete')
                alert('Use the draw tools to draw a polygon!');
            }
          }
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

  .calculation-box {
    height: 75px;
    width: 150px;
    position: absolute;
    bottom: 40vh;
    right: 10vw;
    background-color: rgba(255, 255, 255, 0.9);
    padding: 15px;
    text-align: center;
  }

  p {
    font-family: 'Open Sans';
    margin: 0;
    font-size: 13px;
  }
</style>
