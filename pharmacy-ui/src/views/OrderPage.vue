<template>
  <div class="order-page-wrapper">
    <a-card style="width: 70%; margin: auto;">
      <span style="font-size: large">Оформити замовлення</span>
      <div class="header">
        <div style="width: 20%"><span>Найменування</span></div>
        <div style="width: 20rem"><span>Аптека</span></div>
        <div style="width: 10%"><span>Кількість</span></div>
        <div style="width: 10%"><span>Ціна в аптеці</span></div>
        <div style="width: 10%"><span>Загальна ціна</span></div>
      </div>
      <a-divider/>
      <div class="unavailable-remedies">
      </div>
      <div class="available-remedies" v-if="availableRemedies">
        <BasketItem
          v-for="remedy in availableRemedies"
          :item="remedy"
          :on-select="onPharmacySelect"
          :on-amount-change="onAmountChange"
        />
      </div>
      <div style="display: flex; flex-direction: column">
        <span >{{ `Загальна ціна замовлення: ${totalSum}` }}</span>
        <a-button style="width: 20rem; margin: 1rem auto" type="primary">Замовити</a-button>
      </div>
    </a-card>
  </div>
</template>

<script>
import BasketItem from "../components/common/BasketItem";
import {mapGetters} from "vuex";
import {GET_ORDER} from "@/store/user/actions";

export default {
  name: "OrderPage",
  components: {BasketItem},
  computed: {
    ...mapGetters([
      'order',
    ]),
    availableRemedies() {
      return this.order?.remedies;
    },
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
    }
    ,
    onPharmacySelect(itemId, pharmacyId) {
      this.readOrderIfAbsent();
      this.localOrder.remedies.find(r => r.id === itemId).pharmacy = pharmacyId;
    }
    ,
    onAmountChange(itemId, amount) {
      this.readOrderIfAbsent();
      this.localOrder.remedies.find(r => r.id === itemId).amount = amount;
    }
    ,
  }
  ,
  mounted() {
    this.$store.dispatch(GET_ORDER);
  }
  ,
}
;
</script>

<style scoped lang="scss">
.order-page-wrapper {
  .header {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin: 2rem auto;
  }
}
</style>
