<template>
  <div class="home-page-wrapper">
    <a-input-search
      enter-button
      @search="onSearch"
      class="search-input"
      size="large"
    />
    <span class="about-service">Placeholder for 'about' text.
      Here probably will be few sentences so better adjust layout beforehand </span>
    <Links/>
  </div>
</template>

<script>
import Links from '@/components/home/Links.vue';

export default {
  name: 'HomePage',
  components: { Links },
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
  margin-top: 2rem;
}
</style>
