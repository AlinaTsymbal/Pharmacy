<template>
  <div class="home-page-wrapper">
    <a-input-search
      enter-button
      @search="onSearch"
      class="search-input"
      size="large"
    />
    <span class="about-service">Даний сервіс створено з метою допомоги у підборі та пошуку лікарських засобів за деякими відповідними критеріями та запитами. </span>

    <span class="about-service">На цьому сайті ви також знайдете довідкову інформацію з лікарських засобів (опис , інструкції), актуальні дані про наявність медикаментів і ціни на них в аптеках міста.</span>
    <Links/>
  </div>
</template>

<script>
import Links from '@/components/home/Links.vue';

export default {
  name: 'HomePage',
  components: {
    Links,
  },
  methods: {
    onSearch() {
      console.log('search');
    },
  },
};
</script>

<style scoped lang="scss">
.home-page-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;

  .search-input {
    width: 40%;
  }

  .about-service {
    font-size: 1.5rem;
    width: 40%;
    font-weight: bold;
  }
}

.home-page-wrapper > * {
  padding: 2rem;
}
</style>
