<template>
  <div class="row">
    <div class="column">{{ `${order.client.last_name} ${order.client.last_name}` }}</div>
    <div class="column">{{ order.client.phone }}</div>
    <div class="column">{{ order.created_at }}</div>
    <div class="column" :key="order.id"><a @click="handleClick">Замовлені ліки</a></div>
  </div>
</template>

<script>
export default {
  name: "RemedyListItem",
  props: {
    order: Object,
    handleDetails: Function,
  },
  methods: {
    handleClick() {
      this.handleDetails(this.order.id);
    },
  },
};
</script>

<style scoped lang="scss">

.row {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin: 1rem auto;
  width: 100%;
}
</style>
