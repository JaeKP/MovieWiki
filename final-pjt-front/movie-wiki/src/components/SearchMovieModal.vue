<template>
  <div class="modal-bg" @click.self="hideSearchModal">
    <div>
      <div class="search-modal bg-navbar-black">
        <div class="input-box">
          <input type="text" @input="changeKeyword" />
        </div>

        <search-movie-item
          v-for="(searchInfo, i) in searchInfos"
          :key="i"
          :searchInfo="searchInfo"
          :keyword="keyword"
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
    ...mapActions(["setSearchBar"]),
    hideSearchModal() {
      this.setSearchBar(false);
    },
    changeKeyword(event) {
      this.searchInfo(event.target.value);
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
  z-index: 6;
  display: flex;
  height: 600px;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 1em;
}

input {
  border: 1px solid #dcddde;
  border-radius: 0.3rem;
  background-color: white;
  height: 2.5em;
  padding: 0 0 0 3rem;
  font-size: 1rem;
  width: 90vw;
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
  z-index: 5;
}
.input-box {
  width: 100%;
  display: flex;
  justify-content: center;
}

/* hr {
  width: 78%;
} */
</style>
