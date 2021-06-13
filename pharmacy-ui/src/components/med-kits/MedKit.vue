<template>
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
  </div>
</template>

<script>
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
};
</script>

<style scoped lang="scss">
.med-kit-wrapper {
  display: flex;
  flex-direction: column;
  width: 80%;

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
