<template>
  <div class="link" @click="onclick">
    <p>{{ title }}</p>
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

<style scoped>
.link {
  width: 15rem;
  height: 15rem;
  background-color: red;
}
</style>
