<template>
  <a-modal
    title="Title"
    :visible="modalVisible"
    @ok="handleOk"
    @cancel="handleOk"
  >
    <p>Placeholder for remedy details</p>
  </a-modal>
</template>

<script>
import { eventBus } from '@/main';

export default {
  name: "RemedyDetails",
  data() {
    return {
      modalVisible: false,
    };
  },
  methods: {
    handleOk() {
      this.modalVisible = false;
    },
  },
  mounted() {
    eventBus.$on('openRemedyDetails', (id) => {
      this.modalVisible = true;
    });
  },
};
</script>

<style scoped>

</style>
