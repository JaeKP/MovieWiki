<template>
  <div class="profile-detail__review">
    <div
      v-for="item in reviewList"
      :key="item.pk"
      class="profile-detail__review__item"
      data-aos="zoom-in"
    >
      <div
        @click="moveDetail(item.movie_id.pk)"
        class="profile-detail__review__item__image"
        :style="{
          backgroundImage: `url( https://image.tmdb.org/t/p/original${item.movie_id.poster_path})`,
        }"
      ></div>
      <div class="profile-detail__review__item__content">
        <p class>
          {{ item.content }}
        </p>
        <div class="profile-detail__review__item__tag">
          <span>
            {{ userCreatedAt(item) }}
          </span>
          <!-- <span class="bg-icon-red profile-detail__review__item__tag__heart">
            <font-awesome-icon icon="fa-solid fa-heart" class="font-white" />
            <span class="font-nav-black">{{ item.like_count }}</span>
          </span> -->
        </div>
      </div>
    </div>
    <empty-component
      v-if="isEmpty"
      data="아직 작성한 평가가"
      class="movie-detail__review__empty"
    ></empty-component>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import EmptyComponent from "@/components/EmptyComponent.vue";

export default {
  name: "UserInfoReview",
  components: { EmptyComponent },
  computed: {
    ...mapGetters(["userInfoDetail"]),
    reviewList() {
      return this?.userInfoDetail?.review;
    },
    isEmpty() {
      if (this?.reviewList?.length === 0) {
        return true;
      } else {
        return false;
      }
    },
  },
  methods: {
    userCreatedAt(data) {
      const createdAt = data.created_at.slice(0, 10);
      return createdAt;
    },
    moveDetail(data) {
      this.$router.push({ name: "movieDetail", params: { movieId: data } });
    },
  },
};
</script>

<style scoped>
.profile-detail__review {
  width: 80%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 3em;
  height: 15rem;
}

.profile-detail__review__item {
  display: flex;
  width: 40%;
  border-radius: 1em;
  align-items: center;
  background-color: #eeeeee;
  gap: 2em;
  overflow: hidden;
}

@media (max-width: 1100px) {
  .profile-detail__review__item {
    width: 100%;
  }
}

.profile-detail__review__item__image {
  width: 10rem;
  height: 15rem;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.profile-detail__review__item__content {
  width: 60%;
  height: 15rem;
  padding: 3em 0em;
  border-radius: 0.5em;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
}

.profile-detail__review__item__content > p {
  font-size: 1.2em;
  width: 100%;
}

.profile-detail__review__item__tag__heart {
  padding: 0.4em 1em;
  border-radius: 0.3em;
}

.profile-detail__review__item__tag {
  display: flex;
  flex-wrap: wrap;
  bottom: 0;
  align-items: baseline;
  font-weight: 500;
  gap: 1em;
}

.profile-detail__review__item__tag__heart > span {
  margin-left: 0.5em;
}

.movie-detail__review__empty {
  margin-top: -2.1em;
}
p {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  line-height: 1.5;
  overflow: hidden;
}
</style>
