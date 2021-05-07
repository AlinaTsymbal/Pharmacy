<template>
  <div class="catalog-page-wrapper">
    <CategoriesMenu
      class="categories-menu"
      :categories="getCategories"
      :on-category-select="onCategorySelect"
    />

    <RemedyList
      class="remedies-list"
      :remedies="getRemedies"
    />
  </div>
</template>

<script>
import CategoriesMenu from '../components/catalog/CategoriesMenu.vue';
import RemedyList from '../components/catalog/RemedyList.vue';
import {GET_CATEGORIES, GET_REMEDIES} from '@/store/catalog/actions';
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
      'remedies',
    ]),
    getCategories() {
      return this.categories;
    },
    getRemedies() {
      return this.remedies;
    },
  },
  methods: {
    onCategorySelect(selectedCategories) {
      this.$store.dispatch(GET_REMEDIES, {categories: selectedCategories});
    },
  },
  mounted() {
    this.$store.dispatch(GET_CATEGORIES);
    this.$store.dispatch(GET_REMEDIES);
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
