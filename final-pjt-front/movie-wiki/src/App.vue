<template>
  <div id="app">
    <nav-bar
      @show-sign-up-modal="showSignUpModal"
      @show-log-in-modal="showLogInModal"
    ></nav-bar>
    <card-list></card-list>
    <router-view />
    <the-sign-up-modal
      v-if="signUp"
      class="modal"
      @hide-sign-up-modal="hideSignUpModal"
    />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import TheSignUpModal from "@/components/TheSignUpModal.vue";
import CardList from "./components/CardList.vue";

export default {
  name: "App",
  data() {
    return {
      signUp: false,
      logIn: false,
    };
  },
  components: { NavBar, TheSignUpModal, CardList },
  methods: {
    showSignUpModal(data) {
      this.signUp = data;
    },
    showLogInModal(data) {
      this.logIn = data;
    },
    hideSignUpModal(data) {
      this.signUp = data;
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

.modal {
  width: 100vw;
  height: 100vh;
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(32, 34, 37, 0.8);
}
</style>
