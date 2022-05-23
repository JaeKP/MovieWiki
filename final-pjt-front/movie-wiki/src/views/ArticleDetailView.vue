<template>
  <div class="screen row-article">
    <div class="box-article">
      <div class="article">
        <div class="article__title-bar">
          <div class="article__title-bar__title">
            <p class="article__title">{{ article.title }}</p>
            <font-awesome-icon
              class="aritcle__title__icon"
              icon="fa-solid fa-ellipsis-vertical"
            />
          </div>
          <div class="article__title-bar__user-info">
            <div class="flex-article">
              <router-link
                :to="{
                  name: 'profile',
                  params: { username: article.user_id.username },
                }"
              >
                <user-profile-image
                  width="50px"
                  height="50px"
                  :image="article.user_id.profile_image"
                ></user-profile-image>
              </router-link>
              <div class="flex-article row-article">
                <router-link
                  class="article_nickname"
                  :to="{
                    name: 'profile',
                    params: { username: article.user_id.username },
                  }"
                >
                  <p>{{ article.user_id.nickname }}</p>
                </router-link>
                방금 전
              </div>
            </div>
            <div>
              <font-awesome-icon icon="fa-solid fa-message" />
              {{ article.comment.length }}
              <font-awesome-icon icon="fa-solid fa-heart" />
              {{ article.like_count }}
            </div>
          </div>
        </div>
        <hr class="hr-article" />
        <div>
          {{ article.content }}
        </div>
      </div>
      <comment-form></comment-form>
      <div class="article-comment">
        <comment-item
          v-for="comment in article.comment.reverse()"
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
export default {
  components: { UserProfileImage, CommentForm, CommentItem },
  name: "ArticleDetailView",
  data() {
    return {
      articlePk: this.$route.params.articlePk,
    };
  },
  computed: {
    ...mapGetters(["isAuthor", "article"]),
  },
  methods: {
    ...mapActions(["fetchArticle"]),
    test() {
      console.log("댓글 남기기");
    },
  },
  created() {
    this.fetchArticle(this.articlePk);
  },
};
</script>

<style>
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
  margin-bottom: 3%;
}
.aritcle__title__icon {
  height: 30px;
  padding: 2px;
  color: #40444b;
}
.article__title {
  font-size: 30px;
  color: #40444b;
}
.hr-article {
  border: 0;
  height: 3px;
  width: 98%;
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
  width: 60vw;
}
.article-comment {
  margin-top: 80px;
  min-height: 20vh;
  width: 100%;
  border-radius: 10px;
  background-color: #dcddde;
  padding: 2%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
