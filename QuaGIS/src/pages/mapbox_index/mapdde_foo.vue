<template>

  <div id="mapbox_dde" class="mainMap3"></div>
</template>

<script>

//import datav from '@jiaminghi/data-view'
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css'
import 'vue-awesome/icons/cog';
import axios from "axios";


import {
  onMounted,
} from 'vue'

export default {
  // name: 'Map',
  props: {},
  setup(props, context) {
    console.log(props, context);
    let mapMap = null

    const decorationColors = ['#568aea', '#bebeff'];
    onMounted(() => {
      initMap()

    })


    let info_map_center = 'LatLng[54.84, 33.89]';
    let info_map_zoom = '2.26';
    let info_mouse_pos = '';

    const initMap = () => {
      //这里请换成自己的token
      mapboxgl.accessToken = 'pk.eyJ1Ijoic2FtZWxlIiwiYSI6ImNreW1rZzRhcjE4cWIydnAwczRscWM5OXQifQ.3ZimcrEcttEKZ_BJpDWIxA';
      let map_dde = new mapboxgl.Map({
        container: 'mapbox_dde', // container id 绑定的组件的id
        // style: 'mapbox://styles/mapbox/streets-v11', //地图样式，可以使用官网预定义的样式,也可以自定义
        // style: 'mapbox://styles/mapbox/satellite-v9',
        // style: 'mapbox://styles/mapbox/satellite-streets-v11',
        style: 'mapbox://styles/mapbox/satellite-v9', //地图样式卫星，可以使用官网预定义的样式,也可以自定义
        // style: 'mapbox://styles/mapbox/dark-v10', //地图样式卫星，可以使用官网预定义的样式,也可以自定义

        center: [54.84472718131394, 33.89394107223532], // 初始坐标系，这个是南京建邺附近
        zoom: 2.267,     // starting zoom 地图初始的拉伸比例
        // pitch: 60,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
        // bearing: -17.6, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
        // antialias: true, //抗锯齿，通过false关闭提升性能
      });


      // function onMapClick(e) {
      //   let popup = new mapboxgl.Popup()
      //
      //                 .setLngLat(e.lngLat)
      //                 .setHTML("<b style='color: #3b3d3d;font-size: .15rem'>Location:LatLng[" + e.lngLat.lat.toFixed(3) + "," + e.lngLat.lng.toFixed(3).toString() + "]</b>")
      //                 .addTo(map_dde);
      //             console.log(popup)
      // }


      function onMapmove() {
        info_map_center = 'LatLng[' + map_dde.getCenter().lat.toFixed(3)
          + ',' + map_dde.getCenter().lng.toFixed(3) + ']';
        info_map_zoom = map_dde.getZoom().toFixed(1);
      }

      // function onMapmousemove(e){
      //
      //             info_mouse_pos = 'LatLng[' + e.lngLat.lat.toFixed(3) + ',' + e.lngLat.lng.toFixed(3) + ']';
      //             info_map_zoom = map_dde.getZoom().toFixed(1);
      // }


      // map_dde.on('click', onMapClick);
      // map_dde.on('zoom', onMapZoom);
      map_dde.on('move', onMapmove);
      // map_dde.on('mousemove', onMapmousemove);
      map_dde.on("load", () => {
        // 加载图层，注册事件等都需要写在这里面

        let sn_data = {};

        axios.get('https://ddemd.deep-time.org/json/data-sn')

          .then(
            response => {
              let g_sn_result = response.data.results;

              for (let i = 0; i < g_sn_result.length; i++) {

                for (let key_out in g_sn_result[i]) {
                  let one_data = {};

                  one_data = {
                    "type": "Feature",
                    "geometry": {
                      "type": "Point",
                      "coordinates": [g_sn_result[i][key_out].log, g_sn_result[i][key_out].lat],

                    },
                    "properties": {
                      "Data_SN": g_sn_result[i][key_out].Data_SN,
                      "SectionName": g_sn_result[i][key_out].SectionName
                    }

                  };

                  sn_data.features.push(one_data)

                }


              }


              map_dde.addSource('data_sn', {type: 'geojson', data: sn_data});
              map_dde.addLayer({
                'id': 'data_sn_layer',
                'type': 'circle',
                'source': 'data_sn',
                'paint': {
                  'circle-radius': {
                    'base': 1.75,
                    'stops': [[12, 3], [22, 4]]
                  },
                  'circle-color': 'rgba(117,231,48,0.2)',
                  'circle-opacity': 0,
                }
              })


            }
          )
          .catch(function (error) { // 请求失败处理
            console.log(error);
          });


      });
    };

    let close_e = true;
    return {
      decorationColors,
      close_e,
      info_map_center,
      info_map_zoom,
      info_mouse_pos
    }
  }
}
</script>

<style>
#mapbox_dde {
  width: 100%;
  height: 100vh;
  z-index: 1;
}

.qqq {
  width: 100%;
}

.qqq:hover {
  cursor: pointer;
  color: #5cd9e8;
}

.menue_white {
  border-radius: .04rem;
  z-index: 120;
  width: 100%;
  height: .3rem;
  background-color: rgba(255, 255, 255, 0.2)
}

.white_li {
  position: inherit;
  padding: .07rem;
  font-size: .2rem;
  vertical-align: middle;
}

.white_li:hover {
  cursor: pointer;
  color: #5cd9e8;
}

.white_la {
  font-weight: bold;
  padding-bottom: .2rem;
}

.white_la:hover {
  cursor: pointer;
  color: #5cd9e8;
}

.white_span {
  float: left;
  width: 90%;
}

.chevron_white {
  float: right;
  width: 0.25rem;
  height: 0.25rem
}

.popup_color {
  color: #3b3d3d;
}

.li_line li {
  display: inline;
  width: 25%;
  /*border-*/
}

.bottom_data_box {
  width: 33.3%;
  margin-top: .3rem;
  display: inline-block;
  text-align: center
}

.bottom_h2 {
  padding-bottom: .2rem;
  font-size: .18rem
}

.away_top {
  top: 3rem
}

.grey_box {
  z-index: 100;
  width: 15rem;
  padding: 5px;
  margin: 5px;
  height: 90%;
  background: rgba(50, 50, 50, 0.7);
  position: absolute;
  border-radius: 4px
}

.title_p {
  font-size: .2rem;
  padding-top: .1rem;
  text-align: center;
}

.suojin_label {
  margin-left: .2rem;
}

.dontknow {
  color: #ffffff;
}

.mapboxgl-ctrl-attrib {
  display: none !important;
}
</style>
