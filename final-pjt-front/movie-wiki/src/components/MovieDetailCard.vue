<template>
  <div
    :style="{ backgroundImage: `url(${imageUrl})`, width, height }"
    class="movie-detail-card"
  ></div>
</template>

<script>
export default {
  name: "MovieDetailCard",
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
  computed: {
    imageUrl() {
      const url = `https://image.tmdb.org/t/p/original${this.image}`;
      return url;
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
