<template>
  <div>
      <router-link to="/foo">Go to foo</router-link>
      <router-link to="/bar">Go to bar</router-link>
    <router-view></router-view>
  </div>
</template>
<script>
  export default {
    data() {
      return {};
    },
    mounted() {},
    beforeDestroy() {},
    methods: {}
  };
</script>

<style>

</style>