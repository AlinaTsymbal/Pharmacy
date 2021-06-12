<template>
  <div class="home-page-wrapper">
    <div class="auto-compete-wrapper" style="width: 30rem;">
      <a-auto-complete
        class="global-search"
        size="large"
        style="width: 100%"
        placeholder="Введіть назву препарату"
        option-label-prop="title"
        @select="onSelect"
        :data-source="dataSource"
        v-model="inputValue"
        @search="onSearch"
      >
        <a-input
          v-model="inputValue"
        >
          <a-button
            slot="suffix"
            style="margin-right: -12px"
            class="search-btn"
            size="large"
            type="primary"
          >
            <a-icon type="search"/>
          </a-button>
        </a-input>
      </a-auto-complete>
    </div>
    <span class="about-service">{{ firstPart }}</span>

    <span class="about-service">{{ secondPart }}</span>
    <Links/>
  </div>
</template>

<script>
import Links from '@/components/home/Links.vue';
import { mapGetters } from 'vuex';
import { GET_REMEDIES } from '@/store/catalog/actions';

export default {
  name: 'HomePage',
  components: {
    Links,
  },
  computed: {
    ...mapGetters([
      'remedies',
    ]),
  },
  data() {
    return {
      dataSource: [],
      inputValue: '',
      firstPart: 'Даний сервіс створено з метою допомоги у підборі та пошуку лікарських засобів'
        + ' за деякими відповідними критеріями та запитами.',
      secondPart: 'На цьому сайті ви також знайдете довідкову інформацію з лікарських засобів '
        + '(опис , інструкції), актуальні дані про наявність медикаментів і ціни на них в аптеках міста.',
    };
  },
  methods: {
    onSelect(e) {
      alert(e);
    },
    onSearch() {
      if (this.remedies.length > 0) {
        const searchValue = this.inputValue.toLowerCase();
        if (searchValue) {
          this.dataSource = this.remedies.filter((r) => r.name.toLowerCase().includes(searchValue))
            .map((r) => ({
              text: r.name,
              value: r.id.toString(),
            })).sort((r1, r2) => {
              const firstIndex = r1.text.toLowerCase().indexOf(searchValue);
              const secondIndex = r2.text.toLowerCase().indexOf(searchValue);
              if (firstIndex < secondIndex) {
                return -1;
              }
              if (firstIndex > secondIndex) {
                return 1;
              }
              return 0;
            });
        } else {
          this.dataSource = [];
        }
      } else {
        this.dataSource = [];
      }
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
