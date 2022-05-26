<template>
  <div class="movie-detail__overview">
    <movie-detail-card
      v-if="movieDetail !== undefined"
      :image="movieDetail.poster_path"
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
        <p v-if="!isLike" @click="likeMovies">
          <font-awesome-icon
            icon="fa-solid fa-heart"
            id="movie-detail__overview__content__overview__icon__heart__unlike"
          />
          <span class="movie-detail__overview__content__overview__icon__span"
            >찜하기</span
          >
        </p>
        <p v-else @click="likeMovies">
          <font-awesome-icon
            icon="fa-solid fa-heart"
            id="movie-detail__overview__content__overview__icon__heart__like"
          />
          <span class="movie-detail__overview__content__overview__icon__span"
            >찜하기 취소</span
          >
        </p>
        <button
          id="create-kakao-link-btn"
          @click="kakaoLink"
          class="font-white"
        >
          <font-awesome-icon
            icon="fa-solid fa-arrow-up-from-bracket"
            id="movie-detail__overview__content__overview__icon__share"
          />
          <span
            class="movie-detail__overview__content__overview__icon__share__span"
            >공유하기</span
          >
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import MovieDetailCard from "@/components/MovieDetailCard.vue";
import { mapGetters, mapActions } from "vuex";
import Swal from "sweetalert2";
export default {
  name: "MovieDetailOverView",
  components: {
    MovieDetailCard,
  },
  computed: {
    ...mapGetters([
      "userProfile",
      "movieDetail",
      "movieReviewPopularity",
      "isLoggedIn",
    ]),
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
    kakaoLink() {
      window.Kakao.Link.createDefaultButton({
        container: "#create-kakao-link-btn",
        objectType: "feed",
        content: {
          title: this.movieDetail.title,
          description: this.movieDetail.overview,
          imageUrl: `https://image.tmdb.org/t/p/original${this.movieDetail.poster_path}`,
          link: {
            mobileWebUrl: `http://localhost:8080/movies/${this.movieDetail.id}`,
            webUrl: `http://localhost:8080/movies/${this.movieDetail.id}`,
          },
        },
        social: {
          likeCount: this.movieDetail.like_count,
          commentCount: this.movieReviewPopularity.length,
        },
        buttons: [
          {
            title: "웹으로 보기",
            link: {
              mobileWebUrl: `http://localhost:8080/movies/${this.movieDetail.id}`,
              webUrl: `http://localhost:8080/movies/${this.movieDetail.id}`,
            },
          },
          // {
          //   title: "앱으로 보기",
          //   link: {
          //     mobileWebUrl: `http://localhost:8080/movies/${this.movieDetail.id}`,
          //     webUrl: `http://localhost:8080/movies/${this.movieDetail.id}`,
          //   },
          // },
        ],
      });
    },
    likeMovies() {
      if (this.isLoggedIn) {
        this.likeMovie(this.movieDetail.id);
      } else {
        Swal.fire({
          text: "로그인한 유저만 접근이 가능합니다.",
          icon: "info",
          width: "400px",
          toast: true,
          position: "top-end",
          showConfirmButton: false,
          timer: 2000,
          timerProgressBar: true,
        });
      }
    },
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

.movie-detail__overview__content {
  display: flex;
  flex-direction: column;
  gap: 1em;
  width: 70%;
}

@media (max-width: 1385px) {
  .movie-detail__overview__content {
    width: 60%;
  }
}

@media (max-width: 1030px) {
  .movie-detail__overview__content {
    width: 50%;
  }
}

@media (max-width: 834px) {
  .movie-detail__overview__content {
    width: 100% !important;
  }
}

.movie-detail__overview__content__tag {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5em;
}

.movie-detail__overview__content__tag > div {
  padding: 0.3em 0.5em;
  border-radius: 0.3em;
  color: #40444b;
  font-weight: 600;
  font-size: 1em;
}

.movie-detail__overview__content__title {
  font-size: 2.5em;
  font-weight: 500;
}

.movie-detail__overview__content__tagline {
  font-size: 1.6em;
  font-weight: 400;
}

.movie-detail__overview__content__overview {
  font-size: 1.2em;
  font-weight: 400;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  line-height: 1.8;
  overflow: hidden;
}

.movie-detail__overview__content__runtime {
  font-size: 1.2em;
  font-weight: 500;
}

.movie-detail__overview__content__overview__icon {
  font-size: 2.5em;
  display: flex;
  flex-wrap: wrap;
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

#create-kakao-link-btn {
  display: flex;
  align-items: center;
  gap: 0.6em;
}
#movie-detail__overview__content__overview__icon__share {
  font-size: 3em;
}

.movie-detail__overview__content__overview__icon__share__span {
  font-size: 2em;
  font-weight: 500;
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
