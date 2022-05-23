import drf from "@/api/drf";
import axios from "axios";
import router from "@/router";

export default {
  state: {
    movieDetail: {},
    movieReviewPopularity: {},
    // searchInfos: null,
    // keyword: null,
  },
  getters: {
    // 영화 상세 정보
    movieDetail: (state) => state.movieDetail,
    movieReviewPopularity: (state) => state.movieReviewPopularity,
  },
  mutations: {
    SET_MOVIE_DETAIL: (state, data) => (state.movieDetail = data),
    SET_MOVIE_REVIEW_POPULARITY: (state, data) =>
      (state.movieReviewPopularity = data),
  },
  actions: {
    // 영화 상세정보 vuex에 저장하기
    setMovieDetail({ commit }, data) {
      commit("SET_MOVIE_DETAIL", data);
    },

    //영화 리뷰 정보 vuex에 저장하기
    setMovieReviewPopularity({ commit }, data) {
      commit("SET_MOVIE_REVIEW_POPULARITY", data);
    },

    // 영화 상세정보 요청하기
    fetchMovieDetail({ dispatch }, movieId) {
      axios({
        url: drf.movie.movieDetail(movieId),
        method: "get",
      })
        .then((response) => {
          dispatch("setMovieDetail", response.data);
        })
        .catch((error) => {
          if (error.response.status === 404) {
            router.push({ name: "NotFound" });
          }
        });
    },

    // 영화 좋아요
    likeMovie({ getters, dispatch }, movieId) {
      axios({
        url: drf.movie.likeMovie(movieId),
        method: "post",
        headers: getters.authHeader,
      }).then((response) => {
        dispatch("setMovieDetail", response.data);
      });
    },

    // 영화 리뷰 데이터 조회
    fetchMovieReview({ dispatch }, { movieId, type }) {
      axios({
        url: drf.movie.movieReview(),
        method: "get",
        params: {
          movie_id: movieId,
          type: type,
        },
      }).then((response) => {
        dispatch("setMovieReviewPopularity", response.data);
      });
    },
    // 영화 리뷰 작성
    createMovieReview(
      { getters, dispatch },
      { movieId, type, content, spoiler }
    ) {
      axios({
        url: drf.movie.movieReview(),
        method: "post",
        params: {
          movie_id: movieId,
          type: type,
        },
        data: { content, spoiler },
        headers: getters.authHeader,
      }).then((response) => {
        dispatch("setMovieReviewPopularity", response.data);
      });
    },
    // 영화 리뷰 좋아요
    likeMovieReview({ getters, dispatch }, { type, movieId, reviewId }) {
      axios({
        url: drf.movie.movieReviewDetail(),
        method: "post",
        params: {
          movie_id: movieId,
          type: type,
          review_id: reviewId,
        },
        headers: getters.authHeader,
      }).then((response) => {
        dispatch("setMovieReviewPopularity", response.data);
      });
    },
    //영화 리뷰 삭제
    deleteMovieReview({ getters, dispatch }, { type, movieId, reviewId }) {
      axios({
        url: drf.movie.movieReviewDetail(),
        method: "delete",
        params: {
          movie_id: movieId,
          type: type,
          review_id: reviewId,
        },
        headers: getters.authHeader,
      }).then((response) => {
        dispatch("setMovieReviewPopularity", response.data);
      });
    },
  },
};
