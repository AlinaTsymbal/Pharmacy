<template>
  <div id="router-view-wrapper">
    <Navigation :items="items"/>
    <router-view class="page-content-wrapper"/>
  </div>
</template>

<script>
import Navigation from '@/components/common/Navigation.vue';
import {mapGetters} from "vuex";

export default {
  name: 'TheRouterView',
  components: { Navigation },
  computed: {
    ...mapGetters([
      'basket',
    ]),
    items() {
      return this.basket;
    },
  },
};
</script>

<style scoped lang="scss">
#router-view-wrapper {
  .page-content-wrapper {
    padding: 4rem;
  }
}
</style>
