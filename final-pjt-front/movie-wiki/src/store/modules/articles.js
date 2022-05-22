import axios from "axios";
import drf from "@/api/drf";
import router from "@/router";
// import _ from "lodash";

export default {
  state: {
    articles: [],
    article: {},
  },
  getters: {
    articles: (state) => state.articles,
    article: (state) => state.article,
  },

  mutations: {
    SET_ARTICLES: (state, articles) => (state.articles = articles),
    SET_ARTICLE: (state, article) => (state.article = article),
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username;
    },
  },
  actions: {
    fetchArticles({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.article.articles(),
        method: "get",
        headers: getters.authHeaders,
      })
        .then((response) => commit("SET_ARTICLES", response.data))
        .catch((error) => console.error(error.response));
    },

    fetchArticle({ commit, getters }, articlePk) {
      /* 단일 게시글 받아오기
      GET: article URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */

      axios({
        url: drf.article.article(articlePk),
        method: "get",
        headers: getters.authHeader,
      })
        .then((response) => commit("SET_ARTICLE", response.data))
        .catch((error) => {
          console.error(error.response);
          if (error.response.status == 404) {
            router.push({ name: "NotFound404" });
          }
        });
    },
  },
};
