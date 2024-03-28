<template>
  <div id="map"></div>
</template>

<script>
import "ol/ol.css";
import { Map, View } from "ol";
import TileLayer from "ol/layer/Tile";
import XYZ from "ol/source/XYZ";

export default {
  data() {
    return {};
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      new Map({
        target: "map",
        layers: [
          new TileLayer({
            source: new XYZ({
              url:
                'http://t4.tianditu.gov.cn/DataServer?T=vec_w&X={x}&Y={y}&L={z}&tk=57f1b8146ef867f14189f3f4bb1adc1c',
            }),
          }),
          new TileLayer({
            source: new XYZ({
              url:
                'http://t4.tianditu.gov.cn/DataServer?T=cia_w&X={x}&Y={y}&L={z}&tk=57f1b8146ef867f14189f3f4bb1adc1c',
            }),
            isGroup: true,
            name: "天地图文字标注",
          }),

        ],
        view: new View({
          projection: "EPSG:4326",
          center: [103.3, 35.5],
          zoom: 4,
        }),
      });
    },
  },
};
</script>

<style lang="scss" scoped>
#map {
  height: 90vh;
  width: 100%;
  margin: 0;
  //   background-color: antiquewhite;
}
</style>
