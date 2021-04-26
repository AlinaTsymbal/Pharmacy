<template>
  <a-menu mode="vertical" @click="handleClick">
    <a-menu-item class="category-item" v-for="item in categories" :key="item.id">
      {{ item.name }}
    </a-menu-item>
  </a-menu>
</template>

<script>
export default {
  name: 'CategoriesMenu',
  props: {
    categories: Array,
  },
  methods: {
    handleClick(key) {
      console.log('filter by category is not implemented');
    },
  },
};
</script>

<style scoped>

</style>
