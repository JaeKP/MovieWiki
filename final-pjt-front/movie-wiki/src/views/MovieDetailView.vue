<template>
  <div>
    <div
      class="movie-detail"
      :style="{
        backgroundImage: imagBg,
      }"
    >
      <movie-detail-over-view></movie-detail-over-view>
      <div class="movie-detail__info">
        <a @click="changeComponent('MovieDetailInfo')" :class="infoColor"
          >주요 정보</a
        >
        <a @click="changeComponent('MovieDetailReview')" :class="reviewColor"
          >한줄 평</a
        >
        <hr />
      </div>
      <component
        v-bind:is="currentTabComponent"
        @show-sign-up-modal="showSignUpModal"
        @show-log-in-modal="showLogInModal"
      ></component>
    </div>
  </div>
</template>

<script>
import MovieDetailOverView from "@/components/MovieDetailOverView.vue";
import MovieDetailInfo from "@/components/MovieDetailInfo.vue";
import MovieDetailReview from "@/components/MovieDetailReview.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "MovieDetailView",
  components: {
    MovieDetailOverView,
    MovieDetailInfo,
    MovieDetailReview,
  },
  data() {
    return {
      currentTabComponent: "MovieDetailInfo",
    };
  },
  computed: {
    ...mapGetters(["movieDetail"]),
    infoColor() {
      if (this.currentTabComponent !== "MovieDetailInfo") {
        return "font-gray";
      } else {
        return "font-white";
      }
    },
    reviewColor() {
      if (this.currentTabComponent !== "MovieDetailReview") {
        return "font-gray";
      } else {
        return "font-white";
      }
    },
    imagBg() {
      const url = `https://image.tmdb.org/t/p/original${this.movieDetail.poster_path}`;
      return `linear-gradient( rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85) ), url(${url})`;
    },
    params() {
      return this.$route.params.movieId;
    },
  },
  methods: {
    ...mapActions([
      "fetchMovieDetail",
      "fetchMovieReview",
      "fetchMovieSimilar",
    ]),
    changeComponent(page) {
      this.currentTabComponent = page;
    },
    showSignUpModal() {
      this.$emit("show-sign-up-modal", true);
    },
    showLogInModal() {
      this.$emit("show-log-in-modal", true);
    },
  },
  watch: {
    params() {
      this.fetchMovieDetail(this.params);
      const reviewPopularity = { movieId: this.params, type: 1 };
      this.fetchMovieReview(reviewPopularity);
      const reviewLatest = { movieId: this.params, type: 2 };
      this.fetchMovieReview(reviewLatest);
    },
  },
  created() {
    this.fetchMovieDetail(this.$route.params.movieId);
    const reviewPopularity = { movieId: this.$route.params.movieId, type: 1 };
    this.fetchMovieReview(reviewPopularity);
    const reviewLatest = { movieId: this.$route.params.movieId, type: 2 };
    this.fetchMovieReview(reviewLatest);
  },
  beforeUpdate() {
    console.log(this.movieDetail);
  },
};
</script>
<style scoped>
.movie-detail {
  width: 100vw;
  min-height: calc(100vh - 80px);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 80px;
  gap: 5em;
  background-repeat: repeat-y;
  background-position: center top;
  background-size: 100%;
}

.movie-detail__info {
  width: 80%;
}

.movie-detail__info > a {
  font-size: 1.8em;
  margin-right: 1em;
  font-weight: 500;
}
</style>
