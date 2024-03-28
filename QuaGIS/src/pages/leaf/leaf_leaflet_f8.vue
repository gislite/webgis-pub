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
        center: [37.8, -96],
        zoom: 4,
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
      this.osm2.addTo(this.map);

      var imageUrl = 'https://maps.lib.utexas.edu/maps/historical/newark_nj_1922.jpg';
      var errorOverlayUrl = 'https://cdn-icons-png.flaticon.com/512/110/110686.png';
      var altText = 'Image of Newark, N.J. in 1922. Source: The University of Texas at Austin, UT Libraries Map Collection.';
      var latLngBounds = L.latLngBounds([[40.799311, -74.118464], [40.68202047785919, -74.33]]);

      var imageOverlay = L.imageOverlay(imageUrl, latLngBounds, {
        opacity: 0.8,
        errorOverlayUrl: errorOverlayUrl,
        alt: altText,
        interactive: true
      }).addTo(this.map);
      L.rectangle(latLngBounds).addTo(this.map);
      this.map.fitBounds(latLngBounds);


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
