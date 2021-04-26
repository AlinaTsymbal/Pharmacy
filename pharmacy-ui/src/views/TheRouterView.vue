<template>
  <div id="router-view-wrapper">
    <Navigation/>
    <router-view/>
  </div>
</template>

<script>
import Navigation from '@/components/Navigation.vue';

export default {
  name: 'TheRouterView',
  components: { Navigation },
};
</script>

<style scoped>

</style>
