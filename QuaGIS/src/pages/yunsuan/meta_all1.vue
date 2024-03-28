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
              <td>UID</td>
              <td>Title</td>
              <td>Keywords</td>
            </tr>
            </thead>
            <tbody>

            <tr v-for="(item,index)  in this.info.data" :key="index">
              <td>{{ index }}</td>
              <td> <a @click="tolink(item.UID)" class="text-primary">{{ item.UID }}</a></td>
              <td> {{ item.Title }}</td>
              <td> {{ item.Keywords }}</td>


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
      axios
        .get('http://ddestg.igcloud.tech/api/getAllMetadata')
        .then(
          response => (this.info = response)
        )
        .catch(function (error) { // 请求失败处理
          console.log('Error for info2: ');
          console.log(error);
        });
    },
    tolink(id) {
      this.$axios
        .get('http://ddestg.igcloud.tech/api/getMetadatById?id='+{id})
        .then(res=>{
          this.$router.push(
            {
              path: '/interface/meta_detial',
              query: {
                id
              }
            })
          console.log(res)
        })
        .catch(function (error) { // 请求失败处理
          console.log('Error for res: ');
          console.log(error);
        });


    }

  },


};
</script>

