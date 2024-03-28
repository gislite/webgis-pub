<template>
  <div id="center_fz8">

    <div ref="map_vkz" style=" width: 84%;
    height: 95vh;
    z-index: 1;
    position: absolute">

    </div>

  </div>

</template>

<script>

import L from 'leaflet';
import "leaflet/dist/leaflet.css";


export default {
// name: 'Test',
  mounted() {
    this.init_leaf();

  },


  data() {
    return {
      map: undefined,
    }
  },
  components: {},
  methods: {
    onMapClick(e) {
      this.popup
        .setLatLng(e.latlng)
        .setContent("Location:" + e.latlng.toString())
        .openOn(this.map);
    },
    onMapZoom() {
      // if (this.map.getZoom() > 9) {
      //   this.map.removeLayer(this.glayer_fusheqv);
      // }
      // if (this.map.getZoom() < 8) {
      //   this.map.addLayer(this.glayer_heituqv);
      //
      // }
      //
      // if (this.map.getZoom() < 9) {
      //
      //   this.map.addLayer(this.glayer_fusheqv);
      // }
    },
    init_leaf() {
      //创建地图
      this.map = L.map(this.$refs.map_vkz, {
        center: [39.73, -104.99],
        zoom: 10,
        crs: L.CRS.EPSG3857,
        maxZoom: 18,
        editable: true,
        // 去除放大缩小控件
        // https://stackoverflow.com/questions/16537326/leafletjs-how-to-remove-the-zoom-control
        zoomControl: false,
        layerControl: false,
        attributionControl: false,
        // Attribution: false,
      });
      this.popup = L.popup();
      this.map.on('click', this.onMapClick);
      this.map.on('zoom', this.onMapZoom);


      // 天地图地图及标示  osm，osm1.
      // this.osm = L.tileLayer('http://t4.tianditu.gov.cn/DataServer?T=vec_w&X={x}&Y={y}&L={z}&tk=57f1b8146ef867f14189f3f4bb1adc1c', {
      //   title: '天地图网格图',
      //   maxZoom: 18,
      //   id: "mapbox.streets"
      // });
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


      // this.osm2.addTo(this.grp_tdt);
      // this.osm1.addTo(this.grp_tdt);
      //

      // this.baseMaps = {
      //   '影像': this.osm2,
      //   // '天地图': this.osm,
      //   // '示范区底图': this.l27,
      //
      // };

      // this.overlayMaps = {};

      // this.grp_background.addTo(this.map);

      this.osm2.addTo(this.map);

      // L.geoJSON(states, {
      //   style: function(feature) {
      //     switch (feature.properties.party) {
      //       case 'Republican': return {color: "#ff0000"};
      //       case 'Democrat':   return {color: "#0000ff"};
      //     }
      //   }
      // }).addTo(this.map);
      //
      // L.geoJSON(someFeatures, {
      //   filter: function(feature, layer) {
      //     return feature.properties.show_on_map;
      //   }
      // }).addTo(this.map);

      var littleton = L.marker([39.61, -105.02]).bindPopup('This is Littleton, CO.'),
        denver    = L.marker([39.74, -104.99]).bindPopup('This is Denver, CO.'),
        aurora    = L.marker([39.73, -104.8]).bindPopup('This is Aurora, CO.'),
        golden    = L.marker([39.77, -105.23]).bindPopup('This is Golden, CO.');
      var cities = L.layerGroup([littleton, denver, aurora, golden]);
      var baseMaps = {
        "OpenStreetMap": this.osm2,
      };

      var overlayMaps = {
        "Cities": cities
      };
      var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(this.map);


      L.control.scale({
        position: 'topright',
        maxWidth: '100',
        imperial: false
      }).addTo(this.map);


      // this.map.on('layeradd', this.show_legend);
    },


  }
}
</script>

<style lang="scss" scoped>


#center_fz8 {
  height: 95vh;
}
</style>
