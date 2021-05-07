<template>
  <div class="remedy-sets-page-wrapper">
    <div class="sets-info-wrapper">
      <span>Placeholder</span>
    </div>
    <RemedySet
      v-for="item in remedySets"
      :key="item.id"
      :set="item"
    />
  </div>
</template>

<script>
import RemedySet from '../components/sets/RemedySet.vue';
import {mapGetters} from 'vuex';
import {GET_REMEDY_SETS} from "@/store/remedy-sets/actions";

export default {
  name: 'RemedySetsPage',
  components: {
    RemedySet,
  },
  computed: {
    ...mapGetters([
      'remedySets',
    ]),
  },
  mounted() {
    this.$store.dispatch(GET_REMEDY_SETS);
  },
};
</script>

<style scoped lang="scss">
.remedy-sets-page-wrapper {
  display: flex;
  flex-direction: column;

  .sets-info-wrapper {
    span {
      font-size: large;
      font-weight: bold;
    }
  }

  .remedy-set {
    height: 30rem;
  }
}
</style>
