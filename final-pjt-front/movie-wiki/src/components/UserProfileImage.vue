<template>
  <div>
    <div class="user-profile-image"></div>
  </div>
</template>

<script>
export default {
  name: "UserProfileImage",
};
</script>

<style scoped>
.user-profile-image {
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
</style>
