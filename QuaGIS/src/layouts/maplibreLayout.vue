<template>
  <q-layout view="hHh lpR fFf">

 <EssentialHead />

    <q-drawer show-if-above v-model="store.leftDrawerOpen" side="left" bordered>


      <q-list>
        <q-item-label header>

          MAPLIBRE-GL

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
import EssentialHead from "components/Head.vue";
  import {useCommonFunctionStore} from 'stores/common_function'

const linksList = [
  {
    title: '3D街道地图',
    caption: '示例1',
    icon: 'school',
    link: '/maplibre/index'
  },
  {
    title: '添加地图自带控件',
    caption: '示例2',
    icon: 'school',
    link: '/maplibre/demo2'
  },
  {
    title: '添加常用地图操作',
    caption: '示例3',
    icon: 'school',
    link: '/maplibre/demo3'
  },
  {
    title: '为线条添加动画效果',
    caption: '为线条添加动画效果',
    icon: 'school',
    link: '/maplibre/demo4'
  },
  {
    title: '',
    caption: '示例5',
    icon: 'school',
    link: '/maplibre/demo5'
  },
  {
    title: '',
    caption: '示例6',
    icon: 'school',
    link: '/maplibre/demo6'
  },
  {
    title: '',
    caption: '示例7',
    icon: 'school',
    link: '/maplibre/demo7'
  },
  {
    title: '',
    caption: '示例8',
    icon: 'school',
    link: '/maplibre/demo8'
  },
  {
    title: '',
    caption: '示例9',
    icon: 'school',
    link: '/maplibre/demo9'
  },



];

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialHead,
    EssentialLink
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
