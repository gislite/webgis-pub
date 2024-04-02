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
     try {
        var tileset = Cesium.Cesium3DTileset.fromUrl('https://earthsdk.com/v/last/Apps/assets/dayanta/tileset.json');

        // var tileset = viewer.scene.primitives.add(
        //   new Cesium.Cesium3DTileset({
        //     url: 'https://earthsdk.com/v/last/Apps/assets/dayanta/tileset.json'
        //   })
        // );


        tileset.then(function (tileset) {
          viewer.scene.primitives.add(tileset);
          viewer.camera.viewBoundingSphere(tileset.boundingSphere, new Cesium.HeadingPitchRange(0, -0.5, 0));
          viewer.camera.lookAtTransform(Cesium.Matrix4.IDENTITY);
        });
      } catch (error) {
        console.log(error)
      }


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
