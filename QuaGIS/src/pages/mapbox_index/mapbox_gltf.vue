<template>


  <div id="mapbox_dde" class="mainMap3"></div>
</template>

<script>

//import datav from '@jiaminghi/data-view'
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css'
import 'vue-awesome/icons/cog';
import * as THREE from 'three'
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader';


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



    const initMap = () => {
      //这里请换成自己的token
      // mapboxgl.accessToken = 'pk.eyJ1Ijoic2FtZWxlIiwiYSI6ImNreW1rZzRhcjE4cWIydnAwczRscWM5OXQifQ.3ZimcrEcttEKZ_BJpDWIxA';
    mapboxgl.accessToken = 'pk.eyJ1IjoiY2FvcnVpYmluIiwiYSI6ImNsYWR3MjEwMjA5b2UzcW85dmZlbTVtMTAifQ.4v81PyG-oZ6TVL7IuyCbrg';
      let map = new mapboxgl.Map({
        container: 'mapbox_dde', // container id 绑定的组件的id
        // style: 'mapbox://styles/mapbox/streets-v11', //地图样式，可以使用官网预定义的样式,也可以自定义
        // style: 'mapbox://styles/mapbox/satellite-v9',
        // style: 'mapbox://styles/mapbox/satellite-streets-v11',
        // style: 'mapbox://styles/mapbox/satellite-v9', //地图样式卫星，可以使用官网预定义的样式,也可以自定义
        style: 'mapbox://styles/mapbox/satellite-v9', //地图样式卫星，可以使用官网预定义的样式,也可以自定义
        // style: 'mapbox://styles/mapbox/dark-v10', //地图样式卫星，可以使用官网预定义的样式,也可以自定义
        zoom: 18,
        center: [148.9819, -35.3981],
        pitch: 60,
        bearing: 0, // 地图的初始方向，值是北的逆时针度数，默认是0，即是正北
        antialias: true, // 抗锯齿，通过false关闭提升性能

        // center: [54.84472718131394, 33.89394107223532], // 初始坐标系，这个是南京建邺附近
        // zoom: 2.267,     // starting zoom 地图初始的拉伸比例
        // pitch: 60,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
        // bearing: -17.6, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
        // antialias: true, //抗锯齿，通过false关闭提升性能
      });

   const modelOrigin = [148.9819, -35.39847];
    const modelAltitude = 0;
    const modelRotate = [Math.PI / 2, 0, 0];

    const modelAsMercatorCoordinate = mapboxgl.MercatorCoordinate.fromLngLat(
        modelOrigin,
        modelAltitude
    );

    const modelTransform = {
        translateX: modelAsMercatorCoordinate.x,
        translateY: modelAsMercatorCoordinate.y,
        translateZ: modelAsMercatorCoordinate.z,
        rotateX: modelRotate[0],
        rotateY: modelRotate[1],
        rotateZ: modelRotate[2],
        scale: modelAsMercatorCoordinate.meterInMercatorCoordinateUnits()
    };


    const customLayer = {
        id: '3d-model',
        type: 'custom',
        renderingMode: '3d',
        onAdd: function (map, gl) {
            this.camera = new THREE.Camera();
            this.scene = new THREE.Scene();

            // create two three.js lights to illuminate the model
            const directionalLight = new THREE.DirectionalLight(0xffffff);
            directionalLight.position.set(0, -70, 100).normalize();
            this.scene.add(directionalLight);

            const directionalLight2 = new THREE.DirectionalLight(0xffffff);
            directionalLight2.position.set(0, 70, 100).normalize();
            this.scene.add(directionalLight2);

            const loader = new GLTFLoader();
            loader.load(
                'https://docs.mapbox.com/mapbox-gl-js/assets/34M_17/34M_17.gltf',
                (gltf) => {
                    this.scene.add(gltf.scene);
                }
            );
            this.map = map;

            this.renderer = new THREE.WebGLRenderer({
                canvas: map.getCanvas(),
                context: gl,
                antialias: true
            });

            this.renderer.autoClear = false;
        },
        render: function (gl, matrix) {
            const rotationX = new THREE.Matrix4().makeRotationAxis(
                new THREE.Vector3(1, 0, 0),
                modelTransform.rotateX
            );
            const rotationY = new THREE.Matrix4().makeRotationAxis(
                new THREE.Vector3(0, 1, 0),
                modelTransform.rotateY
            );
            const rotationZ = new THREE.Matrix4().makeRotationAxis(
                new THREE.Vector3(0, 0, 1),
                modelTransform.rotateZ
            );

            const m = new THREE.Matrix4().fromArray(matrix);
            const l = new THREE.Matrix4()
                .makeTranslation(
                    modelTransform.translateX,
                    modelTransform.translateY,
                    modelTransform.translateZ
                )
                .scale(
                    new THREE.Vector3(
                        modelTransform.scale,
                        -modelTransform.scale,
                        modelTransform.scale
                    )
                )
                .multiply(rotationX)
                .multiply(rotationY)
                .multiply(rotationZ);

            this.camera.projectionMatrix = m.multiply(l);
            this.renderer.resetState();
            this.renderer.render(this.scene, this.camera);
            this.map.triggerRepaint();
        }
    };

    map.on('style.load', () => {
        map.addLayer(customLayer);
    });



          let popup = new mapboxgl.Popup({
          closeButton: true,
          closeOnClick: true,
        })

    };

    return {
      decorationColors,
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
