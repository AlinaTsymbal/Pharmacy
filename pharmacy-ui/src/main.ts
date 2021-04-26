import 'ant-design-vue/dist/antd.css';

import Antd from 'ant-design-vue';
import axios from 'axios';
import Vue from 'vue';
import VuexAxios from 'vue-axios';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

Vue.use(Antd);
Vue.use(VuexAxios, axios);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
