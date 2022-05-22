<template>
  <div class="screen">
    <div class="article-table">
      <ul>
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
          <div v-for="article in articles" :key="article.pk">
            <div class="article-list">
              <p class="article__type text">영화 게시판</p>
              <p class="article__blank-left"></p>
              <p class="article__title text">
                <router-link
                  class="router-txet"
                  :to="{ name: 'article', params: { articlePk: article.pk } }"
                >
                  {{ article.title }}
                </router-link>
              </p>
              <p class="article__blank-right"></p>
              <p class="article__nickname text">
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
              <p class="article__like-users text">
                {{ article.like_count }}
              </p>
              <p class="article__time text">
                {{ dateTime(article.created_at) }}
              </p>
            </div>
            <hr class="hr-height" />
          </div>
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ArticleListView",
  computed: {
    ...mapGetters(["articles"]),
  },
  methods: {
    ...mapActions(["fetchArticles"]),
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
    this.fetchArticles();
  },
};
</script>

<style>
.screen {
  background-color: white;
  display: flex;
  justify-content: center;
  min-height: 100%;
}
.article-list {
  display: flex;
  justify-content: space-between;
}
.article__type {
  width: 10%;
  text-align: center;
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

.text {
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
</style>
