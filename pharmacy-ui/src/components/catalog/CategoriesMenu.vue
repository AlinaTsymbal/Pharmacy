<template>
  <a-menu mode="vertical" @click="handleClick" :selectedKeys="selectedKeys">
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
    onCategorySelect: Function,
  },
  data() {
    return {
      selectedKeys: [],
    };
  },
  methods: {
    handleClick(menuItem) {
      const index = this.selectedKeys.indexOf(menuItem.key);
      console.log(index);
      if (index === -1) {
        this.selectedKeys.push(menuItem.key);
      } else {
        this.selectedKeys.splice(index, 1);
      }
      this.onCategorySelect(this.selectedKeys);
    },
  },
};
</script>

<style scoped>

</style>
