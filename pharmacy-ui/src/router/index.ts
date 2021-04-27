import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import About from '@/views/About.vue';
import RouterView from '@/views/TheRouterView.vue';
import HomePage from '@/views/HomePage.vue';
import CatalogPage from '@/views/CatalogPage.vue';
import RemedySetsPage from '@/views/RemedySetsPage.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    redirect: '/home',
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
        component: CatalogPage,
      },
      {
        path: 'sets',
        name: 'RemedySets',
        component: RemedySetsPage,
      },
      {
        path: 'med-kits',
        name: 'Med kits',
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
