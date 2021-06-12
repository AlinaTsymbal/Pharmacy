import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import About from '@/views/About.vue';
import RouterView from '@/views/TheRouterView.vue';
import HomePage from '@/views/HomePage.vue';
import CatalogPage from '@/views/CatalogPage.vue';
import RemedySetsPage from '@/views/RemedySetsPage.vue';
import MedKitsPage from '@/views/MedKitsPage.vue';
import AuthorizationPage from '@/views/AuthorizationPage.vue';
import OrderPage from '@/views/OrderPage.vue';
import OrdersPage from '@/views/OrdersPage.vue';
import RemedyDetailsPage from '@/views/RemedyDetailsPage.vue';
import { isAuthenticated } from '@/utils/authorization';

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
        component: MedKitsPage,
      },
      {
        path: 'about',
        name: 'About',
        component: About,
      },
      {
        path: 'authorization',
        name: 'Authorization',
        component: AuthorizationPage,
      },
      {
        path: 'order',
        name: 'Order',
        component: OrderPage,
      },
      {
        path: 'orders',
        name: 'Orders',
        component: OrdersPage,
      },
      {
        path: 'remedies/:id',
        name: 'Remedy Details',
        component: RemedyDetailsPage,
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

router.beforeEach(isAuthenticated);

export default router;
