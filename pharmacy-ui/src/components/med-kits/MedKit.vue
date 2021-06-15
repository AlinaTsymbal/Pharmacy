<template>
  <a-card style="margin: 2rem 0">
  <div class="med-kit-wrapper">
    <div class="med-kit-name-wrapper">
      <span> {{ kit.name }} </span>
    </div>
    <div v-for="d in description" class="med-kit-info-wrapper">
      <span> {{ d }} </span>
    </div>

    <div class="med-kit-remedies-wrapper">
      <RemedyList
        :remedies="kit.remedies"
      />
    </div>
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
import { ADD_MED_KIT_TO_BASKET } from '@/store/med-kits/actions';
import RemedyList from '../catalog/RemedyList.vue';

export default {
  name: 'MedKit',
  components: {
    RemedyList,
  },
  computed: {
    description() {
      return this.kit?.description.split('\\n');
    },
  },
  props: {
    kit: Object,
  },
  methods: {
    addToBasket() {
      this.$store.dispatch(ADD_MED_KIT_TO_BASKET, this.kit);
    },
  },
};
</script>

<style scoped lang="scss">
.med-kit-wrapper {
  display: flex;
  flex-direction: column;
  width: 100%;

  .med-kit-name-wrapper {
    span {
      float: left;
      font-size: large;
      font-weight: bold;
    }
  }

  .med-kit-info-wrapper {
    span {
      float: left;
      font-size: larger;
    }
  }
}
</style>
