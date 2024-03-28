<template>
  <q-page padding>
    <div id="bottomLeft">
      <div class="bg-color-black">
        <div class="d-flex pt-2 pl-2">
        <span style="color:#5cd9e8">
          <icon name="chart-pie"></icon>
        </span>
          <h3>Metadata Dictionary interface</h3>

        </div>
        <div>


          <q-markup-table :separator="separator" flat bordered>
            <thead>
            <tr>
              <td>datasetId</td>
              <td>datasetStandardName</td>
              <td>datasetStandardNameCh</td>
              <td>datasetDateinfo</td>
            </tr>
            </thead>
            <tbody>
        {{this.info}}
            <tr v-for="(item,index)  in this.info.rows" :key="index">
              {{item}}
              <td>{{ index }}</td>

              <td>  <a :href="'http://ddestg.igcloud.tech/api/getSecondTopicCategoryCode?id='+item.datasetId" target="_blank">{{ item.datasetId }}</a></td>
              <td>{{ item.datasetStandardName }}</td>
              <td>{{ item.datasetStandardNameCh }}</td>
              <td>{{ item.datasetDateinfo }}</td>

            </tr>
            </tbody>
          </q-markup-table>




        </div>
        <div>


        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      info: ''

    };
  },
  mounted() {
    this.get_info()

  },
  methods: {
    get_info() {
      axios
        .post('http://47.243.238.139:2061/api/ext/v1.0/query/getMDCodeAll')
        .then(
          response => (this.info = response)
        )
        .catch(function (error) { // 请求失败处理
          console.log('Error for info2: ');
          console.log(error);
        });
    },

  },


};
</script>

