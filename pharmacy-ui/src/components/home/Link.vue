<template>
  <div class="link" @click="onclick">
    <div class="link-name-wrapper">
      <span >{{ title }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Link',
  props: {
    title: String,
  },
  methods: {
    onclick() {
      this.$router.push(this.title.toLowerCase());
    },
  },
};
</script>

<style scoped lang="scss">
.link {
  width: 20rem;
  height: 20rem;
  background-image: url('../../assets/image-placeholder.png');
  background-size: cover;
  border: 1px solid black;
  border-radius: 1rem;

  .link-name-wrapper {
    margin-top: 1rem;
    span {
      font-size: large;
      font-weight: bold;
      text-shadow: black;
    }
  }
}
</style>
