<template>
  <q-layout view="hHh lpR fFf">

    <EssentialHead/>

    <q-drawer show-if-above v-model="store.leftDrawerOpen" side="left" bordered>


      <q-list>
        <q-item-label header>
          页面三

        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"/>
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
import EssentialHead from "components/Head.vue";

  import {useCommonFunctionStore} from 'stores/common_function'
const linksList = [
  {
    title: 'Home',
    caption: '内容介绍说明',
    icon: 'school',
    link: '/#/openlayers/index'
  },
  {
    title: 'OpenLayers基础',
    caption: 'OpenLayers基础',
    icon: 'code',
    link: '/#/openlayers/ol1'
  },
  {
    title: 'OpenLayers底图',
    caption: '换用天地图底图',
    icon: 'code',
    link: '/#/openlayers/ol2'
  },

];

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    EssentialHead
  },

  setup() {

      const store = useCommonFunctionStore();
    return {
      essentialLinks: linksList,
  store

    }
  }
});
</script>
