<template>
  <div class="profile-detail__review">
    <div
      v-for="item in reviewList"
      :key="item.pk"
      class="profile-detail__review__item"
    >
      <user-info-movie-card
        :movie="item.movie_id"
        width="10rem"
        height="15rem"
      ></user-info-movie-card>
      <div>
        <p class="font-basic">{{ item.content }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import UserInfoMovieCard from "@/components/UserInfoMovieCard.vue";

export default {
  name: "UserInfoReview",
  components: { UserInfoMovieCard },
  computed: {
    ...mapGetters(["userInfoDetail"]),
    reviewList() {
      return this?.userInfoDetail?.review;
    },
  },
};
</script>

<style>
.profile-detail__review {
  width: 80%;
  display: flex;
  flex-direction: column;
  gap: 3em;
  margin-bottom: 4em;
}

.profile-detail__review__item {
  display: flex;
  align-items: center;
}
</style>
