<template>
  <div class="container">
    <div class="profile">
      <user-info @show-user-change-modal="showUserChangeModal"></user-info>
      <div class="profile-detail">
        <button :class="movieColor" @click="changeComponent('UserInfoMovie')">
          내가 찜한 영화
        </button>
        <button
          :class="articleColor"
          @click="changeComponent('UserInfoArticle')"
        >
          내 게시글
        </button>
        <button
          :class="commentColor"
          @click="changeComponent('UserInfoComment')"
        >
          내 댓글
        </button>
        <button :class="reviewColor" @click="changeComponent('UserInfoReview')">
          내 평가
        </button>
        <hr class="font-gray" />
      </div>
      <component :is="currentTabComponent"> </component>
    </div>
    <the-user-change-modal
      v-if="changeModal"
      class="modal"
      @hide-user-change-modal="hideUserChangeModal"
      @delete-user="deleteUser"
    ></the-user-change-modal>
  </div>
</template>

<script>
import UserInfo from "@/components/UserInfo.vue";
import { mapActions, mapGetters } from "vuex";
import TheUserChangeModal from "@/components/TheUserChangeModal.vue";
import UserInfoArticle from "@/components/UserInfoArticle.vue";
import UserInfoComment from "@/components/UserInfoComment.vue";
import UserInfoMovie from "@/components/UserInfoMovie.vue";
import UserInfoReview from "@/components/UserInfoReview.vue";
import Swal from "sweetalert2";

export default {
  name: "UserInfoView",
  components: {
    UserInfo,
    TheUserChangeModal,
    UserInfoArticle,
    UserInfoComment,
    UserInfoReview,
    UserInfoMovie,
  },
  data() {
    return {
      changeModal: false,
      currentTabComponent: "UserInfoMovie",
    };
  },
  methods: {
    ...mapActions(["setUserInfoName", "fetchProfile", "deleteUserData"]),
    showUserChangeModal(data) {
      this.changeModal = data;
    },
    hideUserChangeModal() {
      this.changeModal = false;
      this.fetchProfile(this.params);
    },
    deleteUser() {
      Swal.fire({
        title: "주의하세요!",
        text: "탈퇴시, 모든 데이터는 복구가 불가능합니다.",
        icon: "error",
        width: "25%",
        showCloseButton: true,
        showCancelButton: true,
        focusCancel: true,
        confirmButtonText: "탈퇴하기",
        cancelButtonText: "취소하기",
        confirmButtonColor: "#ED4245",
        cancelButtonColor: "#5865F2",
        position: "center",
        heightAuto: false,
      }).then((response) => {
        if (response.isConfirmed === true) {
          this.deleteUserData(this.userProfile.username);
        }
      });
    },
    changeComponent(page) {
      this.currentTabComponent = page;
    },
  },
  computed: {
    ...mapGetters(["userProfile"]),
    params() {
      return this.$route.params.username;
    },
    movieColor() {
      if (this.currentTabComponent !== "UserInfoMovie") {
        return "font-gray";
      } else {
        return "font-white";
      }
    },
    commentColor() {
      if (this.currentTabComponent !== "UserInfoComment") {
        return "font-gray";
      } else {
        return "font-white";
      }
    },
    articleColor() {
      if (this.currentTabComponent !== "UserInfoArticle") {
        return "font-gray";
      } else {
        return "font-white";
      }
    },
    reviewColor() {
      if (this.currentTabComponent !== "UserInfoReview") {
        return "font-gray";
      } else {
        return "font-white";
      }
    },
  },
  watch: {
    params() {
      this.setUserInfoName(this.params);
    },
  },
  created() {
    this.setUserInfoName(this.$route.params.username);
  },
};
</script>

<style scoped>
.profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 100px;
  gap: 5em;
}

.profile-detail {
  font-size: 2em;
  width: 80%;
}

.profile-detail > button {
  font-size: 0.7em;
  padding: 0.2em;
  margin-right: 1em;
  font-weight: 500;
}
</style>
