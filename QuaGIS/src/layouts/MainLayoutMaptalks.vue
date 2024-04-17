<template>
  <q-layout view="hHh lpR fFf">

    <EssentialHead />

    <q-drawer show-if-above v-model="store.leftDrawerOpen" side="left" bordered>


      <q-list>
        <q-item-label header>
          Maptalks Links
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
    title: 'Example 1',
    caption: '内容介绍说明',
    icon: 'school',
    link: '/maptalks/index'
  },
   {
    title: '3D',
    caption: '内容介绍说明',
    icon: 'school',
    link: '/maptalks/three'
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
