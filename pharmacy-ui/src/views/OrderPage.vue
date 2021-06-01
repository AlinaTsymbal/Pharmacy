<template>
  <div class="order-page-wrapper">
    <a-card style="width: 70%; margin: auto;">
      <span style="font-size: large">Оформити замовлення</span>
      <OdrerTable
        :on-amount-change="onAmountChange"
        :on-pharmacy-select="onPharmacySelect"
        :order="localOrder"
      />
      <div style="display: flex; flex-direction: column">
        <span>{{ `Загальна ціна замовлення: ${totalSum}` }}</span>
        <a-button style="width: 20rem; margin: 1rem auto" type="primary" @click="createOrder">Замовити</a-button>
      </div>
    </a-card>
  </div>
</template>

<script>
import BasketItem from "../components/common/BasketItem";
import {mapGetters} from "vuex";
import {GET_ORDER, MAKE_ORDER} from "@/store/user/actions";
import OdrerTable from "@/components/common/OdrerTable";

export default {
  name: "OrderPage",
  components: {OdrerTable},
  computed: {
    ...mapGetters([
      'order',
    ]),
    totalSum() {
      this.readOrderIfAbsent();
      let sum = 0;
      this.localOrder?.remedies.forEach((r) => {
        const price = parseFloat(r.pharmacies.find(p => p.id === r.pharmacy).price.replace(',', '.')).toFixed(2)
        sum += price * r.amount;
      });
      return parseFloat(sum).toFixed(2);
    },
  },
  data() {
    return {
      localOrder: null,
    };
  },
  methods: {
    readOrderIfAbsent() {
      if (this.localOrder === null) {
        this.localOrder = JSON.parse(JSON.stringify(this.order));
      }
    },
    onPharmacySelect(itemId, pharmacyId) {
      this.readOrderIfAbsent();
      this.localOrder.remedies.find(r => r.id === itemId).pharmacy = pharmacyId;
    },
    onAmountChange(itemId, amount) {
      this.readOrderIfAbsent();
      this.localOrder.remedies.find(r => r.id === itemId).amount = amount;
    },
    createOrder() {
      this.$store.dispatch(MAKE_ORDER, this.localOrder);
    }
  },
  mounted() {
    this.$store.dispatch(GET_ORDER);
  },
};
</script>

<style scoped lang="scss">
.order-page-wrapper {

}
</style>
