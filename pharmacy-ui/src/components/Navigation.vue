<template>
  <a-tabs default-active-key="1" @change="forward">
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
      this.$router.push(key);
    },
  },
};
</script>

<style scoped>

</style>
