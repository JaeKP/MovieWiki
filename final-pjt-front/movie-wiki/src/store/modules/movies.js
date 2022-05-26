import drf from "@/api/drf";
import axios from "axios";
import router from "@/router";

export default {
  state: {
    movieDetail: {},
    similarMovie: [],
    movieReviewPopularity: {},
    movieReviewLatest: {},
    // searchInfos: null,
    // keyword: null,
  },
  getters: {
    // 영화 상세 정보
    movieDetail: (state) => state.movieDetail,
    similarMovie: (state) => state.similarMovie,
    movieReviewPopularity: (state) => state.movieReviewPopularity,
    movieReviewLatest: (state) => state.movieReviewLatest,
  },
  mutations: {
    SET_MOVIE_DETAIL: (state, data) => (state.movieDetail = data),
    SET_SIMINILAR_MOVIE: (state, data) => (state.similarMovie = data),
    PUSH_SIMILAR_MOVIE: (state, data) => state.similarMovie.push(data),
    SET_MOVIE_REVIEW_POPULARITY: (state, data) =>
      (state.movieReviewPopularity = data),
    SET_MOVIE_REVIEW_LATEST: (state, data) => (state.movieReviewLatest = data),
  },
  actions: {
    // 영화 상세정보 vuex에 저장하기
    setMovieDetail({ commit }, data) {
      commit("SET_MOVIE_DETAIL", data);
    },

    // 비슷한 영화 정보 vuex에 저장하기
    setSimilarMovie({ commit }, data) {
      commit("SET_SIMINILAR_MOVIE", data);
    },

    //영화 리뷰 정보 vuex에 저장하기
    setMovieReviewPopularity({ commit }, data) {
      commit("SET_MOVIE_REVIEW_POPULARITY", data);
    },
    //영화 리뷰 정보 vuex에 저장하기
    setMovieReviewLatest({ commit }, data) {
      commit("SET_MOVIE_REVIEW_LATEST", data);
    },

    // 영화 상세정보 요청하기
    fetchMovieDetail({ dispatch }, movieId) {
      axios({
        url: drf.movie.movieDetail(movieId),
        method: "get",
      })
        .then((response) => {
          const movie = response.data;
          dispatch("setMovieDetail", response.data);
          const array = movie?.movie_similar?.slice(0, 5);
          dispatch("fetchMovieSimilar", array);
        })
        .catch((error) => {
          if (error.response.status === 404) {
            router.push({ name: "NotFound" });
          }
        });
    },

    fetchMovieSimilar({ commit }, array) {
      commit("SET_SIMINILAR_MOVIE", []);
      array.forEach((item) => {
        axios({
          url: drf.movie.movieDetail(item),
          method: "get",
        }).then((response) => {
          commit("PUSH_SIMILAR_MOVIE", response.data);
        });
      });
      // console.log(data);
      // dispatch("setSimilarMovie", data);
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
        if (type === 1) {
          dispatch("setMovieReviewPopularity", response.data);
        } else {
          dispatch("setMovieReviewLatest", response.data);
        }
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
        dispatch("setMovieReviewPopularity", response.data.popularity);
        dispatch("setMovieReviewLatest", response.data.latest);
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
        dispatch("setMovieReviewPopularity", response.data.popularity);
        dispatch("setMovieReviewLatest", response.data.latest);
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
        dispatch("setMovieReviewPopularity", response.data.popularity);
        dispatch("setMovieReviewLatest", response.data.latest);
      });
    },
    // 영화 리뷰 업데이트
    updateMovieReview(
      { getters, dispatch },
      { type, movieId, reviewId, content, spoiler }
    ) {
      axios({
        url: drf.movie.movieReviewDetail(),
        method: "put",
        params: {
          movie_id: movieId,
          type: type,
          review_id: reviewId,
        },
        data: { content, spoiler },
        headers: getters.authHeader,
      }).then((response) => {
        dispatch("setMovieReviewPopularity", response.data.popularity);
        dispatch("setMovieReviewLatest", response.data.latest);
      });
    },
  },
};
