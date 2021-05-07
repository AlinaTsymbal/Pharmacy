<template>
  <div class="catalog-page-wrapper">
    <CategoriesMenu
      class="categories-menu"
      :categories="getCategories"
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
import {GET_CATEGORIES} from '@/store/catalog/actions';
import {mapGetters} from "vuex";

export default {
  name: 'CatalogPage',
  components: {
    RemedyList,
    CategoriesMenu,
  },
  computed: {
    ...mapGetters([
      'categories',
    ]),
    getCategories() {
      return this.categories;
    },
  },
  data() {
    return {
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
  mounted() {
    this.$store.dispatch(GET_CATEGORIES);
  },
};
</script>

<style scoped lang="scss">
.catalog-page-wrapper {
  display: flex;
  flex-direction: row;

  .remedy-list {
    height: 60rem;
  }

  .categories-menu {
    width: 20rem;
    height: inherit;
  }
}
</style>
