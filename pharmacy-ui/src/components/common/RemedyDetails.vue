<template>
  <a-modal
    :title="title"
    :visible="modalVisible"
    @ok="handleOk"
    @cancel="handleOk"
  >
    <p> Доступно в аптеках:</p>
    <p v-for="d in details">
      {{ `${d.pharmacy.name} за адресою ${d.pharmacy.address} за ціною ${d.price}` }}
    </p>
  </a-modal>
</template>

<script>
import {eventBus} from '@/main';
import {GET_REMEDY_DETAILS} from "@/store/catalog/actions";

export default {
  name: "RemedyDetails",
  props: {
    details: Array,
  },
  data() {
    return {
      modalVisible: false,
      title: '',
    };
  },
  methods: {
    handleOk() {
      this.modalVisible = false;
    },
  },
  mounted() {
    eventBus.$on('openRemedyDetails', (id, title) => {
      this.modalVisible = true;
      this.title = title;
      this.$store.dispatch(GET_REMEDY_DETAILS, id);
    });
  },
};
</script>

<style scoped>

</style>
