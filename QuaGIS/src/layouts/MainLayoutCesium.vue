<template>
  <q-layout view="hHh lpR fFf">

    <EssentialHead />

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>


      <q-list>
        <q-item-label header>
          页面三
          Essential Links
        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>

  </q-layout>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue';
import EssentialLink from 'components/EssentialLink.vue';
import  EssentialHead from 'components/Head.vue';

const linksList = [
  {
    title: 'CMZL',
    caption: '加载CZML格式数据图形',
    icon: 'school',
    link: '/#/cesium/index'
  },
  {
    title: 'GLTF',
    caption: '加载GLTF 3D数据',
    icon: 'school',
    link: '/#/cesium/gltf'
  },
  {
    title: '长春建筑geojson',
    caption: '加载长春建筑Geojson格式数据',
    icon: 'school',
    link: '/#/cesium/ccjson'
  },
   {
    title: '南京大雁塔',
    caption: '加载南京大雁塔3D模型',
    icon: 'school',
    link: '/#/cesium/nanjing'
  },
];

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    EssentialHead
  },

  setup() {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
});
</script>
