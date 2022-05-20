<template>
  <div>
    <div class="sss">
      <vueper-slides
        class="no-shadow aaa"
        :visible-slides="7"
        :slide-ratio="1 / 5"
        :arrowsOutside="true"
        :bullets="true"
        :gap="1"
        :slide-multiple="3"
        :disableArrowsOnEdges="true"
        :slideImageInside="true"
      >
        <vueper-slide
          class="asa"
          v-for="(slide, i) in movieDatas"
          :key="i"
          :title="slide.title"
          :content="slide.overview"
          :image="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${slide.poster_path}`"
        />
        <div class="back"></div>
      </vueper-slides>
    </div>
    <div class="sss">
      <vueper-slides
        class="no-shadow aaa"
        :visible-slides="7"
        :slide-ratio="1 / 5"
        :arrowsOutside="true"
        :bullets="true"
        :gap="1"
        :slide-multiple="3"
        :disableArrowsOnEdges="true"
        :slideImageInside="true"
      >
        <vueper-slide
          class="asa"
          v-for="(slide, i) in movieDatas2"
          :key="i"
          :title="slide.title"
          :content="slide.overview"
          :image="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${slide.poster_path}`"
        />
        <div class="back"></div>
      </vueper-slides>
    </div>
  </div>
</template>

<script>
// import CardListItem from "./CardListItem.vue";
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";

export default {
  components: { VueperSlides, VueperSlide },
  data() {
    return {
      movieDatas: [],
      movieDatas2: [],
    };
  },
  async created() {
    const response = await fetch("http://localhost:8000/api/v1/movie/list");
    this.movieDatas = await response.json();
    const response2 = await fetch(
      "http://localhost:8000/api/v1/movie/filter?query=2010&type=year"
    );
    this.movieDatas2 = await response2.json();
  },
};
</script>

<style>
.aaa {
  color: white;
}
.sss {
  padding: 2rem;
}
.vueperslide__image {
  border-radius: 10px;
}
.vueperslide__image:hover {
  /* display: none; */
  opacity: 0.5;
}
.vueperslide__title {
  display: none;
  font-size: 2rem;
  border-top: 0;
}
.vueperslide__content {
  margin-top: 2rem;
  display: none;
  /* display: -webkit-box; */
  overflow: hidden;
  line-height: 1.7;
  max-height: 7em; /* 인터넷 익스플로러 호환 */
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
}

.asa:hover .vueperslide__title {
  display: block;
}

.asa:hover .vueperslide__content {
  display: -webkit-box;
}
</style>
