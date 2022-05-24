<template>
  <div>
    <div
      class="user-profile-image"
      :style="{ backgroundImage: `url(${imageUrl})`, width, height }"
    ></div>
  </div>
</template>

<script>
export default {
  name: "UserProfileImage",
  props: {
    width: {
      type: String,
    },
    height: {
      type: String,
    },
    image: {
      type: String,
    },
  },
  computed: {
    // 유저 기본이미지 설정하기 (나중에)
    imageUrl() {
      if (this.image !== null) {
        const url = `http://localhost:8000${this.image}`;
        return url;
      } else {
        return "https://raw.githubusercontent.com/JaeKP/image_repo/main/img/slackProfile.png";
      }
    },
  },
};
</script>

<style scoped>
.user-profile-image {
  width: 60px;
  height: 60px;
  margin-right: 0.5em;
  border: 0px;
  border-radius: 50%;
  background-color: white;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 130%;
}
</style>
