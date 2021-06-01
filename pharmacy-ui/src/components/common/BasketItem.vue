<template>
  <div class="basket-item-wrapper">
    <div class="item-name-wrapper">
      <span>{{item.name}}</span>
    </div>
    <a-select :default-value="item.pharmacies[0]" v-model="selectedPharmacy" style="width: 10rem">
      <a-select-option v-for="pharmacy in item.pharmacies" :key="pharmacy.id">
        {{ pharmacy.name }}
      </a-select-option>
    </a-select>
    <div class="item-amount">
      <a-input type="number" v-model="amount"></a-input>
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
  data() {
    return {
      selectedPharmacy: this.item.pharmacies[0],
      amount: this.item.amount,
    };
  },
  methods: {
    handleSelect(value) {
      this.onSelect(value);
    },
  },
};
</script>

<style scoped lang="scss">

</style>
