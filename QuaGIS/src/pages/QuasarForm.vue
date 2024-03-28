<template>
  <div class="q-pa-md">
    <div class="q-gutter-md" style="max-width: 300px">
      <q-input v-model="text" label="Standard"/>
      <q-input filled v-model="txt1" label="Filled"/>

      <q-input outlined v-model="txt2" label="Outlined"/>

      <q-input standout v-model="text" label="Standout"/>

      <q-input standout="bg-teal text-white" v-model="text" label="Custom standout"/>

      <q-input borderless v-model="text" label="Borderless"/>

      <q-input rounded filled v-model="text" label="Rounded filled"/>

    </div>
    <q-btn @click=ss.increment >{{ ss.counter }}</q-btn>
    <div>{{ info }}</div>
  </div>
</template>


<script>
import {defineComponent} from 'vue'
import {useCounterStore} from '../stores/store-foo'

export default defineComponent({



  data() {

    return {
      ss: useCounterStore(),
      txt1: 1,
      txt2: 2,
      text: 'text',
      info: {'txt1': 1, 'txt2': 2}
    }
  },

  watch: {
    txt1() {
      this.info['txt1'] = this.txt1;
    },
    txt2() {
      this.info['txt2'] = this.txt2
    }
  }

})
</script>
