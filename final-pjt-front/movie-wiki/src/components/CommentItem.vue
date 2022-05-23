<template>
  <li class="comment-object">
    <router-link
      :to="{ name: 'profile', params: { username: comment.user.username } }"
    >
      {{ comment.user.username }}
    </router-link>
    <pre>{{ payload.content }}</pre>
  </li>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "commentItem",
  props: {
    comment: Object,
  },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content,
      },
    };
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
  methods: {
    ...mapActions(["updateComment", "deleteComment"]),
    switchIsEditing() {
      this.isEditing = !this.isEditing;
    },
    onUpdate() {
      this.updateComment(this.payload);
      this.isEditing = false;
    },
  },
};
</script>

<style>
.comment-object {
  width: 80%;
  min-height: 40px;
  margin-top: 10px;
  background-color: #eeeeee;
  border-radius: 5px;
  padding: 1rem;
}
</style>
