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
        center: [125.3154, 43.8784],
        zoom: 9, // starting zoom 地图初始的拉伸比例
        pitch: 50, // 地图的角度，不写默认是0，取值是0-85度，一般在3D中使用
        bearing: 0, // 地图的初始方向，值是北的逆时针度数，默认是0，即是正北
        antialias: true, // 抗锯齿，通过false关闭提升性能
        minZoom: 3,
        maxZoom: 18,
        // center: [54.84472718131394, 33.89394107223532], // 初始坐标系，这个是南京建邺附近
        // zoom: 2.267,     // starting zoom 地图初始的拉伸比例
        // pitch: 60,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
        // bearing: -17.6, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
        // antialias: true, //抗锯齿，通过false关闭提升性能
      });
map_dde.on('load', function() {

     map_dde.addSource('wms-test-source', {
            'type': 'raster',
            'tiles': [
                'http://tile.igadc.cn/service?&SERVICE=WMS&REQUEST=GetMap&LAYERS=qn9326&STYLES=&FORMAT=image%2Fpng&TRANSPARENT=true&VERSION=1.3.0&WIDTH=256&HEIGHT=256&CRS=EPSG%3A3857&BBOX={bbox-epsg-3857}'
            ],
            'tileSize': 256
        });
        map_dde.addLayer(
            {
                'id': 'wms-test-layer',
                'type': 'raster',
                'source': 'wms-test-source',
                'paint': {}
            },)
})

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
          let popup = new mapboxgl.Popup({
          closeButton: true,
          closeOnClick: true,
        })
  map_dde.on('load', () => {
        addMvt();
    });



    function addMvt() {
        map_dde.addLayer({
            // id: 'MULTIPOLYGON',
            id: 'multipolygon',
            type: 'fill-extrusion',
            source: {
                type: 'vector',
                url: 'http://39.100.72.56:6799/martin_cc'
            },
            'source-layer': 'martin_cc',
            paint: {
                'fill-extrusion-color': 'red',
                "fill-extrusion-height": ["get", "height"],
            "fill-extrusion-base": ["get", "baseHeight"],
            "fill-extrusion-opacity": 0.6,
            // "fill-extrusion-ambient-occlusion-ground-attenuation": 0.6,

            }
        });
      map_dde.on('click', 'multipolygon', (e) => {
              popup
                  .setLngLat([Number(e.lngLat.lng), Number(e.lngLat.lat)])
                  .setHTML(
                    ` <div class="hover-popup" >
              <div style="font-size:14px; color:#333">
                <div style="margin-top:5px"><span style="color:#999;">位置：</span><span>` +e.features[0].properties['layer'] +`</span></div>
                <div style="margin-top:5px"><span style="color:#999;">高度：</span><span>` +e.features[0].properties['height'] +`</span></div>
              </div>
            </div>
              `
                  )
                  .addTo(map_dde)
          })

    }



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
