<template>
  <div>
    <div class="profile">
      <user-info @show-user-change-modal="showUserChangeModal"></user-info>
    </div>
    <the-user-change-modal
      v-if="changeModal"
      class="modal"
      @hide-user-change-modal="hideUserChangeModal"
    ></the-user-change-modal>
  </div>
</template>

<script>
import UserInfo from "@/components/UserInfo.vue";
import { mapActions } from "vuex";
import TheUserChangeModal from "@/components/TheUserChangeModal.vue";
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
    params() {
      return this.$route.params.username;
    },
  },
  methods: {
    ...mapActions(["setUserInfoName"]),
    showUserChangeModal(data) {
      this.changeModal = data;
    },
    hideUserChangeModal() {
      this.changeModal = false;
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
