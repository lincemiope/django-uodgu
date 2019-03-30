<template>
  <div class="home">
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "../common/api.service";
export default {
  name: "home",
  components: {
    HelloWorld
  }
};
</script>
