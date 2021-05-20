<template>
  <div class="remedy-set-remedies">
    <div
      v-for="item in remedies"
      class="remedy-item-wrapper"
      :key="item.id"
    >
      <RemedyItem
        :remedy="item"
        style="height: 20rem; width: 15rem"
      />
    </div>
  </div>
</template>

<script>
import RemedyItem from '../catalog/RemedyItem.vue';

export default {
  name: 'RemedySetRemedies',
  components: {
    RemedyItem,
  },
  props: {
    remedies: Array,
  },
};
</script>

<style scoped lang="scss">
.remedy-set-remedies {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;

  .remedy-item-wrapper {
    margin: 1.5rem;
    width: 17%;
  }
}
</style>
