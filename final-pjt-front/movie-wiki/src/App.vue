<template>
  <div id="app">
    <nav-bar
      @show-sign-up-modal="showSignUpModal"
      @show-log-in-modal="showLogInModal"
      @show-profile-modal="showProfileModal"
      @show-search-modal="showSearchModal"
      @hide-search-modal="hideSearchModal"
      class="nav-bar"
    ></nav-bar>
    <router-view />
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
      v-if="SearchMovieModal"
      class="modal__search"
      @hide-search-modal="hideSearchModal"
    ></search-movie-modal>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import TheSignUpModal from "@/components/TheSignUpModal.vue";
import TheLogInModal from "@/components/TheLogInModal.vue";
import TheProfileModal from "@/components/TheProfileModal.vue";
import SearchMovieModal from "./components/SearchMovieModal.vue";

export default {
  name: "App",
  data() {
    return {
      signUp: false,
      logIn: false,
      profileModal: false,
      SearchMovieModal: false,
    };
  },
  components: {
    NavBar,
    TheSignUpModal,
    TheLogInModal,
    TheProfileModal,
    SearchMovieModal,
  },
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
    hideLogInModal(data) {
      this.logIn = data;
    },
    showProfileModal(data) {
      this.profileModal = data;
    },
    hideProfileModal(data) {
      this.profileModal = data;
    },
    hideSearchModal() {
      this.SearchMovieModal = false;
    },
    showSearchModal() {
      this.SearchMovieModal = true;
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap");
@import "@/assets/default.css";
.nav-bar {
  z-index: 3;
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
  z-index: 4;
}

.modal__profile {
  position: fixed;
  top: 80px;
  right: 30px;
  z-index: 4;
}

.modal__search {
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 80px;
  /* right: 30px; */
  z-index: 3;
}
</style>
