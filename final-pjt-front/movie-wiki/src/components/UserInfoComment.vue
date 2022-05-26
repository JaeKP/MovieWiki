<template>
  <div class="profile-detail__comment">
    <div
      v-for="item in commentList"
      :key="item.pk"
      class="profile-detail__comment__item"
      data-aos="zoom-in"
    >
      <user-profile-image
        :image="userInfoDetail.profile_image"
        class="profile-detail__comment__item__image"
      ></user-profile-image>
      <div class="profile-detail__comment__item__content">
        <p>
          {{ item.content }}
        </p>
        <p>
          {{ userCreatedAt(item) }}
        </p>
      </div>
    </div>
    <empty-component v-if="isEmpty" data="아직 작성한 댓글이"></empty-component>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import EmptyComponent from "@/components/EmptyComponent.vue";
import UserProfileImage from "@/components/UserProfileImage.vue";
export default {
  name: "commentItem",
  components: { EmptyComponent, UserProfileImage },
  computed: {
    ...mapGetters(["userInfoDetail"]),
    commentList() {
      return this?.userInfoDetail?.comment;
    },
    isEmpty() {
      if (this?.commentList?.length === 0) {
        return true;
      } else {
        return false;
      }
    },
  },
  methods: {
    userCreatedAt(data) {
      const createdAt = data.created_at.slice(0, 10);
      return createdAt;
    },
  },
};
</script>

<style scoped>
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
  min-height: 200px;
  font-size: 1em;
  font-weight: 400;
  display: flex;
  gap: 2em;
}

.profile-detail__comment__item__content {
  display: flex;
  justify-content: space-between;
  flex-direction: column;
  gap: 2em;
}

.profile-detail__comment__item__content > p:nth-child(1) {
  font-size: 1.2em;
}

.profile-detail__comment__item__content > p:nth-child(2) {
  font-weight: 500;
}

p {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  line-height: 1.5;
  overflow: hidden;
}
</style>
