<template>
  <div>커멘트!</div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "UserInfoComment",
  computed: {
    ...mapGetters(["userInfoDetail"]),
    commentList() {
      return this?.userInfoDetail?.comment;
    },
  },
};
</script>

<style></style>
