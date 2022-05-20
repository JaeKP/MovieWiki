<template>
  <div class="bg-navbar-black nav-container">
    <ul class="font-icon-gray nav-title">
      <li>
        <router-link :to="{ name: 'home' }" class="nav-content">
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
    <ul class="nav-button">
      <font-awesome-icon
        icon="fa-solid fa-magnifying-glass"
        class="font-real-white nav-button-item"
      />
      <button
        class="bg-icon-blue font-real-white nav-button-item"
        @click="signupModal"
      >
        회원가입
      </button>
      <button
        class="bg-real-white font-nav-black nav-button-item"
        @click="loginModal"
      >
        로그인
      </button>
    </ul>

    <!-- <ul class="nav-button">
      <font-awesome-icon
        icon="fa-solid fa-magnifying-glass"
        class="font-real-white nav-button-item search-icon"
      />
      <button class="bg-icon-blue font-real-white nav-button-item">
        회원가입
      </button>
      <button class="bg-real-white font-nav-black nav-button-item">
        로그인
      </button>
    </ul> -->
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {};
  },
  computed: {},
  mothods: {
    signUpModal() {
      this.$emit("signup-modal", true);
    },
    loginModal() {
      this.$emit("login-modal", true);
    },
  },
};
</script>

<style scoped>
.nav-container {
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
  font-size: 1.1vw;
  font-weight: bold;
  transition: 0.4s;
}

a:hover {
  color: white;
  font-size: 1.12vw;
}

.nav-title {
  width: 40%;
  display: flex;
  gap: 1vw;
  justify-content: flex-start;
}

.nav-title li {
  width: 30%;
  text-align: center;
}

.nav-button {
  display: flex;
  width: 25%;
  gap: 2vw;
  align-items: flex-end;
  justify-content: flex-end;
  margin-right: 2vw;
}

.nav-button > .nav-button-item:nth-child(1) {
  font-size: 1.7vw;
}

.nav-button > .nav-button-item:nth-child(2),
.nav-button > .nav-button-item:nth-child(3) {
  padding: 0.4vw;
  border-radius: 0.3rem;
  font-weight: 700;
}

.nav-button-item {
  width: 33.33333;
  font-size: 0.9vw;
  text-align: flex-end;
}
</style>
