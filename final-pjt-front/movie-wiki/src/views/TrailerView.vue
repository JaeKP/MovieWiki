<template>
  <div class="trailer-container">
    <div v-for="(movie, index) in trailerPath" :key="index">
      <div class="tailer-container__iframe">
        <div class="tailer-container__iframe__item">
          <iframe
            :src="trailerUrl(movie.trailer_youtube_key)"
            frameborder="0"
            width="480px"
            height="270px"
          ></iframe>
        </div>
        <div class="trailer-container__icon">
          <font-awesome-icon icon="fa-solid fa-share" />
          <font-awesome-icon icon="fa-solid fa-thumbs-up" />
        </div>
      </div>
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
}

.tailer-container__iframe__item {
  scroll-snap-align: start;
  display: block;
  width: 480px;
  height: 853px;
  border-radius: 1em;
  background-color: black;
  display: flex;
  align-items: center;
}

.tailer-container__iframe {
  display: flex;
  align-items: flex-end;
  justify-content: center;
}

.trailer-container__icon {
  display: flex;
  flex-direction: column;
  gap: 0.5em;
  margin-left: 1em;
  margin-bottom: 1em;
  font-size: 2.5em;
}
</style>
