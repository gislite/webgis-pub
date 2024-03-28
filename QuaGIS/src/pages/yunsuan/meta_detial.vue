<template>
  <q-page padding>
    <div id="bottomLeft">
      <div class="bg-color-black">
        <div class="d-flex pt-2 pl-2">
          <h3>{{this.info.data.title}}</h3>

        </div>
        <div>


          <q-markup-table :separator="separator" flat bordered>

            <tbody>

            <tr v-for="(item,index)  in this.info.data" :key="index">
              <td>{{ index }}</td>
              <td>{{item}}</td>

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
      let id = this.$route.query.id
      axios
        .get('http://ddestg.igcloud.tech/api/getMetadatById?id=' + id)
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

