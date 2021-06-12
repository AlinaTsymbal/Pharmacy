<template>
  <div class="remedy-details-page-wrapper">
    <div class="image-pharmacies-row">
      <div class="image-wrapper">
        <img :src="`data:image/png;base64,${image}`"/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { GET_REMEDY_DETAILS } from '@/store/catalog/actions';

export default {
  name: 'RemedyDetailsPage',
  computed: {
    ...mapGetters([
      'details',
    ]),
    image() {
      if (this.details) {
        return this.details[0].remedy.image;
      }
      return null;
    },
  },
  mounted() {
    this.$store.dispatch(GET_REMEDY_DETAILS, this.$route.params.id);
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
    height: 20rem;
    width: 40%;
    margin-right: 10%;
  }
}
</style>
