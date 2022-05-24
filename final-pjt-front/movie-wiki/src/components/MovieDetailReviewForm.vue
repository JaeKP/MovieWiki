<template>
  <form @submit.prevent="onSubmit" class="movie-detail__review__form">
    <textarea
      placeholder="광고 및 욕설, 비속어나 타인을 비방하는 문구를 사용하면 비공개 될 수 있습니다."
      v-model="inputData.content"
    ></textarea>
    <div>
      <input type="checkbox" id="spoiler" v-model="inputData.spoiler" />
      <label for="spoiler" class="font-white"> 스포일러가 있습니다.</label>
      <button class="comment-submit">댓글 남기기</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from "vuex";
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
    onSubmit() {
      console.log(this.filterType);
      this.createMovieReview(this.inputData);
      this.inputData.content = "";
      this.inputData.spoiler = false;
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
