<template>
  <q-page class="row items-center justify-evenly">
    <div id="center_jfv" class="full-width">

      <div
        class="sidebar"
        :class="{ 'collapsed': isCollapsed }"
        @mouseenter="hoverExpand"
        @mouseleave="hoverCollapse"
      >
        <div class="sidebar-header" @click="toggleCollapse">
          <legend>
            <h3>
              <i class="icon-menu">≡</i>
              <span v-if="!isCollapsed">学科组列表</span>
            </h3>
          </legend>
        </div>

        <hr v-if="!isCollapsed" style="margin: 8px auto"/>

        <div class="sidebar-content">

          <div class="top-buttons">
            <q-btn
              flat
              class="button blue"
              :class="{activity:value==='1'}"
              @click.stop.prevent="get_group_by_grouptype('1','1')">
              <i class="icon-group">👥</i>
              <span v-if="!isCollapsed">学科组</span>
            </q-btn>

            <q-btn
              flat
              class="button blue"
              :class="{activity:value==='8'}"
              @click.stop.prevent="get_group_by_grouptype('8','4')">
              <i class="icon-office">🏢</i>
              <span v-if="!isCollapsed">所领导办公室</span>
            </q-btn>

            <q-btn
              flat
              class="button blue"
              :class="{activity:value==='2'}"
              @click.stop.prevent="get_group_by_grouptype('2','2')">
              <i class="icon-management">📊</i>
              <span v-if="!isCollapsed">管理支撑部门</span>
            </q-btn>

            <q-btn
              flat
              class="button blue"
              :class="{activity:value==='5'}"
              @click.stop.prevent="get_group_by_grouptype('5','5')">
              <i class="icon-other">⋯</i>
              <span v-if="!isCollapsed">其他</span>
            </q-btn>

            <q-btn
              flat
              class="button blue"
              :class="{activity:value==='6'}"
              @click.stop.prevent="get_group_by_grouptype('6','')">
              <i class="icon-all">☰</i>
              <span v-if="!isCollapsed">全部</span>
            </q-btn>

            <q-btn
              flat
              class="button blue"
              :class="{activity:value==='7'}"
              @click.stop.prevent="get_no_group('7','2')">
              <i class="icon-empty">🪑</i>
              <span v-if="!isCollapsed">空房间</span>
            </q-btn>
          </div>

          <hr v-if="!isCollapsed" style="margin:10px auto"/>


          <div v-show="'1'===menu" class="group-list-scrollable">
            <div class="group-list-inner">
              <template v-for="(item,index) in group_type_list" :key="index">
                <q-btn
                  flat
                  class="button green"
                  :class="{activity:value===item.id}"
                  @click.stop.prevent="get_group_content(item.id,item.title)">
                  <div class="shine"></div>
                  <i class="icon-item">•</i>
                  <span v-if="!isCollapsed">{{ item.title }}</span>
                </q-btn>
              </template>
            </div>
          </div>
        </div>

        <div class="sidebar-toggle" @click="toggleCollapse">
          <i>{{ isCollapsed ? '❯' : '❮' }}</i>
        </div>

      </div>


      <transition name="slide-fade">
        <div v-if="!isContentCollapsed" class="content" :class="{activity:content==='content'}">
          <div v-show="group_true_room==='1'">
            <h3>学科组名称: {{ grouptitle }} (房间数量总计：{{ room_group_list.length || 0 }})</h3>
            <q-btn
              class="button orange"
              style="float:right"
              @click.stop.prevent="toggleContentCollapse()">
              折叠
            </q-btn>
            <q-table
              :rows="room_group_list"
              :columns="roomColumns"
              flat
              bordered
              class="table"
            />
          </div>
          <div v-show="group_true_room==='2'">
            <h3>空房间 (房间数量总计：{{ not_group_list?.length || 0 }})</h3>
            <q-btn
              class="button orange"
              style="float:right"
              @click.stop.prevent="toggleContentCollapse()">
              折叠
            </q-btn>
            <q-table
              :rows="not_group_list"
              :columns="roomColumns"
              flat
              bordered
              class="table"
            />
          </div>
        </div>
      </transition>

      <div v-if="isContentCollapsed" class="expand-btn-wrapper">
        <q-btn
          class="button blue"
          @click.stop.prevent="toggleContentCollapse()">
          <div class="shine"></div>
          展开详情
        </q-btn>
      </div>

      <transition name="fade">
        <div v-if="sf_echarts === 'sf_echarts'" class="sf_echarts activity">
          <tables/>
        </div>
      </transition>

      <div class="sf_echarts_btn">
        <q-btn
          class="button blue"
          @click.stop.prevent="toggleSfEcharts()">
          <div class="shine"></div>
          {{ sf_echarts === 'sf_echarts' ? '关闭统计数据图表' : '打开统计数据图表' }}
        </q-btn>
      </div>

      <div class="bottom-buttons row justify-center">
        <q-btn
          v-for="(building, index) in buildings"
          :key="index"
          flat
          class="bottom-btn"
          @click="update_geojson(building.id, building.center)">
          {{ building.name }}
        </q-btn>
      </div>

      <div ref="mapContainer" class="map-container"></div>
    </div>
  </q-page>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import axios from "axios";
