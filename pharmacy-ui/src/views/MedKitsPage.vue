<template>
  <div class="med-kits-page-wrapper">
    <div class="med-kits-info-wrapper" style="width: 100%">
      <span style="font-size: large;">{{aboutPage}}</span>
    </div>
    <div
      class="med-kits-list"
      v-for="item in medKits"
      :key="item.id"
    >
      <MedKit :kit="item"/>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { GET_MED_KITS } from '@/store/med-kits/actions';
import MedKit from '../components/med-kits/MedKit.vue';

export default {
  name: 'MedKitsPage',
  components: {
    MedKit,
  },
  computed: {
    ...mapGetters([
      'medKits',
    ]),
  },
  data() {
    return {
      aboutPage: 'На цій сторінці створено аптечки , які складаються з певних наборів лікарських'
        + ' засобів, що були додані відповідно з призначенням даних аптечок. Зареєстровані '
        + 'користувачі можуть редагувати склад аптечок за власними побажаннями.',
    };
  },
  beforeMount() {
    this.$store.dispatch(GET_MED_KITS);
  },
};
</script>

<style scoped lang="scss">
.med-kits-page-wrapper {
  width: 80%;
  margin: auto;
  display: flex;
  flex-direction: column;
}

.med-kits-page-wrapper > * {
  margin: 2rem;
}
</style>
