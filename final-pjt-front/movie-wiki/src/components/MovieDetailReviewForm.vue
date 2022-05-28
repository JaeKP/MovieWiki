<template>
  <form @submit.prevent="onSubmit" class="movie-detail__review__form">
    <textarea
      placeholder="광고 및 욕설, 비속어나 타인을 비방하는 문구를 사용하면 비공개 될 수 있습니다."
      v-model="inputData.content"
    ></textarea>
    <div>
      <input type="checkbox" id="spoiler" v-model="inputData.spoiler" />
      <label for="spoiler" class="font-white"> 스포일러가 있습니다.</label>
      <button class="comment-submit">작성 하기</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from "vuex";
import Swal from "sweetalert2";
export default {
  name: "MovieDetailReviewForm",
  data() {
    return {
      inputData: {
        content: "",
        spoiler: false,
        type: this.filterType,
        movieId: this.movieDetail.id,
      },
      badWords: ["바보", "멍청이", "시발", "죽음", "죽어", "병신"],
    };
  },
  props: {
    movieDetail: {
      type: Object,
    },
    filterType: {
      type: Number,
    },
  },
  methods: {
    ...mapActions(["createMovieReview"]),
    checkAvailability(arr, val) {
      return arr.some((arrVal) => val.includes(arrVal));
    },
    checkWord() {
      const reviewData = this?.inputData?.content;
      return this.checkAvailability(this.badWords, reviewData);
    },
    onSubmit() {
      if (!this.checkWord()) {
        this.createMovieReview(this.inputData);
        this.inputData.content = "";
        this.inputData.spoiler = false;
      } else {
        Swal.fire({
          text: "부적절한 단어가 포함되어 있습니다.",
          icon: "error",
          width: "400px",
          showConfirmButton: false,
          timer: 2000,
          timerProgressBar: true,
          position: "center",
          heightAuto: false,
        });
      }
      // this.createMovieReview(this.inputData);
      // this.inputData.content = "";
      // this.inputData.spoiler = false;
    },
  },
};
</script>

<style scoped>
.movie-detail__review__form {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: 2em;
  width: 100%;
}

.movie-detail__review__form > textarea {
  width: 100%;
  background-color: #40444b;
  color: #eeeeee;
  border: 0px;
  border-radius: 0.4em;
  height: 100px;
  padding: 1.5em;
}
textarea::placeholder {
  color: #eeeeee;
  font-size: 1.2em;
}

label {
  font-size: 1.2em;
  margin-right: 2em;
}

.movie-detail__review__form > div {
  width: (90% + 3em);
  display: flex;
  align-items: baseline;
}

input[type="checkbox"] {
  zoom: 2;
}
</style>
