<template>
  <div @mouseleave="hideProfileModal">
    <div class="profile-modal">
      <div class="pofile-modal__user">
        <user-profile-image :image="userProfile.image"></user-profile-image>
        <p>{{ userProfile.nickname }}</p>
      </div>
      <div class="profile-modal__router">
        <router-link
          :to="{ name: 'profile', params: { username: userProfile.username } }"
        >
          <a @click="hideProfileModal">내 정보</a>
        </router-link>
        <hr />
        <a @click="[hideProfileModal(), logOut()]">로그아웃</a>
      </div>
    </div>
  </div>
</template>

<script>
import UserProfileImage from "@/components/UserProfileImage.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheProfileModal",
  components: {
    UserProfileImage,
  },
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

a {
  color: #36393f;
}

hr {
  border-top: 0.5px solid #96989d;
  border-bottom: 0 solid white;
}
</style>
