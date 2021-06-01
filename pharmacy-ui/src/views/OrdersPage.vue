<template>
  <div class="orders-page-wrapper">
    <a-card style="width: 70%; margin: auto;">
      <span style="font-size: large">Список замовлень</span>
      <div class="orders-table">
        <div v-for="order in getOrders" :key="order.id" class="row">
          <div class="column">{{ `${order.client.last_name} ${order.client.last_name}` }}</div>
          <div class="column">{{ order.client.phone }}</div>
          <div class="column">{{ order.created_at }}</div>
          <div class="column"><a>Замовлені ліки</a></div>
        </div>
      </div>
    </a-card>
  </div>
</template>

<script>
import {GET_ORDERS} from "@/store/user/actions";
import {mapGetters} from "vuex";

export default {
  name: "OrdersPage",
  computed: {
    ...mapGetters([
      'orders',
    ]),
    getOrders() {
      return this.orders;
    },
  },
  mounted() {
    this.$store.dispatch(GET_ORDERS);
  },
};
</script>

<style scoped lang="scss">
.orders-page-wrapper {
  width: 80%;
  margin: auto;

  .orders-table {
    width: 90%;
    margin: auto;

    .row {
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      margin: 1rem auto;

      .column {
        width: 25%;
      }
    }
  }
}
</style>
