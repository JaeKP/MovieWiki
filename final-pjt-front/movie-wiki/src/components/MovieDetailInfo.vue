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
            width="250px"
            height="375px"
            class="movie-detail__info__detail__person__item__image"
          ></movie-detail-card>
          <div>
            <p class="font-white">Director</p>
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
            width="250px"
            height="375px"
            class="movie-detail__info__detail__person__item__image"
          ></movie-detail-card>
          <div>
            <p class="font-white">{{ item.character_name }}</p>
            <p class="font-white">{{ item.actor_id.name }}</p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div>
        <p>트레일러</p>
        <movie-trailer></movie-trailer>
      </div>
      <div>비슷한 영화</div>
      <movie-detail-card></movie-detail-card>
    </div>
  </div>
</template>

<script>
import MovieDetailCard from "@/components/MovieDetailCard.vue";
import MovieTrailer from "@/components/MovieTrailer.vue";
import { mapGetters } from "vuex";
export default {
  name: "MovieDetailInfo",
  components: {
    MovieDetailCard,
    MovieTrailer,
  },
  computed: {
    ...mapGetters(["movieDetail"]),
    diretor() {
      return this?.movieDetail?.director;
    },
    characters() {
      return this?.movieDetail?.characters_id;
    },
  },
};
</script>

<style scoped>
.movie-detail__info__detail {
  display: flex;
  flex-direction: column;
  width: 80%;
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
}

p {
  font-size: 1.5em;
}

.movie-detail__info__detail__person > div p {
  text-align: center;
}

div > p:nth-child(2) {
  font-weight: 300;
}

.movie-detail__info__detail__person > p {
  font-size: 2em;
  margin-bottom: 0.5em;
}
</style>
