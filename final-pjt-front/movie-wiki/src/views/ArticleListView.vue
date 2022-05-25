<template>
  <div class="screen">
    <div class="article-table">
      <ul>
        <div class="article-list-buttons">
          <div>
            <button @click="allArticle" class="article-type">
              전체 게시판
            </button>
            <button @click="popularArticle" class="article-type">
              인기 게시판
            </button>
            <button @click="selectArticle(1)" class="article-type">
              자유 게시판
            </button>
            <button @click="selectArticle(2)" class="article-type">
              영화 게시판
            </button>
            <button @click="selectArticle(3)" class="article-type">
              배우 게시판
            </button>
          </div>

          <router-link :to="{ name: 'ArticleCreate' }" class="article-create"
            >게시글 작성</router-link
          >
        </div>

        <div class="bg-medium-gray article-table-top">
          <div class="article-list">
            <p class="article__type text-top font-white">게시판</p>
            <p class="article__blank-left"></p>
            <p class="article__title-center text-top font-white">제목</p>
            <p class="article__blank-right"></p>
            <p class="article__nickname text-top font-white">작성자</p>
            <p class="article__like-users text-top font-white">추천수</p>
            <p class="article__time text-top font-white">작성 시각</p>
          </div>

          <hr class="hr-height" />
        </div>
        <div class="article-table-bottom">
          <div v-for="article in pagenatedData" :key="article.pk">
            <div class="article-list">
              <p
                class="article__type__list article-list-text"
                @click="selectArticle(article.article_type.pk)"
              >
                {{ article.article_type.name }}
              </p>
              <p class="article__blank-left"></p>
              <p class="article__title article-list-text">
                <router-link
                  class="router-txet"
                  :to="{ name: 'article', params: { articlePk: article.pk } }"
                >
                  {{ article.title }} [{{ article.comment_count }}]
                </router-link>
              </p>
              <p class="article__blank-right"></p>
              <p class="article__nickname article-list-text">
                <router-link
                  class="router-txet"
                  :to="{
                    name: 'profile',
                    params: { username: article.user_id.username },
                  }"
                >
                  {{ article.user_id.nickname }}
                </router-link>
              </p>
              <p class="article__like-users article-list-text">
                {{ article.like_count }}
              </p>
              <p class="article__time article-list-text">
                {{ dateTime(article.created_at) }}
              </p>
            </div>
            <hr class="hr-height" />
          </div>
        </div>
      </ul>
      <!-- 페이지네이션! -->

      <div class="movie-detail__review__pagenation" :class="isBlur">
        <div>
          <button
            :disabled="pageNum === 0"
            @click="prevPage"
            class="font-nav-black"
          >
            <font-awesome-icon icon="fa-solid fa-angles-left" />
          </button>
          <span class="movie-detail__review__pagenation__count font-icon-gray"
            >{{ pageNum + 1 }} / {{ pageCount }} 페이지</span
          >
          <button
            :disabled="pageNum >= pageCount - 1"
            @click="nextPage"
            class="font-nav-black"
          >
            <font-awesome-icon icon="fa-solid fa-angles-right" />
          </button>
        </div>
      </div>
      <div class="select-box">
        <select name="게시판" id="asdasdasd" v-model="searchType">
          <option value="1">제목</option>
          <option value="2">내용</option>
          <option value="3">제목 + 내용</option>
          <option value="4">작성자</option>
        </select>
        <input
          type="text"
          v-model="payload.query"
          @keyup.enter="articlesSearch"
          class="title__input"
          placeholder="검색어를 입력하세요."
        />
        <button class="search-button" @click="articlesSearch">검색</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "ArticleListView",
  data() {
    return {
      pageSize: 10,
      pageNum: 0,
      payload: {
        type: "all",
        query: null,
        title: null,
        content: null,
        nickname: null,
      },
      searchType: "1",
    };
  },
  computed: {
    ...mapGetters(["articles"]),
    isBlur() {
      if (this?.isLoggedIn !== true) {
        return "blurEffect";
      } else {
        return "";
      }
    },
    pageCount() {
      let listing = this.articles.length;
      let listSize = this.pageSize;
      let page = Math.floor(listing / listSize);
      if (listing % listSize > 0) {
        page = page + 1;
      }
      return page;
    },
    pagenatedData() {
      const start = this.pageNum * this.pageSize;
      const end = start + this.pageSize;
      return this.articles.slice(start, end);
    },
  },
  methods: {
    ...mapActions([
      "fetchArticles",
      "fetchArticlesPopular",
      "fetchArticlesSelect",
    ]),
    allArticle() {
      this.payload.type = "all";
      this.fetchArticles(this.payload);
    },
    popularArticle() {
      this.payload.type = "popular";
      this.fetchArticles(this.payload);
    },
    selectArticle(num) {
      this.payload.type = num;
      this.fetchArticles(this.payload);
    },
    articlesSearch() {
      if (this.searchType === "1") {
        this.payload.title = "on";
        this.payload.content = null;
        this.payload.nickname = null;
      } else if (this.searchType === "2") {
        this.payload.title = null;
        this.payload.content = "on";
        this.payload.nickname = null;
      } else if (this.searchType === "3") {
        this.payload.title = "on";
        this.payload.content = "on";
        this.payload.nickname = null;
      } else if (this.searchType === "4") {
        this.payload.title = null;
        this.payload.content = null;
        this.payload.nickname = "on";
      }

      this.fetchArticles(this.payload);
    },
    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
    },
    dateTime(a) {
      // 게시글 작성 사걱
      const articleDay = new Date(a);
      // 현재시각
      const Day = new Date();
      // 게시글 작성 날짜
      const articleDayDate =
        articleDay.getFullYear() +
        "-" +
        ("00" + (articleDay.getMonth() + 1)).slice(-2) +
        "-" +
        ("00" + articleDay.getDate()).slice(-2);
      // 현재 날짜
      const DayDate =
        Day.getFullYear() +
        "-" +
        ("00" + (Day.getMonth() + 1)).slice(-2) +
        "-" +
        ("00" + Day.getDate()).slice(-2);
      // 게시글 작성 시간
      const articleTime = ("00" + articleDay.getHours()).slice(-2);
      // 게시글 작성 분
      const articleMinute = ("00" + articleDay.getMinutes()).slice(-2);
      // 현재 시간
      const DayTime = ("00" + Day.getHours()).slice(-2);
      // 현재 분
      const Dayminute = ("00" + Day.getMinutes()).slice(-2);

      if (DayDate === articleDayDate) {
        if (
          articleTime === DayTime &&
          (Math.abs(Dayminute - articleMinute) < 6 ||
            Math.abs(Dayminute - articleMinute) > 54)
        ) {
          return "방금 전";
        } else {
          return a.slice(11, 16);
        }
      } else {
        return a.slice(5, 10);
      }
      // const a = article.created_at.slice(5, 10);
    },
  },
  created() {
    this.fetchArticles(this.payload);
  },
};
</script>

