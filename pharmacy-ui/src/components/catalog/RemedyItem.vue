<template>
  <a-card>
    <div class="remedy-image-wrapper">
      <img
        v-if="!imagePresent"
        src="@/assets/image-placeholder.png"
        alt="Remedy image"
      />
      <img
        v-if="imagePresent"
        :src="`data:image/png;base64,${remedy.image}`"
        alt="Remedy image"
      />
    </div>
    <div class="remedy-name-wrapper">
      <span class="remedy-name">{{ remedy.name }}</span>
    </div>
    <div class="item-links">
      <a class="details-link" @click="onDetailsClick">Детальніше</a>
      <a class="add-to-basket-link" @click="onBasketClick">Додати в кошик</a>
    </div>
  </a-card>
</template>

<script>
import { ADD_TO_BASKET } from '@/store/catalog/actions';

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
    onDetailsClick() {
      this.$router.push(`/remedies/${this.remedy.id}`);
    },
  },
};
</script>

<style scoped lang="scss">
.ant-card {
  .ant-card-body {
    height: 14rem;
    width: 12rem;
    display: flex;
    flex-direction: column;

    .remedy-image-wrapper {
      height: 14rem;
      width: 12rem;
      margin: auto;
      
      img {
        max-width: 100%;
        max-height: 100%;
      }
    }

    .remedy-name-wrapper {
      display: flex;

      .remedy-name {
        float: left;
        font-size: 1rem;
        font-weight: bolder;
      }
    }

    .item-links {
      margin-top: auto;
      display: flex;
      flex-direction: row;
      justify-content: space-between;

      a {
        font-size: 0.6rem;
      }
    }
  }
}

</style>
