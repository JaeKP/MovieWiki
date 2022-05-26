import Vue from "vue";
import Vuex from "vuex";
import accounts from "./modules/accounts";
import movies from "./modules/movies";
import articles from "./modules/articles";
import drf from "@/api/drf";
import axios from "axios";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    searchInfos: [],
    keyword: null,
  },
  getters: {},
  mutations: {
    SEARCH_INFO(state, data) {
      state.searchInfos = data[0];
      state.keyword = data[1];
    },
  },

  actions: {
    searchInfo(context, query) {
      const paramsTitle = {
        query: query,
        type: "title",
      };
      const paramsActor = {
        query: query,
        type: "actor",
      };
      const paramsDirector = {
        query: query,
        type: "director",
      };

      const searchData = [];

      // 타이틀
      axios({
        url: drf.movie.movieSearch(),
        method: "get",
        params: paramsTitle,
      })
        .then((response) => {
          if (query == "") {
            response.data = [];
          }
          response.data.forEach((el) => {
            el.type = "movie";
            searchData.push(el);
          });
        })
        .catch((err) => {
          console.log(err);
        });
      // 배우
      axios({
        url: drf.movie.movieSearch(),
        method: "get",
        params: paramsActor,
      })
        .then((response) => {
          if (query == "") {
            response.data = [];
          }
          response.data.forEach((el) => {
            el.type = "actor";
            searchData.push(el);
          });
        })
        .catch((err) => {
          console.log(err);
        });
      // 감독
      axios({
        url: drf.movie.movieSearch(),
        method: "get",
        params: paramsDirector,
      })
        .then((response) => {
          if (query == "") {
            response.data = [];
          }
          response.data.forEach((el) => {
            el.type = "director";
            searchData.push(el);
          });
        })
        .catch((err) => {
          console.log(err);
        });
      console.log(searchData);
      const data = [searchData, query];
      context.commit("SEARCH_INFO", data);
    },
  },
  modules: { accounts, movies, articles },
});

export default store;
