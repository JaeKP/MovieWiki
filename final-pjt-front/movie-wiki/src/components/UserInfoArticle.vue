<template>
  <div>아티클!</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserInfoArticle",
  coputed: {
    ...mapGetters(["userInfoDetail"]),
    articleList() {
      return this?.userInfoDetail?.article;
    },
  },
};
</script>

<style></style>
