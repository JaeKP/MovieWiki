<template>
  <div>
    <div>
      <div class="h1 font-basic recommend-title">{{ Tag }}</div>
      <swiper class="swiper" :options="swiperOption">
        <swiper-slide v-for="movie in movieDatas" :key="movie.id">
          <card-list-item :movie="movie"></card-list-item>
        </swiper-slide>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>
    </div>
  </div>
</template>

<script>
// import CardListItem from "./CardListItem.vue";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";
import CardListItem from "./CardListItem.vue";

export default {
  name: "CardList",
  components: {
    swiper,
    swiperSlide,
    CardListItem,
  },
  props: {
    URL: {
      type: String,
    },
    Tag: {
      type: String,
    },
  },
  data() {
    return {
      movieDatas: [],
      swiperOption: {
        slidesPerView: "auto",
        spaceBetween: 12,
        loopedSlides: "12",
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
    };
  },
  async created() {
    const response = await fetch(this.URL);
    this.movieDatas = await response.json();
  },
};
</script>

<style scoped>
.swiper-slide {
  width: 15rem;
  display: flex;
}
.swiper-button-prev,
.swiper-button-next {
  color: white;
  opacity: 1;
}
.recommend-title {
  margin-top: 5rem;
  margin-bottom: 0.3rem;
  font-size: 23px;
  font-weight: 400;
}
</style>
