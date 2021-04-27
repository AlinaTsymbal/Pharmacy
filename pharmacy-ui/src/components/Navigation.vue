<template>
  <div class="navigation-wrapper">
    <a-tabs :active-key="activeKey" @change="forward">
      <a-tab-pane key="home" tab="Home page"/>
      <a-tab-pane key="catalog" tab="Catalog"/>
      <a-tab-pane key="sets" tab="Remedy sets"/>
      <a-tab-pane key="med-kits" tab="Med kits"/>
      <a-tab-pane key="about" tab="About service"/>
    </a-tabs>
    <div class="additional-links-wrapper">
      <div class="authorization-links">
        <a>Login/Register</a>
      </div>
      <a-popover title="Basket" trigger="hover">
        <template slot="content">
          <Basket :items="[]"/>
        </template>
        <a type="primary" class="basket-popup-trigger"> Hover me</a>
      </a-popover>
    </div>
  </div>
</template>

<script>
import Basket from "@/components/Basket";
export default {
  name: 'Navigation',
  components: {Basket},
  methods: {
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
