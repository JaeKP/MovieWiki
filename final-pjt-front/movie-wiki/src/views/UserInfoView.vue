<template>
  <div>
    <div class="profile">
      <user-info></user-info>
    </div>
  </div>
</template>

<script>
import UserInfo from "@/components/UserInfo.vue";
import { mapActions } from "vuex";
export default {
  name: "UserInfoView",
  components: {
    UserInfo,
  },
  computed: {
    params() {
      return this.$route.params.username;
    },
  },
  methods: {
    ...mapActions(["setUserInfoName"]),
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
