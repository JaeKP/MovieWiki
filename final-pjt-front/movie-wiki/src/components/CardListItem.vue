<template>
  <div class="card">
    <!-- <router-link
      :to="{
        name: 'MovieDetail',
        params: {
          id: movie.id,
        },
      }"
    > -->
    <div class="text">
      <div class="title font-basic h2">{{ movie.title }}</div>
      <hr />
      <div class="content font-basic">{{ movie.overview }}</div>
    </div>
    <img
      v-if="movie.poster_path"
      class="card__image"
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
    />

    <div v-else class="card__no__image mulish">No Poster</div>

    <!-- </router-link> -->
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
};
</script>

<style>
/* radius 여러 개 둬서 모서리 그림자가 라운딩 */
.card {
  width: 15rem;
  border-radius: 5%;
  background-color: black;
  box-shadow: 0px 2px 1px 1px rgba(0, 0, 0, 0.05);
  border: 0;
  /* Swiper의 자체 overflow:hidden 때문에 하단 그림자가 사라짐.. 야매로 해결 */
  margin-bottom: 0.1rem;
}
.card:hover {
  /* transform: scale(1.2); */
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
.card__no__image {
  border-radius: 8px;
  width: 100%;
  height: 18rem;
  background-color: var(--board-header);
  color: var(--header-search);
  text-align: center;
  padding-top: 8rem;
  font-size: 24px;
  font-weight: 700;
}
.text {
  display: none;
  color: white;
  z-index: 1;
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
