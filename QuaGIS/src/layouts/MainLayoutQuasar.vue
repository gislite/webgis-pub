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
    title: 'Home',
    caption: '内容介绍说明',
    icon: 'school',
    link: '/#/quasar'
  },
  {
    title: 'Form',
    caption: 'Quasar表单值组成JSOn',
    icon: 'code',
    link: '/#/quasar/form'
  },
  {
    title: 'GetJson',
    caption: 'Axios库的使用',
    icon: 'chat',
    link: '/#/quasar/json'
  },
  {
    title: 'Three',
    caption: '3D using ThreeJS.',
    icon: 'record_voice_over',
    link: '/#/quasar/three'
  },

 {
    title: 'Vedio',
    caption: 'Show Vedio in Web',
    icon: 'record_voice_over',
    link: '/#/quasar/video'
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
