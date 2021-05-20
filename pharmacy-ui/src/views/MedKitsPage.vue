<template>
  <div class="med-kits-page-wrapper">
    <div class="med-kits-info-wrapper">
      <span style=" width: 20rem; font-size: large;">
        На цій сторінці створено аптечки , які складаються з певних наборів лікарських засобів, що були додані відповідно з призначенням даних аптечок. Зареєстровані користувачі можуть редагувати склад аптечок за власними побажаннями.
      </span>
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
import {mapGetters} from 'vuex';
import MedKit from '../components/med-kits/MedKit.vue';
import {GET_MED_KITS} from '@/store/med-kits/actions';

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
  beforeMount() {
    this.$store.dispatch(GET_MED_KITS);
  },
};
</script>

<style scoped lang="scss">
.med-kits-page-wrapper {
  display: flex;
  flex-direction: column;


}

.med-kits-page-wrapper > * {
  margin: 2rem;
}
</style>
