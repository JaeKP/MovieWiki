// import drf from "@/api/drf";
// import axios from "axios";

export default {
  state: {
    // searchInfos: null,
    // keyword: null,
  },
  getters: {},
  mutations: {
    // SEARCH_INFO(state, data) {
    //   // console.log(items);
    //   // if (items.length !== 0) {
    //   state.searchInfos = data[0];
    //   state.keyword = data[1];
    //   // console.log(data[0]);
    //   // } else if (items === 0) {
    //   //   state.searchInfos = items;
    //   // }
    // },
  },
  actions: {
    // searchInfo(context, keyword) {
    //   const params = {
    //     query: keyword,
    //     type: "title",
    //   };
    //   // console.log(keyword);
    //   axios({
    //     url: drf.movie.movieSearch(),
    //     method: "get",
    //     params,
    //   })
    //     .then((response) => {
    //       console.log(response.data);
    //       const data = [response.data, keyword];
    //       context.commit("SEARCH_INFO", data);
    //       // commit("SEARCH_RECENT", query);
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //       const data = [0, keyword];
    //       context.commit("SEARCH_INFO", data);
    //     });
    // },
  },
};
