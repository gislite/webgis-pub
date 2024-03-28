<template>
  <div id="mapDiv"></div>
</template>

<script>
import 'ol/ol.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';

export default {
  mounted() {
    const map = new Map({
      target: 'mapDiv',
      layers: [
        new TileLayer({
          source: new OSM()
        })
      ],
      view: new View({
        center: [0, 0],
        zoom: 0
      })
    });
    console.log('map: ', map);
  }
};
</script>

<style scoped>
#mapDiv {
  width: 100%;
  height: 90vh;
}
</style>
