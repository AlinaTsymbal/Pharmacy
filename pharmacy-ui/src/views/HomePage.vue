<template>
  <div class="home-page-wrapper">
    <RemedyAutoComplete style="width: 30%" :on-select="onSelect" :on-search="onSearch"/>
    <span class="about-service">{{ firstPart }}</span>

    <span class="about-service">{{ secondPart }}</span>
    <Links/>
  </div>
</template>

<script>
import Links from '@/components/home/Links.vue';
import { GET_REMEDIES } from '@/store/catalog/actions';
import RemedyAutoComplete from '@/components/common/RemedyAutoComplete';

export default {
  name: 'HomePage',
  components: {
    RemedyAutoComplete,
    Links,
  },
  data() {
    return {
      firstPart: 'Даний сервіс створено з метою допомоги у підборі та пошуку лікарських засобів'
        + ' за деякими відповідними критеріями та запитами.',
      secondPart: 'На цьому сайті ви також знайдете довідкову інформацію з лікарських засобів '
        + '(опис , інструкції), актуальні дані про наявність медикаментів і ціни на них в аптеках міста.',
    };
  },
  methods: {
    onSelect(e) {
      this.$router.push(`/remedies/${e}`);
    },
  },
  mounted() {
    this.$store.dispatch(GET_REMEDIES);
  },
};
</script>

<style scoped lang="scss">
.home-page-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;

  .about-service {
    font-size: 1.5rem;
    width: 80%;
    font-weight: bold;
  }
}

.home-page-wrapper > * {
  padding: 2rem;
}
</style>
