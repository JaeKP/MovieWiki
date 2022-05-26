<template>
  <div class="trailer-container">
    <div v-for="(movie, index) in trailerPath" :key="index">
      <!-- <div class="tailer-container__iframe"> -->
      <div
        class="tailer-container__iframe__item"
        @click.self="moveMovieDetail(movie.id)"
      >
        <iframe
          :src="trailerUrl(movie.trailer_youtube_key)"
          frameborder="0"
          width="480px"
          height="270px"
        ></iframe>
      </div>
      <!-- <div class="trailer-container__icon">
          <font-awesome-icon
            class="font-white"
            icon="fa-solid fa-share"
            @click="moveMovieDetail(movie.id)"
            id="move-icon"
          /> -->
      <!-- <font-awesome-icon
            class="font-white"
            icon="fa-solid fa-message"
            id="review-icon"
            @click="showReviewModal"
          /> -->
      <!-- </div> -->
      <!-- </div> -->
      <infinite-loading
        class="trail-container__infinite"
        @infinite="infiniteHandler"
        spinner="circles"
      ></infinite-loading>
    </div>
  </div>
</template>

<script>
import drf from "@/api/drf";
import axios from "axios";
import InfiniteLoading from "vue-infinite-loading";
export default {
  name: "TrailerView",
  components: {
    InfiniteLoading,
  },
  data() {
    return {
      trailerPath: [],
      page: 0,
    };
  },
  methods: {
    getTrailer() {
      axios({
        url: drf.movie.trailer(),
        method: "get",
        params: { page: this.page },
      }).then(({ data }) => {
        this.page = this.page + 1;
        this.trailerPath.push(...data);
      });
    },
    trailerUrl(path) {
      const videoLink = `https://www.youtube.com/embed/${path}`;
      return videoLink;
    },
    infiniteHandler() {
      console.log("바닥!!!!");
      axios({
        url: drf.movie.trailer(),
        method: "get",
        params: { page: this.page },
      }).then(({ data }) => {
        this.page = this.page + 1;
        this.trailerPath.push(...data);
      });
    },
    moveMovieDetail(path) {
      this.$router.push({
        name: "movieDetail",
        params: { movieId: path },
      });
    },
    showReviewModal() {
      this.$emit("show-review-modal", true);
    },
  },
  created() {
    this?.getTrailer();
  },
};
</script>

<style scoped>
.trailer-container {
  overflow: auto;
  scroll-snap-type: y mandatory;
  display: flex;
  flex-direction: column;
  gap: 5em;
  height: 120vh;
  align-items: center;
  justify-content: flex-start;
  margin-top: 2em;
}

.tailer-container__iframe__item {
  scroll-snap-align: start;
  display: block;
  min-width: 350px;
  width: 60vw;
  height: 80vh;
  max-width: 480px;
  /* max-height: 853px; */
  border-radius: 1em;
  background-color: black;
  display: flex;
  align-items: center;
}

/* .tailer-container__iframe {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  margin-right: -4em;
} */

.trailer-container__icon {
  display: flex;
  flex-direction: column;
  gap: 0.7em;
  margin-left: 0.5em;
  margin-bottom: 1em;
  font-size: 2.2em;
}

.trailer-container__icon > * {
  cursor: pointer;
}

#thumbs-up-icon:hover {
  color: #ed4245;
}

#move-icon:hover {
  color: #ed4245;
}

#review-icon:hover {
  color: #ed4245;
}
</style>
