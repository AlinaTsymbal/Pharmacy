<template>
  <div class="remedy-sets-page-wrapper">
    <div class="sets-info-wrapper">
      <span>Placeholder</span>
    </div>
    <RemedySet
      v-for="item in sets"
      :key="item.id"
      :set="item"
    />
  </div>
</template>

<script>
import RemedySet from '../components/sets/RemedySet.vue';

export default {
  name: 'RemedySetsPage',
  components: {
    RemedySet,
  },
  data() {
    return {
      sets: [
        {
          id: 1,
          name: 'Remedy set 1',
          info: 'Remedy set 1',
          remedies: this.sampleRemedies(),
        },
        {
          id: 2,
          name: 'Remedy set 2',
          info: 'Remedy set 2',
          remedies: this.sampleRemedies(),
        },
        {
          id: 3,
          name: 'Remedy set 3',
          info: 'Remedy set 3',
          remedies: this.sampleRemedies(),
        },
      ],
    };
  },
  methods: {
    sampleRemedies() {
      return [
        {
          id: 1,
          name: 'Remedy 1',
        },
        {
          id: 2,
          name: 'Remedy 2',
        },
        {
          id: 3,
          name: 'Remedy 3',
        },
        {
          id: 4,
          name: 'Remedy 4',
        },
        {
          id: 5,
          name: 'Remedy 5',
        },
        {
          id: 6,
          name: 'Remedy 6',
        },
      ];
    },
  },
};
</script>

<style scoped lang="scss">
.remedy-sets-page-wrapper {
  display: flex;
  flex-direction: column;

  .sets-info-wrapper {
    span {
      font-size: large;
      font-weight: bold;
    }
  }

  .remedy-set {
    height: 30rem;
  }
}
</style>
