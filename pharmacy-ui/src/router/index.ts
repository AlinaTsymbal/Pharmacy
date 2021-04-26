import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import About from '@/views/About.vue';
import RouterView from '@/views/TheRouterView.vue';
import HomePage from '@/views/HomePage.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    redirect: '/about',
  },
  {
    path: '/',
    component: RouterView,
    children: [
      {
        path: 'home',
        name: 'Home',
        component: HomePage,
      },
      {
        path: 'catalog',
        name: 'Catalog',
        component: About,
      },
      {
        path: 'sets',
        name: 'RemedySets',
        component: About,
      },
      {
        path: 'pharmacies',
        name: 'Pharmacies',
        component: About,
      },
      {
        path: 'about',
        name: 'About',
        component: About,
      },
    ],
  },
  {
    path: '/*',
    redirect: '/home',
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
