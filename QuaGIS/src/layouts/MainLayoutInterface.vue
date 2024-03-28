<template>
  <q-layout view="hHh lpR fFf">

    <EssentialHead/>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>


      <q-list>
        <q-item-label header>
          Interface
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
import EssentialHead from 'components/Head.vue';

const linksList = [
  {
    title: 'metalist',
    caption: 'Metadata List',
    icon: 'school',
    link: '/#/interface/metalist'
  },
  {
    title: 'meta',
    caption: 'Metadata Dictionary interface',
    icon: 'school',
    link: '/#/interface/meta_dic'
  },
  {
    title: 'storage',
    caption: 'Storage system',
    icon: 'code',
    link: '/#/interface/storage'
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
