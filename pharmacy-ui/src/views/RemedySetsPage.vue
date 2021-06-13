<template>
  <div class="remedy-sets-page-wrapper">
    <div class="sets-info-wrapper" >
      <span class="about-text">
        {{ aboutText }}
      </span>
    </div>
    <RemedySet
      v-for="item in remedySets"
      :key="item.id"
      :set="item"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { GET_REMEDY_SETS } from '@/store/remedy-sets/actions';
import RemedySet from '../components/sets/RemedySet.vue';

export default {
  name: 'RemedySetsPage',
  components: {
    RemedySet,
  },
  computed: {
    ...mapGetters([
      'remedySets',
    ]),
  },
  data() {
    return {
      aboutText: 'На цій сторінці зібрано набори, що складаються з певного переліку лікарських '
        + 'засобів, які були додані відповідно до захворювання , що зазначено в назві кожного '
        + 'набору.Також призначення кожного препарату коротко описано в складі кожної з аптечок.'
        + ' При авторизації Ви зможете редагувати склад аптечок за власними побажаннями.'
        + '(При використанні будь-яких препаратів потрібно звернутись за консультацією до'
        + ' сімейного лікаря).',
    };
  },
  mounted() {
    this.$store.dispatch(GET_REMEDY_SETS);
  },
};
</script>

<style scoped lang="scss">
.remedy-sets-page-wrapper {
  display: flex;
  flex-direction: column;
  width: 80%;
  margin: auto;

  .sets-info-wrapper {
    margin: auto;
    padding-bottom: 4rem;

    .about-text {
      font-weight: bolder;
      font-size: large;
      display:block;
      text-align: left;
    }
  }

  .remedy-set {
    height: 30rem;
  }
}
</style>
