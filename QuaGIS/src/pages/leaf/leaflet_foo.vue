<template>
  <div id="center_fz8">

    <div style="z-index: 100; float: right;width: 200px; padding:5px;margin: 5px; height:95vh;background:rgba(50, 50 ,50, 0.8);position: absolute;border-radius: 4px">
      <form>
        <fieldset style="border: none;">
          <ul>
            <li v-on:click.stop.prevent="leaf_foo3()" class="li_icon_yi">
              <i class="iconfont icon-map-marker-alt"/>
              查看黑土区视图
            </li>
            <li v-on:click.stop.prevent="leaf_foo2()" class="li_icon_yi">
              放大
            </li>
            <li v-on:click.stop.prevent="leaf_foo1()" class="li_icon_yi">
              缩小
            </li>
          </ul>
        </fieldset>
      </form>
      <hr style="margin-top: .1rem; margin-bottom: .1rem"/>
      <form action="">

        <p style="color: #fff;font-size: 18px">
            图层与标注
          </p>

        <fieldset style="border: none;color: #fff">

          <label>

            <input name="Fruit" class="switch" type="checkbox" ref="lyr1" id="lyr1" value="lyr1"
                   v-on:change="swich_lyr_1()"
                   checked="checked"/> 野外台站
          </label>
          <label class="icon_tab">

            <input name="Fruit" class="switch" type="checkbox" ref="i1" id="i1" value="i1" v-on:change="filterMedia()"/>
            标注
          </label>

          <label>

            <input class="switch" name="Fruit" type="checkbox" ref="lyr2" id="lyr2" value="lyr2"
                   v-on:change="swich_lyr_2()"
                   checked="checked"/> 示范地块
          </label>
          <label class="icon_tab">

            <input class="switch" name="Fruit" type="checkbox" ref="i2" id="i2" value="i2"
                   v-on:change="filterMedia2()"/> 标注
          </label>
          <label>

            <input class="switch" name="Fruit" type="checkbox" ref="i3" id="i3" value="i3"
                   v-on:change="filterMedia3()"/> 标注观测设备
          </label>

          <label>

            <input class="switch" name="jiankong" type="checkbox" ref="i4" id="i4" value="i4"
                   v-on:change="filterMedia4()"/> 标注监控设备
          </label>
          <label>

            <input class="switch" name="jichudili" type="checkbox" ref="i5" id="i5" value="i5"
                   v-on:change="filterMedia5()"/> 基础地理
          </label>
<!--          <label>-->

<!--            <input class="switch" name="dimaoleixing" type="checkbox" ref="i6" id="i6" value="i6"-->
<!--                   v-on:change="filterMedia6()"/> 地貌类型-->
<!--          </label>-->
<!--          <label>-->

<!--            <input class="switch" name="tudiliyong" type="checkbox" ref="i7" id="i7" value="i7"-->
<!--                   v-on:change="filterMedia7()"/> 土地利用-->
<!--          </label>-->
<!--          <label>-->

<!--            <input class="switch" name="rurangleixing" type="checkbox" ref="i8" id="i8" value="i8"-->
<!--                   v-on:change="filterMedia8()"/> 土壤类型-->
<!--          </label>-->
<!--          <label>-->

