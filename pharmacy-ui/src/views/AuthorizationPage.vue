<template>
  <div class="authorization-page-wrapper">
      <LoginForm/>
      <RegistrationForm/>
  </div>
</template>

<script>
import LoginForm from '../components/common/LoginForm';
import RegistrationForm from "@/components/common/RegistrationForm";
export default {
  name: 'AuthorizationPage',
  components: {RegistrationForm, LoginForm},
};
</script>

<style scoped lang="scss">
.authorization-page-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}
</style>
