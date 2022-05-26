<template>
  <div class="profile-modal" @mouseleave="hideArticleModal">
    <router-link :to="{ name: 'articleUpdate', params: { articleId } }">
      <button class="pofile-modal__user">{{ type }} 수정</button>
    </router-link>

    <hr />
    <button
      class="pofile-modal__user red-del"
      @click="deleteArticle(articleId)"
    >
      {{ type }} 삭제
    </button>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "TheArticleOptionModal",
  methods: {
    ...mapActions(["deleteArticle"]),
    hideArticleModal() {
      this.$emit("hide-article-modal", false);
    },
  },
  props: {
    type: {
      type: String,
    },
    articleId: {
      type: Number,
    },
  },
};
</script>

<style scoped>
.profile-modal {
  background-color: white;
  z-index: 2;
  width: 100px;
  height: 84px;
  border-radius: 0.3em;
  padding: 1em;
  display: flex;
  flex-direction: column;
  position: absolute;
  align-items: center;
  border: 1px solid #ccc;
}

.pofile-modal__user {
  display: flex;
  padding: 0;
  margin: 0;
  border: 0;
  align-items: center;
  color: #202225;
}

a {
  color: #36393f;
}

hr {
  border-top: 0.5px solid #96989d;
  border-bottom: 0 solid white;
  width: 100%;
}
.red-del {
  color: #fe6b8b;
}
</style>
