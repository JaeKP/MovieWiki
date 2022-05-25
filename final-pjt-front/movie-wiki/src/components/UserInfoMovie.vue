<template>
  <div class="profile-detail__movie">
    <user-info-movie-card
      v-for="item in movieList"
      :key="item.pk"
      :movie="item"
    ></user-info-movie-card>
    <empty-component
      v-if="isEmpty"
      data="좋아요를 누른 영화가"
      class="profile-detail__movie__empty"
    ></empty-component>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import UserInfoMovieCard from "@/components/UserInfoMovieCard.vue";
import EmptyComponent from "./EmptyComponent.vue";
export default {
  name: "UserInfoMovie",
  components: { UserInfoMovieCard, EmptyComponent },
  computed: {
    ...mapGetters(["userInfoDetail"]),
    movieList() {
      return this?.userInfoDetail?.like_movies;
    },
    isEmpty() {
      if (this?.movieList?.length === 0) {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>

<style scoped>
.profile-detail__movie {
  display: flex;
  flex-wrap: wrap;
  width: 80%;
  margin-bottom: 4em;
}

.profile-detail__movie > * {
  margin: 1.5em;
}
.profile-detail__movie__empty {
  margin: auto;
}
</style>
