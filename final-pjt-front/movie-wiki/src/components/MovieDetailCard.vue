<template>
  <div
    :style="{ backgroundImage: `url(${imageUrl})`, width, height }"
    class="movie-detail-card"
  ></div>
</template>

<script>
export default {
  name: "MovieDetailCard",
  computed: {
    imageUrl() {
      return `https://image.tmdb.org/t/p/w500${this.image}`;
    },
  },
  props: {
    image: {
      type: String,
    },
    width: {
      type: String,
    },
    height: {
      type: String,
    },
  },
};
</script>

<style>
.movie-detail-card {
  border-radius: 15px;
  background-color: #2f3136;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
</style>
