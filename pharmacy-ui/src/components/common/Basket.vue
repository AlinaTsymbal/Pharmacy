<template>
  <a-popover title="Кошик" trigger="hover" placement="bottomLeft">
    <template slot="content">
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
              <span>{{ i.amount }}</span>
            </div>
          </div>
        </div>
        <div class="footer" v-if="!isEmpty">
          <a-button type="submit" @click="onCLickHandle">Оформити замовлення</a-button>
        </div>
      </div>
    </template>
    <a type="primary" class="basket-popup-trigger"> Кошик </a>
  </a-popover>
</template>

<script>
import router from '@/router';

export default {
  name: 'Basket',
  computed: {
    isEmpty() {
      return this.items?.length === 0;
    },
  },
  props: {
    items: Array,
  },
  methods: {
    onCLickHandle() {
      router.push('order');
    },
  },
};
</script>

<style scoped lang="scss">
.basket-wrapper, .ant-popover-title {
  padding: 2rem;
  width: 20rem;
  background-color: white;
  display: flex;
  flex-direction: column;

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
    margin: 1rem 0;
    align-self: center;
  }
}
</style>
