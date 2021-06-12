<template>
  <a-modal
    :title="title"
    :visible="modalVisible"
    @ok="handleOk"
    @cancel="handleOk"
    v-if="details"
  >
    <p> Доступно в аптеках:</p>
    <p v-for="d in details.pharmacies">
      {{ `${d.details.name} за адресою ${d.details.address} за ціною ${d.price}` }}
    </p>
  </a-modal>
</template>

<script>
import { eventBus } from '@/main';
import { GET_REMEDY_DETAILS } from '@/store/catalog/actions';

export default {
  name: 'RemedyDetails',
  props: {
    details: Object,
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
