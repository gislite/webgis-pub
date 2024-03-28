<template>
  <div id="wind">

    <div ref="map_vkz" style=" width: 84%;
    height: 95vh;
    z-index: 1;
    position: absolute">

    </div>

  </div>

</template>

<script>

import "leaflet/dist/leaflet.css";
import "leaflet-velocity/dist/leaflet-velocity.css";
import L from "leaflet";
import velocityLayer from "leaflet-velocity/dist/leaflet-velocity";

import watergbr from '../js/water-gbr.json';
import windgbr from '../js/wind-gbr.json';
import windglobal from '../js/wind-global.json'

export default {


  mounted() {

    this.begin_wind();

  },


  data() {
    return {
      map: undefined,
      watergbr: watergbr,
      windgbr: windgbr,
      windglobal: windglobal,
    }
  },
  components: {},
  methods: {

    get_wind(){
      // 天地图地图及标示  osm，osm1.
      this.osm = L.tileLayer('http://t4.tianditu.gov.cn/DataServer?T=vec_w&X={x}&Y={y}&L={z}&tk=57f1b8146ef867f14189f3f4bb1adc1c', {
        title: '天地图网格图',
        maxZoom: 18,
        id: "mapbox.streets"
      });
      this.osm1 = L.tileLayer('http://t4.tianditu.gov.cn/DataServer?T=cia_w&X={x}&Y={y}&L={z}&tk=57f1b8146ef867f14189f3f4bb1adc1c', {
        title: '天地图中文标注',
        maxZoom: 18,
        id: "mapbox.streets"
      });

      this.osm2 = L.tileLayer('http://t4.tianditu.gov.cn/DataServer?T=img_w&X={x}&Y={y}&L={z}&tk=57f1b8146ef867f14189f3f4bb1adc1c', {
        title: '影像',
        maxZoom: 18,
        id: "mapbox.streets"
      });
        var Esri_WorldImagery = L.tileLayer(
          "http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
          {
            attribution:
              "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, " +
              "AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"
          }
        );

        var Esri_DarkGreyCanvas = L.tileLayer(
          "http://{s}.sm.mapstack.stamen.com/" +
          "(toner-lite,$fff[difference],$fff[@23],$fff[hsl-saturation@20])/" +
          "{z}/{x}/{y}.png",
          {
            attribution:
              "Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, " +
              "NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community"
          }
        );

        var baseLayers = {
          Satellite: this.osm2,
          "Grey Canvas": this.osm1
        };

        var map = L.map(this.$refs.map_vkz, {
          layers: [this.osm2]
        });

        var layerControl = L.control.layers(baseLayers);
        layerControl.addTo(map);
        map.setView([-22, 150], 5);

        return {
          map: map,
          layerControl: layerControl
        };

    },
    begin_wind(){
      var mapStuff = this.get_wind();
      var map = mapStuff.map;
      var layerControl = mapStuff.layerControl;
      this.get_windgbr(this.windgbr,layerControl)
      this.get_wind_global(this.windglobal,layerControl,map)
      this.get_water(this.watergbr,layerControl)

    },
    get_windgbr(data,layerControl) {
      var velocityLayer = L.velocityLayer({
        displayValues: true,
        displayOptions: {
          velocityType: "GBR Wind",
          position: "bottomleft",
          emptyString: "No wind data",
          showCardinal: true
        },
        data: data,
        maxVelocity: 10      });

      layerControl.addOverlay(velocityLayer, "Wind - Great Barrier Reef");

    },
    get_wind_global(data,layerControl,map) {
      var velocityLayer = L.velocityLayer({
        displayValues: true,
        displayOptions: {
          velocityType: "Global Wind",
          position: "bottomleft",
          emptyString: "No wind data"
        },
        data: data,
        maxVelocity: 15
      });
      map.addLayer(velocityLayer)
      layerControl.addOverlay(velocityLayer, "Wind - Global");
    },

    get_water(data,layerControl) {
      var velocityLayer = L.velocityLayer({
        displayValues: true,
        displayOptions: {
          velocityType: "GBR Water",
          position: "bottomleft",
          emptyString: "No water data"
        },
        data: data,
        maxVelocity: 0.6,
        velocityScale: 0.1 // arbitrary default 0.005
      });

      layerControl.addOverlay(velocityLayer, "Ocean Current - Great Barrier Reef");
    },

  }
}
</script>

<style lang="scss" scoped>


#wind {
  height: 95vh;
}
</style>
