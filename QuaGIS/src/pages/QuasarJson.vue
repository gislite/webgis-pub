<template>
  <div class="q-pa-md">
    <div class="q-gutter-md" style="max-width: 300px">


      <q-btn @click=ss.increment>{{ ss.counter }}</q-btn>
    </div>
    <div>{{ idx }}</div>
    <div>{{ info.data }}</div>
    <ul>
      <li v-for='product in info.data' v-bind:key='product'> {{ product }}</li>
    </ul>
  </div>
</template>

<script>
// import counter from '../stores/example-store'
import axios from 'axios'
import {defineComponent} from 'vue'
import {useCounterStore} from '../stores/store-foo'

// const $s = useCounterStore()

export default defineComponent({


  data() {
    return {
      ss: useCounterStore(),
      idx: 1,
      info: {'data': 'Hello'},
    }
  },
  mounted() {
    this.intervalId = setInterval(() => {
      this.idx = this.idx + 1;
      this.ss.increment();
    }, 1000 * 1);

    axios
      .get('http://www.igadc.cn/htjson/qx/recent')
      .then(
        response => (this.info = response)
      )
      .catch(function (error) {
        // 请求失败处理
        console.log(error);
      });
  },
  beforeUnmount() {
    clearInterval(this.intervalId);
  },
})
</script>
