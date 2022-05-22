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
    imageUrl() {
      const url = `http://localhost:8000${this.image}`;
      return url;
    },
  },
};
</script>

<style scoped>
.user-profile-image {
  width: 60px;
  height: 60px;
  margin-right: 0.5em;
  border: 1px solid #96989d;
  border-radius: 50%;
  background-color: white;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 130%;
}
</style>
