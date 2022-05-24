import axios from "axios";
import drf from "@/api/drf";
import router from "@/router";
import _ from "lodash";

export default {
  state: {
    articles: [],
    article: {},
  },
  getters: {
    articles: (state) => state.articles,
    article: (state) => state?.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username;
    },
    isArticle: (state) => !_.isEmpty(state.article),
  },

  mutations: {
    SET_ARTICLES: (state, articles) => (state.articles = articles),
    SET_ARTICLE: (state, article) => (state.article = article),
    SET_ARTICLE_COMMENTS: (state, comments) =>
      (state.article.comment = comments),
  },
  actions: {
    fetchArticles({ commit }) {
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
      })
        .then((response) => commit("SET_ARTICLES", response.data))
        .catch((error) => console.error(error.response));
    },

    fetchArticle({ commit }, articlePk) {
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
      })
        .then((response) => commit("SET_ARTICLE", response.data))
        .catch((error) => {
          console.error(error.response);
          if (error.response.status == 404) {
            router.push({ name: "NotFound404" });
          }
        });
    },

    likeArticle({ commit, getters }, articlePk) {
      /* 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.article.likeArticle(articlePk),
        method: "post",
        headers: getters.authHeader,
      })
        .then((res) => commit("SET_ARTICLE", res.data))
        .catch((err) => console.error(err.response));
    },

    createArticle({ commit, getters }, article) {
      /* 게시글 생성
      POST: articles URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      // console.log(article);
      axios({
        url: drf.article.articles(),
        method: "post",
        data: article,
        headers: getters.authHeader,
      }).then((res) => {
        commit("SET_ARTICLE", res.data);
        router.push({
          name: "article",
          params: { articlePk: getters.article.pk },
        });
      });
    },
    updateArticle({ commit, getters }, { pk, title, content }) {
      /* 게시글 수정
      PUT: article URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.article.article(pk),
        method: "put",
        data: { title, content },
        headers: getters.authHeader,
      }).then((res) => {
        commit("SET_ARTICLE", res.data);
        router.push({
          name: "article",
          params: { articlePk: getters.article.pk },
        });
      });
    },

    createComment({ commit, getters }, { articlePk, content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
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
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
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
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
      if (confirm("정말 삭제하시겠습니까?")) {
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
  },
};
