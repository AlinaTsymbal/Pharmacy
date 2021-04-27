<template>
  <a-tabs :active-key="activeKey" @change="forward">
    <a-tab-pane key="home" tab="Home page"/>
    <a-tab-pane key="catalog" tab="Catalog"/>
    <a-tab-pane key="sets" tab="Remedy sets"/>
    <a-tab-pane key="pharmacies" tab="Mini-pharmacies"/>
    <a-tab-pane key="about" tab="About service"/>
  </a-tabs>
</template>

<script>
export default {
  name: 'Navigation',
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

<style scoped>

</style>
