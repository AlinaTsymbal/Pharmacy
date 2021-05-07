import Vue from 'vue';
import Vuex from 'vuex';
import medKits from '@/store/med-kits/module'
import catalog from '@/store/catalog/module'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    medKits,
    catalog,
  },
});
