<template>

    <div id="cesiumContainer"></div>

</template>

<script>
import * as Cesium from 'cesium/Build/Cesium'
import 'cesium/Build/Cesium/Widgets/widgets.css'

export default {
  name: 'CesiumViewer',
  mounted() {
    this.init()
  },
  methods: {
    init:function () {
      Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiZGI4N2U5My0xMTc0LTQyMGItODUyOC0xOWI3MDZiNDNiZDAiLCJpZCI6ODE1OCwiaWF0IjoxNjg0NzIxNDUyfQ.Q4YUWO824I1zUnMuOadI4arml8Xc8vBcuC_I7VdadVA'
      const viewer = new Cesium.Viewer('cesiumContainer', {

        geocoder: false, // 是否显示地理编码器
        homeButton: false, // 是否显示Home按钮
        sceneModePicker: true, // 是否显示场景模式选择器
        navigationHelpButton: false, // 是否显示帮助按钮
        animation: false, // 是否显示动画控件
        timeline: false, // 是否显示时间线控件
        fullscreenButton: false, // 是否显示全屏按钮
        baseLayerPicker: false, // 是否显示图层选择器
        navigationInstructionsInitiallyVisible: false, // 导航指令是否最初可见
        scene3DOnly: true, // 是否仅显示3D场景
        selectedImageryProviderViewModel: undefined, // 地图选择器的默认提供商

      })
      // 你可以在这里添加更多的Cesium Viewer配置和逻辑
    }
  }
}
</script>

