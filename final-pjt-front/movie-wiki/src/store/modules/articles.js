import axios from "axios";
import drf from "@/api/drf";
import router from "@/router";
import _ from "lodash";
import Swal from "sweetalert2";

export default {
  state: {
    articles: [],
    article: {},
    payLoad: {
      type: "all",
      query: null,
      title: null,
      content: null,
      nickname: null,
    },
  },
  getters: {
    articles: (state) => state.articles,
    article: (state) => state?.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username;
    },
    isArticle: (state) => !_.isEmpty(state.article),
    payLoad: (state) => state.payLoad,
  },

  mutations: {
    SET_ARTICLES: (state, articles) => (state.articles = articles),
    SET_ARTICLE: (state, article) => (state.article = article),
    SET_ARTICLE_COMMENTS: (state, comments) =>
      (state.article.comment = comments),
    SET_PAY_LOAD: (state, payload) => (state.payLoad = payload),
  },
  actions: {
    fetchArticles({ commit }, { type, query, title, content, nickname }) {
      const params = {
        type: type,
        query: query,
        title: title,
        content: content,
        nickname: nickname,
      };
      axios({
        url: drf.article.articleSearch(),
        method: "get",
        params,
      })
        .then((response) => commit("SET_ARTICLES", response.data))
        .catch((error) => console.error(error.response));
    },

    fetchArticle({ commit }, articlePk) {
      axios({
        url: drf.article.article(articlePk),
        method: "get",
      })
        .then((response) => commit("SET_ARTICLE", response.data))
        .catch((error) => {
          console.error(error.response);
          if (error.response.status == 404) {
            router.push({ name: "NotFound404" });
          }
        });
    },

    updateArticle({ commit, getters }, { pk, title, content, article_type }) {
      axios({
        url: drf.article.article(pk),
        method: "put",
        data: { title, content, article_type },
        headers: getters.authHeader,
      }).then((res) => {
        commit("SET_ARTICLE", res.data);
        router.push({
          name: "article",
          params: { articlePk: getters.article.pk },
        });
      });
    },

    deleteArticle({ commit, getters }, articlePk) {
      Swal.fire({
        title: "정말 삭제하시겠습니까",
        icon: "error",
        width: "400px",
        showCancelButton: true,
        focusCancel: true,
        confirmButtonText: "삭제",
        cancelButtonText: "취소",
        confirmButtonColor: "#ED4245",
        cancelButtonColor: "#5865F2",
        position: "center",
        heightAuto: false,
      }).then((response) => {
        if (response.isConfirmed === true) {
          axios({
            url: drf.article.article(articlePk),
            method: "delete",
            headers: getters.authHeader,
          })
            .then(() => {
              commit("SET_ARTICLE", {});
              router.push({ name: "articles" });
            })
            .catch((err) => console.error(err.response));
        }
      });
    },

    likeArticle({ commit, getters }, articlePk) {
      axios({
        url: drf.article.likeArticle(articlePk),
        method: "post",
        headers: getters.authHeader,
      })
        .then((res) => commit("SET_ARTICLE", res.data))
        .catch((err) => console.error(err.response));
    },

    createArticle({ commit, getters }, article) {
      axios({
        url: drf.article.articles(),
        method: "post",
        data: article,
        headers: getters.authHeader,
      })
        .then((res) => {
          commit("SET_ARTICLE", res.data);
          router.push({
            name: "article",
            params: { articlePk: getters.article.pk },
          });
        })
        .catch((error) => {
          if (error.response.status === 400) {
            Swal.fire({
              text: "내용을 입력해주세요.",
              icon: "error",
              width: "400px",
              showConfirmButton: false,
              timer: 2000,
              timerProgressBar: true,
              position: "center",
              heightAuto: false,
            });
          }
        });
    },
    createComment({ commit, getters }, { articlePk, content }) {
      const comment = { content };
      axios({
        url: drf.article.comments(articlePk),
        method: "post",
        data: comment,
        headers: getters.authHeader,
      })
        .then((response) => {
          commit("SET_ARTICLE_COMMENTS", response.data);
        })
        .catch((error) => console.error(error.response));
    },
    updateComment({ commit, getters }, { articlePk, commentPk, content }) {
      const comment = { content };
      axios({
        url: drf.article.comment(articlePk, commentPk),
        method: "put",
        data: comment,
        headers: getters.authHeader,
      })
        .then((response) => {
          commit("SET_ARTICLE_COMMENTS", response.data);
        })
        .catch((error) => console.error(error.response));
    },
    deleteComment({ commit, getters, dispatch }, { articlePk, commentPk }) {
      Swal.fire({
        title: "정말 삭제하시겠습니까",
        icon: "error",
        width: "400px",
        showCancelButton: true,
        focusCancel: true,
        confirmButtonText: "삭제",
        cancelButtonText: "취소",
        confirmButtonColor: "#ED4245",
        cancelButtonColor: "#5865F2",
        position: "center",
        heightAuto: false,
      }).then((response) => {
        if (response.isConfirmed === true) {
          axios({
            url: drf.article.comment(articlePk, commentPk),
            method: "delete",
            data: {},
            headers: getters.authHeader,
          })
            .then((res) => {
              commit("SET_ARTICLE_COMMENTS", res.data);
              dispatch("fetchArticle", articlePk);
            })
            .catch((err) => console.error(err.response));
        }
      });
    },
    commentLike({ commit, getters }, { articlePk, commentPk }) {
      axios({
        url: drf.article.commentLike(articlePk, commentPk),
        method: "post",
        headers: getters.authHeader,
      })
        .then((res) => commit("SET_ARTICLE_COMMENTS", res.data))
        .catch((err) => console.error(err.response));
    },
    setPayLoad({ commit }, payload) {
      commit("SET_PAY_LOAD", payload);
    },
  },
};
