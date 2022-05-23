<template>
  <div class="movie-detail__review">
    <div class="sign-up-container" v-if="!isLoggedIn">
      <div class="sign-up-container__recommend">
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
    </div>
    <movie-detail-review-form
      :movieId="movieId"
      v-if="isLoggedIn"
    ></movie-detail-review-form>
    <movie-detail-review-item
      v-for="(item, index) in popularityList"
      :key="index"
      :reviewData="item"
      :class="isBlur"
      @delete-review="deleteReview"
    >
    </movie-detail-review-item>
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
  props: {
    movieId: {
      type: Number,
    },
  },
  computed: {
    ...mapGetters(["isLoggedIn", "movieReviewPopularity"]),
    popularityList() {
      return this?.movieReviewPopularity;
    },
    isBlur() {
      if (this?.isLoggedIn !== true) {
        return "blurEffect";
      } else {
        return "";
      }
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
  },
};
</script>

<style>
.movie-detail__review {
  display: flex;
  position: relative;
  flex-direction: column;
  width: 80%;
  margin-bottom: 5em;
  align-items: center;
  gap: 5em;
  justify-content: center;
}

.blurEffect {
  filter: blur(10px);
  -webkit-filter: blur(8px);
  z-index: 1;
}
.sign-up-container {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 0.3em;
  z-index: 2;
  display: flex;
  justify-content: center;
}

.sign-up-container__recommend {
  width: 400px;
  height: 220px;
  background-color: white;
  position: relative;
  z-index: 2;
  margin-top: 20em;
  border-radius: 0.3em;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.sign-up-container__recommend > p {
  margin-bottom: 1.8em;
  font-size: 1.5em;
  font-weight: 700;
}

.sign-up-container__recommend button {
  width: 100px;
  height: 40px;
  border-radius: 0.3em;
  margin: 0.2em 0.5em;
  font-weight: 600;
  font-size: 1em;
}
</style>
