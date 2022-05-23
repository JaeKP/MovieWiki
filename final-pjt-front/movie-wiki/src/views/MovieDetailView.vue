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
      <component v-bind:is="currentTabComponent"></component>
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
  },
  methods: {
    ...mapActions(["fetchMovieDetail"]),
    changeComponent(page) {
      this.currentTabComponent = page;
    },
  },
  created() {
    this.fetchMovieDetail(this.$route.params.movieId);
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
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
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
