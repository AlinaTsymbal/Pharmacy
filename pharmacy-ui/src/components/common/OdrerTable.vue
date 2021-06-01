<template>
  <div class="order-table-wrapper">
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
  </div>
</template>

<script>
import BasketItem from "@/components/common/BasketItem";
export default {
  name: "OdrerTable",
  components: {BasketItem},
  computed: {
    availableRemedies() {
      return this.order?.remedies;
    },
  },
  props: {
    order: Object,
    onPharmacySelect: Function,
    onAmountChange: Function,
  },
};
</script>

<style scoped lang="scss">
.order-table-wrapper {
  .header {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin: 2rem auto;
  }
}
</style>