<!--            <input class="switch" name="zhibeileixing" type="checkbox" ref="i9" id="i9" value="i9"-->
<!--                   v-on:change="filterMedia9()"/> 植被类型-->
<!--          </label>-->

        </fieldset>
      </form>
      <hr style="margin-top: .1rem; margin-bottom: .1rem"/>

      <form>

          <p style="color: #fff;font-size: 18px">

            快速定位
          </p>


        <fieldset style="border: none;">
          <span v-on:click.stop.prevent="leaf_todikuai([46.78392, 126.561944], 8,'A')"
                class="btn btn-primary btn-sm" :class="{activity:value==='A'}">海伦示范区</span>

          <!--          <label>&ndash;&gt;></label>-->
          <span v-on:click.stop.prevent="leaf_todikuai([47.399397, 126.78193], 12,'B')"
                class="btn btn-info btn-sm icon_tab" :class="{activity:value==='B'}">
            地块1 </span>
          <p/>
          <span v-on:click.stop.prevent="leaf_todikuai([46.48605, 131.876014], 8,'C')"
                class="btn btn-primary btn-sm" :class="{activity:value==='C'}">三江示范区</span>

          <!--          <label>&ndash;&gt;></label>-->
          <!--          <label v-on:click.stop.prevent="leaf_todikuai([46.3609, 130.5488], 14)"-->
          <!--                 class="btn btn-primary btn-sm">地块1 </label>-->
          <span v-on:click.stop.prevent="leaf_todikuai([46.7648, 131.8091], 12,'D')"
                class="btn btn-info btn-sm icon_tab" :class="{activity:value==='D'}">
            地块1 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([47.7921, 134.0867], 13,'E')"
                class="btn btn-info btn-sm" :class="{activity:value==='E'}">
            地块2 </span>
          <p/>
          <span v-on:click.stop.prevent="leaf_todikuai([43.686378, 125.460258], 8,'F')"
                class="btn btn-primary btn-sm" :class="{activity:value==='F'}">长春示范区</span>

          <!--          <label>&ndash;&gt;></label>-->
          <span v-on:click.stop.prevent="leaf_todikuai([44.090789, 125.13977], 13,'G')"
                class="btn btn-info btn-sm icon_tab" :class="{activity:value==='G'}">
            农安 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([43.600551, 124.881926], 13,'H')"
                class="btn btn-info btn-sm" :class="{activity:value==='H'}">
            公主岭 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([43.299373, 124.436047], 14,'I')"
                class="btn btn-info btn-sm" :class="{activity:value==='I'}">
            梨树 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([42.899713, 125.435896], 14,'J')"
                class="btn btn-info btn-sm" :class="{activity:value==='J'}">
            辽河源 </span>
          <p/>
          <span v-on:click.stop.prevent="leaf_todikuai([45.208696, 123.762741], 8,'K')"
                class="btn btn-primary btn-sm" :class="{activity:value==='K'}">大安示范区</span>


          <!--          <label>&ndash;&gt;></label>-->
          <span v-on:click.stop.prevent="leaf_todikuai([45.5846, 123.8997], 13,'L')"
                class="btn btn-info btn-sm icon_tab" :class="{activity:value==='L'}">
            大安站 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([45.25048, 123.440049], 12,'M')"
                class="btn btn-info btn-sm" :class="{activity:value==='M'}">
            牛心套保 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([45.3434, 122.2834], 14,'N')"
                class="btn btn-info btn-sm" :class="{activity:value==='N'}">
            圣一基地 </span>
          <!--          <label v-on:click.stop.prevent="leaf_todikuai([45.5618, 123.0848], 14)" class="btn btn-primary btn-sm">-->
          <!--            洮北基地 </label>-->
          <span v-on:click.stop.prevent="leaf_todikuai([44.551, 123.526], 15,'O')"
                class="btn btn-info btn-sm" :class="{activity:value==='O'}">
            长岭 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([46.087281,  123.926296],13,'P')"
                class="btn btn-info btn-sm" :class="{activity:value==='P'}">
            好雨农业 </span>
          <p/>

          <span v-on:click.stop.prevent="leaf_todikuai([42.277216, 123.25023], 8,'Q')"
                class="btn btn-primary btn-sm" :class="{activity:value==='Q'}">沈阳示范区</span>

          <!--          <label>&ndash;&gt;></label>-->
          <span v-on:click.stop.prevent="leaf_todikuai([42.127702, 121.74589],14,'R')"
                class="btn btn-info btn-sm icon_tab" :class="{activity:value==='R'}">
            地块1 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([42.056112, 123.286129], 13,'S')"
                class="btn btn-info btn-sm" :class="{activity:value==='S'}">
            地块2 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([42.7078, 123.8414], 14,'T')"
                class="btn btn-info btn-sm" :class="{activity:value==='T'}">
            地块3 </span>
          <span v-on:click.stop.prevent="leaf_todikuai([42.801824, 123.963247], 14,'U')"
                class="btn btn-info btn-sm" :class="{activity:value==='U'}">
            地块4 </span>
          <p/>
          <span v-on:click.stop.prevent="leaf_todikuai([48.456056, 121.363088], 8,'V')"
                class="btn btn-primary btn-sm" :class="{activity:value==='V'}">大河湾示范区</span>

          <!--          <label>&ndash;&gt;></label>-->
          <span v-on:click.stop.prevent="leaf_todikuai([47.803842, 123.084146], 12,'W')"
                class="btn btn-info btn-sm icon_tab" :class="{activity:value==='W'}">
            地块1 </span>
          <p/>

          <span v-on:click.stop.prevent="leaf_todikuai([47.663056, 124.461233], 8,'X')"
                class="btn btn-primary btn-sm" :class="{activity:value==='X'}">齐齐哈尔示范区</span>

          <!--          <label>&ndash;&gt;></label>-->
          <span v-on:click.stop.prevent="leaf_todikuai([47.274367, 123.685864], 15,'Y')"
                class="btn btn-info btn-sm icon_tab" :class="{activity:value==='Y'}">
            地块1 </span>
          <p/>
        </fieldset>

      </form>
    </div>


    <div
      style="z-index: 100; float: right;width: 200px;height: 910px; padding:5px;margin: 5px; right: 15px;background:rgba(50, 50 ,50, 0.8);position: absolute;border-radius: 4px; font-size: 10pt;line-height: 16pt;">
      <div style="height: 750px">
        <form>
          <h3 style="font-size: 16px;color: #fff" ref="ref_info_taizhan"><b>{{ this.div_info_taizhan['title'] }}</b>
          </h3>
          <img :src=this.div_info_taizhan.img style="width: 90%;"/>
          <div v-html="this.div_info_taizhan['cnt']" class="fonsize"></div>
          <dv-scroll-board :config="config" style="width: 90%;height: 300px"/>
        </form>
      </div>
      <hr style="position: absolute;margin-top: 20px; width: 97%"/>
      <form style="position: absolute;margin-top: 30px;" class="fonsize">
        <p><b>鼠标位置:</b> {{ this.info_mouse_pos }}</p>
        <p><b>地图中心:</b> {{ this.info_map_center }}</p>
        <p><b>缩放级别:</b> {{ this.info_map_zoom }}</p>
      </form>
    </div>

    <div ref="map_vkz" style=" width: 84%;
    height: 95vh;
    z-index: 1;
    position: absolute">

    </div>

  </div>

