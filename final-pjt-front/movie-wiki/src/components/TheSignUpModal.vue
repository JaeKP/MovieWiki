<template>
  <div>
    <div class="sign-up-modal">
      <div class="sign-up font-medium-gray">
        <h2 class="sign-up__header">회원가입</h2>
        <div class="sign-up__username">
          <label for="uesername">아이디</label>
          <input type="text" id="username" v-model="username" />
        </div>
        <div class="sign-up__region">
          <label for="region">거주 지역</label>
          <select id="region" v-model="region">
            <option disabled value="">거주 지역</option>
            <option>서울</option>
            <option>인천</option>
            <option>울산</option>
            <option>대전</option>
            <option>부산</option>
            <option>경기</option>
            <option>강원</option>
            <option>충남</option>
            <option>충북</option>
            <option>경북</option>
            <option>경남</option>
            <option>전북</option>
            <option>전남</option>
            <option>제주</option>
          </select>
        </div>
        <div class="sign-up__email">
          <label for="email"> 이메일</label>
          <input type="email" v-model="email" />
        </div>
        <div class="sign-up__password1">
          <label for="pasword1">비밀 번호</label>
          <input type="password" id="password1" v-model="password1" />
        </div>
        <div class="sign-up__password2">
          <label for="pasword2">비밀 번호 확인</label>
          <input type="password" id="password2" v-model="password2" />
        </div>
        <div class="sign-up__nickname">
          <label for="nickname">닉네임</label>
          <input type="text" id="nickname" v-model="nickname" />
        </div>
        <div class="sign-up__age">
          <label for="age">나이</label>
          <input type="number" id="age" />
        </div>
      </div>
      <button>회원가입</button>
      <p>다른 아이디로 로그인 하기</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "TheSignUpModal",
  data() {
    return {
      redion: "",
    };
  },
};
</script>

<style scoped>
.sign-up-modal {
  width: 35%;
  padding: 2em;
  border-radius: 0.8em;
  background-color: white;
  z-index: 2;
  display: flex;
  flex-direction: column;
}

.sign-up {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
  grid-template-areas:
    "header ....."
    "username ....."
    "email  nickname"
    "password1 password2"
    "region age";

  gap: 1.3em;
}

.sign-up-modal button {
  margin-top: 2em;
  background-color: #5865f2;
  height: 2.5em;
  color: white;
  font-weight: 800;
  font-size: 1em;
  border-radius: 0.3em;
}

.sign-up-modal p {
  text-align: center;
  margin-top: 1em;
  color: #96989d;
}

.sign-up div {
  display: flex;
  flex-direction: column;
}

input,
select {
  border: 1px solid #b9bbbe;
  border-radius: 0.2rem;
  background-color: white;
  height: 2em;
}

.sign-up__header {
  grid-area: header;
}

.sign-up__username {
  grid-area: username;
}

.sign-up__nickname {
  grid-area: nickname;
}

.sign-up__email {
  grid-area: email;
}

.sign-up__password1 {
  grid-area: password1;
}

.sign-up__password2 {
  grid-area: password2;
}

.sign-up__region {
  grid-area: region;
}

.sign-up__age {
  grid-area: age;
}
</style>
