<template>
  <a-card class="profile-wrapper" v-if="newData">
    <h2>Редагування особистої інформації</h2>
    <div class="input-wrapper">
      <label>Номер телефону:</label>
      <a-input v-model="newData.phone"></a-input>
    </div>
    <div class="input-wrapper">
      <label>Адреса:</label>
      <a-input v-model="newData.address"></a-input>
    </div>
    <div class="input-wrapper">
      <label>Ім'я:</label>
      <a-input v-model="newData.first_name"></a-input>
    </div>
    <div class="input-wrapper">
      <label>Прізвище</label>
      <a-input v-model="newData.last_name"></a-input>
    </div>
    <div class="input-wrapper">
      <label>Email:</label>
      <a-input v-model="newData.email"></a-input>
    </div>
    <a-button
      type="primary"
      style="width: 60%;
      margin: auto"
      @click="updateUser"
    >
      Зберегти зміни
    </a-button>
  </a-card>
</template>

<script>
import { mapGetters } from 'vuex';
import { GET_USER, UPDATE_USER } from '@/store/user/actions';

export default {
  name: 'ProfilePage',
  computed: {
    ...mapGetters([
      'user',
    ]),
  },
  data() {
    return {
      newData: null,
    };
  },
  methods: {
    updateUser() {
      this.$store.dispatch(UPDATE_USER, this.newData);
      this.newData = JSON.parse(JSON.stringify(this.user));
    },
  },
  mounted() {
    this.$store.dispatch(GET_USER, localStorage.getItem('auth-token'));
    this.newData = JSON.parse(JSON.stringify(this.user));
  },
  watch: {
    user(val) {
      this.newData = JSON.parse(JSON.stringify(this.user));
    },
  },
};
</script>

<style scoped lang="scss">
.profile-wrapper {
  width: 40%;
  margin: auto;
  display: flex;
  flex-direction: column;

  .input-wrapper {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 1rem 0;

    label {
      width: 80%;
      text-align: left;
      margin: auto;
    }

    .ant-input {
      width: 80%;
      margin: auto;
    }
  }

}
</style>