import maplibregl from 'maplibre-gl';
import MaplibreGeocoder from '@maplibre/maplibre-gl-geocoder';
import 'maplibre-gl/dist/maplibre-gl.css';
import '@maplibre/maplibre-gl-geocoder/dist/maplibre-gl-geocoder.css';
import tables from './pn_table.vue';

export default {
  components: {
    tables
  },

  setup() {
    const mapContainer = ref(null)
    const map = ref(null)
    const geojsonSource = ref(null)
    const highlightLayer = ref(null)

    const isCollapsed = ref(true)
    const hoverTimer = ref(null)
    const isContentCollapsed = ref(true)
    const sf_echarts = ref('')
    const content = ref('')
    const groupvalue = ref('')
    const menu = ref('')

    const buildings = ref([
      { id: '综合', name: '综合楼', center: [125.392671, 43.999015] },
      { id: '环境', name: '环境楼', center: [125.393695, 43.999015] },
      { id: '湿地', name: '湿地楼', center: [125.394527, 43.999015] },
      { id: '成果', name: '成果楼', center: [125.396324, 43.999015] },
      { id: '农业', name: '农业楼', center: [125.395482, 43.999015] },
      { id: '种质', name: '种质楼', center: [125.397358, 43.999015] },
      { id: '农机', name: '农机楼', center: [125.398165, 43.999015] },
      { id: '', name: '全部', center: [125.394398, 43.999015] }
    ])

    const roomColumns = ref([
      { name: 'building', label: '所属楼', field: 'building', align: 'left' },
      { name: 'num', label: '房间号', field: 'num', align: 'left' },
      { name: 'areafloat', label: '面积', field: 'areafloat', align: 'left' },
      { name: 'staff', label: '备注', field: 'staff', align: 'left' },
      { name: 'staff_num', label: '人员数量', field: 'staff_num', align: 'left' }
    ])

    const group_type_list = ref([])
    const room_group_list = ref([])
    const not_group_list = ref([])
    const grouptitle = ref('')
    const group_true_room = ref('1')
    const highlightRooms = ref(null)
    const building = ref(null)
    const pnameGeoJSON = ref(null)
    const cachedGeoJSON = ref(null)

    const initMap = () => {
      map.value = new maplibregl.Map({
        container: mapContainer.value,
        style: 'https://demotiles.maplibre.org/style.json',
        center: [125.394698, 43.999425],
        zoom: 18,
        maxZoom: 22
      })

      map.value.addControl(new maplibregl.NavigationControl())
      map.value.addControl(new maplibregl.ScaleControl({
        maxWidth: 100,
        unit: 'metric'
      }))
      map.value.addControl(new MaplibreGeocoder({
        maplibregl: maplibregl,
        placeholder: '搜索地点'
      }))

      map.value.on('load', () => {
        fetchAndCacheGeoJSON()
        fetchPnameGeoJSON()
      })
    }

    const fetchAndCacheGeoJSON = async () => {
      try {
        const response = await fetch('https://martin.igadc.cn/')
        cachedGeoJSON.value = await response.json()
        init_geojson(building.value, highlightRooms.value)
      } catch (error) {
        console.error('加载 GeoJSON 失败:', error)
      }
    }

    const fetchPnameGeoJSON = async () => {
      try {
        const response = await fetch('https://martin.igadc.cn/pname/')
        pnameGeoJSON.value = await response.json()
        initPnameLayer()
      } catch (error) {
        console.error('加载 Pname GeoJSON 失败:', error)
      }
    }

    const initPnameLayer = () => {
      if (!pnameGeoJSON.value || !map.value) return

      map.value.addSource('pname-source', {
        type: 'geojson',
        data: pnameGeoJSON.value
      })

      map.value.addLayer({
        id: 'pname-layer',
        type: 'circle',
        source: 'pname-source',
        paint: {
          'circle-radius': 0.2,
          'circle-opacity': 0
        }
      })

      map.value.on('click', 'pname-layer', (e) => {
        if (e.features[0].properties?.roomid) {
          new maplibregl.Popup()
            .setLngLat(e.lngLat)
            .setHTML(`<div><b>名称:</b> ${e.features[0].properties.roomid}</div>`)
            .addTo(map.value)
        }
      })
    }

    const init_geojson = (buildingFilter, highlightRooms) => {
      if (!cachedGeoJSON.value) {
        console.warn('GeoJSON data not loaded yet')
        return
      }

      const data = JSON.parse(JSON.stringify(cachedGeoJSON.value))
      if (buildingFilter) {
        data.features = data.features.filter(feature => {
          return feature.properties && feature.properties.floor.substring(0, 2) === buildingFilter
        })
      }

      if (map.value.getLayer('geojson-layer')) {
        map.value.removeLayer('geojson-layer')
        map.value.removeSource('geojson-source')
      }

      map.value.addSource('geojson-source', {
        type: 'geojson',
        data: data
      })

      const areaColors = {
        '会议室': '#4285F4',
        '展厅': '#EA4335',
        '卫生间': '#34A853',
        '实验室': '#FBBC05',
        '楼梯间': '#78909C',
        '电梯间': '#B0BEC5',
        '走廊': '#FF9800',
        '大厅': '#FF9800'
      }

      map.value.addLayer({
        id: 'geojson-layer',
        type: 'fill',
        source: 'geojson-source',
        paint: {
          'fill-color': [
            'match',
            ['get', 'name'],
            ...Object.entries(areaColors).flat(),
            '#fd8788'
          ],
          'fill-opacity': 0.8,
          'fill-outline-color': '#222'
        }
      })

      if (highlightLayer.value) {
        map.value.removeLayer('highlight-layer')
        map.value.removeSource('highlight-source')
      }

      if (highlightRooms && highlightRooms.length > 0) {
        const highlightFeatures = data.features.filter(feature =>
          highlightRooms.includes(feature.properties.label)
        )

        map.value.addSource('highlight-source', {
          type: 'geojson',
          data: {
            type: 'FeatureCollection',
            features: highlightFeatures
          }
        })

        highlightLayer.value = map.value.addLayer({
          id: 'highlight-layer',
          type: 'fill',
          source: 'highlight-source',
          paint: {
            'fill-color': '#2b35fb',
            'fill-opacity': 0.7,
            'fill-outline-color': '#666'
          }
        })
      }

      map.value.on('click', 'geojson-layer', async (e) => {
        try {
          const feature = e.features[0]
          const floor_num = feature.properties.floor_num || feature.properties.label

          const loadingPopup = new maplibregl.Popup()
            .setLngLat(e.lngLat)
            .setHTML('<div style="padding:10px;">加载中...</div>')
            .addTo(map.value)

          const response = await axios.get(`https://cms.igadc.cn/iga_room/?floor_num=${floor_num}`)
          loadingPopup.remove()

          if (response.data && response.data[0]) {
            const roomData = response.data[0]
            new maplibregl.Popup()
              .setLngLat(e.lngLat)
              .setHTML(`
                <div style="min-width:200px;padding:10px;">
                  <h4 style="margin-top:0;">${roomData.title || '未知房间'}</h4>
                  <p><b>所属楼：</b>${roomData.building || '无'}</p>
                  <p><b>所属楼层：</b>${roomData.floor?.num ? `${roomData.floor.num}楼` : '无'}</p>
                  <p><b>所属学科组：</b>${roomData.group?.[0]?.title || '无学科组'}</p>
                  <p><b>人员信息：</b>${roomData.staff || '无'}</p>
                  <p><b>人员数量：</b>${roomData.staff_num || '0'}</p>
                </div>
              `)
              .addTo(map.value)
          }
        } catch (error) {
          console.error('API请求失败:', error)
          new maplibregl.Popup()
            .setLngLat(e.lngLat)
            .setHTML('<div style="padding:10px;color:red;">数据加载失败</div>')
            .addTo(map.value)
        }
      })

      map.value.on('mouseenter', 'geojson-layer', () => {
        map.value.getCanvas().style.cursor = 'pointer'
      })

      map.value.on('mouseleave', 'geojson-layer', () => {
        map.value.getCanvas().style.cursor = ''
      })
    }

    const update_geojson = (value, center) => {
      building.value = value
      if (map.value) {
        map.value.flyTo({
          center: center,
          zoom: 18
        })
        init_geojson(value, highlightRooms.value)
      }
    }

    const toggleCollapse = () => {
      isCollapsed.value = !isCollapsed.value
      clearTimeout(hoverTimer.value)
    }

    const hoverExpand = () => {
      if (isCollapsed.value) {
        clearTimeout(hoverTimer.value)
        hoverTimer.value = setTimeout(() => {
          isCollapsed.value = false
        }, 200)
      }
    }

    const hoverCollapse = () => {
      if (!isCollapsed.value) {
        clearTimeout(hoverTimer.value)
      }
    }

    const toggleContentCollapse = () => {
      isContentCollapsed.value = !isContentCollapsed.value
      if (!isContentCollapsed.value) {
        content.value = 'content'
      }
    }

    const toggleSfEcharts = () => {
      sf_echarts.value = sf_echarts.value === 'sf_echarts' ? '' : 'sf_echarts'
    }

    const get_group = () => {
      axios.get('https://cms.igadc.cn/iga_group/')
        .then(response => {
          group_type_list.value = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }

    const get_no_group = (val) => {
      content.value = 'content'
      isContentCollapsed.value = false
      group_true_room.value = '2'
      groupvalue.value = val

      axios.get('https://cms.igadc.cn/iga_room/?empty_room=true')
        .then(response => {
          not_group_list.value = response.data
          highlightRooms.value = not_group_list.value.map(room => room.floor_num.toString())
          init_geojson(building.value, highlightRooms.value)
        })
        .catch(error => {
          console.log(error)
        })
    }

    const get_group_content = (groupid, title) => {
      grouptitle.value = title
      content.value = 'content'
      isContentCollapsed.value = false

      axios.get(`https://cms.igadc.cn/iga_room/?group=${groupid}`)
        .then(response => {
          room_group_list.value = response.data
          highlightRooms.value = room_group_list.value.map(room => room.floor_num.toString())
          init_geojson(building.value, highlightRooms.value)
        })
        .catch(error => {
          console.log(error)
        })
    }

    const get_group_by_grouptype = (value, group_type) => {
      group_true_room.value = '1'
      groupvalue.value = value
      menu.value = '1'

      axios.get(`https://cms.igadc.cn/iga_group/?group_type=${group_type}`)
        .then(response => {
          group_type_list.value = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }

    onMounted(() => {
      initMap()
      get_group()
    })

    onBeforeUnmount(() => {
      if (map.value) {
        map.value.remove()
      }
    })

    return {
      mapContainer,
      isCollapsed,
      hoverTimer,
      isContentCollapsed,
      sf_echarts,
      content,
      groupvalue,
      menu,
      buildings,
      roomColumns,
      group_type_list,
      room_group_list,
      not_group_list,
      grouptitle,
      group_true_room,
      highlightRooms,
      building,
      toggleCollapse,
      hoverExpand,
      hoverCollapse,
      toggleContentCollapse,
      toggleSfEcharts,
      update_geojson,
      get_group,
      get_no_group,
      get_group_content,
      get_group_by_grouptype
    }
  }
}
</script>

<style lang="scss" scoped>
#center_jfv {
  position: relative;
  height: calc(100vh - 50px);
  width: 100%;
}

.map-container {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 1;
}

.sidebar {
  z-index: 100;
  width: 60px;
  padding: 5px;
  margin: 5px;
  height: calc(100vh - 60px);
  background: rgba(50, 50, 50, 0.8);
  position: absolute;
  left: 0;
  border-radius: 4px;
  transition: all 0.3s ease;
  overflow: hidden;
  color: white;

  &:not(.collapsed) {
    width: 240px;
  }

  .sidebar-header {
    cursor: pointer;
    padding: 5px;
    text-align: center;

    h3 {
      font-size: 18px;
      margin-top: 8px;
      display: flex;
      align-items: center;
      justify-content: center;

      i {
        margin-right: 8px;
      }
    }
  }

  .sidebar-content {
    height: calc(100% - 50px);
    display: flex;
    flex-direction: column;

    .top-buttons {
      display: flex;
      flex-direction: column;
    }

    .group-list-scrollable {
      flex: 1;
      overflow-y: auto;
      margin: 5px 0;
      max-height: 500px;

      .group-list-inner {
        display: flex;
        flex-direction: column;
      }
    }
  }

  .sidebar-toggle {
    position: absolute;
    bottom: 10px;
    left: 0;
    right: 0;
    text-align: center;
    cursor: pointer;
    padding: 5px;
    color: white;

    i {
      font-size: 16px;
      transition: all 0.3s ease;

      &:hover {
        color: #5cd9e8;
      }
    }
  }
}

.button {
  display: flex;
  align-items: center;
  padding: 8px 10px;
  margin: 3px 0;
  transition: all 0.2s ease;
  white-space: nowrap;
  overflow: hidden;
  text-align: left;
  border-radius: 4px;
  color: white;

  i {
    margin-right: 8px;
    font-size: 18px;
    flex-shrink: 0;
  }

  span {
    overflow: hidden;
    text-overflow: ellipsis;
  }

  &:hover {
    transform: translateX(3px);
  }

  &.blue {
    background: rgba(0, 120, 215, 0.7);

    &.activity {
      background: rgba(0, 90, 180, 0.9);
    }
  }

  &.green {
    background: rgba(0, 180, 90, 0.7);

    &.activity {
      background: rgba(0, 150, 70, 0.9);
    }
  }

  &.orange {
    background: rgba(255, 140, 0, 0.7);

    &.activity {
      background: rgba(220, 120, 0, 0.9);
    }
  }
}

.content {
  width: fit-content;
  max-width: 500px;
  height: auto;
  max-height: 80vh;
  top: 20px;
  overflow-y: auto;
  padding: 10px;
  margin: 5px;
  left: 250px;
  background: rgba(20, 20, 20, 0.8);
  position: absolute;
  border-radius: 4px;
  font-size: 10pt;
  line-height: 16pt;
  z-index: 100;
  color: white;

  h3 {
    font-size: 22px;
    margin: 15px auto;
  }
}

.expand-btn-wrapper {
  position: absolute;
  right: 70px; /* 根据侧边栏宽度调整 */
  top: 220px;
  z-index: 100;
}

.bottom-buttons {
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.8);
  padding: 5px;
  border-radius: 4px;
}

.bottom-btn {
  margin: 0 5px;
  min-width: 80px;
  color: #333;
  font-weight: bold;
}

.sf_echarts_btn {
  display: inline-block;
  z-index: 100;
  float: right;
  padding: 5px;
  margin: 5px;
  right: 10px;
  position: absolute;
  border-radius: 4px;
  font-size: 10pt;
  line-height: 16pt;
}

.sf_echarts {
  display: inline-block;
  z-index: 100;
  padding: 5px;
  margin: 5px;
  left: 250px;
  background: rgba(20, 20, 20, 0.8);
  position: absolute;
  border-radius: 4px;
  font-size: 10pt;
  line-height: 16pt;
  color: white;
}


.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.table {
  width: 100%;
  background: rgba(255, 255, 255, 0.9);
  color: #333;

  :deep(th) {
    background: #f0f0f0;
    font-weight: bold;
  }
}

@media (max-width: 768px) {
  .sidebar {
    width: 50px !important;

    &:not(.collapsed) {
      width: 200px !important;
    }
  }

  .content {
    max-width: 90%;
    left: 210px !important;
  }

  .expand-btn-wrapper {
    right: 60px !important;
  }
}
</style>
