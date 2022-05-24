<template>
  <div>
    <div class="profile">
      <user-info @show-user-change-modal="showUserChangeModal"></user-info>
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
import Swal from "sweetalert2";

export default {
  name: "UserInfoView",
  components: {
    UserInfo,
    TheUserChangeModal,
  },
  data() {
    return {
      changeModal: false,
    };
  },
  computed: {
    ...mapGetters(["userProfile"]),
    params() {
      return this.$route.params.username;
    },
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
}
</style>
