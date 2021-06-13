<template>
  <div class="authorization-page-wrapper">
      <LoginForm/>
      <RegistrationForm/>
  </div>
</template>

<script>
import RegistrationForm from '@/components/common/RegistrationForm';
import LoginForm from '../components/common/LoginForm';

export default {
  name: 'AuthorizationPage',
  components: {
    RegistrationForm,
    LoginForm,
  },
};
</script>

<style scoped lang="scss">
.authorization-page-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}
</style>
