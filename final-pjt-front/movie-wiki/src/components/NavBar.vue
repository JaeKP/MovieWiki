<template>
  <div class="bg-navbar-black nav">
    <ul class="font-icon-gray nav__title">
      <li>
        <router-link :to="{ name: 'home' }" class="nav__content">
          홈
        </router-link>
      </li>
      <li>
        <router-link :to="{ name: 'trailer' }"> 트레일러 </router-link>
      </li>
      <li>
        <router-link :to="{ name: 'articles' }"> 게시판 </router-link>
      </li>
    </ul>
    <ul class="nav__button" v-show="!isLoggedIn">
      <font-awesome-icon
        icon="fa-solid fa-magnifying-glass"
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
    <ul class="nav__profile" v-show="isLoggedIn">
      <font-awesome-icon
        icon="fa-solid fa-magnifying-glass"
        class="font-real-white nav__icon nav__profile__item"
        v-if="!searchBar"
      />
      <font-awesome-icon
        icon="fa-solid fa-x"
        v-if="searchBar"
        class="font-real-white nav__icon nav__profile__item"
      />
      <div class="nav__profile__item" @click="showProfileModal"></div>
    </ul>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "NavBar",
  data() {
    return {
      searchBar: true,
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn"]),
  },
  methods: {
    showSignUpModal() {
      this.$emit("show-sign-up-modal", true);
    },
    showLogInModal() {
      this.$emit("show-log-in-modal", true);
    },
    showProfileModal() {
      this.$emit("show-profile-modal", true);
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
  width: 30%;
  display: flex;
  justify-content: flex-start;
}

@media (max-width: 1210px) {
  .nav__title {
    width: 50%;
  }
  .nav > .nav__button {
    width: 45%;
  }
}

.nav__title li {
  width: 30%;
  text-align: center;
}

.nav__button {
  display: flex;
  width: 25%;
  gap: 2em;
  align-items: flex-end;
  justify-content: flex-end;
  margin-right: 2em;
}

.nav__button > .nav__button__item:nth-child(1) {
  font-size: 2em;
}

.nav__button > .nav__button__item:nth-child(2),
.nav__button > .nav__button__item:nth-child(3) {
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

.nav__profile > div {
  background-image: url(@/assets/profile.png);
  width: 60px;
  height: 60px;
  margin-right: 0.5em;
  border: 2px solid #333;
  border-radius: 50%;
  background-color: white;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
}

.nav__profile > .nav__profile__item:nth-child(1) {
  font-size: 2em;
}
</style>
