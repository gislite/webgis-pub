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
        center: [51.505, -0.09],
        crs: L.CRS.EPSG3857,
        zoom: 13,
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


      var circle = L.circle([51.508, -0.11], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: 500
      }).addTo(this.map);

      var polygon = L.polygon([
        [51.509, -0.08],
        [51.503, -0.06],
        [51.51, -0.047]
      ]).addTo(this.map);


      var marker = L.marker([51.5, -0.09]).addTo(this.map);

      marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
      circle.bindPopup("I am a circle.");
      polygon.bindPopup("I am a polygon.");



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
