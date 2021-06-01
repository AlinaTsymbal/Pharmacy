<template>
  <div :class="`link ${title.toLowerCase()}`" @click="onclick" >
    <div class="link-name-wrapper">
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
  width: 30rem;
  height: 30rem;
  background-size: 30rem 30rem;
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

.med-kits {
    background-image: url('../../assets/med-kits.jpg');
}

.catalog {
    background-image: url('../../assets/catalog.jpg');
}

.sets {
    background-image: url('../../assets/sets.jpg');
}

</style>
