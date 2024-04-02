<template>

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
        destination: Cesium.Cartesian3.fromDegrees(125.1, 47.15, 1700000),
        orientation: {
          heading: Cesium.Math.toRadians(0),
          pitch: Cesium.Math.toRadians(-90),
          roll: Cesium.Math.toRadians(0)
        }
      })

    });
    return {
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



</style>
