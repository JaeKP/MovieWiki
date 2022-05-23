<template>
  <li class="comment-object">
    <div class="flex-comment">
      <div class="flex-row">
        <router-link
          :to="{
            name: 'profile',
            params: { username: payload.username },
          }"
        >
          <user-profile-image
            width="50px"
            height="50px"
            :image="payload.profileImage"
          ></user-profile-image>
        </router-link>
        <div>
          <router-link
            class="comment_nickname"
            :to="{ name: 'profile', params: { username: payload.username } }"
          >
            {{ payload.nickname }}
          </router-link>
        </div>
      </div>
      <div>
        <button @click="showCommentModal" class="modal-button">
          <font-awesome-icon
            v-if="userProfile.username === payload.username"
            class="comment__title__icon"
            icon="fa-solid fa-ellipsis-vertical"
          />
        </button>

        <div class="comment__modal">
          <OptionMoadal
            type="댓글"
            v-if="optionModal"
            @hide-article-modal="hideCommentModal"
            @switch-is-editing="switchIsEditing"
            :payload="payload"
          ></OptionMoadal>
        </div>
      </div>
    </div>

    <hr />
    <span v-if="!isEditing" class="comment-content">{{ payload.content }}</span>

    <span v-if="isEditing">
      <textarea v-model="payload.content"></textarea>
      <div class="update-b">
        <button @click="onUpdate" class="comment-update udapte-submit">
          Update
        </button>
        <button @click="closeIsEditing" class="comment-update update-cancle">
          Cancle
        </button>
      </div>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import UserProfileImage from "./UserProfileImage.vue";
import OptionMoadal from "@/components/OptionModal.vue";
export default {
  components: { UserProfileImage, OptionMoadal },
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
        username: this.comment.user.username,
        created_at: this.comment.created_at,
        nickname: this.comment.user.nickname,
        profileImage: this.comment.user.profile_image,
      },
      optionModal: false,
    };
  },
  computed: {
    ...mapGetters(["userProfile"]),
  },
  methods: {
    ...mapActions(["updateComment", "deleteComment"]),
    switchIsEditing() {
      if (!this.isEditing) {
        this.isEditing = !this.isEditing;
      }
      this.optionModal = false;
    },
    closeIsEditing() {
      this.isEditing = !this.isEditing;
    },
    onUpdate() {
      console.log(this.comment);
      this.updateComment(this.payload);
      this.isEditing = false;
    },
    hideCommentModal() {
      this.optionModal = false;
    },
    showCommentModal() {
      this.optionModal = true;
    },
  },
};
</script>

<style>
.comment-object {
  width: 100%;
  min-height: 200px;
  margin-top: 40px;
  background-color: white;
  border-radius: 5px;
  padding: 2rem;
}
.comment_nickname {
  font-weight: 400;
  font-size: 23px;
  line-height: 33px;
  text-decoration: none;
  color: #40444b;
  line-height: 18px;
}
.flex-comment {
  display: flex;
  justify-content: space-between;
}
.flex-column {
  flex-direction: column;
}
.flex-row {
  display: flex;
  flex-direction: row;
}
.comment-content {
  font-family: "Noto Sans KR";
  font-weight: 400;
  font-size: 20px;
  line-height: 33px;
  color: #40444b;
}
.comment__modal {
  width: 100%;
  display: flex;
  justify-content: end;
  padding-right: 10px;
  margin-bottom: 3%;
}
.comment__title__icon {
  height: 20px;
  padding: 2px;
  color: #40444b;
}
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
.comment-update {
  padding: 3px 0 0 3;
  margin: 0;
  gap: 24px;
  padding-bottom: 5px;
  border: 0;
  border-radius: 5px;
  font-weight: 500;
  font-size: 17px;
  line-height: 28px;
  letter-spacing: 0.15px;
  color: #ffffff;
  width: 75px;
  height: 35px;
}
.update-cancle {
  color: #fe6b8b;
}
.udapte-submit {
  color: #787cf3;
}
.update-b {
  display: flex;
  justify-content: end;
}
</style>
