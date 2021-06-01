<template>
  <div class="basket-item-wrapper">
    <div class="item-name-wrapper">
      <span>{{ item.name }}</span>
    </div>
    <a-select
      :default-value="item.pharmacies[0]"
      v-if="item"
      v-model="selectedPharmacyId"
      style="width: 20rem"
      @change="handleSelect"
      mode="default"
    >
      <a-select-option v-for="pharmacy in item.pharmacies" :key="pharmacy.id">
        {{ pharmacy.name }}
      </a-select-option>
    </a-select>
    <div class="item-amount">
      <a-input type="number" v-model="amount"></a-input>
    </div>
    <div class="item-price">
      <span>{{ selectedPharmacy.price }}</span>
    </div>
    <div class="item-total">
      <span>{{ totalPrice }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "BasketItem",
  props: {
    item: Object,
    onSelect: Function,
  },
  computed: {
    getPrice() {
      return this.selectedPharmacy?.price;
    },
    getAmount() {
      return this.amount;
    },
    totalPrice() {
      return parseFloat(
        parseFloat(
          this.selectedPharmacy?.price.replace(',', '.')).toFixed(2) * this.getAmount
      ).toFixed(2);
    },
  },
  data() {
    return {
      selectedPharmacyId: this.item.pharmacies[0].id,
      selectedPharmacy: this.item.pharmacies[0],
      amount: this.item.amount,
    };
  },
  methods: {
    handleSelect(value) {
      this.onSelect(value);
      this.selectedPharmacyId = value;
      this.selectedPharmacy = this.item.pharmacies.find(p => p.id === this.selectedPharmacyId);
    },
  },
};
</script>

<style scoped lang="scss">
.basket-item-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin: 1rem auto;

  .item-name-wrapper {
    width: 20%;
  }

  .item-amount {
    width: 10%;
  }

  .item-price {
    width: 10%;
  }

  .item-total {
    width: 10%;
  }
}
</style>
