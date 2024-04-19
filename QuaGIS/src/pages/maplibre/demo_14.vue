<template>

  <div id="mapid" class="absolute"></div>
  <div class="map-overlay top">
    <div class="map-overlay-inner">
        <fieldset>
            <label>Select layer</label>
            <select id="layer" name="layer">
                <option value="water">Water</option>
                <option value="building-3d">Buildings</option>
            </select>
        </fieldset>
        <fieldset>
            <label>Choose a color</label>
            <div id="swatches"></div>
        </fieldset>
    </div>
</div>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';

  export default {
    name: "demo_14",
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
   const swatches = document.getElementById('swatches');
    const layer = document.getElementById('layer');
    const colors = [
        '#ffffcc',
        '#a1dab4',
        '#41b6c4',
        '#2c7fb8',
        '#253494',
        '#fed976',
        '#feb24c',
        '#fd8d3c',
        '#f03b20',
        '#bd0026'
    ];

    colors.forEach((color) => {
        const swatch = document.createElement('button');
        swatch.style.backgroundColor = color;
        swatch.addEventListener('click', () => {
            map.setPaintProperty(
                layer.value,
                layer.value === 'water' ? 'fill-color' : 'fill-extrusion-color',
                color
            );
        });
        swatches.appendChild(swatch);
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
   .map-overlay {
        font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
        position: absolute;
        width: 200px;
        top: 0;
        right: 0;
        padding: 10px;
    }

    .map-overlay .map-overlay-inner {
        background-color: #fff;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        border-radius: 3px;
        padding: 10px;
        margin-bottom: 10px;
    }

    .map-overlay-inner fieldset {
        border: none;
        padding: 0;
        margin: 0 0 10px;
    }

    .map-overlay-inner fieldset:last-child {
        margin: 0;
    }

    .map-overlay-inner select {
        width: 100%;
    }

    .map-overlay-inner label {
        display: block;
        font-weight: bold;
        margin: 0 0 5px;
    }

    .map-overlay-inner button {
        display: inline-block;
        width: 36px;
        height: 20px;
        border: none;
        cursor: pointer;
    }

    .map-overlay-inner button:focus {
        outline: none;
    }

    .map-overlay-inner button:hover {
        box-shadow: inset 0 0 0 3px rgba(0, 0, 0, 0.1);
    }
</style>
