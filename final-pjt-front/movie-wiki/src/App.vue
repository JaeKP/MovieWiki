<template>
  <div id="app">
    <nav-bar @signup-modal="signupModal" @login-modal="loginModal"></nav-bar>
    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  name: "App",
  data() {
    return {
      signUp: false,
      login: false,
    };
  },
  components: { NavBar },
  methods: {
    signupModal(data) {
      console.log(data);
    },
    loginModal(data) {
      console.log(data);
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap");
@import "@/assets/default.css";

body {
  font-family: "Noto Sans KR", sans-serif;
}
</style>
