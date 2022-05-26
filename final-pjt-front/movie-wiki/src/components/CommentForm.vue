<template>
  <form @submit.prevent="onSubmit" class="article-comment-set" action="">
    <textarea
      v-model="content"
      placeholder="광고 및 욕설, 비속어나 타인을 비방하는 문구를 사용하면 비공개 될 수 있습니다."
    ></textarea>
    <div class="content-end flex-article">
      <button class="comment-submit">댓글 남기기</button>
    </div>
  </form>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Swal from "sweetalert2";
export default {
  name: "CommentForm",
  data() {
    return {
      content: "",
      badWords: ["바보", "멍청이", "시발", "병신"],
    };
  },
  computed: {
    ...mapGetters(["article"]),
  },
  methods: {
    ...mapActions(["createComment"]),
    checkAvailability(arr, val) {
      return arr.some((arrVal) => val.includes(arrVal));
    },
    checkWord() {
      return this.checkAvailability(this.badWords, this.content);
    },
    onSubmit() {
      if (!this.checkWord()) {
        this.createComment({
          articlePk: this.article.pk,
          content: this.content,
        });
        this.content = "";
      } else {
        Swal.fire({
          text: "부적절한 단어가 포함되어 있습니다.",
          icon: "error",
          width: "400px",
          showConfirmButton: false,
          timer: 2000,
          timerProgressBar: true,
          position: "center",
          heightAuto: false,
        });
      }
    },
  },
};
</script>

<style>
textarea {
  border: 1px solid #dcddde;
  border-radius: 0.3rem;
  background-color: white;
  height: 4em;
  padding: 1rem;
  font-size: 1rem;
  font-family: "Noto Sans KR";
  width: calc(100% - 2rem);
  font-weight: 1rem;
  resize: none;
  outline-color: #fe6b8b;
}
.article-comment-set {
  display: flex;
  flex-direction: column;
  margin-top: 40px;
  width: 100%;
  align-items: flex-end;
}

.comment-submit {
  padding: 3px 0 0 3;
  margin-top: 5px;
  gap: 24px;
  background: #36393f;
  border: 0;
  border-radius: 5px;
  font-weight: 500;
  font-size: 19px;
  line-height: 28px;
  letter-spacing: 0.15px;
  color: #ffffff;
  width: 134px;
  height: 48px;
}
.comment-submit:hover {
  border: 1px solid #eeeeee;
}
</style>
