<template>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>


      <q-list>
        <q-item-label
          header
        >
          Essential Links
        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>


</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import EssentialLink from 'components/EssentialLink.vue';

const linksList = [
  {
    title: 'Home',
    caption: '内容介绍说明',
    icon: 'school',
    link: '/'
  },
  {
    title: 'Leaflet',
    caption: '轻量级WebGIS类库',
    icon: 'code',
    link: '/#/sleaflet'
  },
  {
    title: 'OpenLayers',
    caption: '全能型WebGIS类库',
    icon: 'chat',
    link: '/#/sopenlayers'
  },
  {
    title: 'MapTalks',
    caption: 'Developed in China',
    icon: 'record_voice_over',
    link: '/#/smaptalks'
  },
  {
    title: 'MapBox',
    caption: '精美地图',
    icon: 'rss_feed',
    link: '/#/smapbox'
  },

  {
    title: 'Cesium',
    caption: '开源的3D GIS',
    icon: 'favorite',
    link: '/#/scesium'
  }
];

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
});
</script>
