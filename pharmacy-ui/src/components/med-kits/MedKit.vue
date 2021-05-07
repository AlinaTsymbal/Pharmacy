<template>
  <div class="med-kit-wrapper">
    <div class="med-kit-name-wrapper">
      <span> {{ kit.name }} </span>
    </div>
    <div class="med-kit-info-wrapper">
      <span> {{ kit.description }} </span>
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
  props: {
    kit: Object,
  },
};
</script>

<style scoped lang="scss">
.med-kit-wrapper {
  display: flex;
  flex-direction: column;

  .med-kit-name-wrapper, .med-kit-info-wrapper {
    span {
      float: left;
      margin: 1rem;
      font-size: large;
      font-weight: bold;
    }
  }
}
</style>
