<template>
  <div class="remedy-list">
    <div
      class="remedy-item-wrapper"
      v-for="item in remedies"
      :key="item.id"
    >
      <RemedyItem
        style="height: 20rem; width: 15rem"
        :remedy="item"
      />
    </div>
  </div>
</template>

<script>
import RemedyItem from './RemedyItem.vue';

export default {
  name: 'RemedyList',
  components: {
    RemedyItem,
  },
  props: {
    remedies: Array,
  },
};
</script>

<style scoped lang="scss">
.remedy-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;

  .remedy-item-wrapper {
    width: 20%;
  }
}

.remedy-list > * {
  margin: 2rem;
}
</style>
