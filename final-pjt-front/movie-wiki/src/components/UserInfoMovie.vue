<template>
  <div class="profile-detail__movie">
    <user-info-movie-card
      v-for="item in movieList"
      :key="item.pk"
      :movie="item"
    ></user-info-movie-card>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import UserInfoMovieCard from "@/components/UserInfoMovieCard.vue";
export default {
  name: "UserInfoMovie",
  components: { UserInfoMovieCard },
  computed: {
    ...mapGetters(["userInfoDetail"]),
    movieList() {
      return this?.userInfoDetail?.like_movies;
    },
  },
};
</script>

<style>
.profile-detail__movie {
  display: flex;
  flex-wrap: wrap;
  width: 80%;
  margin-bottom: 4em;
}

.profile-detail__movie > * {
  margin: 1.5em;
}
</style>
