<template>
  <div id="center_fz8">
  <div
      style="z-index: 100; width: 180px; padding:5px;margin: 5px; height:20vh;background:rgba(50, 50 ,50, 0.8);position: absolute;border-radius: 4px">
    <div class="mouse_content">
      <form style="position: absolute;margin-top: 30px;" class="fonsize">
        <p><b>鼠标位置:</b> {{ this.info_mouse_pos }}</p>
        <p><b>地图中心:</b> {{ this.info_map_center }}</p>
        <p><b>缩放级别:</b> {{ this.info_map_zoom }}</p>
      </form>
    </div>

    </div>
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
  mounted() {
    this.init_leaf();

  },


  data() {
    return {
      map: undefined,
        info_map_center: undefined,
      info_map_zoom: undefined,
      info_mouse_pos: undefined,
    }
  },
  components: {},
  methods: {
    leaf_add(){
      this.soil.addTo(this.map)
    },
    leaf_foo(){
      this.map.removeLayer(this.soil)
    },
    onMapClick(e) {
      this.popup
        .setLatLng(e.latlng)
        .setContent("Location:" + e.latlng.toString())
        .openOn(this.map);
    },


     test_fun2: function () {


      this.info_map_center = this.map.getCenter().lat.toFixed(3) + ',' + this.map.getCenter().lng.toFixed(3);
      this.info_map_zoom = this.map.getZoom();

    },
     test_fun3: function (e) {


      this.info_mouse_pos = e.latlng.lat.toFixed(3) + ',' + e.latlng.lng.toFixed(3);
      this.info_map_zoom = this.map.getZoom();

    },
    init_leaf() {
      //创建地图
      this.map = L.map(this.$refs.map_vkz, {
        center: [47.15, 125.1],
        zoom: 6,
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
      this.map.on('move', this.test_fun2);
      this.map.on('mousemove', this.test_fun3);
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


     this.soil = L.tileLayer.wms('http://tile.igadc.cn/service?', {
        title:'turang',
        layers: 'qn9126',
        format: 'image/png',
        transparent: true,
        backgroundColor: '#0f0f0f',
      });
      this.soil.addTo(this.map)

      L.control.scale({
        position: 'topright',
        maxWidth: '100',
        imperial: false
      }).addTo(this.map);
    },
  }
}
</script>

<style lang="scss" scoped>


#center_fz8 {
  height: 95vh;
    .li_icon_yi {
    width: 100%;
    color: #fff;
    list-style: none;
  }

  .li_icon_yi:hover {
    cursor: pointer;
    color: #5cd9e8;
  }
  .mouse_content{

    padding: 5px;
    border-radius: 4px;
    font-size: 10pt;
    line-height: 16pt;
    color:#fff
  }
}
</style>
