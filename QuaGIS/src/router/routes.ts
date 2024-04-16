import {RouteRecordRaw} from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
   component: () => import('layouts/MainLayoutLeaflet.vue'),
    children: [
    {
        path: '',
        redirect: ('/leaflet/index'),
        component: () => import('pages/mapbox_index/mapbox_foo.vue')
      },
    ],

  },

  {
    path: '/intro',
    component: () => import('layouts/MainLayoutIntro.vue'),
    children: [
    {
        path: '',
        redirect: ('/intro/index'),
        component: () => import('pages/index_IndexPage.vue')
      },
      {path: 'index', component: () => import('pages/index_IndexPage.vue')},
      {path: 'intro1', component: () => import('pages/index_leaflet_foo.vue')},
      {path: 'intro2', component: () => import('pages/index_openlayers_foo.vue')},
      {path: 'intro3', component: () => import('pages/index_maptalks_foo.vue')},
    ],
  },
  {
    path: '/mapbox',
    component: () => import('layouts/MainLayoutMapbox.vue'),
    children: [

      {
        path: '',
        redirect: ('/mapbox/index'),
        component: () => import('pages/mapbox_index/mapbox_foo.vue')
      },
      {path: 'index', component: () => import('pages/mapbox_index/mapbox_foo.vue')},
      {path: 'gltf', component: () => import('pages/mapbox_index/mapbox_gltf.vue')},
      {path: 'bmapbox', component: () => import('pages/mapbox_index/mapdde_foo.vue')},
    ],
  },

  {
    path: '/leaflet',
    component: () => import('layouts/MainLayoutLeaflet.vue'),
    children: [
    {
        path: '',
        redirect: ('/leaflet/index'),
        component: () => import('pages/mapbox_index/mapbox_foo.vue')
      },
      {path: 'index', component: () => import('pages/leaf/leaf_leaflet_f3.vue')},
      {path: 'lf3', component: () => import('pages/leaf/leaf_leaflet_f3.vue')},
      {path: 'lf4', component: () => import('pages/leaf/leaf_leaflet_f4.vue')},
      {path: 'lf6', component: () => import('pages/leaf/leaf_leaflet_f6.vue')},
      {path: 'lf7', component: () => import('pages/leaf/leaf_leaflet_f7.vue')},
      {path: 'lf8', component: () => import('pages/leaf/leaf_leaflet_f8.vue')},
      {path: 'lf9', component: () => import('pages/leaf/leaf_leaflet_f9.vue')},
      {path: 'lf12', component: () => import('pages/leaf/leaf_leaflet_f12.vue')},
      {path: 'lf13', component: () => import('pages/leaf/leaf_leaflet_f13.vue')},
      {path: 'lf14', component: () => import('pages/leaf/leaf_leaflet_f14.vue')},
      {path: 'lf15', component: () => import('pages/leaf/leaf_leaflet_f15.vue')},
      {path: 'bleaflet', component: () => import('pages/leaf/leaf_leaflet_foo.vue')},
      // {path: 'bmaptalks', component: () => import('pages/maptalks_foo.vue')},

      {path: 'bwind', component: () => import('pages/leaf/leaf_leaflet_wind.vue')},
    ],
  },


  {
    path: '/openlayers',
    component: () => import('layouts/MainLayoutOpenLayers.vue'),
    children: [
    {
        path: '',
        redirect: ('/openlayers/index'),
        component: () => import('pages/openlayers/ol_openlayers_foo.vue')
      },
     {path: 'index', component: () => import('pages/openlayers/ol_openlayers_foo.vue')},
      {path: 'ol1', component: () => import('pages/openlayers/ol_openlayers_foo.vue')},
      {path: 'ol2', component: () => import('pages/openlayers/ol_openlayers_show2.vue')},

    ],
  },

  {
    path: '/maptalks',
    component: () => import('layouts/MainLayoutMaptalks.vue'),
    children: [
    {
        path: '',
        redirect: ('/maptalks/index'),
        component: () => import('pages/maptalks/maptalks_foo.vue')
      },
      {path: 'index', component: () => import('pages/maptalks/maptalks_foo.vue')},
      {path: 'three', component: () => import('pages/maptalks/maptalks_3d.vue')},
    ],
  },
  {
    path: '/cesium',
    component: () => import('layouts/MainLayoutCesium.vue'),
    children: [
    {
        path: '',
        redirect: ('/cesium/index'),
        component: () => import('pages/cesium/cesium_foo.vue')
      },
      {path: 'index', component: () => import('pages/cesium/cesium_foo.vue')},
      {path: 'gltf', component: () => import('pages/cesium/cesium_gltf.vue')},
      {path: 'ccjson', component: () => import('pages/cesium/cesium_ccjson.vue')},
      {path: 'nanjing', component: () => import('pages/cesium/cesium_nanjing.vue')},
      {path: 'index', component: () => import('pages/cesium/cesium_index.vue')},
    ],
  },





  {
    path: '/maplibre',
    component: () => import('layouts/maplibreLayout.vue'),
    children: [
    {
        path: '',
        redirect: ('/maplibre/index'),
        component: () => import('pages/maptalks/maptalks_foo.vue')
      },
      {path: 'index', component: () => import('pages/maplibre/demo_1.vue')},
      // {path: 'demo2', component: () => import('pages/maptalks/maptalks_3d.vue')},
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
