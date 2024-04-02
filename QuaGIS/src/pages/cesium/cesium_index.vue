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
        var tileset = Cesium.Cesium3DTileset.fromUrl({url: './data/tiles/tileset.json'})
        // tileset.style = new Cesium.Cesium3DTileStyle({
        //   color:'#f00'
        // })

        tileset.then(function (argument) {
          viewer.scene.primitives.add(tileset);
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

      } catch (error) {
        console.log(error)
      }


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


    });


    return {}
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
