<template>
  <div id="map" class="container"></div>
</template>
<script>
import 'maptalks/dist/maptalks.css';
import * as maptalks from 'maptalks';

import * as THREE from 'three'
import {ThreeLayer} from 'maptalks.three'


export default {
  data() {
    return {
      buidingColor: "#0fdaf5",
    };
  },
  mounted() {
    this.init_leaf()
  },
  methods: {
    init_leaf() {


      this.map = new maptalks.Map('map', {
        center: [125.1, 47.15],

        zoom: 6,
        pitch: 60,
        baseLayer: new maptalks.TileLayer('base', {
          urlTemplate: 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
          // urlTemplate: 'http://t{s}.tianditu.gov.cn/img_w/wmts?tk=bb11a33c4377f10603478ed166691455&SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=img&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TileMatrix={z}&TileCol={x}&TileRow={y}',
          subdomains: ['a', 'b', 'c', 'd'],
          attribution: '© <a href="http://osm.org">OpenStreetMap</a> contributors, © <a href="https://carto.com/">CARTO</a>',
        }),
        layers: [
          new maptalks.WMSTileLayer('wms', {
            'urlTemplate': 'http://tile.igadc.cn/service?',
            'crs': 'EPSG:3857',
            'layers': 'qn9326',
            'styles': '',
            'version': '1.3.0',
            'format': 'image/png',
            'transparent': true,
            'uppercase': true
          })
        ]
      });


      var threeLayer = new ThreeLayer('t', {
        forceRenderOnMoving: true,
        forceRenderOnRotating: true
        // animation: true
      });
      threeLayer.prepareToDraw = function (gl, scene) {
        var light = new THREE.DirectionalLight(0xffffff);
        light.position.set(0, -10, 10).normalize();
        scene.add(light);
        scene.add(new THREE.AmbientLight(0xffffff, 0.5));

      };
      threeLayer.addTo(this.map);

      let url = "data/gson_shifanqv.geojson";

      fetch(url)
        .then(function (res) {
          return res.text();
        })
        .then(function (text) {
          return JSON.parse(text).features;
        })
        .then(function (features) {
          let extrudeFactor = 1;
          let meshes = [];
          for (let feature of features) {
            let height = feature.properties.height || 61;

            let material = new THREE.MeshPhongMaterial({
              color: getColor(height),
            });
            let extrudePolygon = threeLayer.toExtrudePolygon(
              maptalks.GeoJSON.toGeometry(feature),
              {
                interactive: false,
                height: extrudeFactor * height,
                topColor: '#0fdaf5',
              },
              material
            );
            threeLayer.addMesh(extrudePolygon);
            meshes.push(extrudePolygon);
          }
          window.meshes = meshes;
        });

      function getColor(height) {
        let rgb;
        if (height < 61.4) {
          rgb = "112,112,123";
        } else if (height >= 61.4 && height < 104.8) {
          rgb = "135,139,155";
        } else if (height >= 104.8 && height < 148.2) {
          rgb = "231,241,245";
        } else if (height >= 148.2 && height < 236) {
          rgb = "162,169,183";
        } else {
          rgb = "1,0,0";
        }
        return `rgb(${rgb})`;
      }
    },


  }
};
</script>

<style lang="scss">
.container {
  width: 100%;
  height: 90vh
}
</style>

