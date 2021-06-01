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
        <BasketItem v-for="remedy in availableRemedies" :item="remedy" :on-select="onPharmacySelect"/>
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
  },
  data() {
    return {
      localOrder: null,
    };
  },
  methods: {
    onPharmacySelect(value) {
    },
  },
  mounted() {
    this.$store.dispatch(GET_ORDER);
  },
};
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
