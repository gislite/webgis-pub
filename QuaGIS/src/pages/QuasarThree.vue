<template>
  <p><b>说明</b></p>
  <p>使用了一个项目，结合了VueJS3, ThreeJS, Vite 。资源文件放到 <code>public</code> 文件夹。</p>
  <p>https://github.com/troisjs/trois</p>
  <p>https://troisjs.github.io/guide/install.html</p>
  <p>https://troisjs.github.io/examples/models/gltf.html</p>
  <Renderer ref="renderer" antialias :orbit-ctrl="{ enableDamping: true }" resize>
    <Camera :position="{ x: 1, y: 0, z: 0 }" />
    <Scene>
      <AmbientLight></AmbientLight>
      <GltfModel src="/scene.gltf" />
    </Scene>
  </Renderer>
</template>

<script>
import {
  AmbientLight,
  Camera,
  GltfModel,
  Renderer,
  Scene,
} from 'troisjs';
export default {
  components: {
    AmbientLight,
    Camera,
    GltfModel,
    Renderer,
    Scene,
  },
};
</script>
