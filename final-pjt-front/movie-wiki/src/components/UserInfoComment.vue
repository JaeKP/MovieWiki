<template>
  <div class="profile-detail__comment">
    <div
      v-for="item in commentList"
      :key="item.pk"
      class="profile-detail__comment__item"
      data-aos="zoom-in"
    >
      <p class="profile-detail__comment__item__content">
        {{ item.content }}
      </p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "commentItem",
  computed: {
    ...mapGetters(["userInfoDetail"]),
    commentList() {
      return this?.userInfoDetail?.comment;
    },
  },
};
</script>

<style>
.profile-detail__comment {
  display: flex;
  flex-direction: column;
  width: 80%;
  gap: 2em;
  align-items: center;
  justify-content: center;
  margin-bottom: 4em;
}

.profile-detail__comment__item {
  background-color: #eeeeee;
  width: 60%;
  min-width: 300px;
  border-radius: 0.5em;
  padding: 2em;
  min-height: 100px;
  font-size: 1em;
  font-weight: 400;
}
</style>
