<template>
  <div id="router-view-wrapper">
    <Navigation :items="items"/>
    <router-view class="page-content-wrapper"/>
    <RemedyDetails :details="details"/>
  </div>
</template>

<script>
import Navigation from '@/components/common/Navigation.vue';
import {mapGetters} from "vuex";
import RemedyDetails from "@/components/common/RemedyDetails";

export default {
  name: 'TheRouterView',
  components: {RemedyDetails, Navigation },
  computed: {
    ...mapGetters([
      'basket',
      'details',
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
