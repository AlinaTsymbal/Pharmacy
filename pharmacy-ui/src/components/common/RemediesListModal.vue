<template>
  <a-modal
    width="50rem"
    :visible="visible"
    @cancel="() => this.visible = false"
    @ok="() => this.visible = false"
  >
    <div class="list-wrapper">
      <div class="row">
        <div>Назва</div>
        <div>Аптека</div>
        <div>Ціна</div>
        <div>Кількість</div>
      </div>
    </div>
    <div v-for="item in items" :key="item.id" class="row">
      <div>{{ item.remedy.name }}</div>
      <div>{{ item.pharmacy.name }}</div>
      <div>{{ item.price }}</div>
      <div>{{ item.amount }}</div>
    </div>
    </div>
  </a-modal>
</template>

<script>
import {eventBus} from "@/main";

export default {
  name: "RemediesListModal",
  props: {
    items: Array,
  },
  data() {
    return {
      visible: false,
    };
  },
  mounted() {
    eventBus.$on('openListModal', () => {
      this.visible = true;
    });
  },
};
</script>

<style scoped lang="scss">
.row {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;

  div {
    width: 30rem;
  }
}
</style>
