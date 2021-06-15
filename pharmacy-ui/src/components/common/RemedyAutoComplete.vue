<template>
    <div class="auto-compete-wrapper">
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
            v-if="!hideSearch"
          >
            <a-icon type="search"/>
          </a-button>
        </a-input>
      </a-auto-complete>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'RemedyAutoComplete',
  computed: {
    ...mapGetters([
      'remedies',
    ]),
  },
  props: {
    onSelect: Function,
    hideSearch: {
      type: Boolean,
      required: false,
    },
  },
  data() {
    return {
      dataSource: [],
      inputValue: '',
    };
  },
  methods: {
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
};
</script>

<style scoped lang="scss">
.auto-compete-wrapper {
  width: 100%;
}
</style>
