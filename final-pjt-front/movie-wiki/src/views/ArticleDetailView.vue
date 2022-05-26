<template>
  <div class="screen row-article">
    <div class="box-article">
      <div class="article">
        <div class="article__title-bar">
          <div class="article__title-bar__title">
            <p class="article__title">{{ article.title }}</p>
            <button @click="showArticleModal">
              <font-awesome-icon
                v-if="userProfile.username === username"
                class="aritcle__title__icon"
                icon="fa-solid fa-ellipsis-vertical"
              />
            </button>
          </div>
          <div class="article__modal">
            <article-option-modal
              v-if="optionModal"
              @hide-article-modal="hideArticleModal"
              type="글"
              :articleId="articlePk"
            ></article-option-modal>
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
              <div class="flex-article row-article nickname-title-bar">
                <router-link
                  class="article_nickname"
                  :to="{
                    name: 'profile',
                    params: { username: username },
                  }"
                >
                  <p>{{ nickname }}</p>
                </router-link>
                <p class="article_time">{{ createdAt }}</p>
              </div>
            </div>
            <div class="social-info">
              <font-awesome-icon icon="fa-solid fa-message" />
              {{ articleCommentLength }}
              <font-awesome-icon icon="fa-solid fa-heart" />
              {{ articleLikeCount }}
            </div>
          </div>
        </div>
        <hr class="hr-article" />
        <div class="article-space">
          <div class="article__content">
            <Viewer
              v-if="article.content != null"
              :initialValue="article.content"
            />
          </div>
          <div class="like-button-space">
            <button class="article-like-button" @click="likeArticle(articlePk)">
              <font-awesome-icon icon="fa-solid fa-heart" />
              {{ articleLikeCount }}
            </button>
          </div>
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
import "@toast-ui/editor/dist/toastui-editor.css";
import { Viewer } from "@toast-ui/vue-editor";
import ArticleOptionModal from "@/components/articleOptionModal.vue";

export default {
  components: {
    UserProfileImage,
    CommentForm,
    CommentItem,
    Viewer,
    ArticleOptionModal,
  },
  name: "ArticleDetailView",
  data() {
    return {
      articlePk: this.$route.params.articlePk,
      optionModal: false,
    };
  },
  computed: {
    ...mapGetters(["isAuthor", "article", "userProfile"]),
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
      return this?.article?.like_count;
    },
    articleComment() {
      return this?.article?.comment;
    },
    createdAt() {
      return this?.article?.created_at?.slice(0, 10);
    },
  },
  methods: {
    ...mapActions(["fetchArticle", "likeArticle", "deleteArticle"]),
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
.box-article {
  margin-bottom: 50px;
}

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
  justify-content: flex-end;
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
.article-like-button {
  background-color: #ed4245;
  color: white;
  border-radius: 5px;
  font-size: 16px;
  min-width: 3rem;
  height: 2rem;
  padding: 0px 0 0 2px;
}
.like-button-space {
  display: flex;
  padding: 2rem;
}
.article-space {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 40vh;
}
.social-info {
  color: #40444b;
}
.nickname-title-bar {
  align-items: start;
}
.article_time {
  margin-left: 6px;
  font-size: 13px;
  line-height: 18px;
  margin-top: 10px;
  color: #40444b;
}

@media (max-width: 1500px) {
  .box-article {
    width: 80vw;
  }
}
</style>
