<template>
  <div class="create-form">
    <article-form v-if="isArticle" :article="article" action="수정">
    </article-form>
  </div>
</template>

<script>
import ArticleForm from "@/components/ArticleForm.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "ArticleUpdateView",
  components: { ArticleForm },
  computed: {
    ...mapGetters(["article", "isArticle"]),
  },
  methods: {
    ...mapActions(["fetchArticle"]),
  },
  created() {
    this.fetchArticle(this.$route.params.articlePk);
  },
};
</script>

<style>
.create-form {
  background-color: #eeeeee;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
}
</style>
