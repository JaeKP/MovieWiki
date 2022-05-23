<template>
  <div>
    <movie-detail-over-view></movie-detail-over-view>
  </div>
</template>

<script>
import MovieDetailOverView from "@/components/MovieDetailOverView.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "MovieDetailView",
  components: {
    ...mapGetters(["movieDetail"]),
    MovieDetailOverView,
  },
  methods: {
    ...mapActions(["fetchMovieDetail"]),
  },
  created() {
    this.fetchMovieDetail(this.$route.params.movieId);
  },
};
</script>
<style></style>
