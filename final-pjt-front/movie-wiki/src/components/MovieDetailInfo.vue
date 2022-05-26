<template>
  <div class="movie-detail__info__detail">
    <div
      class="movie-detail__info__detail__person"
      v-if="movieDetail !== undefined"
    >
      <p class="font-basic movie-detail__info__title">감독 및 배우</p>
      <div>
        <div
          v-for="item in diretor"
          :key="item.name"
          class="movie-detail__info__detail__person__item"
        >
          <movie-detail-card
            :image="item.profile_path"
            width="150px"
            height="225px"
            class="movie-detail__info__detail__person__item__image"
          ></movie-detail-card>
          <div>
            <p class="font-basic">감독</p>
            <p class="font-basic">{{ item.name }}</p>
          </div>
        </div>
        <div
          v-for="(item, index) in characters"
          :key="index"
          class="movie-detail__info__detail__person__item"
        >
          <movie-detail-card
            :image="item.actor_id.profile_path"
            width="150px"
            height="225px"
            class="movie-detail__info__detail__person__item__image"
          ></movie-detail-card>
          <div>
            <p class="font-basic">{{ item.character_name }}</p>
            <p class="font-basic">{{ item.actor_id.name }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="movie-detail__info__detail__trailer">
      <p class="font-basic movie-detail__info__title">트레일러</p>
      <iframe
        :src="trailerUrl"
        frameborder="0"
        width="100%"
        height="400px"
      ></iframe>
    </div>
    <div class="movie-detail__info__detail__similar">
      <p class="font-basic movie-detail__info__title">비슷한 영화</p>
      <div>
        <user-info-movie-card
          v-for="movie in movieSimilar"
          :key="movie.id"
          :movie="movie"
        ></user-info-movie-card>
      </div>
    </div>
  </div>
</template>

<script>
import MovieDetailCard from "@/components/MovieDetailCard.vue";
import UserInfoMovieCard from "@/components/UserInfoMovieCard.vue";

import { mapGetters } from "vuex";
export default {
  name: "MovieDetailInfo",
  components: {
    MovieDetailCard,
    UserInfoMovieCard,
  },
  computed: {
    ...mapGetters(["movieDetail", "similarMovie"]),
    diretor() {
      return this?.movieDetail?.director;
    },
    characters() {
      return this?.movieDetail?.characters_id;
    },
    trailerId() {
      return this?.movieDetail?.trailer_youtube_key;
    },
    trailerUrl() {
      const videoId = `https://www.youtube.com/embed/${this.trailerId}`;
      return videoId;
    },
    movieSimilar() {
      return this?.similarMovie;
    },
  },
  // methods: {
  //   ...mapActions(["fetchMovieSimilar"]),
  // },
  // beforeUpdated() {
  //   const arr = this.movieDetail.movie_similar.slice(0, 5);
  //   this.fetchMovieSimilar(arr);
  // },
};
</script>

<style scoped>
.movie-detail__info__detail {
  display: flex;
  flex-direction: column;
  width: 80%;
  gap: 5em;
  margin-bottom: 10em;
}

.movie-detail__info__detail__person > div {
  display: flex;
  width: 100%;
  flex-wrap: wrap;
  margin-left: -1.5em;
}

.movie-detail__info__detail__person__item {
  display: flex;
  flex-direction: column;
  gap: 1.5em;
  align-items: center;
  padding: 1.5em;
  width: 16%;
  min-width: 180px;
  max-width: 250px;
}

p {
  font-size: 1.2em;
}

.movie-detail__info__detail__person > div p {
  text-align: center;
  font-weight: 200;
}

.movie-detail__info__title {
  font-size: 1.7em;
  margin-bottom: 0.5em;
  font-weight: 700;
}

.movie-detail__info__detail__trailer {
  width: 50%;
}

iframe {
  min-width: 400px;
  border-radius: 0.5em;
  margin-top: 2em;
  max-width: 800px;
}

.movie-detail__info__detail__similar > div {
  display: flex;
  gap: 3em;
  flex-wrap: wrap;
  margin-top: 3em;
}

p {
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  line-height: 1.8;
  overflow: hidden;
}
</style>
