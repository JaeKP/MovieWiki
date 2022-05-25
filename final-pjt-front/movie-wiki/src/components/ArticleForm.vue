<template>
  <form @submit.prevent="onSubmit">
    <div class="editor">
      <div class="select-box">
        <select name="게시판" id="asdasdasd" v-model="newArticle.article_type">
          <option value="1">자유 게시판</option>
          <option value="2">영화 게시판</option>
          <option value="3">배우 게시판</option>
        </select>
        <input
          type="text"
          v-model="newArticle.title"
          class="title__input"
          placeholder="제목을 입력하세요."
        />
      </div>

      <editor
        class="editor-main first"
        ref="toastuiEditor"
        :options="editorOptions"
        height="40rem"
        language="ko-KR"
        initialEditType="wysiwyg"
        previewStyle="vertical"
      />
    </div>

    <div class="article-create-button">
      <button class="article-update">{{ action }}</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from "vuex";
import "tui-color-picker/dist/tui-color-picker.css";
import "@toast-ui/editor-plugin-color-syntax/dist/toastui-editor-plugin-color-syntax.css";
import colorSyntax from "@toast-ui/editor-plugin-color-syntax";
import "@toast-ui/editor/dist/toastui-editor.css";
import { Editor } from "@toast-ui/vue-editor";

export default {
  name: "ArticleForm",
  components: {
    editor: Editor,
  },
  props: {
    article: Object,
    action: String,
  },
  data() {
    return {
      editorOptions: {
        hideModeSwitch: true,
        plugins: [colorSyntax],
      },
      newArticle: {
        title: this.article.title,
        content: this.article.content,
        article_type: this.article.type,
      },
    };
  },

  methods: {
    ...mapActions(["createArticle", "updateArticle"]),
    onSubmit() {
      const articleData = {
        title: this.newArticle.title,
        content: this.$refs.toastuiEditor.invoke("getMarkdown"),
        article_type: this.newArticle.article_type,
      };
      if (this.action === "작성") {
        this.createArticle(articleData);
      } else if (this.action === "update") {
        const payload = {
          pk: this.article.pk,
          ...this.newArticle,
        };
        this.updateArticle(payload);
      }
    },
  },
  computed: {
    content() {
      return this.$refs.toastuiEditor.invoke("getMarkdown");
    },
  },
};
</script>

<style scoped>
.editor {
  background-color: var(--header);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 70vw;
  margin-top: 60px;
}

.title__input {
  border: 1px solid #dcddde;
  border-radius: 0 0.4rem 0.4rem 0;
  background-color: white;
  height: 1em;
  padding: 1rem;
  font-size: 1rem;
  font-family: "Noto Sans KR";
  width: calc(100% - 2rem);

  resize: none;
  outline-color: #fe6b8b;
}
.editor-main {
  margin-top: 30px;
  width: 100%;
  font-family: "Noto Sans KR";
}
.select-box {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}
select {
  padding: 0.3rem;
  border-radius: 0.4rem 0 0 0.4rem;
  border: 1px solid #dcddde;
  border-right: 0px;
  font-family: "Noto Sans KR";
  outline-color: #fe6b8b;
}
.article-update {
  padding: 3px 0 0 3;
  margin-top: 0.5rem;
  gap: 24px;
  padding-bottom: 5px;
  border: 0;
  border-radius: 0.2rem;
  font-weight: 500;
  font-size: 17px;
  line-height: 28px;
  letter-spacing: 0.15px;
  color: white;
  background-color: #787cf3;
  width: 75px;
  height: 35px;
}
.article-create-button {
  width: 100%;
  display: flex;
  justify-content: flex-end;
}
</style>
