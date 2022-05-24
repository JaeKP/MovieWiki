<template>
  <div class="movie-detail__review" ref="top">
    <!-- 로그인을 안 했고 리뷰가 작성 되어 있는 경우 회원가입 유도-->
    <div class="sign-up__recommend" v-if="!isLoggedIn && !isEmpty">
      <p>로그인하고 한줄 평 보기 🎉</p>
      <div class="sign-up-container__recommend__btn">
        <button class="bg-medium-gray font-white" @click="showLogInModal">
          로그인
        </button>
        <button class="bg-icon-blue font-white" @click="showSignUpModal">
          회원 가입
        </button>
      </div>
    </div>
    <!-- 로그인을 한 경우 form을 보여준다.-->
    <movie-detail-review-form
      :movieDetail="movieDetail"
      v-if="isLoggedIn"
      :filterType="filterType"
    ></movie-detail-review-form>
    <!-- 필터 -->
    <div class="movie-detail__review__filter" :class="isBlur">
      <div>
        <a @click="changefilterTypePopular" :class="fontColor1">인기 순</a>
        <a @click="changefilterTypeLatest" :class="fontColor2">최신 순</a>
      </div>
      <hr />
    </div>
    <!-- 리뷰 -->
    <movie-detail-review-item
      v-for="item in pagenatedData"
      :key="item.id"
      :reviewData="item"
      :class="isBlur"
      @delete-review="deleteReview"
      :filterType="filterType"
    >
    </movie-detail-review-item>

    <!-- 페이지네이션! -->
    <div class="movie-detail__review__pagenation" :class="isBlur">
      <button :disabled="pageNum === 0" @click="prevPage" class="font-white">
        <font-awesome-icon icon="fa-solid fa-angles-left" />
      </button>
      <span class="movie-detail__review__pagenation__count font-icon-gray"
        >{{ pageNum + 1 }} / {{ pageCount }} 페이지</span
      >
      <button
        :disabled="pageNum >= pageCount - 1"
        @click="nextPage"
        class="font-white"
      >
        <font-awesome-icon icon="fa-solid fa-angles-right" />
      </button>
    </div>
    <!-- 리뷰가 비어있는 경우 -->
    <div
      v-if="isEmpty"
      class="bg-navbar-black font-white movie-detail__review__empty"
    >
      <p>아직 등록된 리뷰가 없습니다 😢</p>
      <p>리뷰를 남겨주세요!</p>
    </div>
  </div>
</template>

<script>
import MovieDetailReviewForm from "@/components/MovieDetailReviewForm.vue";
import MovieDetailReviewItem from "@/components/MovieDetailReviewItem.vue";
import Swal from "sweetalert2";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "MovieDetailReview",
  components: {
    MovieDetailReviewForm,
    MovieDetailReviewItem,
  },
  data() {
    return {
      filterType: 1,
      pageSize: 5,
      pageNum: 0,
    };
  },
  computed: {
    ...mapGetters([
      "isLoggedIn",
      "movieDetail",
      "movieReviewPopularity",
      "movieReviewLatest",
    ]),
    movieList() {
      if (this.filterType !== 1) {
        return this?.movieReviewLatest;
      } else {
        return this?.movieReviewPopularity;
      }
    },
    isBlur() {
      if (this?.isLoggedIn !== true) {
        return "blurEffect";
      } else {
        return "";
      }
    },
    isEmpty() {
      if (this.movieReviewPopularity.length === 0) {
        return true;
      } else {
        return false;
      }
    },
    fontColor1() {
      if (this.filterType !== 1) {
        return "font-gray";
      } else {
        return "font-white";
      }
    },
    fontColor2() {
      if (this.filterType !== 2) {
        return "font-gray";
      } else {
        return "font-white";
      }
    },
    pageCount() {
      let listing = this.movieList.length;
      let listSize = this.pageSize;
      let page = Math.floor(listing / listSize);
      if (listing % listSize > 0) {
        page = page + 1;
      }
      return page;
    },
    pagenatedData() {
      const start = this.pageNum * this.pageSize;
      const end = start + this.pageSize;
      return this.movieList.slice(start, end);
    },
  },
  methods: {
    ...mapActions(["deleteMovieReview"]),
    showSignUpModal() {
      this.$emit("show-sign-up-modal", true);
    },
    showLogInModal() {
      this.$emit("show-log-in-modal", true);
    },
    deleteReview(data) {
      Swal.fire({
        title: "정말 삭제하시겠습니까",
        icon: "error",
        width: "400px",
        showCancelButton: true,
        focusCancel: true,
        confirmButtonText: "삭제",
        cancelButtonText: "취소",
        confirmButtonColor: "#ED4245",
        cancelButtonColor: "#5865F2",
        position: "center",
        heightAuto: false,
      }).then((response) => {
        if (response.isConfirmed === true) {
          this.deleteMovieReview(data);
        }
      });
    },
    changefilterTypePopular() {
      this.filterType = 1;
      this.pageNum = 0;
    },
    changefilterTypeLatest() {
      this.filterType = 2;
      this.pageNum = 0;
    },
    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
    },
  },
};
</script>

<style scoped>
.movie-detail__review {
  display: flex;
  position: relative;
  flex-direction: column;
  width: 70%;
  max-width: 1500px;
  margin-bottom: 10em;
  align-items: center;
  gap: 5em;
  justify-content: center;
  min-height: 300px;
}

.blurEffect {
  filter: blur(10px);
  -webkit-filter: blur(8px);
  z-index: 1;
}
.sign-up__recommend {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.1);
  background-color: white;
  width: 400px;
  height: 220px;
  border-radius: 0.3em;
  margin-top: 4em;
  z-index: 2;
  border-radius: 0.3em;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  top: 0px;
}

.sign-up__recommend > p {
  margin-bottom: 1.8em;
  font-size: 1.5em;
  font-weight: 700;
}

.sign-up__recommend button {
  width: 100px;
  height: 40px;
  border-radius: 0.3em;
  margin: 0.2em 0.5em;
  font-weight: 600;
  font-size: 1em;
}

.movie-detail__review__empty {
  margin-top: 10em;
  width: 100%;
  height: 200px;
  display: flex;
  flex-direction: column;
  gap: 0.4em;
  padding: 1.5em;
  border-radius: 0.4em;
  justify-content: center;
  font-size: 1.2em;
  align-items: center;
}

hr {
  width: 250px;
  display: inline-block;
}

.movie-detail__review__filter a {
  margin-right: 2em;
  margin-left: 0.5em;
  font-size: 1.2em;
  padding: 0 0.5em;
  font-weight: 500;
}

.movie-detail__review__filter {
  width: 100%;
}

.movie-detail__review__pagenation {
  display: flex;
  gap: 2em;
  align-items: center;
}

.movie-detail__review__pagenation button {
  padding: 0.5em;
  font-size: 2em;
}

.movie-detail__review__pagenation__count {
  font-size: 1.2em;
}
</style>
