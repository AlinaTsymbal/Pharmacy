<template>
  <a-card class="remedy-item-wrapper">
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
      <a class="add-to-basket-link">Add to basket</a>
    </div>
  </a-card>
</template>

<script>
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
};
</script>

<style scoped lang="scss">
.remedy-item-wrapper {
  display: flex;
  flex-direction: column;
  width: 25rem;
  height: 25rem;
  padding: 1rem;

  .remedy-image-wrapper {
    img {
      padding: 1rem;
      width: 20rem;
      height: 18rem;
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
