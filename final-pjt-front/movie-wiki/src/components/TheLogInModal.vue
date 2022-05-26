<template>
  <div @click.self="hideLogInModal">
    <form
      @submit.prevent="[logIn(credential), hideLogInModal()]"
      class="log-in-modal"
    >
      <h1 class="font-medium-gray">로그인</h1>
      <input type="text" v-model="credential.username" placeholder="아이디" />
      <input
        type="password"
        v-model="credential.password"
        placeholder="비밀번호"
      />
      <button>로그인</button>
      <a @click.self="[hideLogInModal(), showSignUpModal()]">회원 가입</a>
    </form>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "TheLogInModal",
  data() {
    return {
      credential: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    ...mapActions(["logIn"]),
    hideLogInModal() {
      this.$emit("hide-log-in-modal", false);
    },
    showSignUpModal() {
      this.$emit("show-sign-up-modal", true);
    },
  },
};
</script>

<style scoped>
.log-in-modal {
  width: 20%;
  min-width: 350px;
  padding: 2em;
  border-radius: 0.8em;
  background-color: white;
  z-index: 99;
  display: flex;
  flex-direction: column;
  gap: 1em;
}

input {
  border: 1px solid #dcddde;
  border-radius: 0.2rem;
  background-color: white;
  height: 3em;
  font-weight: 500;
}

button {
  margin-top: 2em;
  background-color: #5865f2;
  height: 3em;
  color: white;
  font-weight: 600;
  font-size: 1em;
  border-radius: 0.3em;
}

a {
  font-weight: 300;
  color: #96989d;
  text-align: center;
}

h1 {
  margin-bottom: 1em;
}
</style>
