<template>
  <a-card style="margin: 2rem 0">
    <div class="remedy-set-wrapper">
      <div class="set-name-wrapper">
        <span class="set-name"> {{ set.name }} </span>
      </div>
      <div v-for="d in description" class="set-info-wrapper">
        <span> {{ d }} </span>
      </div>
      <RemedyList :remedies="set.remedies"/>
      <a-button
        style="width: 75%;
         align-self: center"
        @click="addToBasket"
      >
        Додати набір в корзину
      </a-button>
    </div>
  </a-card>
</template>

<script>

import RemedyList from '@/components/catalog/RemedyList';
import { ADD_SET_TO_BASKET } from '@/store/remedy-sets/actions';

export default {
  name: 'RemedySet',
  components: {
    RemedyList,
  },
  props: {
    set: Object,
  },
  computed: {
    description() {
      return this.set?.description.split('\\n');
    },
  },
  methods: {
    addToBasket() {
      this.$store.dispatch(ADD_SET_TO_BASKET, this.set);
    },
  },
};
</script>

<style scoped lang="scss">
.remedy-set-wrapper {
  display: flex;
  flex-direction: column;

  .set-name-wrapper {

    .set-name {
      float: left;
      text-align: left;
      font-size: large;
      font-weight: bold;
    }
  }

  .set-info-wrapper {
    span {
      float: left;
      text-align: left;
    }
  }
}
</style>
