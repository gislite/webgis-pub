
import { defineStore } from 'pinia';

export const useCommonFunctionStore = defineStore('common_function', {
  state: () => ({
    leftDrawerOpen: true,
  }),
  // getters: {
  //   doubleCount: (state) => state.counter * 2,
  // },
  actions: {
    toggleLeftDrawer() {
      this.leftDrawerOpen=!this.leftDrawerOpen
    },
  },
});
