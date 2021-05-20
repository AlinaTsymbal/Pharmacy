<template>
  <a-card>
    <div class="remedy-image-wrapper">
      <img
        v-if="!imagePresent"
        src="@/assets/image-placeholder.png"
        alt="Remedy image"
      />
    </div>
    <div class="remedy-name-wrapper">
      <span class="remedy-name">{{ remedy.name }}</span>
    </div>
    <div class="item-links">
      <a class="details-link">Details</a>
      <a class="add-to-basket-link" @click="onBasketClick">Add to basket</a>
    </div>
  </a-card>
</template>

<script>
import {ADD_TO_BASKET} from "@/store/catalog/actions";

export default {
  name: 'RemedyItem',
  computed: {
    imagePresent() {
      return this.remedy.image;
    },
  },
  props: {
    remedy: Object,
  },
  methods: {
    onBasketClick() {
      this.$store.dispatch(ADD_TO_BASKET, this.remedy);
    },
  },
};
</script>

<style scoped lang="scss">
.ant-card {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;

  .remedy-image-wrapper {
    height: 60%;
    img {
      padding: 1rem;
      width: 100%;
      height: 100%;
    }
  }

  .remedy-name-wrapper {
    display: flex;

    .remedy-name {
      float: left;
    }
  }

  .item-links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
}



</style>
