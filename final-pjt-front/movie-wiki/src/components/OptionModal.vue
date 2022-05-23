<template>
  <div class="profile-modal" @mouseleave="hideArticleModal">
    <button class="pofile-modal__user" @click="switchIsEditing">
      {{ type }} 수정
    </button>
    <hr />
    <button class="pofile-modal__user red-del" @click="deleteComment(payload)">
      {{ type }} 삭제
    </button>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "OptionModal",
  methods: {
    ...mapActions(["deleteComment"]),
    hideArticleModal() {
      this.$emit("hide-article-modal", false);
    },
    switchIsEditing() {
      this.$emit("switch-is-editing");
    },
  },
  props: {
    type: {
      type: String,
    },
    payload: {
      type: Object,
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
