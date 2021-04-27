<template>
  <div class="remedy-set-wrapper">
    <div class="set-name-wrapper">
      <span> {{ set.name }} </span>
    </div>
    <div class="set-info-wrapper">
      <span> {{ set.info }} </span>
    </div>
    <RemedySetRemedies :remedies="set.remedies"/>
  </div>
</template>

<script>

import RemedySetRemedies from '@/components/sets/RemedySetRemedies.vue';

export default {
  name: 'RemedySet',
  components: {
    RemedySetRemedies,
  },
  props: {
    set: Object,
  },
};
</script>

<style scoped lang="scss">
.remedy-set-wrapper {
  display: flex;
  flex-direction: column;

  .set-name-wrapper, .set-info-wrapper {
    margin: 2rem 0;
    span {
      float: left;
      font-size: large;
      font-weight: bold;
    }
  }
}
</style>
