<template>
  <div class="map-box">
   <div id="cesiumContainer">

    </div>
  </div>
</template>

<script>
import * as Cesium from "cesium";
export default {
   name: "cesiumContainer",
  data() {
    return {
      viewer: '',
      imageryLayers: '',
    }
  },
  mounted() {
    this.init();
  },
  methods: {

    init: function () {


      Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiZGI4N2U5My0xMTc0LTQyMGItODUyOC0xOWI3MDZiNDNiZDAiLCJpZCI6ODE1OCwiaWF0IjoxNjg0NzIxNDUyfQ.Q4YUWO824I1zUnMuOadI4arml8Xc8vBcuC_I7VdadVA'
      const viewer = new Cesium.Viewer("cesiumContainer", {
        geocoder: false,
        // homeButton:false,
        sceneModePicker: false,
        // baseLayerPicker:false,
        // navigationHelpButton:false,
        animation: false,
        // creditContainer:"credit",
        timeline: false,
        fullscreenButton: false,
        vrButton: false,
        // terrainProvider: Cesium.createWorldTerrain(),


      })

      viewer.cesiumWidget.creditContainer.style.display = "none";
      viewer.scene.globe.enableLighting = true;
      viewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(125.1, 47.15, 17000000),
        orientation: {
          heading: Cesium.Math.toRadians(0),
          pitch: Cesium.Math.toRadians(-90),
          roll: Cesium.Math.toRadians(0)
        }
      })


      var czml = [
        {
          "id": "document",
          "name": "box",
          "version": "1.0"
        }, {
          "id": "shape2",
          "name": "Red box with black outline",
          "position": {
            "cartographicDegrees": [-107.0, 40.0, 300000.0]
          },
          "box": {
            "dimensions": {
              "cartesian": [400000.0, 300000.0, 500000.0]
            },
            "material": {
              "solidColor": {
                "color": {
                  "rgba": [255, 0, 0, 128]
                }
              }
            },
            "outline": true,
            "outlineColor": {
              "rgba": [0, 0, 0, 255]
            }
          }
        }];
      var dataSourcePromise = Cesium.CzmlDataSource.load(czml);
      viewer.dataSources.add(dataSourcePromise);
      viewer.zoomTo(dataSourcePromise);

      window.viewer = viewer;
    },

    initCCjz: function () {
      window.viewer.dataSources.remove(window.geojsn);
      var tileset = new Cesium.Cesium3DTileset({url: './data/tiles/tileset.json'})
      // tileset.style = new Cesium.Cesium3DTileStyle({
      //   color:'#f00'
      // })

      tileset.readyPromise.then(function (argument) {

        tileset.style = new Cesium.Cesium3DTileStyle({
          color: {
            conditions: [

              ["${height} >= 30", "rgba(45, 0, 75, 0.5)"],
              ["${height} >= 24", "rgb(102, 71, 151)"],
              ["${height} >= 18", "rgb(170, 162, 204)"],
              ["${height} >= 12", "rgb(224, 226, 238)"],
              ["${height} >= 8", "rgb(252, 230, 200)"],
              ["${height} >= 5", "rgb(248, 176, 87)"],
              ["${height} >= 3", "rgb(198, 106, 11)"],
              ["true", "rgb(127, 59, 8)"],
            ]
          }
        })
      })

      // // 高亮元素
      // const hightLighted = {
      //   feautre: undefined,
      //   originalColor: new Cesium.Color(),
      // }
      //
      // viewer.screenSpaceEventHandler.setInputAction(function onLeftClick(event) {
      //   // 清除之前的高亮元素
      //   if (Cesium.defined(hightLighted.feature)) {
      //     hightLighted.feature.color = hightLighted.originalColor;
      //     hightLighted.feature = undefined;
      //   }
      //
      //   // 选择新要素
      //   const pickedFeature = viewer.scene.pick(event.position);
      //   if (!Cesium.defined(pickedFeature)) {
      //     return;
      //   }
      //
      //   // 存储选中要素的信息
      //   hightLighted.feature = pickedFeature;
      //   Cesium.Color.clone(
      //       pickedFeature.color,
      //       hightLighted.originalColor
      //   );
      //   // 高亮选中元素
      //   pickedFeature.color = Cesium.Color.YELLOW;
      // }, Cesium.ScreenSpaceEventType.LEFT_CLICK)



      window.viewer.scene.primitives.add(tileset);
      window.viewer.flyTo(tileset)
     window.baiMoObject = tileset
    },
    initCCjson: function () {
    window.viewer.scene.primitives.remove(window.baiMoObject);
     var promise = Cesium.GeoJsonDataSource.load('./data/cc.geojson', {clampToGround: true})

      promise.then(function (dataSources) {
        window.viewer.dataSources.add(dataSources)
        let entities = dataSources.entities.values
        for (let i = 0; i < entities.length; i++) {
          let entity = entities[i]
          entity.polygon.height = 0
          entity.polygon.heightReference = Cesium.HeightReference.RELATIVE_TO_GROUND
          entity.polygon.extrudedHeightReference = Cesium.HeightReference.RELATIVE_TO_GROUND
          entity.polygon.extrudedHeight = entity.properties.Elevation._value
          entity.polygon.material = Cesium.Color.RED.withAlpha(0.6)
          entity.polygon.outline = true
          entity.polygon.outlineColor = Cesium.Color.BLUE
          entity.polygon.extrudedHeight = 200

        }

      })
    window.viewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(125.1, 47.15, 17000000),
        orientation: {
          heading: Cesium.Math.toRadians(0),
          pitch: Cesium.Math.toRadians(-90),
          roll: Cesium.Math.toRadians(0)
        }
      })
      window.geojsn = promise
    },
    initGltf: function () {
      var entity = viewer.entities.add({
        position: Cesium.Cartesian3.fromDegrees(
            148.9819,
            -35.3981,
        ),
        model: {
          uri: "https://docs.mapbox.com/mapbox-gl-js/assets/34M_17/34M_17.gltf",
        }
      });
      window.viewer.zoomTo(entity)
    },
    initGsonshifq: function () {

      var promise = Cesium.GeoJsonDataSource.load(gsonShifanqu)
      promise.then(function (dataSources) {
        window.viewer.dataSources.add(dataSources)
        let entities = dataSources.entities.values
        for (let i = 0; i < entities.length; i++) {
          let entity = entities[i]
          entity.name = entity.properties.地块名
          entity.polygon.material = Cesium.Color.BLUE
          entity.billboard = false
          entity.polygon.heightReference = Cesium.HeightReference.CLAMP_TO_GROUND
          entity.description = `<div class="cesium-infoBox">
                           <p>地块名称： ${entity.properties.地块名}</p>
                            <p>测算面积：${entity.properties.测算面}</p>
                            <p>所属经营主：${entity.properties.所属经}</p>
                          </div>`

        }
      })
    },

    initTileset: function () {
      var tileset = window.viewer.scene.primitives.add(
          new Cesium.Cesium3DTileset({
            url: 'https://earthsdk.com/v/last/Apps/assets/dayanta/tileset.json'
          })
      );
      tileset.readyPromise.then(function () {
        window.viewer.camera.viewBoundingSphere(tileset.boundingSphere, new Cesium.HeadingPitchRange(0, -0.5, 0));
        window.viewer.camera.lookAtTransform(Cesium.Matrix4.IDENTITY);
      });
    },
    changRadio: function (aa, quqing) {
      var overlayMaps_f = {
        'i5': this.base_geography,
        'i6': this.geomor,
        'i8': this.soil,
        'i9': this.vegetation,
        'i10': this.glayer_fusheqv,

      };
      window.viewer.imageryLayers.remove(this.xianshi)
      this.xianshi = window.viewer.imageryLayers.addImageryProvider(overlayMaps_f[aa])


    },
    check_location: function (lat, lon) {
      window.viewer.camera.flyTo({
            destination: Cesium.Cartesian3.fromDegrees(lon, lat, 15000.0),
            orientation: {
              heading: Cesium.Math.toRadians(175.0),
              pitch: Cesium.Math.toRadians(-35.0),
              roll: 0.0
            }
          }
      )
    },
    check_back: function () {
      window.viewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(125.1, 47.15, 17000000),
        orientation: {
          heading: Cesium.Math.toRadians(0),
          pitch: Cesium.Math.toRadians(-90),
          roll: Cesium.Math.toRadians(0)
        }
      })
    },
    create_box: function () {
      var redBox = viewer.entities.add({
        name: 'Red box with black outline',
        position: Cesium.Cartesian3.fromDegrees(107.0, 40.0, 300000.0),
        box: {
          dimensions: new Cesium.Cartesian3(400000.0, 30000.0, 50000.0),
          material: Cesium.Color.RED.withAlpha(0.5),
          outline: true,
          outlineColor: Cesium.Color.BLACK
        }
      });

      window.viewer.zoomTo(redBox);
    }

  },


}
</script>
