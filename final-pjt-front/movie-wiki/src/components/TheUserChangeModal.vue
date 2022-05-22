<template>
  <div @click.self="hideUserChangeModal">
    <form
      class="change-modal"
      @submit.prevent="[submitChangeModal(), hideUserChangeModal()]"
    >
      <h1>회원 정보 수정</h1>
      <div class="change-modal__image">
        <user-profile-image
          width="130px"
          height="130px"
          class="change-modal__image__profile"
        />
        <label for="image"><font-awesome-icon icon="fa-solid fa-file-circle-plus"/></label>
        <input
          type="file"
          id="image"
          @change="changeProfileImage"
          ref="userImage"
          accept="image/*"
        />
      </div>
      <div>
        <label for="nickname">닉네임</label>
        <input
          type="text"
          id="nickname"
          v-model="credential.nickname"
          maxlength="10"
        />
      </div>
      <div>
        <label for="region">거주 지역</label>
        <select type="text" id="region" v-model="credential.region">
          <option disabled value="">선택해주세요</option>
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
        <label for="age">나이</label>
        <input
          type="number"
          id="age"
          v-model.number="credential.age"
          min="0"
          max="100"
        />
      </div>
      <button class="bg-icon-blue">정보 수정</button>
      <a> 회원 탈퇴</a>
    </form>
  </div>
</template>

<script>
import UserProfileImage from "@/components/UserProfileImage.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  components: { UserProfileImage },
  name: "TheUserChangeModal",
  data() {
    return {
      credential: {
        username: "",
        nickname: "",
        age: "",
        region: "",
        profile_image: "",
      },
    };
  },
  computed: {
    ...mapGetters(["userInfoDetail"]),
  },
  methods: {
    ...mapActions(["changeProfile"]),
    submitChangeModal() {
      this.changeProfile(this.credential);
    },

    changeProfileImage() {
      this.credential.profile_image = this.$refs.userImage.files;
    },
    hideUserChangeModal() {
      this.$emit("hide-user-change-modal", false);
    },
  },
  created() {
    this.credential.nickname = this.userInfoDetail.nickname;
    this.credential.age = this.userInfoDetail.age;
    this.credential.region = this.userInfoDetail.region;
    this.credential.profile_image = this.userInfoDetail.profile_image;
    this.credential.username = this.userInfoDetail.username;
  },
};
</script>

<style>
.change-modal {
  width: 50%;
  background-color: white;
  padding: 3em;
  border-radius: 0.4em;
  display: flex;
  flex-direction: column;
}
.change-modal > * {
  width: 100%;
}

#image {
  display: none;
}

.change-modal__image {
  display: flex;
  justify-content: center;
}

.change-modal__image {
  position: relative;
}

.change-modal__image label {
  position: absolute;
  bottom: 0px;
  left: 52%;
  font-size: 3em;
}
</style>
