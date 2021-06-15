<template>
  <div class="order-page-wrapper">
    <a-card style="width: 80%; margin: auto;">
      <span style="font-size: large">Оформити замовлення</span>
      <OdrerTable
        :on-amount-change="onAmountChange"
        :on-pharmacy-select="onPharmacySelect"
        :order="getOrder"
      />
      <div style="display: flex; flex-direction: column">
        <span>{{ `Загальна ціна замовлення: ${totalSum}` }}</span>
        <a-button style="width: 20rem; margin: 1rem auto" type="primary" @click="createOrder">Замовити</a-button>
      </div>
    </a-card>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { GET_ORDER, MAKE_ORDER } from '@/store/user/actions';
import OdrerTable from '@/components/common/OdrerTable';
import { GET_REMEDIES } from '@/store/catalog/actions';

export default {
  name: 'OrderPage',
  components: {
    OdrerTable,
  },
  computed: {
    ...mapGetters([
      'order',
    ]),
    totalSum() {
      this.readOrderIfAbsent();
      let sum = 0;
      this.localOrder?.remedies.forEach((r) => {
        const price = parseFloat(r.pharmacies.find((p) => p.id === r.pharmacy).price.replace(',', '.')).toFixed(2);
        sum += price * r.amount;
      });
      return parseFloat(sum).toFixed(2);
    },
    getOrder() {
      return this.localOrder;
    },
  },
  data() {
    return {
      localOrder: null,
    };
  },
  methods: {
    readOrderIfAbsent(force) {
      if (this.localOrder === null || force) {
        this.localOrder = JSON.parse(JSON.stringify(this.order));
      }
    },
    onPharmacySelect(itemId, pharmacyId) {
      this.readOrderIfAbsent();
      this.localOrder.remedies.find((r) => r.id === itemId).pharmacy = pharmacyId;
    },
    onAmountChange(itemId, amount) {
      this.readOrderIfAbsent();
      this.localOrder.remedies.find((r) => r.id === itemId).amount = amount;
    },
    createOrder() {
      this.$store.dispatch(MAKE_ORDER, this.localOrder);
    },
  },
  mounted() {
    this.$store.dispatch(GET_ORDER);
    this.$store.dispatch(GET_REMEDIES);
  },
  watch: {
    order(val) {
      this.readOrderIfAbsent(true);
    },
  },
};
</script>

<style scoped lang="scss">
.order-page-wrapper {

}
</style>