<style>
.screen {
  background-color: #eeeeee;
  display: flex;
  justify-content: center;
  min-height: calc(100vh - 80px);
}
.article-list {
  display: flex;
  justify-content: space-between;
}
.article__type {
  width: 10%;
  text-align: center;
}
.article__type__list {
  width: 10%;
  text-align: center;
}
.article__type__list:hover {
  text-decoration: underline;
}
.article__title {
  width: 50%;
}
.article__title-center {
  width: 50%;
  text-align: center;
}

.article__nickname {
  width: 10%;
  text-align: center;
}
.article__like-users {
  width: 9%;
  text-align: center;
}
.article__time {
  width: 10%;
  text-align: center;
}
.hr-height {
  border: 0;
  height: 3px;
  background: #b9bbbe;
}
.article-table {
  margin-top: 180px;
  width: 65%;
}
.article-table-top {
  border-radius: 10px 10px 0 0;
  padding-top: 6px;
  line-height: 32px;
}
.article-table-bottom {
  border-radius: 0 0 10px 10px;
}

.article-list-text {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 23px;
  color: #40444b;
}
.article__blank-left {
  width: 5%;
}
.article__blank-right {
  width: 5%;
}
.text-top {
  font-size: 20px;
}
.router-txet {
  text-decoration: none;
  color: inherit;
}
.router-txet:hover {
  text-decoration: underline;
}
.article-create {
  text-align: center;
  padding-top: 0.3rem;
  margin-top: 0.5rem;
  gap: 24px;
  padding-bottom: 5px;
  border: 0;
  border-radius: 0.3rem;
  font-weight: 500;
  font-size: 17px;
  line-height: 28px;
  letter-spacing: 0.15px;
  color: white;
  background-color: #faa81a;
  width: 100px;
  height: 40px;
  text-decoration: none;
  margin-bottom: 0.3rem;
}
.article-create:hover {
  border: 1px solid #eeeeee;
}
.article-list-buttons {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.article-type {
  text-align: center;
  padding-top: 0.3rem;
  margin-top: 0.5rem;
  gap: 24px;
  padding-bottom: 5px;
  border: 0;
  border-radius: 0.3rem;
  font-weight: 500;
  font-size: 17px;
  line-height: 28px;
  letter-spacing: 0.15px;
  color: white;
  background-color: #96989d;
  width: 100px;
  height: 40px;
  text-decoration: none;
  margin-bottom: 0.3rem;
  margin-right: 0.3rem;
}
.article-type:hover {
  border: 1px solid #eeeeee;
}

.movie-detail__review__pagenation {
  width: 100%;
  display: flex;
  gap: 2em;
  align-items: center;
  justify-content: center;
}

.movie-detail__review__pagenation button {
  padding: 0.5em;
  font-size: 2em;
}

.movie-detail__review__pagenation__count {
  font-size: 1.2em;
}

.title__input {
  border: 1px solid #dcddde;

  background-color: white;
  height: 1em;
  padding: 1rem;
  font-size: 1rem;
  font-family: "Noto Sans KR";
  width: calc(100% - 2rem);

  resize: none;
  outline-color: #fe6b8b;
}
.select-box {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}
select {
  padding: 0.3rem;
  border-radius: 0.4rem 0 0 0.4rem;
  border: 1px solid #dcddde;
  border-right: 0px;
  font-family: "Noto Sans KR";
  outline-color: #fe6b8b;
}
.search-button {
  height: 3.05rem;
  margin-top: 0.02rem;

  font-weight: 500;
  font-size: 17px;
  color: white;
  background-color: #36393f;
  width: 100px;
  border-radius: 0 0.4rem 0.4rem 0;
}
.search-button:hover {
  border: 1px solid #eeeeee;
}
</style>
