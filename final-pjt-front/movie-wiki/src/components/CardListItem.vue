<template>
  <div class="card" @click="moveMovieDetail">
    <div class="text">
      <div class="title font-basic h2">{{ title }}</div>
      <hr />
      <div class="content font-basic">{{ overview }}</div>
    </div>
    <img
      v-if="posterPath"
      class="card__image"
      :src="`https://image.tmdb.org/t/p/w300${posterPath}`"
    />
  </div>
</template>

<script>
export default {
  name: "CardListItem",
  props: {
    movie: {
      type: Object,
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
    title() {
      return this?.movie?.title;
    },
    overview() {
      return this?.movie?.overview;
    },
    posterPath() {
      return this?.movie?.poster_path;
    },
  },
};
</script>

<style scoped>
/* radius 여러 개 둬서 모서리 그림자가 라운딩 */
.card {
  width: 15rem;
  border-radius: 5%;
  background-color: #2f3136;
  height: 23rem;
  /* box-shadow: 0px 2px 1px 1px rgba(0, 0, 0, 0.05); */
  border: 0;
  z-index: 4;
  /* Swiper의 자체 overflow:hidden 때문에 하단 그림자가 사라짐.. 야매로 해결 */
  /* margin-bottom: 0.1rem; */
}

.card:hover {
  cursor: pointer;
}

.card:hover > .card__image {
  transition: all 0.3s;
  opacity: 0.5;
}

.card__image {
  border-radius: 5%;
  width: 100%;
  height: 23rem;
  object-fit: cover;
}

.text {
  display: none;
  color: white;
  z-index: 7;
  padding: 1rem;
  font-weight: 400;
}

.text > .title {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card:hover .text {
  display: block;
  position: absolute;
}

.card:hover .content {
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  line-height: 1.8;
  overflow: hidden;
}
</style>
