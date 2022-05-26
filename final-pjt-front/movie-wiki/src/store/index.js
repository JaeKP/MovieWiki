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
    searchInfos: null,
    keyword: null,
  },
  getters: {},
  mutations: {
    SEARCH_INFO(state, data) {
      data[0].sort(function (a, b) {
        if (a.title.length > b.title.length) {
          return 1;
        }
        if (a.title.length < b.title.length) {
          return -1;
        }
        // a must be equal to b
        return 0;
      });
      state.searchInfos = data[0].slice(0, 5);
      state.keyword = data[1];
    },
  },

  actions: {
    searchInfo(context, query) {
      const paramsTitle = {
        query: query,
        type: "title",
      };

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
          const data = [response.data, query];
          context.commit("SEARCH_INFO", data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  modules: { accounts, movies, articles },
});

export default store;
