<template>
  <div class="catalog-page-wrapper">
    <CategoriesMenu
      class="categories-menu"
      :categories="categories"
    />

    <RemedyList
      class="remedies-list"
      :remedies="remedies"
    />
  </div>
</template>

<script>
import CategoriesMenu from '../components/catalog/CategoriesMenu.vue';
import RemedyList from '../components/catalog/RemedyList.vue';

export default {
  name: 'CatalogPage',
  components: { RemedyList, CategoriesMenu },
  data() {
    return {
      categories: [
        {
          id: 1,
          name: 'category 1',
        },
        {
          id: 2,
          name: 'category 1',
        },
        {
          id: 3,
          name: 'category 1',
        },
        {
          id: 4,
          name: 'category 1',
        },
        {
          id: 5,
          name: 'category 1',
        },
      ],
      remedies: [
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
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.catalog-page-wrapper {
  display: flex;
  flex-direction: row;

  .categories-menu {
    width: 20rem;
    height: inherit;
  }
}
</style>
