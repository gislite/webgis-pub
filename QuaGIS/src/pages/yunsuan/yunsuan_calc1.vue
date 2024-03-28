<template>

<!--  <q-breadcrumbs padding>-->
<!--    <q-breadcrumbs-el label="Home" icon="home"></q-breadcrumbs-el>-->
<!--    <q-breadcrumbs-el label="Components" icon="widgets"></q-breadcrumbs-el>-->
<!--    <q-breadcrumbs-el label="Breadcrumbs"></q-breadcrumbs-el>-->
<!--  </q-breadcrumbs>-->


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
              <td>NO.</td>
              <td>Code</td>
              <td>Name</td>
              <td>Definition</td>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item,index)  in this.info.data" :key="index">
              <td>{{ index }}</td>

              <td><a @click="tolink(item.Code)" class="text-primary "> {{ item.Code }} </a></td>
              <td>{{ item.Name }}</td>
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
import axios from 'axios';
import {useRouter} from 'vue-router'

const $route = useRouter()
export default {
  data() {
    return {
      info: '',

    };
  },
  mounted() {
    this.get_info()

  },
  methods: {
    get_info() {
      axios
        .get('http://ddestg.igcloud.tech/api/getFirstTopicCategoryCode')
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
      .get('http://ddestg.igcloud.tech/api/getSecondTopicCategoryCode?id='+{id})
      .then(res=>{
        this.$router.push(
          {
            path: '/interface/meta_dic2',
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

