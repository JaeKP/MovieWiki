<template>
  <div class="screen">
    <div class="article">
      <div class="article__title-bar">
        <user-profile-image
          width="100px"
          height="100px"
          :image="article.profile_image"
        ></user-profile-image>

        <h1>{{ article.title }}</h1>
      </div>
      <hr />
      <div>
        {{ article.content }}
        {{ article.profile_image }}
      </div>
    </div>
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
    ...mapGetters(["article"]),
    // likeCount() {
    //   return this.article.like_users?.length;
    // },
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
.screen {
  background-color: #dcddde;
  display: flex;
  justify-content: center;
}
.article {
  background-color: #dcddde;
  width: 50%;
  margin-top: 50px;
  height: 100vh;
  border-radius: 10px;
}
</style>
