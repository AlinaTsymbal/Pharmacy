<template>
  <div class="basket-wrapper">
    <div v-if="isEmpty">
      <span>Basket is empty!</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Basket',
  computed: {
    isEmpty() {
      return this.items.length === 0;
    },
  },
  props: {
    items: Array,
  },
};
</script>

<style scoped>

</style>
