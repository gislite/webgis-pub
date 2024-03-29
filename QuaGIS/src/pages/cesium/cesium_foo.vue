<template>
  <div id="cesiumContainer" ref="cesiumContainer"></div>
</template>

<script setup>
import { onMounted } from "vue";
import * as Cesium from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";

Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiZGI4N2U5My0xMTc0LTQyMGItODUyOC0xOWI3MDZiNDNiZDAiLCJpZCI6ODE1OCwiaWF0IjoxNjg0NzIxNDUyfQ.Q4YUWO824I1zUnMuOadI4arml8Xc8vBcuC_I7VdadVA'

window.CESIUM_BASE_URL = "/Cesium/";


onMounted(() => {
  var viewer = new Cesium.Viewer("cesiumContainer", {
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

      window.viewer = viewer;
});


</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#cesiumContainer {
  width: 100vw;
  height: 100vh;
}
</style>
