<template>
  <q-layout view="hHh lpR fFf">

    <EssentialHead />

    <q-drawer show-if-above v-model="store.leftDrawerOpen" side="left" bordered>


      <q-list>
        <q-item-label header>
          页面三

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

  import {useCommonFunctionStore} from 'stores/common_function'
const linksList = [
  {
    title: '长春3维可视化',
    caption: '长春建筑3维展示',
    icon: 'school',
    link: '/mapbox/index'
  },
    {
    title: '加载GLTF',
    caption: '加载GLTF数据展示',
    icon: 'school',
    link: '/mapbox/gltf'
  },
   {
    title: '基础实例',
    caption: 'Mapbox简单基础示例',
    icon: 'school',
    link: '/mapbox/bmapbox'
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
