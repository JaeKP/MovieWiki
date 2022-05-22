import drf from "@/api/drf";
import axios from "axios";
import router from "@/router";

export default {
  state: {
    movieDetail: {},
    // searchInfos: null,
    // keyword: null,
  },
  getters: {
    // 영화 상세 정보
    movieDetail: (state) => state.movieDetail,
  },
  mutations: {
    SET_MOVIE_DETAIL: (state, data) => (state.movieDetail = data),
  },
  actions: {
    // 영화 상세정보 vuex에 저장하기
    setMovieDetail({ commit }, data) {
      commit("SET_MOVIE_DETAIL", data);
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
        console.log(response);
        dispatch("fetchMovieDetail", movieId);
      });
    },
  },
};
