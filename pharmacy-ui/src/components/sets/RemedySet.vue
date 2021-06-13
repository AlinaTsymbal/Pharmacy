<template>
  <div class="remedy-set-wrapper">
    <div class="set-name-wrapper">
      <span class="set-name"> {{ set.name }} </span>
    </div>
    <div v-for="d in description" class="set-info-wrapper">
      <span> {{ d }} </span>
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
  computed: {
    description() {
      return this.set?.description.split('\\n');
    },
  },
};
</script>

<style scoped lang="scss">
.remedy-set-wrapper {
  display: flex;
  flex-direction: column;

  .set-name-wrapper {

    .set-name {
      float: left;
      text-align: left;
      font-size: large;
      font-weight: bold;
    }
  }

  .set-info-wrapper {
    span {
      float: left;
      text-align: left;
    }
  }
}
</style>
