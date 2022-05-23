<template>
  <div class="movie-detail__info__detail">
    <div class="movie-detail__info__detail__person">
      <p class="font-white">감독 및 배우</p>
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
            <p class="font-white">감독</p>
            <p class="font-white">{{ item.name }}</p>
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
            <p class="font-white">{{ item.character_name }}</p>
            <p class="font-white">{{ item.actor_id.name }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="movie-detail__info__detail__content">
      <div class="movie-detail__info__detail__content__div">
        <div>
          <p class="font-white">트레일러</p>
          <iframe
            :src="trailerUrl"
            frameborder="0"
            width="100%"
            height="350px"
          ></iframe>
        </div>
        <div>
          <p class="font-white">비슷한 영화</p>
          <movie-detail-card></movie-detail-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieDetailCard from "@/components/MovieDetailCard.vue";
import { mapGetters } from "vuex";
// import drf from "@/api/drf";
// import axios from "axios";
export default {
  name: "MovieDetailInfo",
  components: {
    MovieDetailCard,
  },
  data() {
    return {
      similar: [],
    };
  },
  computed: {
    ...mapGetters(["movieDetail"]),
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
      const array = this?.movieDetail?.movie_similar;
      return array.slice(0, 3);
    },
  },
  // beforeUpdate() {
  //   const array = this?.movieSimilar;
  //   array.forEach((item) => {
  //     axios({
  //       url: drf.movie.movieDetail(item),
  //       method: "get",
  //     }).then((response) => {
  //       this.similar.push(response);
  //     });
  //   });
  // },
};
</script>

<style scoped>
.movie-detail__info__detail {
  display: flex;
  flex-direction: column;
  width: 80%;
  gap: 5em;
  margin-bottom: 5em;
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
}

div > p:nth-child(2) {
  font-weight: 300;
}

.movie-detail__info__detail__person > p {
  font-size: 1.7em;
  margin-bottom: 0.5em;
}

.movie-detail__info__detail__content {
  width: 100%;
}

.movie-detail__info__detail__content__div {
  display: flex;
  flex-wrap: wrap;
  gap: 5em;
}

.movie-detail__info__detail__content__div > div:nth-child(1) {
  width: 40%;
  min-width: 400px;
  max-width: 600px;
}

.movie-detail__info__detail__content__div > div:nth-child(2) {
  width: 50%;
}
iframe {
  min-width: 400px;
  border-radius: 0.5em;
}

p {
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  line-height: 1.8;
  overflow: hidden;
}
</style>
