<template>
  <div class="basket-item-wrapper">
    <div class="item-name-wrapper" v-if="!beingEdited">
      <span>{{ item.name }}</span>
    </div>
    <a-select
      :default-value="item.pharmacies[0]"
      v-if="item && !beingEdited"
      v-model="selectedPharmacyId"
      style="width: 30%;"
      @change="handleSelect"
      mode="default"
    >
      <a-select-option
        v-for="pharmacy in item.pharmacies" :key="pharmacy.id">
        {{ pharmacy.name }}
      </a-select-option>
    </a-select>
    <div v-if="beingEdited" style="width: 50%; padding-left: 5%">
      <RemedyAutoComplete :hide-search="true" style=""/>
    </div>
    <div class="item-amount">
      <a-input type="number" v-model="amount" @change="handleAmountChange" :disabled="beingEdited"/>
    </div>
    <div class="item-price">
      <span>{{ selectedPharmacy.price }}</span>
    </div>
    <div class="item-total">
      <span>{{ totalPrice }}</span>
    </div>
    <div class="actions" v-if="!beingEdited">
      <a style="margin-right: 0.5rem" @click="handleReplaceClick">Замінити</a>
      <a @click="removeFromBasket">Видалити</a>
    </div>
    <div class="actions" v-if="beingEdited">
      <a style="margin-right: 0.5rem" @click="() => alert('NOT IMPLEMENTED')">Застосувати</a>
      <a @click="() => alert('NOT IMPLEMENTED')">Відмінити</a>
    </div>
  </div>
</template>

<script>
import { DELETE_FROM_BASKET } from '@/store/user/actions';
import RemedyAutoComplete from '@/components/common/RemedyAutoComplete';

export default {
  name: 'BasketItem',
  components: { RemedyAutoComplete },
  props: {
    remedies: Array,
    item: Object,
    onSelect: Function,
    onAmountChange: Function,
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
          this.selectedPharmacy?.price.replace(',', '.'),
        ).toFixed(2) * this.getAmount,
      ).toFixed(2);
    },
  },
  data() {
    return {
      beingEdited: false,
      selectedPharmacyId: this.item.pharmacies[0].id,
      selectedPharmacy: this.item.pharmacies[0],
      amount: this.item.amount,
    };
  },
  methods: {
    handleSelect(value) {
      this.onSelect(this.item.id, value);
      this.selectedPharmacyId = value;
      this.selectedPharmacy = this.item.pharmacies.find((p) => p.id === this.selectedPharmacyId);
    },
    handleAmountChange() {
      if ((this.amount) !== '') {
        this.onAmountChange(this.item.id, this.amount);
      }
    },
    removeFromBasket() {
      this.$store.dispatch(DELETE_FROM_BASKET, this.item.id);
    },
    handleReplaceClick() {
      this.beingEdited = true;
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
    margin-left: 0.5rem
  }

  .item-price {
    width: 10%;
  }

  .item-total {
    width: 10%;
  }

  .actions {
    width: 20%;
  }
}

.visible {
  visibility: hidden;
}
</style>
