<template>
  <div class="orders-page-wrapper">
    <a-card style="width: 70%; margin: auto;">
      <span style="font-size: large">Список замовлень</span>
      <div class="orders-table">
        <div v-for="order in getOrders" :key="order.id" class="row">
          <RemedyListItem :order="order" :handle-details="handleClick"/>
        </div>
      </div>
    </a-card>
    <RemediesListModal :items="remedies"/>
  </div>
</template>

<script>
import { GET_ORDERS } from '@/store/user/actions';
import { mapGetters } from 'vuex';
import RemediesListModal from '@/components/common/RemediesListModal';
import RemedyListItem from '@/components/common/RemedyListItem';
import { eventBus } from '@/main';

export default {
  name: 'OrdersPage',
  components: {
    RemedyListItem,
    RemediesListModal,
  },
  computed: {
    ...mapGetters([
      'orders',
    ]),
    getOrders() {
      return this.orders;
    },
    remedies() {
      return this.order?.remedies;
    },
  },
  data() {
    return {
      order: null,
      visible: false,
    };
  },
  methods: {
    handleClick(id) {
      this.order = this.orders.find((o) => o.id === id);
      eventBus.$emit('openListModal');
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
