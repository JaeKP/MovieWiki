<template>
  <div class="bg-navbar-black nav">
    <div class="nav__title">
      <div class="nav__title__logo" @click="moveHome"></div>
      <ul class="font-icon-gray nav__title__list">
        <li @click="[hideSearchModal(), hideHamburgerModal()]">
          <router-link :to="{ name: 'home' }" class="nav__content">
            홈
          </router-link>
        </li>
        <li @click="[hideSearchModal(), hideHamburgerModal()]">
          <router-link
            :to="{
              name: 'articles',
              params: { newPayload: newPayload },
            }"
          >
            게시판
          </router-link>
        </li>
        <li @click="[hideSearchModal(), hideHamburgerModal()]">
          <router-link :to="{ name: 'trailer' }"> 쇼츠 </router-link>
        </li>
      </ul>
    </div>
    <!-- 로그인 x -->
    <ul class="nav__button" v-show="!isLoggedIn">
      <font-awesome-icon
        @click="showHambergerModal"
        icon="fa-solid fa-bars"
        class="font-real-white nav__button__item nav__icon__react nav__icon"
      />
      <font-awesome-icon
        v-if="!searchModal"
        icon="fa-solid fa-magnifying-glass"
        @click="showSearchModal"
        class="font-real-white nav__button__item nav__icon"
      />
      <font-awesome-icon
        icon="fa-solid fa-x"
        v-else
        @click="hideSearchModal"
        class="font-real-white nav__button__item"
      />
      <button
        class="bg-icon-blue font-real-white nav__button__item"
        @click="showSignUpModal"
      >
        회원가입
      </button>
      <button
        class="bg-real-white font-nav-black nav__button__item"
        @click="showLogInModal"
      >
        로그인
      </button>
    </ul>
    <!-- 로그인 했을 때 -->
    <ul class="nav__profile" v-if="isLoggedIn">
      <font-awesome-icon
        @click="showHambergerModal"
        icon="fa-solid fa-bars"
        class="font-real-white nav__icon__react nav__profile__item"
      />
      <font-awesome-icon
        @click="showSearchModal"
        icon="fa-solid fa-magnifying-glass"
        class="font-real-white nav__profile__item"
        v-if="!searchModal"
      />
      <font-awesome-icon
        @click="hideSearchModal"
        icon="fa-solid fa-x"
        v-else
        class="font-real-white nav__profile__item"
      />
      <user-profile-image
        @click.native="[showProfileModal(), hideSearchModal()]"
        :image="userProfile.image"
      ></user-profile-image>
    </ul>
    <!-- 반응형 웹 -->
    <!-- <ul class="nav__button__react" v-show="!isLoggedIn">
      <font-awesome-icon
        @click="showHambergerModal"
        icon="fa-solid fa-bars"
        class="font-real-white nav__icon__react"
      />
      <font-awesome-icon
        @click="showSearchModal"
        icon="fa-solid fa-magnifying-glass"
        class="font-real-white nav__icon__react"
        v-if="!searchModal"
      />
      <font-awesome-icon
        @click="hideSearchModal"
        icon="fa-solid fa-x"
        v-else
        class="font-real-white nav__icon__react"
      />
      <button
        class="bg-icon-blue font-real-white nav__button__item"
        @click="showSignUpModal"
      >
        회원가입
      </button>
      <button
        class="bg-real-white font-nav-black nav__button__item"
        @click="showLogInModal"
      >
        로그인
      </button>
    </ul> -->
    <!-- 반응형 웹 (모바일대응 => 로그인x) -->
    <!-- <ul class="nav__button__react__mobile" v-show="!isLoggedIn">
      <font-awesome-icon
        @click="showHambergerModal"
        icon="fa-solid fa-bars"
        class="font-real-white nav__icon__react"
      />
      <font-awesome-icon
        @click="showSearchModal"
        icon="fa-solid fa-magnifying-glass"
        class="font-real-white nav__icon__react"
        v-if="!searchModal"
      />
      <font-awesome-icon
        @click="hideSearchModal"
        icon="fa-solid fa-x"
        v-else
        class="font-real-white nav__icon__react"
      />
    </ul> -->
  </div>
