<template>
  <div
    style="z-index: 100; float: right;width: 200px; padding:5px;margin: 5px; height:80vh;background:rgba(50, 50 ,50, 0.8);position: absolute;border-radius: 4px">

    <form action="">

      <fieldset style="border: none;">

        <div class="button blue" v-on:click.stop.prevent="initTileset()">
          <div class="shine"></div>
          南京大雁塔
        </div>
        <div class="button blue" v-on:click.stop.prevent="initCCjz()">
          <div class="shine"></div>
          长春建筑3dtiles
        </div>
        <br/>
        <div class="button blue" v-on:click.stop.prevent="initGltf()">
          <div class="shine"></div>
          GLTF
        </div>
        <p/>
        <div class="button blue" v-on:click.stop.prevent="create_box()">
          <div class="shine"></div>
          添加形状
        </div>
        <div class="button blue" v-on:click.stop.prevent="initCCjson()">
          <div class="shine"></div>
          长春建筑 geojson
        </div>
      </fieldset>
    </form>


  </div>
  <div id="cesiumContainer" ref="cesiumContainer"></div>
</template>

<script>
import {onMounted} from "vue";
import * as Cesium from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";

export default {
  setup() {
    Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiZGI4N2U5My0xMTc0LTQyMGItODUyOC0xOWI3MDZiNDNiZDAiLCJpZCI6ODE1OCwiaWF0IjoxNjg0NzIxNDUyfQ.Q4YUWO824I1zUnMuOadI4arml8Xc8vBcuC_I7VdadVA'

    window.CESIUM_BASE_URL = "/Cesium/";
    let viewer = null
    onMounted(() => {
       viewer = new Cesium.Viewer("cesiumContainer", {
        // 是否显示信息窗口
        // infoBox: false,
        // 是否创建动画
        animation: false,
        // 是否显示图层选择器
        baseLayerPicker: false,
        // 是否显示全屏按钮
        fullscreenButton: false,
        // 是否显示右上角的查询按钮
        geocoder: false,
        // 是否显示HOME按钮
        homeButton: false,
        // 是否显示场景控制按钮
        sceneModePicker: false,
        // 是否显示帮助按钮
        navigationHelpButton: false,
        // 是否显示时间轴
        timeline: false,
      });

      // 设置沙箱允许使用JS
      var iframe = document.getElementsByClassName("cesium-infoBox-iframe")[0];
      iframe.setAttribute(
        "sandbox",
        "allow-same-origin allow-scripts allow-popups allow-forms"
      );
      iframe.setAttribute("src", "");

      // // 隐藏cesiumLogo
      viewer.cesiumWidget.creditContainer.style.display = "none";

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



    });
  function create_box() {
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

      viewer.zoomTo(redBox);
    }
    function initCCjz() {

      var tileset = new Cesium.Cesium3DTileset({url: './data/tiles/tileset.json'})
      // tileset.style = new Cesium.Cesium3DTileStyle({
      //   color:'#f00'
      // })

      tileset.readyPromise.then(function (argument) {

        // tileset.style = new Cesium.Cesium3DTileStyle({
        //   color: {
        //     conditions: [
        //
        //       ["${height} >= 30", "rgba(45, 0, 75, 0.5)"],
        //       ["${height} >= 24", "rgb(102, 71, 151)"],
        //       ["${height} >= 18", "rgb(170, 162, 204)"],
        //       ["${height} >= 12", "rgb(224, 226, 238)"],
        //       ["${height} >= 8", "rgb(252, 230, 200)"],
        //       ["${height} >= 5", "rgb(248, 176, 87)"],
        //       ["${height} >= 3", "rgb(198, 106, 11)"],
        //       ["true", "rgb(127, 59, 8)"],
        //     ]
        //   }
        // })
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


      viewer.scene.primitives.add(tileset);
      viewer.flyTo(tileset)
      window.baiMoObject = tileset
    }


    function initCCjson() {
      viewer.scene.primitives.remove(window.baiMoObject);
      var promise = Cesium.GeoJsonDataSource.load('./data/cc.geojson', {clampToGround: true})

      promise.then(function (dataSources) {
        viewer.dataSources.add(dataSources)
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
      viewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(125.1, 47.15, 17000000),
        orientation: {
          heading: Cesium.Math.toRadians(0),
          pitch: Cesium.Math.toRadians(-90),
          roll: Cesium.Math.toRadians(0)
        }
      })
      window.geojsn = promise
    }


    function initGltf() {
      var entity = viewer.entities.add({
        position: Cesium.Cartesian3.fromDegrees(
          148.9819,
          -35.3981,
        ),
        model: {
          uri: "https://docs.mapbox.com/mapbox-gl-js/assets/34M_17/34M_17.gltf",
        }
      });
      viewer.zoomTo(entity)
    }

    function initGsonshifq() {

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
    }


    function initTileset() {

      var tileset = viewer.scene.primitives.add(
       new Cesium.Cesium3DTileset({
          url: 'https://earthsdk.com/v/last/Apps/assets/dayanta/tileset.json'
        })
      );


      tileset.readyPromise.then(function () {
     
        viewer.camera.viewBoundingSphere(tileset.boundingSphere, new Cesium.HeadingPitchRange(0, -0.5, 0));
        viewer.camera.lookAtTransform(Cesium.Matrix4.IDENTITY);
      });

    }

    return {
      initCCjz,
      initCCjson,
      initGltf,
      initGsonshifq,
      initTileset,
      create_box,
    }
  }

}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#cesiumContainer {
  width: 84vw;
  height: 89.6vh;
}
.button {
  min-height: 0.5em;
  display: inline-block;
  padding: 8px;
  margin: 7px;
  cursor: pointer;
  opacity: 0.9;

  color: #FFF;
  font-size: 14px;
  font-weight: bold;
  letter-spacing: 1px;
  text-shadow: rgba(0,0,0,1) 0px 1px 2px;

  background: #434343;
  border: 1px solid #242424;

  -webkit-border-radius: 4px;
  -khtml-border-radius: 4px;
  -moz-border-radius: 4px;
  -o-border-radius: 4px;
  border-radius: 4px;
  -webkit-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -khtml-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -moz-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -o-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -webkit-transition: all 0.1s linear;
  -khtml-transition: all 0.1s linear;
  -moz-transition: all 0.1s linear;
  -o-transition: all 0.1s linear;
  transition: all 0.1s linear;
}
.button:hover {
  -webkit-box-shadow: rgba(0,0,0,0.5) 0px 2px 5px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -khtml-box-shadow: rgba(0,0,0,0.5) 0px 2px 5px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -moz-box-shadow: rgba(0,0,0,0.5) 0px 2px 5px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -o-box-shadow: rgba(0,0,0,0.5) 0px 2px 5px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  box-shadow: rgba(0,0,0,0.5) 0px 2px 5px, inset rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(0,0,0,0.25) 0px 0px 0px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
}
.button:active {
  -webkit-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px,inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -khtml-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px,inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -moz-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  -o-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
}
.shine {
  z-index: 999;
  display: block;
  position: relative;
  background: -moz-linear-gradient(left, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 50%, rgba(255,255,255,0) 100%);
  background: -webkit-gradient(linear, left top, right top, color-stop(0%,rgba(255,255,255,0)), color-stop(50%,rgba(255,255,255,1)), color-stop(100%,rgba(255,255,255,0)));
  background: -webkit-linear-gradient(left, rgba(255,255,255,0) 0%,rgba(255,255,255,1) 50%,rgba(255,255,255,0) 100%);
  background: -o-linear-gradient(left, rgba(255,255,255,0) 0%,rgba(255,255,255,1) 50%,rgba(255,255,255,0) 100%);
  background: -ms-linear-gradient(left, rgba(255,255,255,0) 0%,rgba(255,255,255,1) 50%,rgba(255,255,255,0) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#00ffffff', endColorstr='#00ffffff',GradientType=1 );
  background: linear-gradient(left, rgba(255,255,255,0) 0%,rgba(255,255,255,1) 50%,rgba(255,255,255,0) 100%);
  padding: 0px 12px;
  top: -12px;
  left: -24px;
  height: 1px;
  -webkit-box-shadow: rgba(255,255,255,0.2) 0px 1px 5px;
  -khtml-box-shadow: rgba(255,255,255,0.2) 0px 1px 5px;
  -moz-box-shadow: rgba(255,255,255,0.2) 0px 1px 5px;
  -o-box-shadow: rgba(255,255,255,0.2) 0px 1px 5px;
  box-shadow: rgba(255,255,255,0.2) 0px 1px 5px;
  -webkit-transition: all 0.3s ease-in-out;
  -khtml-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}
.button:hover .shine {left: 24px;}
.button:active .shine {opacity: 0;}

.button.gray {background: #555;}
.button.blue {background: #3a617e;}
.button.green {background: #477343;}
.button.red {background: #723131;}
.button.purple {background: #4b3f5e;}
.button.orange {background: #624529;}
.button.info {background: #309e70;}
.button.primay {background: #337ab7;;}
.button {
  &.activity {
    //background: #204d74;
    -webkit-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px,inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
    -khtml-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px,inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
    -moz-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
    -o-box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
    box-shadow: rgba(255,255,255,0.25) 0px 1px 0px, inset rgba(255,255,255,0) 0px 1px 0px, inset rgba(0,0,0,0.5) 0px 0px 5px, inset rgba(255,255,255,0.03) 0px 20px 0px, inset rgba(0,0,0,0.15) 0px -20px 20px, inset rgba(255,255,255,0.05) 0px 20px 20px;
  }}
.blue{
  &.activity {
    background: #122b40;}
}
.green{
  &.activity {
    background: #3c763d;}
}

</style>
