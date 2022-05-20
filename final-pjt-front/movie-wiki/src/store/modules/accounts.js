import router from "@/router";
import drf from "@/api/drf";
import axios from "axios";
import Swal from "sweetalert2";

export default {
  state: {
    token: localStorage.getItem("token") || "",
    currentUser: {},
    userProfile: JSON.parse(localStorage.getItem("userProfile")) || {},
  },
  getters: {
    // 로그인
    isLoggedIn: (state) => !!state.token,
    currentUser: (state) => state.currentUser,
    userProfile: (state) => state.userProfile,
    // 유저의 토큰
    authHeader: (state) => ({ Authorization: `Token ${state.token}` }),
  },
  mutations: {
    SET_TOKEN: (state, token) => (state.token = token),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_PROFILE: (state, userProfile) => (state.userProfile = userProfile),
  },
  actions: {
    // 토큰 저장하기
    saveToken({ commit }, token) {
      commit("SET_TOKEN", token);
      localStorage.setItem("token", token);
    },

    // 토큰 제거하기
    removeToken({ commit }) {
      commit("SET_TOKEN", "");
      localStorage.setItem("token", "");
    },
    removeprofile({ commit }) {
      commit("SET_PROFILE", "");
      localStorage.setItem("profile", "");
    },

    // 프로필 저장하기
    fetchProfile({ getters, commit }, { username }) {
      axios({
        url: drf.accounts.profile(username),
        method: "get",
        header: getters.authHeader,
      }).then((response) => {
        const profileDict = {
          username: response.data.username,
          nickname: response.data.nickname,
          age: response.data.age,
          region: response.data.region,
          image: response.data.profile_image,
        };
        const JsonProfileDict = JSON.stringify(profileDict);
        console.log(profileDict);
        commit("SET_PROFILE", profileDict);
        localStorage.setItem("userProfile", JsonProfileDict);
      });
    },

    // 토큰과 맞는 username과 프로필 가져오기
    fetchCurrentUser({ dispatch, getters, commit, state }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: "get",
          headers: getters.authHeader,
        })
          .then((response) => {
            commit("SET_CURRENT_USER", response.data);
            dispatch("fetchProfile", state.currentUser);
          })
          .catch((error) => {
            if (error.response.status === 401) {
              dispatch("removeToken");
              dispatch("removeProfile");
              router.push({ name: "login" });
            }
          });
      }
    },

    signUp({ dispatch }, credential) {
      /* 
      POST: 사용자 입력정보를 signup URL로 보내기
      성공하면 응답 토큰 저장, 현재 사용자 정보 받기, 메인 페이지(ArticleListView)로 이동
      실패하면 에러 메시지 표시
      */
      axios({
        url: drf.accounts.signup(),
        method: "post",
        data: credential,
      })
        .then((response) => {
          const token = response.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
        })
        .catch((error) => {
          // 오류 내용을 뽑는다. 
          const err = JSON.parse(error.request.response);
          const errMessage = Object.values(err)[0][0]
          // 오류 알럿! 
          Swal.fire({
            title: errMessage,
            icon: 'error',
            toast: true,
            width: "25%",
            confirmButtonColor: '#5865f2',
          });
        })
    },

    logIn({ dispatch }, credentials) {
      /* 
        POST: 사용자 입력정보를 Login URL로 보내기 
        성공하면 응답 토큰 저장, 현재 사용자 정보 받기 , 메인 페이지로 이동
        실패하면 에러 메시지를 표시한다. 
      */
      axios({
        url: drf.accounts.login(),
        method: "post",
        data: credentials,
      })
        .then((response) => {
          const token = response.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    logOut({ getters, dispatch }) {
      /* 
      POST: token을 logout URL로 보내기
        성공하면 토큰 삭제, 사용자 알람, LoginView로 이동
        실패하면 에러 메시지 표시
      */
      axios({
        url: drf.accounts.logout(),
        method: "post",
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch("removeToken");
          alert("성공적으로 logout!");
          router.push({ name: "login" });
        })
        .error((error) => {
          console.error(error.response);
        });
    },
  },
};
