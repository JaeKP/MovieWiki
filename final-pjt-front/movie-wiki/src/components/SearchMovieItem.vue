<template>
  <ul>
    <router-link
      :to="{
        name: 'movieDetail',
        params: { movieId: searchInfo.id },
      }"
      v-if="searchInfo.title"
    >
      <li style="display: flex">
        <p class="font-gray">{{ start() }}</p>
        <p class="font-basic">{{ bold() }}</p>
        <p class="font-gray">{{ end() }}</p>
        <p class="font-medium-gray">({{ type }})</p>
      </li>
    </router-link>
    <div v-if="!searchInfo.title">
      <li style="display: flex">
        <p class="font-gray">{{ start() }}</p>
        <p class="font-basic">{{ bold() }}</p>
        <p class="font-gray">{{ end() }}</p>
        <p class="font-medium-gray">({{ type }})</p>
      </li>
    </div>
  </ul>
</template>

<script>
export default {
  name: "SearchMovieItem",
  data() {
    return {
      type: "",
    };
  },
  props: {
    searchInfo: {
      type: Object,
    },
    keyword: {
      type: String,
    },
  },
  methods: {
    bold() {
      if (this.searchInfo.title) {
        const start = this.searchInfo.title.indexOf(this.keyword);
        const end = start + this.keyword.length;
        let part = this.searchInfo.title.slice(start, end);
        if (this.searchInfo.title[end - 1] === " ") {
          part = this.searchInfo.title.slice(start, end) + "\u200b";
        }
        return part;
      } else {
        const start = this.searchInfo.name.indexOf(this.keyword);
        const end = start + this.keyword.length;
        let part = this.searchInfo.name.slice(start, end);
        if (this.searchInfo.name[end - 1] === " ") {
          part = this.searchInfo.name.slice(start, end) + "\u200b";
        }
        return part;
      }
    },
    start() {
      if (this.searchInfo.title) {
        const start = this.searchInfo.title.indexOf(this.keyword);
        let part = this.searchInfo.title.slice(0, start);

        if (this.searchInfo.title[start - 1] === " ") {
          part = this.searchInfo.title.slice(0, start) + "\u200b";
        }
        return part;
      } else {
        const start = this.searchInfo.name.indexOf(this.keyword);
        let part = this.searchInfo.name.slice(0, start);

        if (this.searchInfo.name[start - 1] === " ") {
          part = this.searchInfo.name.slice(0, start) + "\u200b";
        }
        return part;
      }
    },
    end() {
      if (this.searchInfo.title) {
        const start = this.searchInfo.title.indexOf(this.keyword);
        const end = start + this.keyword.length;
        let part = this.searchInfo.title.slice(
          end,
          this.searchInfo.title.length
        );
        if (this.searchInfo.title[end] === " ") {
          part =
            "\u200b" +
            this.searchInfo.title.slice(end, this.searchInfo.title.length);
        }
        return part;
      } else {
        const start = this.searchInfo.name.indexOf(this.keyword);
        const end = start + this.keyword.length;
        let part = this.searchInfo.name.slice(end, this.searchInfo.name.length);
        if (this.searchInfo.name[end] === " ") {
          part =
            "\u200b" +
            this.searchInfo.name.slice(end, this.searchInfo.name.length);
        }
        return part;
      }
    },
  },
  created() {
    if (this.searchInfo.type === "movie") {
      this.type = "영화";
    } else if (this.searchInfo.type === "actor") {
      this.type = "배우";
    } else if (this.searchInfo.type === "director") {
      this.type = "감독";
    }
  },
};
</script>

<style scoped>
li {
  width: 75vw;
  align-items: start;
}

p {
  /* color: white; */
  font-size: 2rem;
}
</style>
