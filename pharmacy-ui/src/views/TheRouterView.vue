<template>
  <div id="router-view-wrapper">
    <Navigation/>
    <router-view class="page-content-wrapper"/>
  </div>
</template>

<script>
import Navigation from '@/components/common/Navigation.vue';

export default {
  name: 'TheRouterView',
  components: { Navigation },
};
</script>

<style scoped lang="scss">
#router-view-wrapper {
  .page-content-wrapper {
    padding: 4rem;
  }
}
</style>
