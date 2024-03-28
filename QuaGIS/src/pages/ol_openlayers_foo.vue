<template>
  <div id="app">
    <MapView/>
  </div>
</template>

<script>
import MapView from './utils/ol_mapview.vue'

export default {
  name: 'App',
  components: {
    MapView
  }
}
</script>

<style>
html, body {
  padding: 0;
  margin: 0;
  height: 100%;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}
</style>
