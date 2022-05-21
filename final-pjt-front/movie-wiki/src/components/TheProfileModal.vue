<template>
  <div @mouseleave="hideProfileModal">
    <div class="profile-modal">
      <div class="pofile-modal__user">
        <div class="nav__profile__item"></div>
        <p>{{ userProfile.nickname }}</p>
      </div>
      <div class="profile-modal__router">
        <a @click="hideProfileModal">내 정보</a>
        <hr />
        <a @click="[hideProfileModal(), logOut()]">로그아웃</a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheProfileModal",
  computed: {
    ...mapGetters(["userProfile"]),
  },
  methods: {
    ...mapActions(["logOut"]),
    hideProfileModal() {
      this.$emit("hide-profile-modal", false);
    },
  },
};
</script>

<style scoped>
.profile-modal {
  background-color: white;
  z-index: 2;
  width: 200px;
  border-radius: 0.3em;
  padding: 1em;
  display: flex;
  flex-direction: column;
  gap: 2em;
}

.pofile-modal__user {
  display: flex;
  align-items: center;
  color: #202225;
}

.pofile-modal__user > div {
  background-image: url(@/assets/profile.png);
  width: 60px;
  height: 60px;
  margin-right: 0.5em;
  border: 1px solid #96989d;
  border-radius: 50%;
  background-color: white;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
}

.profile-modal__router {
  color: #36393f;
}

hr {
  border-top: 0.5px solid #96989d;
  border-bottom: 0 solid white;
}
</style>
