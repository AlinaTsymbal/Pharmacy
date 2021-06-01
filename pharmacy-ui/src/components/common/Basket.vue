<template>
  <div class="basket-wrapper">
    <div v-if="isEmpty">
      <span>Basket is empty!</span>
    </div>
    <div v-if="!isEmpty" class="basket-content-wrapper">
      <div class="row" style="margin-bottom: 1rem">
        <div class="column-left">
          <span>Найменування</span>
        </div>
        <div class="column-right">
          <span>Кількість</span>
        </div>
      </div>
      <div v-for="i in items" :key="i.id" class="row">
        <div class="column-left">
          <span>{{ i.name }}</span>
        </div>
        <div class="column-right">
          <span>{{i.amount}}</span>
        </div>
      </div>
    </div>
    <div class="footer">
      <a-button type="submit" style="margin-left: auto">Оформити замовлення</a-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Basket',
  computed: {
    isEmpty() {
      return this.items.length === 0;
    },
  },
  props: {
    items: Array,
  },
};
</script>

<style scoped lang="scss">
.basket-wrapper {
  width: 20rem;

  .basket-content-wrapper {
    width: 100%;

    .row {
      width: 100%;
      display: flex;
      flex-direction: row;

      .column-left {
        width: 70%;
      }
      .column-right {
        width: 30%;
      }
    }
  }

  .footer {
    margin-top: 1rem;
  }
}
</style>
