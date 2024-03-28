<template>
  <q-page padding>
    <div id="bottomLeft">
      <div class="bg-color-black">
        <div class="d-flex pt-2 pl-2">
          <h3>Metadata Dictionary interface</h3>

        </div>
        <div>


          <q-markup-table :separator="separator" flat bordered>
            <thead>
            <tr>
              <td>NO.</td>
              <td>Code2rdconceptname</td>
              <td>Code3rdconceptname</td>
              <td>Code</td>

              <td>Definition</td>
            </tr>
            </thead>
            <tbody>

            <tr v-for="(item,index)  in this.info.data" :key="index">
              <td>{{ index }}</td>
              <td> {{ item.Code2rdconceptname }}</td>
              <td> {{ item.Code3rdconceptname }}</td>
              <td> {{ item.Code }}</td>

              <td>{{ item.Definition }}</td>

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
import axios from 'axios'

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
      let id=this.$route.query.id
      axios
        .get('http://ddestg.igcloud.tech/api/getThirdTopicCategoryCode?id='+id)
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

