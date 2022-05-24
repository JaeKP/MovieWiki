<template>
  <div class="create-form">
    <article-form :article="article" action="작성"></article-form>
  </div>
</template>

<script>
import ArticleForm from "@/components/ArticleForm.vue";

export default {
  name: "ArticleCreateView",

  components: { ArticleForm },
  data() {
    return {
      article: {
        pk: null,
        title: "",
        content: "",
        type: "1",
      },
    };
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
