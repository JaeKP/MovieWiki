<template>
  <ul @click="searchSelect">
    <li style="display: flex">
      <p class="font-gray">{{ start() }}</p>
      <p class="font-basic">{{ bold() }}</p>
      <p class="font-gray">{{ end() }}</p>
    </li>
  </ul>
</template>

<script>
export default {
  name: "SearchMovieItem",
  props: {
    searchInfo: {
      type: Object,
    },
    keyword: {
      type: String,
    },
    type: {
      type: String,
    },
  },
  methods: {
    bold() {
      const start = this.searchInfo[this.type].indexOf(this.keyword);
      const end = start + this.keyword.length;
      let part = this.searchInfo[this.type].slice(start, end);
      if (this.searchInfo[this.type][end - 1] === " ") {
        part = this.searchInfo[this.type].slice(start, end) + "\u200b";
      }
      return part;
    },
    start() {
      const start = this.searchInfo[this.type].indexOf(this.keyword);
      let part = this.searchInfo[this.type].slice(0, start);

      if (this.searchInfo[this.type][start - 1] === " ") {
        part = this.searchInfo[this.type].slice(0, start) + "\u200b";
      }
      return part;
    },
    end() {
      const start = this.searchInfo[this.type].indexOf(this.keyword);
      const end = start + this.keyword.length;
      let part = this.searchInfo[this.type].slice(
        end,
        this.searchInfo[this.type].length
      );
      if (this.searchInfo[this.type][end] === " ") {
        part =
          "\u200b" +
          this.searchInfo[this.type].slice(
            end,
            this.searchInfo[this.type].length
          );
      }
      return part;
    },
    searchSelect() {},
  },
};
</script>

<style scoped>
li {
  width: 75vw;
  align-items: start;
}

p {
  color: white;
  font-size: 2rem;
}
</style>
