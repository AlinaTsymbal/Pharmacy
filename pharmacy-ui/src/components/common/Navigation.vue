<template>
  <div class="navigation-wrapper">
    <div class="service-name-wrapper">
      <span> Сервіс П&П Ліків</span>
    </div>
    <a-tabs :active-key="activeKey" @change="forward">
      <a-tab-pane key="/home" tab="Головна сторінка"/>
      <a-tab-pane key="/catalog" tab="Каталог"/>
      <a-tab-pane key="/sets" tab="Набори ліків"/>
      <a-tab-pane key="/med-kits" tab="Міні-аптечки"/>
      <a-tab-pane key="/about" tab="Про сервіс"/>
      <a-tab-pane key="/orders" tab="Замовлення" v-if="isAdmin"/>
    </a-tabs>
    <div class="additional-links-wrapper">
      <div class="authorization-links" v-if="!loggedIn">
        <a @click="redirectLogin">Вхід/Реєстрація</a>
      </div>
      <div class="authorization-links" v-if="loggedIn">
        <a @click="hadleLogout">Вийти</a>
      </div>
      <a-popover title="Basket" trigger="hover">
        <template slot="content">
          <Basket :items="items"/>
        </template>
        <a type="primary" class="basket-popup-trigger"> Кошик </a>
      </a-popover>
    </div>
  </div>
</template>

<script>
import Basket from '@/components/common/Basket';
import { LOGOUT } from '@/store/user/actions';

export default {
  name: 'Navigation',
  components: {
    Basket,
  },
  computed: {
    loggedIn() {
      return this.user;
    },
    isAdmin() {
      return this.user?.type === 'ADMIN';
    },
  },
  props: {
    user: Object,
    items: Array,
  },
  methods: {
    redirectLogin() {
      this.$router.push('authorization');
    },
    forward(key) {
      this.activeKey = key;
      this.$router.push(key);
    },
    hadleLogout() {
      this.$store.dispatch(LOGOUT);
    },
  },
  data() {
    return {
      activeKey: 'home',
    };
  },
  mounted() {
    this.activeKey = this.$router.currentRoute.path.split('/')[1];
  },
  watch: {
    $route(to, from) {
      if (to.path !== from.path) {
        // eslint-disable-next-line prefer-destructuring
        this.activeKey = to.path.split('/')[1];
      }
    },
  },
};
</script>

<style scoped lang="scss">
.navigation-wrapper {
  position: fixed;
  width: 100%;
  background: white;
  z-index: 9;

  .additional-links-wrapper {
    display: flex;
    flex-direction: row;
    position: absolute;
    right: 2rem;
    top: 1rem;

    .authorization-links {
      display: flex;
      flex-direction: row;
    }

    .basket-popup-trigger {
      margin-left: 2rem;
    }
  }

  .service-name-wrapper {
    position: absolute;
    left: 1rem;
    top: 1rem;

    span {
      font-size: 1rem;
      color: blue;
      font-weight: bolder;
    }
  }
}
</style>