</template>

<script>
import axios from "axios"
import L from 'leaflet';
import "leaflet/dist/leaflet.css";

import gsonShebei from "../js/gson_shebei";
import gsonJiankong from "../js/gson_jiankong";

import gsonFusheqv from "../js/gson_fusheqv";

import gsonTaizhan from "../js/gson_taizhan";
import gsonZhaopian from "../js/gson_photo";


import gsonShifanqv from "../js/gson_shifanqv";

export default {
// name: 'Test',
  mounted() {

    this.init_leaf();
    this.filterMedia();
    this.filterMedia2();
    this.filterMedia3();
    this.filterMedia4();
    this.filterMedia5();
    // this.filterMedia6();
    // this.filterMedia7();
    // this.filterMedia8();
    // this.filterMedia9();
    // this.leaf_todikuai();
    this.intervalId = setInterval(() => {
      axios
        .get('http://www.igadc.cn/htjson/qx/recent')
        .then(
          response => (this.info = response)
        )
        .catch(function (error) { // 请求失败处理
          console.log(error);
          // this.info = {}
        });
    }, 1000 * 1);


  },

  beforeUnmount() {
    clearInterval(this.intervalId);

    clearInterval(this.intervalId3);
  },
  data() {
    return {
      value: "",
      selectCurriculums: '',
      curriculums: ['地块1'],

      selectCurriculums1: '',
      curriculums1: ['地块1', '地块2'],
      config: {},
      select2: '',
      shijian: '',
      // img_info: img_info,
      info_map_center: undefined,
      info_map_zoom: undefined,
      info_mouse_pos: undefined,

      div_info_taizhan: {title: '会战地图', cnt: '在地图中展示了整个黑土区，地图中可以看到7个辐射区。分别为大河湾、海伦、三江、大安、长春、沈阳辐射区。', img: ''},


      info: {'data': 'Hello'},
      gsonShebei: gsonShebei,
      gsonTaizhan: gsonTaizhan,
      gsonShifanqv: gsonShifanqv,
      gsonJiankong: gsonJiankong,
      gsonZhaopian: gsonZhaopian,
      gsonFusheqv: gsonFusheqv,

      map: undefined,
      popup: undefined,
      opt_taizhan: {
        pointToLayer: function (feature, latlng) {
          return L.circleMarker(latlng);
          // return L.Marker(latlng);
        },
        // icon: myIcon,
        style: this.style,
        onEachFeature: this.onEachTaizhan
      }
    }
  },
  components: {},
  methods: {

    // getValue: function(){
    //   console.log('您选择了', this.select2)
    //   if(this.select2 !=''){
    //   var x = this.select2.split(';')[0]
    //   var y = this.select2.split(';')[1]
    //   this.leaf_todikuai(eval(x),parseInt(y))
    //   }
    //
    // },
    leaf_todikuai: function (aa, zoom_fac, val) {
      this.map.setView(aa, zoom_fac);
      this.value = val

    },

    test_fun2: function () {


      this.info_map_center = this.map.getCenter();
      this.info_map_zoom = this.map.getZoom();

    },
    test_fun3: function (e) {


      this.info_mouse_pos = e.latlng;
      this.info_map_zoom = this.map.getZoom();

    },
    swich_lyr_1() {

      if (this.$refs.lyr1.checked == true) {
        this.gson_taizhan.setStyle({opacity: 1, fillOpacity: 1});
      } else {
        this.gson_taizhan.setStyle({opacity: 0, fillOpacity: 0});
      }
    },
    swich_lyr_2() {

      if (this.$refs.lyr2.checked == true) {

        this.gson_shifanqv.setStyle({opacity: 1, fillOpacity: .1});


      } else {

        this.gson_shifanqv.setStyle({opacity: 0, fillOpacity: 0});

      }
    },

    filterMedia() {


      if (this.$refs.i1.checked == true) {

        this.gson_taizhan.eachLayer(function (feature) {
          feature.openTooltip();
        });
      } else {
        this.gson_taizhan.eachLayer(function (feature) {
          feature.closeTooltip();
        });
      }
    },
    filterMedia2() {

      if (this.$refs.i2.checked == true) {

        this.gson_shifanqv.eachLayer(function (feature) {


          feature.openTooltip();

        });
      } else {
        this.gson_shifanqv.eachLayer(function (feature) {

          feature.closeTooltip();

        });

      }
    },
    filterMedia3() {

      if (this.$refs.i3.checked == true) {

        this.gson_shebei.eachLayer(function (feature) {


          feature.openTooltip();

        });
      } else {
        this.gson_shebei.eachLayer(function (feature) {

          feature.closeTooltip();

        });

      }
    },
    filterMedia4() {

      if (this.$refs.i4.checked == true) {

        this.gson_jiankong.eachLayer(function (feature) {


          feature.openTooltip();

        });
      } else {
        this.gson_jiankong.eachLayer(function (feature) {

          feature.closeTooltip();

        });

      }
    },
    filterMedia5() {

      if (this.$refs.i5.checked == true) {
        this.map.addLayer(this.base_geography);
      } else {
        this.map.removeLayer(this.base_geography);
      }
    },
    filterMedia6() {

      if (this.$refs.i6.checked == true) {
        this.map.addLayer(this.geomor);
      } else {
        this.map.removeLayer(this.geomor);
      }
    },
    filterMedia7() {

      if (this.$refs.i7.checked == true) {
        this.map.addLayer(this.landuse);
      } else {
        this.map.removeLayer(this.landuse);
      }
    },
    filterMedia8() {

      if (this.$refs.i8.checked == true) {
        this.map.addLayer(this.soil);
      } else {
        this.map.removeLayer(this.soil);
      }
    },
    filterMedia9() {

      if (this.$refs.i9.checked == true) {
        this.map.addLayer(this.vegetation);
      } else {
        this.map.removeLayer(this.vegetation);
      }
    },
    onMapClick(e) {
      this.popup
        .setLatLng(e.latlng)
        .setContent("Location:" + e.latlng.toString())
        .openOn(this.map);
    },
    onMapZoom() {
      if (this.map.getZoom() > 9) {
        this.map.removeLayer(this.glayer_fusheqv);
      }
      if (this.map.getZoom() < 8) {
        this.map.addLayer(this.glayer_heituqv);

      }

      if (this.map.getZoom() < 9) {

        this.map.addLayer(this.glayer_fusheqv);
      }
    },
    init_leaf() {
      //创建地图
      this.map = L.map(this.$refs.map_vkz, {
        center: [47.15, 125.1],
        crs: L.CRS.EPSG3857,
        zoom: 6,
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

      this.base_geography = L.tileLayer.wms('http://47.94.22.90:9012/service?', {
        layers: 'q_ht_boundary_boundary',
        format: 'image/png',
        transparent: true,
        backgroundColor: '#0f0f0f',
      });
      this.geomor = L.tileLayer.wms('http://47.94.22.90:9012/service?', {
        layers: 'q_ht_geomor_geomor',
        format: 'image/png',
        transparent: true,
        backgroundColor: '#0f0f0f',
      });
      this.landuse = L.tileLayer.wms('http://47.94.22.90:9012/service?', {
        layers: 'q_ht_landuse_landuse',
        format: 'image/png',
        transparent: true,
        backgroundColor: '#0f0f0f',
      });
      this.soil = L.tileLayer.wms('http://47.94.22.90:9012/service?', {
        layers: 'q_ht_soil_soil',
        format: 'image/png',
        transparent: true,
        backgroundColor: '#0f0f0f',
      });
      this.vegetation = L.tileLayer.wms('http://47.94.22.90:9012/service?', {
        layers: 'q_ht_vegetation_vegetation',
        format: 'image/png',
        transparent: true,
        backgroundColor: '#0f0f0f',
      });

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

      this.grp_tdt = new L.LayerGroup();
      this.osm2.addTo(this.grp_tdt);
      this.osm1.addTo(this.grp_tdt);

      this.grp_tdt.addTo(this.map);


      this.greenIcon = {
        radius: 5,
        color: '#000000',
        opacity: 1,
        fillColor: '#666666',
        fillOpacity: 1,
      };


      this.glayer_heituqv = L.tileLayer.wms('http://47.94.22.90:9012/service?', {
        layers: 'q_base_htbnd',
        format: 'image/png',
        transparent: true,
        backgroundColor: '#000000',
      }).addTo(this.map);

      // this.glayer_fusheqv = L.geoJson(this.gsonFusheqv, {
      //   style: this.style_fushqv,
      //   onEachFeature: this.onEachFusheqv
      // }).addTo(this.map);

      this.glayer_fusheqv = L.tileLayer.wms('http://47.94.22.90:9012/service?', {
        layers: 'q_base_fushebase',
        format: 'image/png',
        transparent: true,
        backgroundColor: '#000000',
      }).addTo(this.map);

      // GeoJson数据

      this.gson_shifanqv = L.geoJson(this.gsonShifanqv, {
        onEachFeature: this.onEachShifanqv
      }).addTo(this.map);

      // this.gson_shifanqv.on('tooltipopen', this.rightInfo);
      this.gson_shifanqv.on('popupopen', this.rightInfo);

      this.gson_zhaopian = L.geoJson(this.gsonZhaopian, {
        pointToLayer: function (feature, latlng) {
          // alert(latlng);
          return L.circleMarker(latlng);
        },
        style: this.style_zhaopian,
        // icon: myIcon,
        // style: this.style_jiankong,


        onEachFeature: this.onEachZhaopian
      }).on('click', function (e) {
        console.log(e.target);
        console.log(e.originalEvent);
        console.log(e._source);
        // alert(e.latlng);

        // alert('Clicked on a member of the group!');
      }).addTo(this.map);

      this.gson_zhaopian.on('popupopen', this.onMapClick9);


      this.gson_jiankong = L.geoJson(this.gsonJiankong, {
        pointToLayer: function (feature, latlng) {
          return L.circleMarker(latlng);
        },
        // icon: myIcon,
        style: this.style_jiankong,

        onEachFeature: this.onEachJiankong
      }).addTo(this.map);


      this.gson_shebei = L.geoJson(this.gsonShebei, {
        pointToLayer: function (feature, latlng) {
          return L.circleMarker(latlng);
        },
        // icon: myIcon,
        style: this.style_shebei,

        onEachFeature: this.onEachShebei
      }).addTo(this.map);
      // this.gson_shebei.on('popupopen', this.onMapClick12);
      this.gson_taizhan = L.geoJson(this.gsonTaizhan, this.opt_taizhan
      ).addTo(this.map);

      // this.gson_taizhan.on('tooltipopen', this.onMapClick8);
      this.gson_taizhan.on('popupopen', this.onMapClick8);

      // this.grp_taizhan = new L.LayerGroup();
      this.grp_background = new L.LayerGroup();


      // this.glayer_fusheqv.addTo(this.grp_taizhan);


      this.glayer_fusheqv.addTo(this.grp_background);
      this.glayer_heituqv.addTo(this.grp_background);
      // this.osm1.addTo(cities);


      this.grp_background.addTo(this.map);
      // this.grp_taizhan.addTo(this.map);


      this.baseMaps = {
        '影像': this.osm2,
        // '天地图': this.osm,
        // '示范区底图': this.l27,

      };

      this.overlayMaps = {
        // 'bnd': this.glayer_heituqv,
        '辐射区': this.grp_background,
        // '示范区': this.lyr_shifanqv,
        '台站': this.gson_taizhan,
        '观测设备': this.gson_shebei,
      };

      this.grp_background.addTo(this.map);


      L.control.scale({
        position: 'bottomright',
        maxWidth: '100',
        imperial: false
      }).addTo(this.map);
      this.map.on('layeradd', this.show_legend);
    },


    onMapClick8: function (e) {


      var marker = e.popup._source;

      console.log('aaaaaaaaaaaaaaa')


      var info2 = marker.feature.properties.label + ' ' + marker.feature.geometry.type + ' ' + marker.feature.geometry.coordinates.toString();
      console.log('bbbbbbbbbbbbb')

      axios
        .get('http://www.igadc.cn/htjson/qx/recent')
        .then(
          response => (this.info = response)
        )
        .then(
          info2 = info2 + ' ' + JSON.stringify(this.info.data)
        )

        .catch(function (error) { // 请求失败处理
          console.log(error);
          // this.info = {}
        });

      var info3 = '<b>' + marker.feature.properties.label + '</b><br />' +
        '<b>介绍: </b><br />' + marker.feature.properties.introduce + '<br />' +
        '<b>编辑日期: </b>' + marker.feature.properties.edit_time + '<br />' +
        '<b>信息编辑人:</b>' + marker.feature.properties.edit + ' ';
      this.div_info_taizhan['title'] = '野外台站信息：';
      this.div_info_taizhan['img'] = marker.feature.properties.img;
      // this.div_info_taizhan['img'] = 'http://www.igadc.cn/static/cache/u63fe.png';
      this.div_info_taizhan['cnt'] = info3;
      // this.div_info_taizhan['cnt'] = info2;
      // alert(this.info_taizhan_intro);

      this.config = {};
    },
    rightInfo: function (e) {


      var marker = e.popup._source;

      console.log('aaaaaaaaaaaaaaa')


      var info2 = '<b>地块名称：</b>' + marker.feature.properties.地块名 + '<br /><p />' +

        '<b>面积：</b>' + marker.feature.properties.测算面 + '亩<br /><p />' +
        '<b>所属经营主：</b>' + marker.feature.properties.所属经 + '<br /><p />' +
        '<b>录入人姓名：</b>' + marker.feature.properties.录入人 + '<br /><p />' +
        '<b>位置：</b>' + marker.feature.properties.省 + marker.feature.properties.市 + marker.feature.properties.县 + marker.feature.properties.乡 + marker.feature.properties.村;
      console.log('bbbbbbbbbbbbb')


      this.div_info_taizhan['title'] = '示范区地块信息：';
      this.div_info_taizhan['img'] = '';
      this.div_info_taizhan['cnt'] = info2;
      // alert(this.info_taizhan_intro);
      this.config = {};

    },
    onMapClick9: function (ev) {


      var marker = ev.popup._source;


      this.div_info_taizhan['title'] = marker.feature.properties.title;
      this.div_info_taizhan['img'] = "http://r.osgeo.cn:8008/htimg/" + marker.feature.properties.img + "-s.jpg";
      this.div_info_taizhan['cnt'] = marker.feature.properties.date;
      this.config = {};
      // alert(ev.originalEvent.path[0]);
    },
    onMapClick12: function (ev12) {


      var marker = ev12.popup._source;

      var uid = marker.feature.properties.devid;
      this.get_data(uid)

      console.log(this.div_info_taizhan)
    },
    get_data(uid) {

      var url = 'http://www.igadc.cn/htjson/zhishang?devid=' + uid

      axios
        .get(url)
        .then(
          response => {
            this.config = {
              header: ["类型", "数值"],
              data: response.data.results,
              rowNum: 6, //表格行数
              headerHeight: 25,
              headerBGC: "#0f1325", //表头
              oddRowBGC: "#0f1325", //奇数行
              evenRowBGC: "#171c33", //偶数行
              index: false,
              columnWidth: [100],
              align: ["center"],
              indexHeader: null
            };
            this.div_info_taizhan['cnt'] = '<h5>时间：' + response.data.date + '</h5>'
          }
        )
        .catch(function (error) { // 请求失败处理
          console.log(error);
          this.info = {}
        });
      this.div_info_taizhan['img'] = ''
      this.div_info_taizhan['title'] = '设备：' + uid
    },

    onEachTaizhan: function (feature, layer) {

      // layer.bindPopup(feature.properties.name);

      if (feature.properties.kind == 1) {
        layer.bindTooltip("<div><b>" + feature.properties.label + "</b></div>",
          {
            permanent: true,
            direction: 'auto',
            // direction: "center",
            className: 'kind1',
          });
      } else if (feature.properties.kind == 2) {
        layer.bindTooltip("<div><b>" + feature.properties.label + "</b></div>",
          {
            permanent: true,
            direction: 'auto',
            className: 'kind2',
          });
      } else if (feature.properties.kind == 3) {
        layer.bindTooltip("<div><b>" + feature.properties.label + "</b></div>",
          {
            permanent: true,
            direction: 'auto',
            className: 'kind3',
          });
      } else {
        layer.bindTooltip("<div><b>" + feature.properties.label + "</b></div>",
          {
            permanent: true,
            direction: 'auto',
            className: 'kind4',
          });
      }


      layer.bindPopup(
        "<b>" + feature.properties.label + "</b>"
      )


      layer.on('click', function (e) {

        console.log(e.latlng);
        console.log(this.info_taizhan_intro);


      });
    },
    onEachShebei: function (feature, layer) {


      layer.bindTooltip("<div><b>" + feature.properties.devid + "</b></div>",
        {
          permanent: false,
          direction: 'auto',
          // direction: "center",
          className: "shebei",
        });
      layer.bindPopup(
        "<p v-bind:id=''>DEV ID: " + feature.properties.devid + "</p>"
      )
    },
    onEachFusheqv: function (feature, layer) {


      layer.bindTooltip("<div style='background-color:rgba(255,255,255,0);padding:0;margin:0; color:gray;'><b>" + feature.properties.NAME + "</b></div>",
        {
          permanent: true,
          direction: 'auto',
          // direction: "center",
          className: "leaflet-tooltip-own",
        });


    },
    onEachShifanqv: function (feature, layer) {

      layer.bindTooltip("<div><b>" + feature.properties.地块名 + "</b></div>",
        {
          permanent: false,
          // direction: 'center',
          // direction: "center",
          className: "leaflet-tooltip-own",
        });

      layer.bindPopup(
        "<b>" + feature.properties.地块名 + "</b>"
      )

    },

    onEachJiankong: function (feature, layer) {

      layer.bindTooltip("<div><b>" + feature.properties.name + "</b></div>",
        {
          permanent: false,
          // direction: 'center',
          // direction: "center",
          className: "jiankong",
        });
      layer.bindPopup(
        "<b>" + feature.properties.name + "</b>"
      )
    },

    onEachZhaopian: function (feature, layer) {


      layer.bindPopup(
        '<a><img src="http://r.osgeo.cn:8008/htimg/' + feature.properties.img +
        '-s.jpg" style="width:300px;" />' +
        '<p>' + '拍摄日期：' + feature.properties.date +
        '</p></a>',
      )
    },

    getColor: function (d) {
      return d == 1 ? '#F59545' :
        d == 2 ? '#71A2DD' :
          d == 3 ? '#18DE72' :
            d == 4 ? '#8A71AB' :
              '#000000';
    },
    getColor_fusheqv: function (d) {
      return d == 1 ? '#F59545' :
        d == 2 ? '#18DE72' :
          d == 3 ? '#71A2DD' :
            d == 4 ? '#8A71AB' :
              d == 5 ? '#F59545' :
                d == 6 ? '#18DE72' :
                  '#8A71AB';
    },
    style_shebei: function (feature) {
      return {
        radius: 3,
        weight: 1,
        opacity: 1,
        color: '#ffff22',
        fillOpacity: 0.9,
        fillColor: this.getColor(feature.properties.kind)
      };
    },
    style_jiankong: function () {
      return {
        radius: 6,
        weight: 1,
        opacity: 1,
        color: '#ff22ff',
        fillOpacity: 0.9,
        fillColor: '#ff22ff'
      };
    },
    style_zhaopian: function () {
      return {
        radius: 5,
        weight: 1,
        opacity: 1,
        color: '#ffee22',
        fillOpacity: 0.9,
        fillColor: '#eeff22'
      };
    },
    style: function (feature) {
      return {
        radius: 9,
        weight: 1,
        opacity: 1,
        color: '#333333',
        fillOpacity: 0.9,
        fillColor: this.getColor(feature.properties.kind)
      };
    },
    style_fushqv: function (feature) {
      return {
        radius: 9,
        weight: 1,
        opacity: .7,
        color: '#333333',
        fillOpacity: 0.7,
        fillColor: this.getColor_fusheqv(feature.properties.id)
      };
    },
    leaf_foo2: function () {
      this.map.zoomIn(1);
    },
    leaf_foo1: function () {
      this.map.zoomOut(1);
    },
    leaf_foo3: function () {

      this.map.setView([47.15, 125.1], 6);


    },
    leaf_remove_soil: function () {
      this.map.removeLayer(this.soil_map);
    },
    leaf_add_soil: function () {
      this.map.addLayer(this.soil_map);
    },

    style2: function () {
      return {
        radius: 8,
        weight: 1,
        opacity: 1,
        color: '#a65982',
        fillOpacity: 1,
        fillColor: '#ddd132',
      };
    },

  }
}
</script>

<style lang="scss" scoped>

#center_fz8 {
  height: 95vh;

  .btn {
    &.activity {
      background: #7B68EE;
      border: #8A71AB 1px solid;
      color: #fff;
    }
  }

  input[type=checkbox].switch {
    margin-right: 5px;
    outline: none;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    position: relative;
    width: 30px;
    height: 15px;
    border-radius: 15px;
    border: 1px solid #ccc;
    background-color: #ccc;
    top: 2px
  }

  input[type=checkbox].switch::after {
    content: '';
    display: inline-block;
    width: 15px;
    height: 14px;
    border-radius: 50%;
    background-color: #fff;
    box-shadow: 0 0 2px #999;
    transition: left 0.1s linear;
    position: absolute;
    top: 0;
    left: 0;
  }

  input[type=checkbox].switch:checked {
    background-color: #1ab394;
  }

  input[type=checkbox].switch:checked::after {
    position: absolute;
    top: 0;
    left: 50%;
  }


  .li_icon_yi {
    width: 100%;
    color: #fff;
    list-style: none;
  }

  .li_icon_yi:hover {
    cursor: pointer;
    color: #5cd9e8;
  }


  .text {
    color: #c3cbde;
  }

  .leaflet-popup-tip-container {
    background-color: rgba(255, 0, 0, 0.0);
    display: none;
  }

  .btn-sm {
    padding: 2px;
  }

  form {
    margin: .1rem;
    margin-top: .3rem;
    font-size: .18rem;
  }

  fieldset {

    label {
      font-size: 14px;
      margin: 10px 0;
      display: flex;

    }

    ul li {
      font-size: 14px;
    }
  }

  .icon_tab {
    margin-left: 15px;
  }
  .fonsize {
    font-size: 14px;
    color: #fff;
  }
}
</style>
