<template>
  <div class="screen row-article">
    <div class="box-article">
      <div class="article">
        <div class="article__title-bar">
          <div class="article__title-bar__title">
            <p class="article__title">{{ article.title }}</p>
            <button @click="showArticleModal">
              <font-awesome-icon
                class="aritcle__title__icon"
                icon="fa-solid fa-ellipsis-vertical"
              />
            </button>
          </div>
          <div class="article__modal">
            <OptionMoadal
              v-if="optionModal"
              @hide-article-modal="hideArticleModal"
              type="글"
            ></OptionMoadal>
          </div>
          <div class="article__title-bar__user-info">
            <div class="flex-article">
              <router-link
                :to="{
                  name: 'profile',
                  params: { username },
                }"
              >
                <user-profile-image
                  width="50px"
                  height="50px"
                  :image="profileImage"
                ></user-profile-image>
              </router-link>
              <div class="flex-article row-article">
                <router-link
                  class="article_nickname"
                  :to="{
                    name: 'profile',
                    params: { username },
                  }"
                >
                  <p>{{ nickname }}</p>
                </router-link>
                방금 전
              </div>
            </div>
            <div>
              <font-awesome-icon icon="fa-solid fa-message" />
              {{ articleCommentLength }}
              <font-awesome-icon icon="fa-solid fa-heart" />
              {{ articleLikeCount }}
            </div>
          </div>
        </div>
        <hr class="hr-article" />
        <div class="article__content">
          {{ article.content }}
        </div>
      </div>
      <comment-form></comment-form>
      <div class="article-comment">
        <comment-item
          v-for="comment in articleComment"
          :key="comment.pk"
          :comment="comment"
        ></comment-item>
      </div>
    </div>
  </div>
</template>

<script>
import UserProfileImage from "@/components/UserProfileImage.vue";
import { mapGetters, mapActions } from "vuex";
import CommentForm from "@/components/CommentForm.vue";
import CommentItem from "@/components/CommentItem.vue";
import OptionMoadal from "@/components/OptionModal.vue";
export default {
  components: { UserProfileImage, CommentForm, CommentItem, OptionMoadal },
  name: "ArticleDetailView",
  data() {
    return {
      articlePk: this.$route.params.articlePk,
      optionModal: false,
    };
  },
  computed: {
    ...mapGetters(["isAuthor", "article"]),
    username() {
      return this?.article?.user_id?.username;
    },
    profileImage() {
      return this?.article?.user_id?.profile_image;
    },
    nickname() {
      return this?.article?.user_id?.nickname;
    },
    articleCommentLength() {
      return this?.article?.comment?.length;
    },
    articleLikeCount() {
      return this?.article?.comment?.like_count;
    },
    articleComment() {
      return this?.article?.comment;
    },
  },
  methods: {
    ...mapActions(["fetchArticle"]),
    hideArticleModal() {
      this.optionModal = false;
    },
    showArticleModal() {
      this.optionModal = true;
    },
  },
  created() {
    this.fetchArticle(this.articlePk);
  },
};
</script>

<style scoped>
.article {
  background-color: #dcddde;
  width: 100%;
  margin-top: 50px;
  min-height: 40vh;
  border-radius: 10px;
}
.article__title-bar {
  padding: 3% 3% 1% 3%;
}
.article__title-bar__title {
  display: flex;
  justify-content: space-between;
}
.aritcle__title__icon {
  height: 30px;
  padding: 2px;
  color: #40444b;
}
.article__title {
  font-size: 27px;
  color: #40444b;
}
.hr-article {
  border: 0;
  height: 2px;
  width: 97%;
  background: white;
}
.article__title-bar__user-info {
  display: flex;
  justify-content: space-between;
}
.article_nickname {
  margin-left: 5px;
  font-size: 22px;
  text-decoration: none;
  color: inherit;
  line-height: 18px;
}
.flex-article {
  display: flex;
}
.row-article {
  flex-direction: column;
  align-items: center;
}

.box-article {
  width: 50vw;
  max-width: 1000px;
}
.article-comment {
  min-height: 20vh;
  width: 100%;
  border-radius: 10px;

  display: flex;
  flex-direction: column;
  align-items: center;
}
.article__modal {
  width: 100%;
  display: flex;
  justify-content: end;
  padding-right: 10px;
  margin-bottom: 3%;
}
.article__content {
  padding: 2rem;
  margin-left: 5px;
  font-size: 20px;
  color: inherit;
  line-height: 18px;
}
</style>
