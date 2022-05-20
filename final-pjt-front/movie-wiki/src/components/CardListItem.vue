<template>
  <div class="carousel-item active">
    <div class="col-md-2">
      <div class="card">
        <div class="card-img">
          <img :src="imgURL" class="img-fluid" />
        </div>
        <div class="card-img-overlay"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardListItem",
  props: {
    movie: {
      type: Object,
    },
  },
  computed: {
    imgURL: function () {
      const videoId = this.movie.poster_path;
      return `https://www.themoviedb.org/t/p/w600_and_h900_bestv2${videoId}`;
    },
  },
};
</script>

<style>
/* @media (max-width: 767px) {
  .carousel-item > div {
    display: none;
  }
  .carousel-item > div:first-child {
    display: block;
  }
}
.carousel-item.active,
.carousel-item-next,
.carousel-item-prev {
  display: flex;
}
@media (min-width: 768px) {
  .carousel-item-end.active,
  .carousel-item-next {
    transform: translateX(25%);
  }
  .carousel-item-start.active,
  .carousel-item-prev {
    transform: translateX(-25%);
  }
}
.carousel-item-end,
.carousel-item-start {
  transform: translateX(0);
} */
</style>
