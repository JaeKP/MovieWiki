<template>
  <div @click.self="hideUserChangeModal">
    <form
      class="change-modal"
      @submit.prevent="[submitChangeModal(), hideUserChangeModal()]"
    >
      <h1 class="font-medium-gray">회원 정보 수정</h1>
      <div class="change-modal__image">
        <div>
          <user-profile-image
            width="130px"
            height="130px"
            :image="userProfile.image"
          />
          <label for="image" class="font-nav-black"
            ><font-awesome-icon icon="fa-solid fa-circle-plus"
          /></label>
          <input
            type="file"
            id="image"
            @change="[changeProfileImage()]"
            ref="userImage"
            accept="image/*"
          />
        </div>
      </div>
      <div>
        <label for="nickname">닉네임</label>
        <input
          type="text"
          id="nickname"
          v-model="credential.nickname"
          maxlength="10"
          minlength="2"
        />
      </div>
      <div>
        <div>
          <label for="region">거주 지역</label>
          <select type="text" id="region" v-model="credential.region" required>
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
        </div>
        <div>
          <label for="age">나이</label>
          <input
            type="number"
            id="age"
            v-model.number="credential.age"
            min="10"
            max="99"
            required
          />
        </div>
      </div>
      <div>
        <button class="bg-icon-blue">정보 수정</button>
        <a class="font-icon-gray" @click="deleteUser"> 회원 탈퇴</a>
      </div>
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
    ...mapGetters(["userInfoDetail", "userProfile"]),
  },
  methods: {
    ...mapActions(["changeProfile", "temporaryImageUpload"]),
    submitChangeModal() {
      this.changeProfile(this.credential);
    },

    changeProfileImage() {
      this.credential.profile_image = this.$refs.userImage.files;
      this.temporaryImageUpload(this.credential);
    },
    hideUserChangeModal() {
      this.$emit("hide-user-change-modal", false);
    },
    deleteUser() {
      this.$emit("delete-user");
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

<style scoped>
.change-modal {
  width: 40%;
  background-color: white;
  padding: 3em;
  border-radius: 0.4em;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2em;
}

@media (max-width: 1000px) {
  .change-modal {
    width: 50%;
  }
}

@media (max-width: 900px) {
  .change-modal {
    width: 60%;
  }
}

@media (max-width: 700px) {
  .change-modal {
    width: 70%;
  }
}

@media (max-width: 550px) {
  .change-modal {
    width: 80%;
  }
}

@media (max-width: 400px) {
  .change-modal {
    width: 90%;
    padding: 2em;
  }
}
.change-modal > div,
h1 {
  width: 100%;
}

.change-modal > div:last-child {
  display: flex;
  flex-direction: column;
  align-items: center;
}

button {
  width: 50%;
  padding: 0.7em;
  border-radius: 0.3em;
  color: white;
  font-weight: 600;
  font-size: 1.1em;
  text-align: center;
}

a {
  display: block;
}

#image {
  display: none;
}

.change-modal__image {
  display: flex;
  justify-content: center;
}

.change-modal__image > div {
  width: 130px;
  height: 130px;
  position: relative;
}

.change-modal__image label {
  position: absolute;
  bottom: 0;
  right: 0;
  font-size: 2.5em;
}

.change-modal > div:nth-child(4) {
  display: flex;
  justify-content: center;
  gap: 2em;
}

.change-modal > div:nth-child(4) > div {
  width: 50%;
}

input,
select {
  border: 1px solid #dcddde;
  border-radius: 0.2rem;
  background-color: white;
  height: 2.5em;
  font-weight: 600;
  max-width: 300px;
  width: 100%;
  font-size: 1.2em;
}

label[for="image"] {
  display: block;
  font-weight: 300;
  background-color: white;
  border-radius: 50%;
  height: 40px;
  line-height: 0px;
}

label[for="nickname"],
label[for="region"],
label[for="age"] {
  display: block;
  font-weight: 300;
  font-size: 1em;
}
</style>
