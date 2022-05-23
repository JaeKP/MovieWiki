<template>
  <div class="movie-detail__overview">
    <movie-detail-card
      v-if="imageUrl !== undefined"
      :image="imageUrl"
      width="300px"
      height="450px"
      class="movie-detail__overview__content__poster"
    ></movie-detail-card>
    <div class="movie-detail__overview__content">
      <div class="movie-detail__overview__content__tag">
        <div class="bg-icon-green">
          {{ releasedDate }}
        </div>
        <div v-for="(genre, index) in genres" :key="index" class="bg-icon-gray">
          {{ genre.name }}
        </div>
      </div>
      <p class="font-basic movie-detail__overview__content__title">
        {{ movieDetail.title }}
      </p>
      <p class="font-gray movie-detail__overview__content__tagline">
        {{ movieDetail.tagline }}
      </p>
      <p class="font-gray movie-detail__overview__content__overview">
        {{ movieDetail.overview }}
      </p>
      <p class="font-basic movie-detail__overview__content__runtime">
        상영시간: {{ movieDetail.runtime }}분
      </p>
      <div class="movie-detail__overview__content__overview__icon">
        <p>
          <font-awesome-icon
            icon="fa-solid fa-star"
            id="movie-detail__overview__content__overview__icon__star"
          />
          {{ movieDetail.vote_avg }}
        </p>
        <p v-if="isLike" @click="likeMovie(movieDetail.id)">
          <font-awesome-icon
            icon="fa-solid fa-heart"
            id="movie-detail__overview__content__overview__icon__heart__unlike"
          />
          <span class="movie-detail__overview__content__overview__icon__span"
            >찜하기</span
          >
        </p>
        <p v-else @click="likeMovie(movieDetail.id)">
          <font-awesome-icon
            icon="fa-solid fa-heart"
            id="movie-detail__overview__content__overview__icon__heart__like"
          />
          <span class="movie-detail__overview__content__overview__icon__span"
            >찜하기 취소</span
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import MovieDetailCard from "@/components/MovieDetailCard.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "MovieDetailOverView",
  components: {
    MovieDetailCard,
  },
  computed: {
    ...mapGetters(["movieDetail", "userProfile"]),
    imageUrl() {
      return this.movieDetail.poster_path;
    },
    // likeUsers() {
    //   if (this.movieDetail.like_users !== undefined) {
    //     return this.movieDetail.like_users;
    //   } else {
    //     return [];
    //   }
    // },
    isLike() {
      if (this?.movieDetail?.like_users?.includes(this.userProfile.id)) {
        return true;
      } else {
        return false;
      }
    },
    releasedDate() {
      return this?.movieDetail?.released_date?.slice(0, 4);
    },
    genres() {
      return this?.movieDetail?.genre_ids;
    },
  },
  methods: {
    ...mapActions(["likeMovie"]),
  },
};
</script>

<style scoped>
.movie-detail__overview {
  width: 80%;
  display: flex;
  gap: 2em;
  align-items: center;
  flex-wrap: wrap;
}

.movie-detail__overview__content__poster {
  width: 20%;
}
.movie-detail__overview__content {
  display: flex;
  flex-direction: column;
  gap: 1em;
  width: 80%;
}

.movie-detail__overview__content__tag {
  display: flex;
  gap: 0.5em;
}

.movie-detail__overview__content__tag > div {
  padding: 0.3em 0.5em;
  border-radius: 0.3em;
  color: #40444b;
  font-weight: 600;
  font-size: 1.5em;
}

.movie-detail__overview__content__title {
  font-size: 3em;
  font-weight: 500;
}

.movie-detail__overview__content__tagline {
  font-size: 2em;
  font-weight: 400;
}

.movie-detail__overview__content__overview {
  font-size: 1.5em;
  font-weight: 400;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  line-height: 1.8;
  overflow: hidden;
}

.movie-detail__overview__content__runtime {
  font-size: 1.5em;
  font-weight: 500;
}

.movie-detail__overview__content__overview__icon {
  font-size: 3em;
  display: flex;
  gap: 2em;
  color: white;
  font-weight: 500;
}

#movie-detail__overview__content__overview__icon__star {
  font-size: 1.2em;
  color: #faa81a;
}
#movie-detail__overview__content__overview__icon__heart__like {
  font-size: 1.2em;
  color: #ed4245;
}

#movie-detail__overview__content__overview__icon__heart__like:hover {
  color: #96989d;
}

#movie-detail__overview__content__overview__icon__heart__unlike {
  font-size: 1.2em;
  color: #96989d;
}

#movie-detail__overview__content__overview__icon__heart__unlike:hover {
  color: #ed4245;
}

.movie-detail__overview__content__overview__icon > p:nth-child(2) {
  display: flex;
  align-items: center;
  gap: 0.2em;
  cursor: pointer;
}

.movie-detail__overview__content__overview__icon__span {
  font-size: 0.7em;
}
</style>
