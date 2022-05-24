<template>
  <div
    class="card"
    @click="moveMovieDetail"
    :style="{ backgroundImage: `url(${imageUrl})`, width, height }"
  >
    <div class="card-text">
      <div class="card-text__title font-basic h2">{{ movie.title }}</div>
      <hr class="card-text__hr" />
      <div class="card-text__content font-basic">{{ movie.overview }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserInfoMovieCard",
  props: {
    movie: {
      type: Object,
    },
    width: {
      type: String,
    },
    height: {
      type: String,
    },
  },
  methods: {
    moveMovieDetail() {
      this.$router.push({
        name: "movieDetail",
        params: { movieId: this.movie.id },
      });
    },
  },
  computed: {
    imageUrl() {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`;
    },
  },
};
</script>

<style scoped>
.card {
  width: 16rem;
  height: 24rem;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  border-radius: 1em;
  background-color: #2f3136;
  gap: 2em;
}

.card:hover {
  cursor: pointer;
}
.card:hover .card-text__hr,
.card:hover .card-text__title,
.card:hover .card-text__content {
  display: block;
  transition: 0.3s;
}

.card:hover .card-text__title {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card:hover .card-text__content {
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  line-height: 1.4;
  overflow: hidden;
  text-align: left;
  word-wrap: break-word;
}

.card:hover .card-text {
  background-color: rgba(0, 0, 0, 0.6);
  transition: 0.3s;
}

.card-text {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  border-radius: 1em;
}

.card-text__hr {
  display: none;
  width: 90%;
}
.card-text__title {
  display: none;
  color: white;
  padding: 1rem;
  font-weight: 500;
  font-size: 1.5rem;
}
.card-text__content {
  display: none;
  color: white;
  padding: 1rem;
  height: 8rem;
}
</style>
