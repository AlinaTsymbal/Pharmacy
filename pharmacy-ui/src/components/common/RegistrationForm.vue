<template>
  <div>
    <h2>Register</h2>
    <a-card>
      <a-form
        style="width: 30rem"
        id="components-form-demo-normal-registration"
        class="registration-form"
        @submit="handleSubmit"
      >
        <a-form-item>
          <a-input
            v-model="username"
            v-decorator="[
          'username',
          { rules: [{ required: true, message: 'Please input your username!' }] },
        ]"
            placeholder="Username"
          >
            <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)"/>
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-input
            v-model="password"
            v-decorator="[
          'password',
          { rules: [{ required: true, message: 'Please input your Password!' }] },
        ]"
            type="password"
            placeholder="Password"
          >
            <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)"/>
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-button
            type="primary"
            html-type="submit"
            class="login-form-button"
            style="width: 100%"
          >
            Register
          </a-button>
        </a-form-item>
      </a-form>
    </a-card>
  </div>
</template>

<script>
import { REGISTER } from '@/store/user/actions';

export default {
  name: 'RegistrationForm',
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: 'normal_registration' });
  },
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log(values);
          this.$store.dispatch(REGISTER, {
            username: this.username,
            password: this.password,
          });
        }
      });
    },
  },
};
</script>

<style scoped>

</style>
