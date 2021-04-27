<template>
  <div class="links-wrapper">
    <Link title="Catalog"/>
    <Link title="Sets"/>
    <Link title="Med-kits"/>
  </div>
</template>

<script>
import Link from './Link.vue';

export default {
  name: 'Links',
  components: { Link },
};
</script>

<style scoped lang="scss">
.links-wrapper {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.links-wrapper > * {
  margin-left: 2rem;
}
</style>
