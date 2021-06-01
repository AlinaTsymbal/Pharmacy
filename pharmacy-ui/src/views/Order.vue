<template>
  <div class="order-page-wrapper">
    <div class="unavailable-remedies">
    </div>
    <div class="available-remedies">
      <BasketItem v-for=""/>
    </div>
  </div>
</template>

<script>
import BasketItem from "../components/common/BasketItem";
import {mapGetters} from "vuex";

export default {
  name: "Order",
  components: {BasketItem},
  computed: {
    ...mapGetters([
      'order',
    ]),
  },
  data() {
    return {
      order: null,
    };
  },
  methods: {
    onPharmacySelect(value) {
      alert(value);
    },
  },
};
</script>

<style scoped>

</style>
