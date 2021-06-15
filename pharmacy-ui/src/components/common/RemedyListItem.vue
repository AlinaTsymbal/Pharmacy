<template>
  <div class="row">
    <div class="column">{{ `${order.client.last_name} ${order.client.last_name}` }}</div>
    <div class="column">{{ order.client.phone }}</div>
    <div class="column">{{ order.created_at }}</div>
    <div class="column" :key="order.id"><a @click="handleClick">Замовлені ліки</a></div>
    <div class="column">{{ getStatus() }}</div>
    <div class="column" v-if="order.resolved_at === null">
      <a @click="closeOrder"> Закрити замовлення</a>
    </div>
    <div class="column" v-if="order.resolved_at !== null">
      <span style="visibility: hidden">test </span>
    </div>
  </div>
</template>

<script>
import moment from 'moment';
import { CLOSE_ORDER } from '@/store/user/actions';

export default {
  name: 'RemedyListItem',
  props: {
    order: Object,
    handleDetails: Function,
  },
  methods: {
    handleClick() {
      this.handleDetails(this.order.id);
    },
    moment,
    getStatus() {
      if (!this.order.resolved_at) {
        return `Замовлено ${this.moment(this.order.created_at).format('YYYY:MM:HH:mm')}`;
      }
      const start = moment(this.order.created_at, 'DD-MM-YYYY');
      const finish = moment(this.order.resolved_at, 'DD-MM-YYYY');
      return `Виконаний ${start.diff(finish, 'minutes')} днів тому`;
    },
    closeOrder() {
      this.$store.dispatch(CLOSE_ORDER, this.order.id);
    },
  },
};
</script>

<style scoped lang="scss">

.row {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin: 1rem auto;
  width: 100%;

  .column {
    width: 20%;
  }
}
</style>
