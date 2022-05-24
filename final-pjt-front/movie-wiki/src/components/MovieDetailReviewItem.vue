<template>
  <div class="movie-detail__review__list">
    <div class="movie-detail__review__list__profile">
      <user-profile-image
        :image="reviewData.user_id.profile_image"
        width="80px"
        height="80px"
      ></user-profile-image>
      <p class="font-basic">{{ userNickName }}</p>
      <!-- <p class="font-basic">{{ userAge }}</p> -->
    </div>
    <div class="movie-detail__review__list__item">
      <!-- 스포일러 댓글이 아닐 때 -->
      <div class="movie-detail__review__list__item__div" v-if="!isSpoiler">
        <p class="font-white">{{ reviewData.content }}</p>
      </div>
      <!-- 스포일러 댓글일 때 -->
      <div
        v-else
        class="movie-detail__review__list__item__div__isSpoiler"
        @click="checkSpoiler"
      >
        <div>
          <p>스포일러가 있습니다.</p>
          <p>>> 확인하기</p>
        </div>
      </div>
      <div class="movie-detail__review__list__item__div2">
        <font-awesome-icon
          :class="isLike"
          icon="fa-solid fa-thumbs-up"
          @click="clickLike"
          class="movie-detail__review__list__item__div2__like"
        />
        <span
          v-if="filterType == 1"
          class="font-basic movie-detail__review__list__item__div2__count"
          >{{ reviewData.like_count }}</span
        >
        <span v-if="filterType == 2" class="font-basic">{{
          userCreatedAt
        }}</span>
        <button v-if="isAuthor" @click="deleteReview">
          <font-awesome-icon icon="fa-solid fa-x" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import UserProfileImage from "@/components/UserProfileImage.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "MovieDetailReviewItem",
  components: {
    UserProfileImage,
  },
  data() {
    return {
      reivewInfo: {
        type: this.filterType,
        movieId: this.reviewData.movie_id,
        reviewId: this.reviewData.id,
      },
      isSpoiler: this.reviewData.spoiler,
    };
  },
  props: {
    reviewData: {
      type: Object,
    },
    filterType: {
      type: Number,
    },
  },
  computed: {
    ...mapGetters(["userProfile"]),
    userNickName() {
      const nickname = this.reviewData.user_id.nickname;
      const length = nickname.length - 2;
      const hiddenName1 = nickname.substr(0, 2);
      const array = new Array(length).fill("*");
      const hiddenName2 = array.join("");
      return hiddenName1 + hiddenName2;
    },
    userAge() {
      const age = `${this.reviewData.user_id.age}`.slice(0, 1);
      return `${age}0 대`;
    },
    userCreatedAt() {
      const createdAt = this.reviewData.created_at.slice(0, 10);
      return createdAt;
    },
    isLike() {
      if (this.reviewData.like_users.includes(this?.userProfile?.id)) {
        return "font-icon-red";
      } else {
        return "font-basic";
      }
    },
    isAuthor() {
      return this?.userProfile?.username === this.reviewData.user_id.username;
    },
  },

  methods: {
    ...mapActions(["likeMovieReview"]),
    checkSpoiler() {
      this.isSpoiler = false;
    },
    clickLike() {
      this.likeMovieReview(this.reivewInfo);
    },
    deleteReview() {
      this.$emit("delete-review", this.reivewInfo);
    },
  },
};
</script>

<style scoped>
.movie-detail__review__list {
  width: 100%;
  display: flex;
  gap: 2em;
  align-items: center;
  justify-content: center;
}

.movie-detail__review__list__item {
  width: 80%;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  position: relative;
  gap: 0.3em;
}

.movie-detail__review__list__item__div {
  background-color: #40444b;
  color: #eeeeee;
  width: 100%;
  height: 130px;
  border-radius: 0.5em;
  display: flex;
  align-items: center;
}

.movie-detail__review__list__item__div__isSpoiler {
  background-color: #dcddde;
  color: #40444b;
  width: 100%;
  height: 130px;
  border-radius: 0.5em;
  display: flex;
  align-items: center;
}

.movie-detail__review__list__item__div__isSpoiler * {
  width: 100%;
  text-align: center;
  font-weight: 500;
}

.movie-detail__review__list__item__div2 {
  display: flex;
  align-items: center;
  font-size: 0.9em;
}

.movie-detail__review__list__item__div2__like {
  font-size: 2em;
  cursor: pointer;
  margin-right: 0.5em;
}

.movie-detail__review__list__item__div2__count {
  font-size: 1.3em;
  font-weight: 700;
}

.movie-detail__review__list__profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 150px;
}

.movie-detail__review__list__profile > p:nth-child(2) {
  font-size: 1.2em;
  font-weight: 400;
}

/* .movie-detail__review__list__profile > p:nth-child(3) {
  margin-top: -0.7em;
  font-size: 1em;
  font-weight: 400;
} */

/* .movie-detail__review__list__item::before {
  content: "";
  border-top: 0px solid transparent;
  border-left: 50px solid transparent;
  border-right: 0px solid transparent;
  border-bottom: 30px solid #40444b;
  position: relative;
  top: 78px;
  left: -50px;
} */
p {
  padding: 0.25em 2em;
  font-size: 1.2em;
  font-weight: 300;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  line-height: 1.8;
  overflow: hidden;
}

button {
  padding: 0.5em;
  border-radius: 0.2em;
  margin-left: 1em;
  position: absolute;
  top: 0.2px;
  right: 0px;
}

button > * {
  font-weight: 800;
  font-size: 1.5em;
  color: black;
}
</style>
