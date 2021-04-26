<template>
  <div class="remedy-list">
    <RemedyItem
      v-for="item in remedies"
      :key="item.id"
      :remedy="item"
    />
  </div>
</template>

<script>
import RemedyItem from './RemedyItem.vue';

export default {
  name: 'RemedyList',
  components: { RemedyItem },
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
}

.remedy-list > * {
  margin: 2rem;
}
</style>
