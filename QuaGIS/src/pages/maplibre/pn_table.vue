<template>
  <div class="table-container">
    <div class="table-controls">
      <!-- 替换为 select 形式的学科组筛选 -->
      <div class="group-select-container">
        <label>学科组筛选：</label>
        <select
            v-model="selectedGroup"
            class="group-select"
            @change="resetSelection"
        >
          <option value="">全部学科组</option>
          <option
              v-for="group in uniqueGroups"
              :key="group"
              :value="group"
          >
            {{ group }}
          </option>
        </select>
      </div>

      <div class="sort-controls">
        <label>排序方式:</label>
        <select v-model="sortField" class="sort-select">
          <option value="group">学科组</option>
          <option value="count">办公总数量</option>
          <option value="area">总面积</option>
          <option value="staff_num">人员数量</option>
          <option value="average_area">人均面积</option>
        </select>
        <button @click="toggleSortDirection" class="sort-direction">
          {{ sortDirection === 'asc' ? '升序 ↑' : '降序 ↓' }}
        </button>
      </div>
    </div>

    <div class="table-responsive"   ref="scrollContainer"
      @mousedown="startDrag"
      @mousemove="doDrag"
      @mouseup="stopDrag"
      @mouseleave="stopDrag">
      <table class="enhanced-table">
        <thead>
        <tr>
          <th>学科组</th>
          <th>办公室总数量</th>
          <th>总面积</th>
          <th>人员数量</th>
          <th>人均面积</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(item, index) in filteredAndSortedData" :key="index">
          <td>{{ item.group }}</td>
          <td>{{ item.count }}</td>
          <td>{{ item.area }}</td>
          <td>{{ item.staff_num || 1 }}</td>
          <td>{{ item.average_area || 1 }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      info: '',
      tableinfo: [],
      selectedGroup: '',
      sortField: 'group',
      sortDirection: 'asc',
    }
  },
  computed: {
    uniqueGroups() {
      const groups = new Set();
      (this.tableinfo.result || []).forEach(item => {
        groups.add(item.group);
      });
      return Array.from(groups).sort();
    },

    filteredAndSortedData() {
      let data = this.tableinfo.result || [];

      if (this.selectedGroup) {
        data = data.filter(item => item.group === this.selectedGroup);
      }

      return data.sort((a, b) => {
        const fieldA = a[this.sortField] || 0;
        const fieldB = b[this.sortField] || 0;

        let comparison = 0;
        if (fieldA > fieldB) {
          comparison = 1;
        } else if (fieldA < fieldB) {
          comparison = -1;
        }

        return this.sortDirection === 'asc' ? comparison : -comparison;
      });
    }
  },
  methods: {
    async fetchAndCacheGeoJSON() {
      try {
        const response = await fetch('https://cms.igadc.cn/iga_group/ajax/iga_statistics/');
        this.tableinfo = await response.json();
        console.log('表格数据加载成功:', this.tableinfo.result);
      } catch (error) {
        console.error('加载数据失败:', error);
      }
    },

    toggleSortDirection() {
      this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
    },

    resetSelection() {
      // 选择变化时保持当前逻辑
    },
    startDrag(e) {
      this.isDragging = true;
      this.startY = e.pageY - this.$refs.scrollContainer.offsetTop;
      this.scrollTop = this.$refs.scrollContainer.scrollTop;
      this.$refs.scrollContainer.style.cursor = 'grabbing';
      this.$refs.scrollContainer.style.userSelect = 'none';
    },

    doDrag(e) {
      if (!this.isDragging) return;
      e.preventDefault();
      const y = e.pageY - this.$refs.scrollContainer.offsetTop;
      const walk = (y - this.startY) * 2; // 滚动速度系数
      this.$refs.scrollContainer.scrollTop = this.scrollTop - walk;
    },

    stopDrag() {
      this.isDragging = false;
      this.$refs.scrollContainer.style.cursor = '';
      this.$refs.scrollContainer.style.userSelect = '';
    }
  },
  created() {
    this.fetchAndCacheGeoJSON();
  }
}
</script>

<style scoped>
.table-container {
  margin: 20px;
  font-family: Arial, sans-serif;
}

.table-controls {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
  align-items: center;
}

.group-select-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

.group-select {
  padding: 8px 12px;
  width: 200px;
  border: 1px solid #ddd;
  border-radius: 4px;
  height: 36px; /* 保持与其他控件一致的高度 */
}

.sort-controls {
  display: flex;
  align-items: center;
  gap: 10px;
}

.sort-select {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  height: 36px;
}

.sort-direction {
  padding: 8px 12px;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  height: 36px;
}

.table-responsive {
  width: 100%;
  height: calc(100vh - 280px); /* 固定高度，保持一致性 */
  overflow-y: auto;
}

.table-responsive {
  cursor: grab;
}

.table-responsive:active {
  cursor: grabbing;
}

.enhanced-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  background: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  border-radius: 6px;
  overflow: hidden;
}

.enhanced-table thead th {
  background-color: #3498db;
  color: white;
  font-weight: 500;
  padding: 12px 15px;
  text-align: left;
  position: sticky;
  top: 0;
}

.enhanced-table td {
  padding: 12px 15px;
  border-bottom: 1px solid #e0e0e0;
  color: #333;
  vertical-align: middle;
}

.enhanced-table tbody tr:nth-child(even) {
  background-color: #f8f9fa;
}

.enhanced-table tbody tr:hover {
  background-color: #e9f5ff;
}

.enhanced-table tbody tr:last-child td {
  border-bottom: none;
}

.enhanced-table thead th:hover {
  background-color: #2980b9;
  cursor: pointer;
}

.enhanced-table thead tr:first-child th:first-child {
  border-top-left-radius: 6px;
}

.enhanced-table thead tr:first-child th:last-child {
  border-top-right-radius: 6px;
}

.enhanced-table tbody tr:last-child td:first-child {
  border-bottom-left-radius: 6px;
}

.enhanced-table tbody tr:last-child td:last-child {
  border-bottom-right-radius: 6px;
}

.enhanced-table td:nth-child(2),
.enhanced-table td:nth-child(3) {
  text-align: right;
  font-family: 'Roboto Mono', monospace;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .table-controls {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }

  .group-select {
    width: 100%;
  }
}
</style>
