<template>
  <div id="router-view-wrapper">
    <Navigation :items="items" :user="loggedUser"/>
    <router-view class="page-content-wrapper"/>
    <RemedyDetails :details="details"/>
  </div>
</template>

<script>
import Navigation from '@/components/common/Navigation.vue';
import {mapGetters} from "vuex";
import RemedyDetails from "@/components/common/RemedyDetails";
import {GET_BASKET} from "@/store/catalog/actions";

export default {
  name: 'TheRouterView',
  components: {RemedyDetails, Navigation },
  computed: {
    ...mapGetters([
      'basket',
      'details',
      'user',
    ]),
    items() {
      return this.basket?.remedies;
    },
    loggedUser() {
      return this.user;
    },
  },
  mounted() {
    this.$store.dispatch(GET_BASKET);
  }
};
</script>

<style scoped lang="scss">
#router-view-wrapper {
  .page-content-wrapper {
    padding: 4rem;
  }
}
</style>
