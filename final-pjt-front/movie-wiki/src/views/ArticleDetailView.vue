<template>
  <div class="screen row-article">
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
    <form class="article-comment-set" action="">
      <textarea
        placeholder="광고 및 욕설, 비속어나 타인을 비방하는 문구를 사용하면 비공개 될 수 있습니다."
      ></textarea>
    </form>
    <div class="article-comment"></div>
  </div>
</template>

<script>
import UserProfileImage from "@/components/UserProfileImage.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  components: { UserProfileImage },
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
  },
  created() {
    this.fetchArticle(this.articlePk);
  },
};
</script>

<style>
.article {
  background-color: #dcddde;
  width: 60%;
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
.article-comment {
  margin-top: 80px;
  height: 20vh;
  width: 60%;
  border-radius: 10px;
  background-color: #dcddde;
  padding: 2%;
}
textarea {
  border: 1px solid #dcddde;
  border-radius: 0.3rem;
  background-color: white;
  height: 4em;
  padding: 1rem 0 0 1rem;
  font-size: 1rem;
  font-family: "Noto Sans KR";
  width: 98%;
  font-weight: 1rem;
  resize: none;
  /* color: #b9bbbe; */
}
.article-comment-set {
  margin-top: 80px;
  width: 60%;
}
</style>
