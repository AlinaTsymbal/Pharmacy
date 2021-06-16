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
      <a
        v-if="loggedIn && !isAdmin"
        class="profile-link" style="margin-left: 1.5rem"
        @click="redirectProfile"
      >
        Профіль
      </a>
      <Basket :items="items" v-if="loggedIn && !isAdmin" class="basket-popup-trigger"/>
    </div>
  </div>
</template>

<script>
import Basket from '@/components/common/Basket';
import { GET_USER, LOGOUT } from '@/store/user/actions';

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
      this.$router.push('/authorization');
    },
    forward(key) {
      this.activeKey = key;
      this.$router.push(key);
    },
    redirectProfile() {
      this.$router.push('/profile');
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
    const token = localStorage.getItem('auth-token');
    if (token) {
      this.$store.dispatch(GET_USER);
    }
    this.activeKey = `/${this.$router.currentRoute.path.split('/')[1]}`;
  },
  watch: {
    $route(to, from) {
      if (to.path !== from.path) {
        // eslint-disable-next-line prefer-destructuring
        this.activeKey = `/${to.path.split('/')[1]}`;
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
