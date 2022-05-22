import Vue from "vue";
import Vuex from "vuex";
import accounts from "./modules/accounts";
import movies from "./modules/movies";
import articles from "./modules/articles";
import drf from "@/api/drf";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    searchInfos: {
      title: [],
      actor: [],
    },
    keyword: null,
  },
  getters: {},
  mutations: {
    SEARCH_INFO(state, data) {
      if ((data[2] === "title") & (state.searchInfos.actor.length < 5)) {
        state.searchInfos[data[2]] = data[0].slice(
          0,
          5 - state.searchInfos.actor.length
        );
        // console.log(state.searchInfos.title.length);
        // console.log(state.searchInfos.actor.length);
      } else if ((data[2] === "actor") & (state.searchInfos.title.length < 5)) {
        state.searchInfos[data[2]] = data[0].slice(
          0,
          5 - state.searchInfos.title.length
        );
      }

      state.keyword = data[1];
      // console.log(data[2]);
    },
  },
  actions: {
    searchInfo(context, querytype) {
      const params = {
        query: querytype[0],
        type: querytype[1],
      };
      // console.log(keyword);

      axios({
        url: drf.movie.movieSearch(),
        method: "get",
        params,
      })
        .then((response) => {
          // console.log(response.data);
          if (querytype[0] == "") {
            response.data = [];
          }
          const data = [response.data, querytype[0], querytype[1]];
          context.commit("SEARCH_INFO", data);

          // commit("SEARCH_RECENT", query);
        })
        .catch((err) => {
          console.log(err);
          const data = [0, querytype[0], querytype[1]];
          context.commit("SEARCH_INFO", data);
        });
    },
  },
  modules: { accounts, movies, articles },
});
