<template>
  <div class="map-box">
    <div id="cesiumContainer"></div>
  </div>
</template>

<script>
import * as Cesium from "cesium";

export default {
  name: "cesiumContainer",
  mounted() {
    new Cesium.Viewer("cesiumContainer");


  }
};
</script>
