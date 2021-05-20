<template>
  <div class="navigation-wrapper">
    <a-tabs :active-key="activeKey" @change="forward">
      <a-tab-pane key="home" tab="Головна сторінка"/>
      <a-tab-pane key="catalog" tab="Каталог"/>
      <a-tab-pane key="sets" tab="Набори ліків"/>
      <a-tab-pane key="med-kits" tab="Міні-аптечки"/>
      <a-tab-pane key="about" tab="Про сервіс"/>
    </a-tabs>
    <div class="additional-links-wrapper">
      <div class="authorization-links">
        <a @click="redirectLogin">Login/Register</a>
      </div>
      <a-popover title="Basket" trigger="hover">
        <template slot="content">
          <Basket :items="items"/>
        </template>
        <a type="primary" class="basket-popup-trigger"> Basket </a>
      </a-popover>
    </div>
  </div>
</template>

<script>
import Basket from '@/components/common/Basket';

export default {
  name: 'Navigation',
  components: {
    Basket,
  },
  props: {
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
}
</style>
