<template>
  <q-page id="page6_p4_q1" class="bg-dark q-pa-md">
    <!-- 顶部标题栏 -->
    <q-toolbar class="q-pt-md q-pl-md">
      <q-icon name="bar_chart" color="cyan-8" size="sm" />
      <q-toolbar-title class="text-h6 text-cyan-8 q-mx-md">
        知识图谱
      </q-toolbar-title>
      <q-separator dark color="cyan-8" class="q-ml-md" style="height: 2px; width: 150px" />
    </q-toolbar>

    <div class="row q-mt-md">
      <!-- 知识图谱容器 -->
      <div class="col-10">
        <div class="viz-container">
          <div id="viz"></div>
        </div>
      </div>

      <!-- 分类按钮组 -->
      <div class="col-2 q-pl-md">
        <q-btn-group vertical class="q-gutter-y-md">
          <q-btn
            v-for="(btnConfig, index) in buttonConfigs"
            :key="index"
            :color="btn === btnConfig.id ? 'primary' : 'secondary'"
            :label="btnConfig.label"
            @click="reload(btnConfig.category, btnConfig.id)"
            class="custom-btn"
            :class="{ 'active-btn': btn === btnConfig.id }"
          />
        </q-btn-group>
      </div>
    </div>
  </q-page>
</template>

<script>
import { ref } from 'vue'
import NeoVis from 'neovis.js/dist/neovis.js';

export default {
  setup() {
    const btn = ref('F')
    const viz = ref(null)
    const buttonConfigs = [
      { id: 'A', label: '农业', category: '农业' },
      { id: 'B', label: '法律', category: '法律' },
      { id: 'C', label: '生态', category: '生态' },
      { id: 'D', label: '环境', category: '环境' },
      { id: 'E', label: '土壤', category: '土壤' },
      { id: 'F', label: '全部', category: '' }
    ]

    const draw = () => {
      const config = {
        container_id: "viz",
        server_url: "neo4j://39.100.254.142:7687",
        server_user: "demodemo",
        server_password: "passdemo",
        labels: {
          "农业": {
            "caption": "name",
            "size": "pagerank",
            "community": "community",
            font: { size: 30 },
            color: {
              border: "#c0a378",
              background: "#d9c8ae",
              highlight: { border: "#c0a378" }
            }
          },
          "法律": {
            "caption": "name",
            "size": "pagerank",
            font: { size: 20 }
          },
          "生态": {
            "caption": "name",
            "font": { size: 26, color: "#000000" }
          },
          "环境": {
            "caption": "name",
            "font": { size: 36, color: "#000000" },
            "title_properties": ["desc"],
            "community": "community"
          },
          "土壤": {
            "caption": "name",
            "font": { size: 36, color: "#000000" },
            "title_properties": ["desc"],
            "community": "community"
          }
        },
        relationships: {
          "recommand_drug": { "thickness": "1", "caption": false }
        },
        arrows: false,
        hierarchical: false,
        initial_cypher: "MATCH (n)-[r]->(m) RETURN n,r,m limit 30"
      }

      viz.value = new NeoVis.default(config)
      viz.value.render()
    }

    const reload = (aa, str) => {
      btn.value = str
      const cypher = aa ? `MATCH (n:${aa})-[r]->(m) RETURN n,r,m LIMIT 25`
                       : 'MATCH (n)-[r]->(m) RETURN n,r,m LIMIT 25'
      viz.value.renderWithCypher(cypher)
    }

    return { btn, buttonConfigs, draw, reload }
  },
  mounted() {
    this.draw()
  }
}
</script>

<style lang="scss" scoped>
#page6_p4_q1 {
  height: 94vh;
  border-radius: 16px;

  .viz-container {
    width: 100%;
    height: 86vh;
    border: 1px solid $grey-9;
    padding: 10px;
    border-radius: 20px;
    background: $dark-page;

    #viz {
      width: 100%;
      height: 100%;
      font: 22px Arial;
    }
  }

  .custom-btn {
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;

    &::before {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: rgba(255, 255, 255, 0.1);
      transform: rotate(30deg);
      transition: all 0.6s ease;
      opacity: 0;
    }

    &.active-btn {
      transform: translateY(-3px);
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);

      &::before {
        opacity: 1;
        top: -30%;
        left: -30%;
      }
    }

    &:hover:not(.active-btn) {
      transform: scale(1.05);
      &::before {
        opacity: 0.5;
      }
    }
  }
}
</style>
