<template>
  <div class="remedy-details-page-wrapper">
    <div class="image-pharmacies-row">
      <div class="image-wrapper">

      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'RemedyDetailsPage',
  computed: {
    ...mapGetters([
      'user',
    ]),
  },
};
</script>

<style scoped lang="scss">
.remedy-details-page-wrapper {
  display: flex;
  flex-direction: column;

  .image-pharmacies-row {
    display: flex;
    flex-direction: row;
  }

  .image-wrapper {
    width: 40%;
    margin-right: 10%;
  }
}
</style>