</template>

<script>
import UserProfileImage from "@/components/UserProfileImage.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "NavBar",
  components: {
    UserProfileImage,
  },
  data() {
    return {
      newPayload: {
        type: "all",
        query: null,
        title: null,
        content: null,
        nickname: null,
      },
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "userProfile", "searchBar"]),
    searchModal() {
      return this.searchBar;
    },
  },
  methods: {
    ...mapActions(["setSearchBar"]),
    showSignUpModal() {
      this.$emit("show-sign-up-modal", true);
    },
    showLogInModal() {
      this.$emit("show-log-in-modal", true);
    },
    showProfileModal() {
      this.$emit("show-profile-modal", true);
    },
    showSearchModal() {
      this.setSearchBar(true);
      this.$emit("hide-hamburger-modal");
    },
    hideSearchModal() {
      this.setSearchBar(false);
    },
    hideHamburgerModal() {
      this.$emit("hide-hamburger-modal");
    },
    showHambergerModal() {
      this.$emit("show-hamburger-modal");
    },
    moveHome() {
      this.$router.push({
        name: "home",
      });
    },
  },
};
</script>

<style scoped>
.nav {
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  right: 0;
}

ul {
  display: flex;
}

a {
  text-align: center;
  text-decoration: none;
  color: inherit;
  display: block;
  padding: 1em;
  font-size: 1.2em;
  font-weight: bold;
  transition: 0.4s;
}

a:hover {
  color: white;
  font-size: 1.25em;
}

.nav__title {
  margin-left: 10px;
  width: 30%;
  display: flex;
  align-items: center;
}

.nav__title__logo {
  text-align: center;
  width: 100px;
  background-image: url("@/assets/logo.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 70%;
  height: 70px;
}

.nav__title__list {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  flex-grow: 1;
}

@media (max-width: 1500px) {
  .nav__title {
    width: 45%;
  }
}

@media (max-width: 1000px) {
  .nav__title {
    width: 65%;
    flex-grow: 1;
  }
}

@media (max-width: 800px) {
  .nav__title__list {
    display: none;
  }
  .nav__title {
    width: 100px;
  }
  .nav__button {
    width: 100% !important;
    flex-grow: 1;
  }
  .nav .nav__icon__react {
    display: block;
  }
}

@media (max-width: 585px) {
  .nav__title {
    width: 70px !important;
  }
  .nav__button > .nav__button__item {
    font-weight: 600;
    font-size: 0.8em;
    padding: 0.3em;
  }
  .nav > .nav__button {
    gap: 0.5em;
  }
  .nav__button > .nav__button__item:nth-child(1),
  .nav__button > .nav__button__item:nth-child(2) {
    font-size: 1.5em !important;
  }
  .nav__title__logo {
    width: 70px;
  }
}

.nav__icon__react {
  display: none;
}

.nav__title li {
  width: 30%;
  text-align: center;
}

.nav__button {
  display: flex;
  width: 35%;
  gap: 2em;
  align-items: center;
  justify-content: flex-end;
  margin-right: 2em;
}

.nav__button > .nav__button__item:nth-child(1),
.nav__button > .nav__button__item:nth-child(2) {
  font-size: 2em;
}

.nav__button > .nav__button__item:nth-child(3),
.nav__button > .nav__button__item:nth-child(4) {
  padding: 0.5em 1em;
  border-radius: 0.3rem;
  font-weight: 600;
}

.nav__button__item {
  width: 33.33333;
  font-size: 1em;
  text-align: flex-end;
}

.nav__profile {
  display: flex;
  gap: 2em;
  align-items: center;
  margin-right: 2em;
}

.nav__profile > .nav__profile__item:nth-child(1),
.nav__profile > .nav__profile__item:nth-child(2) {
  font-size: 2em;
}
</style>
