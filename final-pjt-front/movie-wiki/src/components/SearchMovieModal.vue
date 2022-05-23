<template>
  <div class="modal-bg" @click.self="hideSearchModal">
    <div>
      <div class="search-modal bg-navbar-black">
        <input type="text" @input="changeKeyword" />
        <search-movie-item
          v-for="searchInfo in searchInfos.title"
          :key="searchInfo.id"
          :searchInfo="searchInfo"
          :keyword="keyword"
          type="title"
        ></search-movie-item>
        <search-movie-item
          v-for="searchInfo in searchInfos.actor"
          :key="searchInfo.id"
          :searchInfo="searchInfo"
          :keyword="keyword"
          type="name"
        ></search-movie-item>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import SearchMovieItem from "./SearchMovieItem.vue";
export default {
  components: { SearchMovieItem },
  name: "SearchMovieModal",
  data() {
    return {};
  },
  computed: {
    ...mapState(["searchInfos", "keyword"]),
  },
  methods: {
    hideSearchModal() {
      this.$emit("hide-search-modal", false);
    },
    changeKeyword(event) {
      const querytype = [event.target.value, "title"];
      this.searchInfo(querytype);
      const querytype2 = [event.target.value, "actor"];
      this.searchInfo(querytype2);
    },
    ...mapActions(["searchInfo"]),
  },
};
</script>

<style scoped>
.search-modal {
  width: 100%;
  margin-top: 80px;
  min-width: 350px;
  padding: 3em 2em 20em 2em;
  z-index: 2;
  display: flex;

  flex-direction: column;
  align-items: center;
  gap: 1em;
}

input {
  border: 1px solid #dcddde;
  border-radius: 0.3rem;
  background-color: white;
  height: 2.5em;
  padding: 0 0 0 3rem;
  font-size: 1rem;
  width: 75%;
  font-weight: 1rem;
  outline-color: #fe6b8b;
  /* color: #b9bbbe; */
}

.modal-bg {
  width: 100vw;
  height: calc(100vh);
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-color: rgba(32, 34, 37, 0.8);
  z-index: 1;
}

/* hr {
  width: 78%;
} */
</style>
