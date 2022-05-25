<template>
  <div>
    <card-list
      URL="http://localhost:8000/api/v1/movie/list"
      Tag="최신 인기 영화"
    ></card-list>
  </div>
</template>

<script>
import CardList from "@/components/CardList.vue";

export default {
  components: { CardList },
  name: "HomeView",
};
</script>

<style></style>
