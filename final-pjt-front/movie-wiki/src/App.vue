<template>
  <div id="app">
    <nav-bar
      @show-sign-up-modal="showSignUpModal"
      @show-log-in-modal="showLogInModal"
      @show-profile-modal="showProfileModal"
      @hide-hamburger-modal="hideHamburgerModal"
      @show-hamburger-modal="showHambuergerModal"
      class="nav-bar"
    ></nav-bar>
    <router-view
      @show-sign-up-modal="showSignUpModal"
      @show-log-in-modal="showLogInModal"
      :key="$route.fullPath"
    />
    <the-sign-up-modal
      v-if="signUp"
      class="modal"
      @hide-sign-up-modal="hideSignUpModal"
      @show-log-in-modal="showLogInModal"
    />
    <the-log-in-modal
      v-if="logIn"
      class="modal"
      @hide-log-in-modal="hideLogInModal"
      @show-sign-up-modal="showSignUpModal"
    ></the-log-in-modal>
    <the-profile-modal
      v-if="profileModal"
      @hide-profile-modal="hideProfileModal"
      class="modal__profile"
    ></the-profile-modal>
    <search-movie-modal
      v-if="searchModal"
      class="modal__search"
    ></search-movie-modal>
    <the-hamburger-modal
      class="modal__hamburger"
      @hide-hamburger-modal="hideHamburgerModal"
      v-if="hamburgerModal"
    ></the-hamburger-modal>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import TheSignUpModal from "@/components/TheSignUpModal.vue";
import TheLogInModal from "@/components/TheLogInModal.vue";
import TheProfileModal from "@/components/TheProfileModal.vue";
import SearchMovieModal from "./components/SearchMovieModal.vue";
import TheHamburgerModal from "@/components/TheHamburgerModal.vue";
import { mapGetters } from "vuex";
export default {
  name: "App",
  data() {
    return {
      signUp: false,
      logIn: false,
      profileModal: false,
      hamburgerModal: false,
    };
  },
  components: {
    NavBar,
    TheSignUpModal,
    TheLogInModal,
    TheProfileModal,
    SearchMovieModal,
    TheHamburgerModal,
  },
  computed: {
    ...mapGetters(["searchBar"]),
    searchModal() {
      return this.searchBar;
    },
  },
  methods: {
    showSignUpModal(data) {
      this.signUp = data;
      this.hamburgerModal = false;
    },
    showLogInModal(data) {
      this.logIn = data;
      this.hamburgerModal = false;
    },
    hideSignUpModal(data) {
      this.signUp = data;
    },
    hideLogInModal(data) {
      this.logIn = data;
    },
    showProfileModal(data) {
      this.profileModal = data;
      this.hamburgerModal = false;
    },
    hideProfileModal(data) {
      this.profileModal = data;
    },
    // hideSearchModal(data) {
    //   this.searchMovieModal = data;
    // },
    // showSearchModal(data) {
    //   this.searchMovieModal = data;
    // },
    hideHamburgerModal() {
      this.hamburgerModal = false;
    },
    showHambuergerModal() {
      this.hamburgerModal = true;
    },
    // showReviewModal(data) {
    //   this.reviewModal = data;
    // },
    // hideReviewModal(data) {
    //   this.reviewModal = data;
    // },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap");
@import "@/assets/default.css";
.nav-bar {
  z-index: 12;
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
  z-index: 12;
}

.modal__profile {
  position: fixed;
  top: 80px;
  right: 30px;
  z-index: 8;
}

.modal__hamburger {
  z-index: 8;
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

.modal__search {
  width: 100vw;
  height: calc(100%-80px);
  position: fixed;
  top: 80px;
  /* right: 30px; */
  z-index: 10;
  background-color: rgba(32, 34, 37, 0.8);
}
</style>
